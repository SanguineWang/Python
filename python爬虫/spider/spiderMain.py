from spider import urlManager, downloader, parser, outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = urlManager.UrlManager()
        self.downloader = downloader.HtmlDownloader()
        self.parser = parser.HtmlParser()
        self.outputer = outputer.HtmlOutputer()

    def craw1(self, root_url):
        # 爬取
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                # 打印当前爬取次数，和链接
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
               #爬取次数控制
                if count == 20:
                    break
                count = count + 1
            except:
                print("craw failed")

        self.outputer.output_html()

    def craw2(self, root_url):
        self.urls.add_new_url(root_url)
        new_url = self.urls.get_new_url()
        html_cont = self.downloader.download(new_url)
        if html_cont is None:
            print('下载失败')
        new_urls1 = self.parser.parse_urls(new_url, html_cont)
        self.urls.add_new_urls(new_urls1)
        count = 0
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print(new_url)
                html_cont = self.downloader.download(new_url)
                print("down_success")
                new_data= self.parser.parse_data(new_url,html_cont)
                print(new_data)
                self.outputer.collect_data(new_data)
                count = count + 1
                print(count)
            except:
                print("爬取失败")
                print("craw failed")
        self.outputer.output_html()



if __name__ == "__main__":
    root_url = "http://www.xzw.com/astro/"
    obj_spider = SpiderMain()
    #obj_spider.craw1(root_url)
    obj_spider.craw2(root_url)

