import psycopg2
from config import load_config
import connect

def create_tables():
    commands = (
        """
        CREATE TABLE operatingsystems (
            systemId SERIAL PRIMARY KEY,
            systemName VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE operatingsystemsVersions(
            osvId SERIAL PRIMARY KEY,
            systemId INT NOT NULL,
            versionName VARCHAR(255) NOT NULL,
            FOREIGN KEY (systemId)
            REFERENCES operatingsystems (systemId) 
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE computers(
            computerId SERIAL PRIMARY KEY,
            computerName VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE computersParts(
            computerId INTEGER NOT NULL,
            systemId INTEGER NOT NULL,
            PRIMARY KEY (computerId, systemId),
            FOREIGN KEY (computerId)
                REFERENCES computers (computerId)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (systemId)
                REFERENCES operatingsystems (systemId)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE binaryfiles(
            binaryId SERIAL PRIMARY KEY,
            computerId INT NOT NULL,
            fileName VARCHAR(255) NOT NULL,
            binaryPath BYTEA NOT NULL,
            FOREIGN KEY (computerId)
            REFERENCES computers (computerId) 
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )

    try:
        config = load_config()
        with connect.connect_to_database(config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    print(command)
                    cur.execute(command)
                cur.close()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_tables()
    
