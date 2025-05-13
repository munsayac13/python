import psycopg2
from config import load_config
import connect

def add_operatingsystemsversions(systemId, versionName):
    try:
        config = load_config()
        with connect.connect_to_database(config) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL add_operatingsystemsversions(%s,%s)', (systemId, versionName))
            cur.close()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    add_operatingsystemsversions(4, "debian-linux-x64-4000")
    add_operatingsystemsversions(5, "ubuntu-linux-x64-5000")
    add_operatingsystemsversions(6, "centos-linux-x64-6000")

