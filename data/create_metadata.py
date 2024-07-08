from database import get_conn

states = {
        1: "Архангай аймаг",
        2: "Баян-Өлгий аймаг",
        3: "Баянхонгор аймаг",
        4: "Булган аймаг",
        5: "Говь-Алтай аймаг",
        6: "Говьсүмбэр аймаг",
        7: "Дархан-Уул аймаг",
        8: "Дорноговь аймаг",
        9: "Дорнод аймаг",
        10: "Дундговь аймаг",
        11: "Завхан аймаг",
        12: "Орхон аймаг",
        13: "Сэлэнгэ аймаг",
        14: "Сүхбаатар аймаг",
        15: "Төв аймаг",
        16: "Увс аймаг",
        17: "Ховд аймаг",
        18: "Хэнтий аймаг",
        19: "Хөвсгөл аймаг",
        20: "Өвөрхангай аймаг",
        21: "Өмнөговь аймаг",
        22: "Багануур дүүрэг",
        23: "Улаанбаатар",
        24: "Дорноговь аймаг /Замын Үүд"
    }

subjects = {
    1: "Монгол улсын түүх",
    2: "Физик", 
    3: "Хими",
    4: "Газар зүй",
    5: "Англи хэл",
    6: "Биологи", 
    7: "Математик", 
    8: "Монгол хэл",
    9: "Орос хэл", 
    10: "Нийгэм судлал"
}

def create_states_table():
    try:
        cur = conn.cursor()

        cur.execute("create table states ( \
            id int, \
            name varchar \
        )")

        conn.commit()
    except:
        print('Table exists')

        conn.rollback()

def create_subjects_table():
    try:
        cur = conn.cursor()

        cur.execute("create table subjects ( \
            id int, \
            name varchar \
        )")

        conn.commit()
    except:
        print('Table exists')

        conn.rollback()

def insert_states_data():
    db_cursor = conn.cursor()

    for x in states:
        print(x)

        values = (x, states[x])
        db_cursor.execute("INSERT INTO states (id, name) VALUES (%s, %s)", values)

    conn.commit()

def insert_subjects_data():
    db_cursor = conn.cursor()

    for x in subjects:
        print(x)

        values = (x, subjects[x])
        db_cursor.execute("INSERT INTO subjects (id, name) VALUES (%s, %s)", values)

    conn.commit()


conn = get_conn()

create_states_table()
create_subjects_table()

insert_states_data()
insert_subjects_data()
