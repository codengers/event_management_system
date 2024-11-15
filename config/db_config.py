import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'event.db')

def get_connection():
    return sqlite3.connect(DB_PATH)

def drop_table():
    conn = get_connection()
    c = conn.cursor()
    c.execute('DROP TABLE attendees')
    conn.commit()
    print("Table dropped successfully")
    conn.close()   
def initialize_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute(
    '''
        CREATE TABLE IF NOT EXISTS attendees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            phone TEXT NOT NULL,
            amount REAL NOT NULL,
            num_persons INTEGER NOT NULL,
            email TEXT NOT NULL,
            qr_code_path TEXT NOT NULL,
            attended BOOLEAN DEFAULT 0,
            user_created_date TEXT DEFAULT CURRENT_TIMESTAMP,
            user_updated_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    '''
    )
    conn.commit()
    conn.close()
