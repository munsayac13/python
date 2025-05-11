import psycopg2
from config import load_config
import connect

def insert_operatingsystems(systemName):
    """
    INSERT a new operatingsystem into table
    """

    INSERTSQL="""
    INSERT INTO operatingsystems(systemname) VALUES (%s) RETURNING systemid;
    """

    LASTIDSQL="""
    SELECT systemid from operatingsystems ORDER BY systemid DESC LIMIT 1;
    """

    systemId = None;
    try:
        config = load_config()
        with connect.connect_to_database(config) as conn:
            with conn.cursor() as cur:
                print(INSERTSQL)

                # Display last systemId
                cur.execute(LASTIDSQL)
                rows = cur.fetchone()
                if rows:
                    lastsystemId = rows[0]
                    print("Last SystemId:", lastsystemId)

                # execute Insert Statement
                # "(systemName,)" is needed otherwise error
                # not all arguments converted during string formatting
                cur.execute(INSERTSQL, (systemName,))
                rows = cur.fetchone()
                # get the generated id back
                if rows:
                    systemId = rows[0]
                    print("New SystemId:", systemId)
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return systemId
    
if __name__ == "__main__":
    insert_operatingsystems("WINDOWS 99")
    print("############")
    insert_operatingsystems("WINDOWS 2000")
    print("############")
    insert_operatingsystems("WINDOWS XP")