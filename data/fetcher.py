import requests
import sys

def get_data(link):
    d = requests.get(link)

    return d.text

def get_2024():
    for x in range(1,25):
        for y in range(1, 11):
            url = 'http://list.eec.mn/' + str(x) + '/' + str(y) + '.html'

            res = get_data(url)

            with open('2024/' + str(x) + '-' + str(y) + '.html', 'w') as file:
                file.write(res)

def get_2025():
    for x in range(1,24):
        for y in range(1, 11):
            url = 'http://list.eec.mn/2025/' + str(x) + '/' + str(y) + '.html'

            res = get_data(url)

            with open('2025/' + str(x) + '-' + str(y) + '.html', 'w') as file:
                file.write(res)

if __name__ == '__main__':
    if(sys.argv[1] == '2024'):
        get_2024()

    if(sys.argv[1] == '2025'):
        get_2025()