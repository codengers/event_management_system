# Event Management System

This is a Python-based Event Management System for managing attendees, generating QR codes, marking attendance, and generating reports.

## Features

- Generate QR codes for attendees.
- Mark attendance via QR code scanning.
- Export attendee details as an Excel report.
- Simple graphical user interface (GUI).

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the application:
    ```bash
    python main.py
    ```

## Folder Structure

- `config/`: Database configuration.
- `models/`: Database models.
- `services/`: Business logic for QR generation, attendance, and reporting.
- `ui/`: User interface.
- `data/`: SQLite database.
- `qrcodes/`: Generated QR codes.


### 1. Clone the Repository
```bash
git clone https://github.com/codengers/event_management_system.git
cd event_management_system
