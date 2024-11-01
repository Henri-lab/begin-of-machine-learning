import unittest
from src.spiders.main_spider import MainSpider


class TestMainSpider(unittest.TestCase):

    def test_fetch(self):
        spider = MainSpider("https://example.com")
        content = spider.fetch()
        self.assertIsNotNone(content)


if __name__ == "__main__":#When a Python script is run directly, the special variable __name__ is automatically set to the string "__main__"
    unittest.main()
