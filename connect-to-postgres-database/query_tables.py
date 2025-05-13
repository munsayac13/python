import psycopg2
from config import load_config
import connect

def get_operatingsystems():

    QUERYSQL="""
    SELECT * FROM operatingsystems;
    """
    try:
        config = load_config()
        with connect.connect_to_database(config) as conn:
            with conn.cursor() as cur:
                cur.execute(QUERYSQL)
                rows = cur.fetchall()
                #print(rows)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return rows
    
def get_operatingsystems_and_versions():

    # Shows duplicate columns
    #QUERYSQL="""
    #SELECT * FROM operatingsystems 
    #    INNER JOIN operatingsystemsversions ON operatingsystems.systemid=operatingsystemsversions.systemid;
    #"""

    # Shows only specific columns
    QUERYSQL="""
    SELECT os.systemid, os.systemname, osv.versionname FROM operatingsystems os
        INNER JOIN operatingsystemsversions osv ON os.systemid=osv.systemid;
    """

    try:
        config = load_config()
        with connect.connect_to_database(config) as conn:
            with conn.cursor() as cur:
                cur.execute(QUERYSQL)
                rows = cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return rows
    
if __name__ == "__main__":
    systems = get_operatingsystems()
    for system in systems:
        print(system[0], system[1])

    systemversions = get_operatingsystems_and_versions()
    for version in systemversions:
        print("Distro:",version[1],"-", "Patch Version:", version[2])


