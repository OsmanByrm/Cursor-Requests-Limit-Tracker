import json
import os
from datetime import datetime

class Database:
    def __init__(self):
        self.db_file = 'cursor_requests.json'
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as f:
                json.dump([], f)

    def log_request(self, remaining_requests, total_requests, event_type='check'):
        try:
            with open(self.db_file, 'r') as f:
                logs = json.load(f)
        except:
            logs = []

        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'remaining_requests': remaining_requests,
            'total_requests': total_requests,
            'event_type': event_type
        }
        
        logs.append(log_entry)
        
        with open(self.db_file, 'w') as f:
            json.dump(logs, f, indent=2)

    def get_latest_request_count(self):
        try:
            with open(self.db_file, 'r') as f:
                logs = json.load(f)
                if logs:
                    latest = max(logs, key=lambda x: x['timestamp'])
                    return latest['remaining_requests']
        except:
            pass
        return None

    def get_daily_usage(self):
        try:
            with open(self.db_file, 'r') as f:
                logs = json.load(f)
                
            today = datetime.utcnow().date()
            today_logs = [
                log for log in logs 
                if datetime.fromisoformat(log['timestamp']).date() == today
            ]
            
            if today_logs:
                first_log = min(today_logs, key=lambda x: x['timestamp'])
                latest_log = max(today_logs, key=lambda x: x['timestamp'])
                
                return {
                    'requests_used': first_log['remaining_requests'] - latest_log['remaining_requests'],
                    'remaining_requests': latest_log['remaining_requests'],
                    'total_requests': latest_log['total_requests']
                }
        except:
            pass
        return None 