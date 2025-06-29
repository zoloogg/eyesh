import json
import psycopg2
import os

database_host = os.environ.get("DATABASE_HOST", "127.0.0.1")
database = os.environ.get("DATABASE", "psotgres")
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

def create_table():
    try:
        cur = conn.cursor()

        cur.execute("create table raw_data ( \
            year int, \
            state_id int,\
            subject_id int,\
            rank varchar,\
            registration_number varchar, \
            raw_score int, \
            calculated_score double precision, \
            percentile double precision, \
            grade varchar \
        )")

        conn.commit()
    except:
        print('Table exists')

        conn.rollback()

def upload_psql(filename):
    f = open(filename, "r")
        
    data = f.read()

    data = json.loads(data)

    db_cursor = conn.cursor()

    for cur in data:
        print(cur)

        values = (cur['year'],cur['state'],cur['subject'],cur['rank'],cur['registration_number'],cur['raw_score'],cur['calculated_score'],cur['percentile'],cur['grade'])
        db_cursor.execute("INSERT INTO raw_data (year, state_id, subject_id, rank, registration_number, raw_score, calculated_score, percentile, grade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", values)

    conn.commit()

def upload_2024():
    for x in range(1,25):
        for y in range(1,11):
            upload_psql('./2024/json/' + str(x) + '-' + str(y) + '.json')

create_table()
upload_2024()