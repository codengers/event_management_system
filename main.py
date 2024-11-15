from config.db_config import initialize_db
#from config.db_config import drop_table
from ui.app_ui import main_ui

if __name__ == "__main__":
    #drop_table()
    initialize_db()
    main_ui()
    