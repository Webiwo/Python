import unittest
from unittest.mock import patch, Mock
from web_scraper.hacker_news import scrap_hacker_news


class TestScrapHackerNews(unittest.TestCase):
    @patch("web_scraper.hacker_news.requests.get")
    def test_scrap_hacker_news_returns_top_article(self, mock_get):

        fake_html = '''
        <html>
            <body>
                <span class="titleline">
                    <a href="https://example.com/article1">Article One</a>
                </span>
                <span class="score">100 points</span>

                <span class="titleline">
                    <a href="https://example.com/article2">Article Two</a>
                </span>
                <span class="score">250 points</span>
            </body>
        </html>
        '''

        mock_response = Mock()
        mock_response.text = fake_html
        mock_get.return_value = mock_response

        title, link, votes = scrap_hacker_news()

        self.assertEqual(title, "Article Two")
        self.assertEqual(link, "https://example.com/article2")
        self.assertEqual(votes, 250)


    @patch("web_scraper.hacker_news.requests.get")
    def test_scrap_hacker_news_with_empty_html(self, mock_get):
        mock_response = Mock()
        mock_response.text = "<html><body></body></html>"
        mock_get.return_value = mock_response

        title, link, votes = scrap_hacker_news()
        self.assertIsNone(title)
        self.assertIsNone(link)
        self.assertEqual(votes, 0)


    @patch("web_scraper.hacker_news.requests.get")
    def test_scrap_hacker_news_with_failed_request(self, mock_get):
        mock_get.side_effect = Exception("Network error")

        title, link, votes = scrap_hacker_news()
        self.assertIsNone(title)
        self.assertIsNone(link)
        self.assertEqual(votes, 0)


if __name__ == "__main__":
    unittest.main()
