import libs.crawler as crawler

url = "https://news.naver.com/"
bs_obj = crawler.crawl(url)

print(bs_obj)