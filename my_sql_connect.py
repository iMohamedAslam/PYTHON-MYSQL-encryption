import mysql.connector
from password_utils import get_decrypted_password

def connect_to_mysql():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=get_decrypted_password(),
        database="test"

    )
    print("connected to my mysql successfully")
    print(get_decrypted_password())
    conn.close()

if __name__ == "__main__":
    connect_to_mysql()

