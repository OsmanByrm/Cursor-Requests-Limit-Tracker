import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Email Configuration
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))

# Notification Settings
NOTIFICATION_THRESHOLD = int(os.getenv('NOTIFICATION_THRESHOLD', '100'))
# Time interval between checks in minutes
CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', '30'))

# Database Settings
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./cursor_requests.db')

# API Settings
CURSOR_API_URL = os.getenv('CURSOR_API_URL', 'https://api.cursor.sh')
API_KEY = os.getenv('CURSOR_API_KEY') 