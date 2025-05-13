import psycopg2
from config import load_config
import connect

def create_functions():
    """
    FUNCTIONS returns VALUE. STORED PROCEDURE does not return any VALUE.
    """
    GETOSVERBYDISTROSQL="""
    CREATE OR REPLACE FUNCTION get_operatingsystems_versions_by_distro(distro VARCHAR) RETURNS TABLE(systemid INTEGER, versionname VARCHAR) AS
    $$
    BEGIN
    	RETURN QUERY
	
    	SELECT os.systemid, osv.versionname FROM operatingsystems os
    		INNER JOIN operatingsystemsversions osv ON os.systemid=osv.systemid
    		WHERE os.systemname = distro;
    END; $$
    LANGUAGE plpgsql;
    """

    try:
        config = load_config()
        with connect.connect_to_database(config) as conn:
            with conn.cursor() as cur:
                cur.execute(GETOSVERBYDISTROSQL)
            cur.close()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)   
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_functions()
