from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime

class CursorLogin:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.setup_driver()

    def setup_driver(self):
        """Setup Chrome driver with headless mode"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")  # Required for headless on Mac
        
        # Set up ChromeDriver for Mac ARM64
        os.environ['WDM_ARCHITECTURE'] = 'arm64'
        service = Service()
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def login(self):
        """Login to Cursor website"""
        try:
            print("Starting login process...")
            # Navigate to auth page
            auth_url = "https://authenticator.cursor.sh/?client_id=client_01GS6W3C96KW4WRS6Z93JCE2RJ&redirect_uri=https%3A%2F%2Fcursor.com%2Fapi%2Fauth%2Fcallback&response_type=code&state=%257B%2522returnTo%2522%253A%2522%252Fsettings%2522%257D"
            print(f"Navigating to auth page...")
            self.driver.get(auth_url)
            
            # Wait for and enter email
            print("Entering email...")
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
            )
            email_input.clear()
            email_input.send_keys(self.email)
            
            # Click continue button
            print("Clicking continue...")
            continue_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
            continue_button.click()
            
            # Wait for and enter password
            print("Entering password...")
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
            )
            password_input.clear()
            password_input.send_keys(self.password)
            
            # Click sign in button
            print("Clicking sign in...")
            sign_in_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='intent'][type='submit']"))
            )
            sign_in_button.click()
            
            # Wait for login to complete
            print("Waiting for login to complete...")
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='dashboard']"))
            )
            
            print("Login successful!")
            return True
            
        except Exception as e:
            print(f"Login failed with error: {str(e)}")
            return False
        finally:
            self.driver.quit()

def main():
    email = os.getenv("CURSOR_EMAIL")
    password = os.getenv("CURSOR_PASSWORD")
    
    if not email or not password:
        print("Error: CURSOR_EMAIL and CURSOR_PASSWORD environment variables must be set")
        return
    
    cursor = CursorLogin(email, password)
    cursor.login()

if __name__ == "__main__":
    main() 