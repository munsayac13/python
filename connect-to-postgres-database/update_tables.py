import psycopg2
from config import load_config
import connect


def update_operatingsystemsversions(systemId, currentVersionName, newVersionName):
    """ 
    Update operating system version name
    """

    updated_row_count = 0

    UPDATESQL = """
    UPDATE operatingsystemsversions SET versionName=%s WHERE systemId=%s AND versionName=%s RETURNING *;
    """

    versionName = None
    try:
        config = load_config()
        with connect.connect_to_database(config) as conn:
            with conn.cursor() as cur:
                # execute Insert Statement
                # "(systemName,)" is needed otherwise error
                # not all arguments converted during string formatting
                cur.execute(UPDATESQL, (newVersionName,systemId,currentVersionName))
                rows = cur.fetchone()
                print(rows)
                versionName=rows[1]

            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return versionName

if __name__ == "__main__":
    update_operatingsystemsversions(4, "debian-linux_x64_1001", "debian-linux_x86_64_2001")
    update_operatingsystemsversions(5, "ubuntu-linux_x64_30.50", "ubuntu-linux_x86_64_1.10")
    update_operatingsystemsversions(6, "centos-linux_x64_10.80", "centos-linux_x86_64_4.88")