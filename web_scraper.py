import requests
from bs4 import BeautifulSoup

class WebScraper:
    def scrape_web_page(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Извлекаем заголовок страницы
                page_title = soup.title.string

                # Извлекаем все ссылки на странице
                links = []
                for link in soup.find_all('a'):
                    link_text = link.get_text()
                    link_href = link.get('href')
                    links.append({'text': link_text, 'href': link_href})

                return {'title': page_title, 'links': links}
            else:
                return {'error': 'HTTP Error'}
        except Exception as e:
            return {'error': str(e)}