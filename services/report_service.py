import pandas as pd
import os
from models.attendee import Attendee
from datetime import datetime

def generate_report():
    attendees = Attendee.get_all_attendees()

    df = pd.DataFrame(attendees, columns=['ID', 'Username', 'Phone', 'Amount', 'Persons', 'Email', 'QR Code Path', 'Attended', 'Created Date', 'Updated Date'])
    os.makedirs("reports", exist_ok=True)
    report_path = "reports/attendees_report_{}.xlsx".format(datetime.now().strftime("%Y-%m-%d"))
    df.to_excel(report_path, index=False)
    print(f"Report saved to {report_path}")        