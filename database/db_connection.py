# database/db_connection.py

import cx_Oracle

# Adjust these configurations to match your local Oracle DB
HOSTNAME = "localhost"
PORT = 1521
SERVICE_NAME = "XE"  # or the service name you used during installation
USERNAME = "your_username"
PASSWORD = "your_password"

def get_connection():
    """
    Returns a connection object to the Oracle database.
    """
    # For cx_Oracle:
    dsn_tns = cx_Oracle.makedsn(HOSTNAME, PORT, service_name=SERVICE_NAME)
    conn = cx_Oracle.connect(user=USERNAME, password=PASSWORD, dsn=dsn_tns)
    return conn

if __name__ == "__main__":
    # Quick test
    try:
        connection = get_connection()
        print("Successfully connected to Oracle Database!")
    except cx_Oracle.Error as e:
        print("Error connecting to Oracle Database:", e)
    finally:
        if 'connection' in locals():
            connection.close()
