import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from plyer import notification
from .config import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    SMTP_SERVER,
    SMTP_PORT,
    NOTIFICATION_THRESHOLD
)

class NotificationManager:
    @staticmethod
    def send_email_notification(remaining_requests, total_requests):
        if not all([EMAIL_ADDRESS, EMAIL_PASSWORD]):
            return False

        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = f'Cursor API Request Alert - {remaining_requests} requests remaining'

        body = f"""
        Your Cursor API request usage alert:
        
        Remaining Requests: {remaining_requests}
        Total Requests: {total_requests}
        Usage: {total_requests - remaining_requests}/{total_requests}
        
        You have reached the notification threshold of {NOTIFICATION_THRESHOLD} remaining requests.
        Please monitor your usage carefully.
        """

        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Failed to send email notification: {str(e)}")
            return False

    @staticmethod
    def send_desktop_notification(remaining_requests, total_requests):
        try:
            notification.notify(
                title='Cursor API Request Alert',
                message=f'Remaining requests: {remaining_requests}/{total_requests}',
                app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
                timeout=10,  # seconds
            )
            return True
        except Exception as e:
            print(f"Failed to send desktop notification: {str(e)}")
            return False

    def notify(self, remaining_requests, total_requests):
        """Send both email and desktop notifications"""
        email_sent = self.send_email_notification(remaining_requests, total_requests)
        desktop_sent = self.send_desktop_notification(remaining_requests, total_requests)
        return email_sent or desktop_sent 