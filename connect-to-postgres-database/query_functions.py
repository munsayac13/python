import psycopg2
from config import load_config
import connect


def get_operatingsystems_versions_by_distro(distro):
    try:
        config = load_config()
        with connect.connect_to_database(config) as conn:
            with conn.cursor() as cur:
                cur.callproc('get_operatingsystems_versions_by_distro', (distro,))
                row = cur.fetchone()
                print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    get_operatingsystems_versions_by_distro("DEBIAN")
    get_operatingsystems_versions_by_distro("UBUNTU")
    get_operatingsystems_versions_by_distro("CENTOS")