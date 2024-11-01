from spiders import main_spider

if __name__ == "__main__":
    url = "https://example.com"
    spider = main_spider.MainSpider(url)
    html = spider.fetch()
    if html:
        parsed_data = spider.parse(html)
        print(parsed_data)
