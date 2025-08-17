from mysql.connector import connect, Error

def create_database():
    connection = None
    cursor_object = None
    try:
        connection = connect(
            host="localhost",
            user="root",
            password="password1234"
        )

        if connection.is_connected():
            cursor_object = connection.cursor()
            cursor_object.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if cursor_object:
            cursor_object.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
