import unittest
from unittest.mock import Mock
from web_scraper import WebScraper

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = WebScraper()

    def test_scrape_web_page_successful(self):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = """
            <html>
                <head>
                    <title>Тестовая страница</title>
                </head>
                <body>
                    <a href="https://example.com">Ссылка 1</a>
                    <a href="https://example.org">Ссылка 2</a>
                </body>
            </html>
        """
        self.scraper.requests.get = Mock(return_value=mock_response)

        result = self.scraper.scrape_web_page('https://example.com')

        expected_result = {
            'title': 'Тестовая страница',
            'links': [
                {'text': 'Ссылка 1', 'href': 'https://example.com'},
                {'text': 'Ссылка 2', 'href': 'https://example.org'},
            ]
        }
        self.assertEqual(result, expected_result)

    def test_scrape_web_page_http_error(self):
        mock_response = Mock()
        mock_response.status_code = 404
        self.scraper.requests.get = Mock(return_value=mock_response)

        result = self.scraper.scrape_web_page('https://example.com')

        self.assertEqual(result, {'error': 'HTTP Error'})

    def test_scrape_web_page_network_error(self):
        self.scraper.requests.get = Mock(side_effect=ConnectionError('Network Error'))

        result = self.scraper.scrape_web_page('https://example.com')

        self.assertEqual(result, {'error': 'Network Error'})

if __name__ == '__main__':
    unittest.main()
