import os
import psycopg2

def get_conn():
    database_host = os.environ.get("DATABASE_HOST", "127.0.0.1")
    database = os.environ.get("DATABASE", "postgres")
    database_user = os.environ.get('DATABASE_USER', 'postgres')
    database_password = os.environ.get('DATABASE_PASSWORD', 'fred')
    database_port = os.environ.get('DATABASE_PORT', "5432")

    conn = psycopg2.connect(
        database = database,
        user = database_user,
        password = database_password,
        host = database_host,
        port = database_port
    )

    return conn