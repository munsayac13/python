import psycopg2

try:
    conn = psycopg2.connect(
        host="192.168.44.133",
        database="k3s",
        user="postgres",
        password="devops",
        port="5432"
    )
    cursor = conn.cursor()
    print("Connection Successful!")

    cursor.execute("SELECT version();")
    dbVersion = cursor.fetchone()
    print(f"PostgreSQL version: {dbVersion}")

except psycopg2.Error as e: 
    print(f"Error connecting to Postgresql: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()
        print("PostgresSQL connection closed!")
