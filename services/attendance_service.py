from models.attendee import Attendee

def mark_attendance(phone):
    Attendee.mark_attendance(phone)
    print("Attendance marked for phone: {}".format(phone))
