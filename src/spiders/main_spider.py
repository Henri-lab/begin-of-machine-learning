import requests
from bs4 import BeautifulSoup

class MainSpider:
    def __init__(self, start_url):
        self.start_url = start_url

    def fetch(self):
        response = requests.get(self.start_url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch {self.start_url}")
            return None

    def parse(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        # 这里根据需要编写解析逻辑
        return soup

if __name__ == "__main__":
    url = "https://example.com"
    spider = MainSpider(url)
    html = spider.fetch()
    if html:
        parsed_data = spider.parse(html)
        print(parsed_data)
