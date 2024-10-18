import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_data():
    url = 'https://www.nasdaq.com/market-activity/stocks/aapl/historical'  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Exemplo de extração (ajuste conforme o site escolhido)
    data = []
    table = soup.find('table', {'class': 'historical-data__table'})
    rows = table.find('tbody').find_all('tr')

    for row in rows[:10]:  # Pegar os últimos 10 dias
        cols = row.find_all('td')
        date_str = cols[0].text.strip()
        open_price = cols[1].text.strip()
        high_price = cols[2].text.strip()
        low_price = cols[3].text.strip()
        close_price = cols[4].text.strip()
        volume = cols[5].text.strip()

        data.append({
            'Date': date_str,
            'Open': open_price,
            'High': high_price,
            'Low': low_price,
            'Close': close_price,
            'Volume': volume
        })

    return data
