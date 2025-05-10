import psycopg2
from config import load_config

# psycop2.extensions.connection does not support the asynchronous context manager protocol
# therefore async and await cannot be used
def connect(config):
    try:
        # The ** argument in Python functions allows a function to accept an arbitrary number of keyword arguments. These arguments are passed to the function as a dictionary, where the keys are the argument names and the values are the argument values. This is useful when you want to create a function that can accept a variable number of named options or settings.
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL Server')
            return conn
    except(psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    config = load_config()
    connect(config)