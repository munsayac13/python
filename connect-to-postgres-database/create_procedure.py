import psycopg2
from config import load_config
import connect

def create_procedure():
    SQL="""
    CREATE OR REPLACE PROCEDURE add_operatingsystemsversions(
        new_systemid INTEGER,
        new_versionname VARCHAR
    )
    AS $$
    DECLARE
        v_systemid INT;
        v_versionname VARCHAR;
    BEGIN
        INSERT INTO operatingsystemsversions(systemid, versionname)
        VALUES(new_systemid, new_versionname)
        RETURNING systemid INTO v_systemid;
    END;
    $$
    LANGUAGE PLPGSQL;
    """

    try:
        config = load_config()
        with connect.connect_to_database(config) as conn:
            with conn.cursor() as cur:
                cur.execute(SQL)
            cur.close()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_procedure()