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

    #print(INSERTSQL)
    systemId = None;
    try:
        config = load_config()
        with connect.connect_to_database(config) as conn:
            with conn.cursor() as cur:

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
    
def insert_multiple_operatingsystems(systemNames):
    INSERTSQL="""
    INSERT INTO operatingsystems(systemname) VALUES (%s) RETURNING *;
    """

    LASTIDSQL="""
    SELECT systemid from operatingsystems ORDER BY systemid DESC LIMIT 1;
    """

    SELECTSQL="""
    SELECT systemid from operatingsystems WHERE systemname=%s;
    """

    #print(INSERTSQL)
    systemId = []
    try:
        config = load_config()
        with connect.connect_to_database(config) as conn:
            with conn.cursor() as cur:


                # Display last systemId
                cur.execute(LASTIDSQL)
                rows = cur.fetchone()
                if rows:
                    lastsystemId = rows[0]
                    print("Last SystemId:", lastsystemId)

                # execute Insert Statement
                # "(systemName,)" is needed otherwise error
                # not all arguments converted during string formatting
                cur.executemany(INSERTSQL, systemNames)
                
                # get systemId of all new rows
                for systemName in systemNames:
                    cur.execute(SELECTSQL, (systemName,))
                    row = cur.fetchone()
                    systemId.append(row[0])
                
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return systemId
    

def insert_operatingsystemsVersions(systemId, versionName):
    INSERTSQL="""
    INSERT INTO operatingsystemsVersions(systemId, versionName) VALUES (%s, %s) RETURNING versionName;
    """
    #print(INSERTSQL)

    try:
        config = load_config()
        with connect.connect_to_database(config) as conn:
            with conn.cursor() as cur:
                
                # execute Insert Statement
                # "(systemName,)" is needed otherwise error
                # not all arguments converted during string formatting
                cur.execute(INSERTSQL, (systemId,versionName))
                rows = cur.fetchone()
                
                # get the generated version name back
                if rows:
                    versionName = rows[0]
                    print("Version Name:", versionName)
                conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    #finally:
    #    return systemId
    
if __name__ == "__main__":
    SYSIDONE=insert_operatingsystems("WINDOWS 99")
    print("############")
    
    SYSIDTWO=insert_operatingsystems("WINDOWS 2000")
    print("############")
    
    SYSIDTHREE=insert_operatingsystems("WINDOWS XP")
    print("############")
    insert_multiple_operatingsystems(
        [
            ("DEBIAN",),
            ("UBUNTU",),
            ("CENTOS",)
        ]
    )
    print("############")
    insert_operatingsystemsVersions(4, "debian-linux_x64_1001")
    print("############")
    insert_operatingsystemsVersions(5, "ubuntu-linux_x64_30.50")
    print("############")
    insert_operatingsystemsVersions(6, "centos-linux_x64_10.80")
    print("############")