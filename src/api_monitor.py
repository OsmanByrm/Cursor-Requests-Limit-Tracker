import time
import os
import sys
from datetime import datetime
from .database import Database
from .notification import NotificationManager
from .config import CHECK_INTERVAL
import requests
import json

class CursorAPIMonitor:
    def __init__(self):
        self.db = Database()
        self.notification_manager = NotificationManager()
        self.session = requests.Session()
        self.base_url = "https://cursor.sh"
        self.setup_session()

    def setup_session(self):
        """Set up the session with necessary headers"""
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })

    def login(self):
        """Login to Cursor"""
        try:
            email = os.getenv("CURSOR_EMAIL")
            password = os.getenv("CURSOR_PASSWORD")

            # Get CSRF token
            response = self.session.get(f"{self.base_url}/api/csrf")
            response.raise_for_status()
            csrf_token = response.json().get('csrfToken')
            
            # Add CSRF token to headers
            self.session.headers.update({
                'X-CSRF-Token': csrf_token
            })

            # Start login process
            login_data = {
                "email": email,
                "password": password,
                "callbackUrl": f"{self.base_url}/settings"
            }
            
            response = self.session.post(f"{self.base_url}/api/auth/callback/credentials", json=login_data)
            response.raise_for_status()

            # Check if we're logged in by trying to access the usage data
            test_response = self.session.get(f"{self.base_url}/api/user/me")
            test_response.raise_for_status()

            return True
        except Exception as e:
            print(f"Login failed: {str(e)}")
            return False

    def get_usage_data(self):
        """Get usage data from Cursor API"""
        try:
            # First try to get user data
            response = self.session.get(f"{self.base_url}/api/user/me")
            response.raise_for_status()
            user_data = response.json()
            
            # Then get usage data
            response = self.session.get(f"{self.base_url}/api/user/usage")
            response.raise_for_status()
            usage_data = response.json()
            
            # Extract premium model usage
            premium_usage = usage_data.get("premium_models", {})
            current = premium_usage.get("used", 0)
            total = premium_usage.get("limit", 150)  # Default to 150 if not specified
            
            return current, total
        except Exception as e:
            print(f"Error getting usage data: {str(e)}")
            return None, None

    def should_notify(self, current_usage, previous_usage):
        """Determine if we should send a notification"""
        if previous_usage is None:
            return False
        
        increase = current_usage - previous_usage
        return increase >= 20

    def monitor(self):
        """Main monitoring loop"""
        print("Starting Cursor API usage monitor...")
        previous_usage = None
        
        while True:
            try:
                if not self.login():
                    print("Login failed, retrying in next iteration...")
                    time.sleep(CHECK_INTERVAL * 60)
                    continue

                current_usage, total_limit = self.get_usage_data()
                
                if current_usage is not None:
                    print(f"\nCurrent Cursor Premium Usage: {current_usage}/{total_limit}")
                    
                    # Log the current usage
                    self.db.log_request(current_usage, total_limit)
                    
                    # Check if we need to send notifications
                    if previous_usage is not None and self.should_notify(current_usage, previous_usage):
                        message = f"Cursor Premium usage increased by {current_usage - previous_usage} requests. Current usage: {current_usage}/{total_limit}"
                        self.notification_manager.send_desktop_notification(current_usage, total_limit)
                    
                    previous_usage = current_usage
            except Exception as e:
                print(f"Error in monitoring loop: {str(e)}")
            
            time.sleep(CHECK_INTERVAL * 60)

def main():
    monitor = CursorAPIMonitor()
    try:
        monitor.monitor()
    except KeyboardInterrupt:
        print("\nStopping monitor...")
        sys.exit(0)

if __name__ == "__main__":
    main() 