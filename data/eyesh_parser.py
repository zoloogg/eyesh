import json
from bs4 import BeautifulSoup
import sys

def parse_data(year, state_id, subject_id, filename):
    try:
        f = open(filename, "r")

        data = f.read()
        parsed_html = BeautifulSoup(data)

        rows = parsed_html.find('table').findAll('tr')

        data = []

        isSkipped = False
        for r in rows:
            tds = r.findAll('td')

            rank = tds[0].getText().strip()
            registration_number = tds[1].getText().strip()
            raw_score = tds[2].getText().strip()
            calculated_score = tds[3].getText().strip()
            percentile = tds[4].getText().strip()
            grade = tds[5].getText().strip()

            cur = {
                "year": year,
                "state": state_id,
                "subject": subject_id,
                "rank": rank,
                "registration_number": registration_number,
                "raw_score": raw_score,
                "calculated_score": calculated_score,
                "percentile": percentile,
                "grade": grade
            }

            if(isSkipped == False):
                isSkipped = True
            else:
                data.append(cur)

        return data
    except:
        print('FAIL')
        return []

def parse_2024():
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


    for x in states:
        for y in subjects:
            jjj = parse_data(2024,x,y, '2024/html/' + str(x) + '-' + str(y) + '.html')

            print(x,y,len(jjj))
            with open('2024/json/' + str(x) + '-' + str(y) + '.json', 'w') as file:
                file.write(json.dumps(jjj))

def parse_2025():
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
        23: "Улаанбаатар"
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


    for x in states:
        for y in subjects:
            jjj = parse_data(2025,x,y, '2025/html/' + str(x) + '-' + str(y) + '.html')

            print(x,y,len(jjj))
            with open('2025/json/' + str(x) + '-' + str(y) + '.json', 'w') as file:
                file.write(json.dumps(jjj))

if __name__ == '__main__':
    if(sys.argv[1] == '2024'):
        parse_2024()

    if(sys.argv[1] == '2025'):
        parse_2025()