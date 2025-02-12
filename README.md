# Cursor Requests Limit Tracker

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/yourusername/cursor-requests-limit/graphs/commit-activity)

## 🤔 The Problem
<img width="842" alt="image" src="https://github.com/user-attachments/assets/415acda0-cbdf-4210-9bd8-312442f82b9f" />


When using Cursor IDE, you have a monthly limit on API requests (e.g., 500 requests for premium models like GPT-4). It's easy to lose track of these requests and suddenly find yourself running out of quota when you need it most. Without proper monitoring:

- You might unexpectedly hit your limit during critical development work
- There's no easy way to track your daily/weekly usage patterns
- You won't know when you're approaching your limit
- You can't plan your usage effectively across the month

<img width="872" alt="Screenshot 2025-02-07 at 2 01 38 PM" src="https://github.com/user-attachments/assets/fd17c158-fd6d-4f97-a788-a55d784acf05" />



## 💡 The Solution

This Python application solves these problems by:

- 🔍 Actively monitoring your Cursor API request usage
- ⚠️ Sending timely notifications before you hit limits
- 📊 Providing usage analytics and trends
- 🎯 Helping you manage your quota more effectively

📊 A Python application that helps you monitor and track your Cursor API request usage, providing timely notifications when you're approaching your limit.

<div align="center">
  <img src="docs/assets/demo.gif" alt="Demo GIF" width="600px">
</div>

## 🌟 Features

- 📈 Real-time tracking of remaining API requests for Cursor
- 📧 Email notifications when reaching specified thresholds
- 🔔 Desktop notifications when opening Cursor
- 📊 Comprehensive daily usage statistics
- ⚙️ Highly configurable notification thresholds
- 🔄 Automatic monitoring and alerts
- 💾 Local SQLite database for usage history

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Cursor API access
- Email account for notifications (Gmail recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cursor-requests-limit.git
   cd cursor-requests-limit
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your configuration:
   ```ini
   EMAIL_ADDRESS=your-email@example.com
   EMAIL_PASSWORD=your-app-specific-password
   NOTIFICATION_THRESHOLD=100
   ```

## 🛠️ Technical Stack

- **Python 3.8+**: Core programming language
- **SQLite**: Local database for storing request history
- **smtplib**: Email notification system
- **plyer**: Cross-platform desktop notifications
- **FastAPI**: API endpoint monitoring
- **SQLAlchemy**: Database ORM

## 📁 Project Structure

```
cursor-requests-limit/
├── src/                    # Source code
│   ├── __init__.py
│   ├── database.py        # Database operations
│   ├── notification.py    # Notification system
│   ├── api_monitor.py     # API monitoring logic
│   └── config.py          # Configuration management
├── tests/                 # Test suite
│   └── __init__.py
├── .env.example          # Environment variables template
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## ⚙️ Configuration Options

| Variable | Description | Default |
|----------|-------------|---------|
| `NOTIFICATION_THRESHOLD` | Remaining requests threshold | 100 |
| `EMAIL_ADDRESS` | Notification email address | None |
| `EMAIL_PASSWORD` | App-specific email password | None |
| `CHECK_INTERVAL` | API check interval (minutes) | 30 |

## 🚀 Usage

1. Start the monitoring service:
   ```bash
   python src/api_monitor.py
   ```

2. The application will automatically:
   - Monitor your Cursor API usage in real-time
   - Send email alerts when approaching limits
   - Display desktop notifications
   - Record usage statistics

## 📊 Monitoring Dashboard

Access the monitoring dashboard at `http://localhost:8000/dashboard` to view:
- Current API usage
- Historical usage patterns
- Notification history
- System status

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Cursor team for providing the API
- Contributors and users of this project
- Open source community

## 📬 Contact

- Project Link: [https://github.com/yourusername/cursor-requests-limit](https://github.com/OsmanByrm/Cursor-Requests-Limit-Tracker)
- Report Issues: Loading
  

---

<div align="center">
  Made with by Osman Bayram :)
</div>
