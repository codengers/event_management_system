from config.db_config import get_connection
from datetime import datetime

class Attendee:    
    @staticmethod
    def add_attendee(username, phone, amount, num_persons, email, qr_code_path):
        print("username: {}".format(username))
        print("phone: {}".format(phone))
        print("amount: {}".format(amount))
        print("num_persons: {}".format(num_persons))
        print("email: {}".format(email))
        print("qr_code_path: {}".format(qr_code_path))
        
        conn = get_connection()
        cursor = conn.cursor()

        # Check if attendee already exists
        cursor.execute('SELECT * FROM attendees WHERE phone = ?', (phone,))
        existing_attendee = cursor.fetchone()
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if not existing_attendee:
            cursor.execute(''' 
                INSERT INTO attendees (username, phone, amount, num_persons, email, qr_code_path, user_created_date, user_updated_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)        
            ''', (username, phone, amount, num_persons, email, qr_code_path, current_time, current_time))

        conn.commit()
        conn.close()

    @staticmethod
    def update_attendee(username, phone, amount, num_persons, email, qr_code_path, attendee_id):
        print("username: {}".format(username))
        print("phone: {}".format(phone))
        print("amount: {}".format(amount))
        print("num_persons: {}".format(num_persons))
        print("email: {}".format(email))
        print("qr_code_path: {}".format(qr_code_path))
        print("attendee_id: {}".format(attendee_id))
        
        conn = get_connection()
        cursor = conn.cursor()

        # Check if attendee already exists
        cursor.execute('SELECT * FROM attendees WHERE id = ?', (attendee_id,))
        existing_attendee = cursor.fetchone()
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if existing_attendee:
            # Update the existing attendee
            cursor.execute('''
                UPDATE attendees
                SET username = ?, phone = ?, amount = ?, num_persons = ?, email = ?, qr_code_path = ?, user_updated_date = ?
                WHERE id = ?
            ''', (username, phone, amount, num_persons, email, qr_code_path, current_time, attendee_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_attendee(phone):
        """Deletes an attendee from the database by phone number."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM attendees WHERE phone = ?', (phone,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_attendee_by_phone(phone):
        """Retrieves an attendee's details by phone number."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM attendees WHERE phone = ?', (phone,))
        attendee = cursor.fetchone()
        conn.close()
        return attendee

    @staticmethod
    def get_all_attendees():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(''' SELECT id, username, phone, amount, num_persons, email, qr_code_path, attended, user_created_date, user_updated_date FROM attendees''')
        attendees = cursor.fetchall()
        conn.close()
        return attendees
        
    @staticmethod
    def mark_attendance(phone):
        conn = get_connection()
        cursor = conn.cursor()
        
        current_time = datetime.dtrftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('UPDATE attendees SET attended = 1, user_updated_date = ? WHERE phone = ?', (current_time, phone))
        conn.commit()
        conn.close()
    