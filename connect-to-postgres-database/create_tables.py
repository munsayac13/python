import psycopg2
from config import load_config

def create_tables():
    commands = (
        """
        CREATE TABLE operatingsystems (
            systemId SERIAL PRIMARY KEY,
            systemName VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE computers(
            computerId SERIAL PRIMARY KEY,
            computerName VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE operatingsystemsVersions(
            systemId INTEGER PRIMARY KEY,
            versionName VARCHAR(255) NOT NULL,
            FOREIGN KEY (systemId)
            REFERENCES operatingsystems (systemId) 
            ON UPDATE CASCADE ON DELETE CASCADE
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
        """
    )

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    print(command)
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
    