import mysql.connector

connection = None

try:

    connection = mysql.connector.connect(
        host='db',
        user='docker',
        passwd='docker',
        db='python_sample')
    cursor = connection.cursor()
    sql = '''
        CREATE TABLE student (
        student_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50) NULL,
        last_name VARCHAR(50) NULL,
        birthday DATE NULL,
        gender ENUM('F','M','E')
        )'''
    cursor.execute(sql)

    cursor.execute("SHOW TABLES")
    print(cursor.fetchall())

    cursor.close()

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if connection is not None and connection.is_connected():
        connection.close()