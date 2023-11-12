import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        self.requests = requests
    def scrape_web_page(self,url):
        try:
            responce = requests.get(url)
            if(responce.status_code == 200):
                soup = BeautifulSoup(responce.text, 'html.parser')
                page_tittle = soup.title.string
                links = []
                for link in soup.find_all('a'):
                    link_text = link.get_text()
                    link_href = link.get('href')
                    links.append({'text':link_text, 'href': link_href})
                return {'title':page_tittle, 'links':links}
            else:
                return {'error': 'HTTP Error'}
        except Exception as e:
            return {'error':str(e)}