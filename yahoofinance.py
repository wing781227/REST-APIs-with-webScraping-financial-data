import requests
from bs4 import BeautifulSoup

def getStockData(symbol):
    headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
        'symbol': symbol,
        'Previous Close': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test': 'PREV_CLOSE-value'}).text,
        'Open': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'OPEN-value'}).text,
        'Bid': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'BID-value'}).text,
        'Ask': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'ASK-value'}).text,
        'Day\'s Range': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'DAYS_RANGE-value'}).text,
        '52 Week Range': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'FIFTY_TWO_WK_RANGE-value'}).text,
        'Volume': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'TD_VOLUME-value'}).text,
        'News': soup.find('a', {'data-wf-caas-prefetch':'1'}).text,
        'current price': soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,
        'current time': soup.find('div', {'class': 'C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm Whs(n)'}).text,
        'News_links': soup.find('a', {'data-wf-caas-prefetch': '1'}).get('href'),
    } 
    return stock

# print(getStockData('TSM'))


def getNewsData(symbol):
    headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = {
        'symbol': symbol,
        'title': soup.find('a', {'data-wf-caas-prefetch':'1'}).text,
        'News_links': soup.find('a', {'data-wf-caas-prefetch': '1'}).get('href'),
        'current price': soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,
        'current time': soup.find('div', {'class': 'C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm Whs(n)'}).text
    }

    data_uuid = soup.find('a', {'data-wf-caas-prefetch': '1'}).get('data-uuid')
    
    url = 'https://finance.yahoo.com/'+data['News_links']
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    News_published_time = soup.find('time').get('datetime')
    data['News_published_time'] = News_published_time
    return data, data_uuid




    