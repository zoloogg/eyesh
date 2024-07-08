import requests
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

get_2024()