from bs4 import BeautifulSoup
import requests
import json

def parse_command(name:str) -> str:
    '''
    Парсим ссылку на команду. 
    '''
    url = f'https://www.sports.ru/search/search.json?query={name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        if len(data) < 1:
            return 'Комманды не найдены'
        else:
            return data['suggestions'][0]['link']

def get_command_stat(url: str) -> dict:
    response = requests.get(url + 'calendar/')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_ = 'stat-table')
    tbody = table.find('tbody')
    td = tbody.find_all('tr')
    #td = tbody.find_all('td', class_ = 'alRight padR20')
    games = []
    for line in td:
        #print('-'*10)
        where = line.find('td', class_ = 'alRight padR20').text
        #print(line.find('a', class_ = 'score').text.strip())
        data = line.find('a', class_ = 'score').text.strip()
        data = data.split(' ')
        data = [i.strip() for i in data]
        score = []
        for line in data:
            try:
                score.append(int(line))
            except ValueError:
                pass

        games.append({'where':where, 'score': score})
        #print(games)
    return games

def parse_live_games() -> dict:
    '''Вытаскиваем данные с fonbet о предстоящих играх'''
    pass

if __name__ == '__main__':
    print('test')
    print(get_command_stat(parse_command('Барс')))
