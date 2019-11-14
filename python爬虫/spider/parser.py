import re
from urllib import parse
from urllib.parse import urlparse



#解析器
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, new_url, html_cont):
        if new_url is None or html_cont is None:
            return 0
        soup = BeautifulSoup(html_cont, 'html.parser',from_encoding='utf-8')
        new_urls= self._get_new_urls(new_url,soup)
        new_data= self._get_new_data(new_url,soup)
        return  new_urls,new_data

    def parse_urls(self, new_url, html_cont):
        if new_url is None or html_cont is None:
            return 0
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(new_url, soup)

        return new_urls

    def parse_data(self, new_url, html_cont):
        if new_url is None or html_cont is None:
            return 0
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

        new_data = self._get_new_data(new_url, soup)
        return  new_data

    def _get_new_urls(self, page_url, soup, ):
        new_urls = set()
   #<a target="_blank" href="/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80/7073760" data-lemmaid="7073760">计算机程序设计语言</a>
   #<div class="a-nav">
   #<a class="icon0" target="_blank" href="/astro/aries/" hidefocus="true" title="白羊座"></a>
        links=soup.find('div',class_="a-nav").find_all('a',href=re.compile(r"/astro/*/"))
        for link in links:
            new_url = link ['href']
            new_full_url = parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data={}
        res_data['url'] =page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        #<div class="info"><dl><dt><span><i class="xz_1"></i></span><h1><strong class="f_yh">白羊座</strong>
        title_node = soup.find('div',class_="info").find('h1').find('strong',class_="f_yh")
        res_data['title']=title_node.get_text()
        print(res_data['title'])
        #<small>3月21日-4月19日</small>
        data_node = soup.find('div',class_="info").find('h1').find('small')
        res_data['data']=data_node.get_text()
        print(res_data['data'])

       #< div class ="lemma-summary" label-module="lemmaSummary" >
        #<dd><p>白羊座有一种让人看见就觉得开心的感觉，因为总是看起来都是那么地热情、阳光、乐观、坚强，对朋友也慷概大方，性格直来直往，就是有点小脾气。白羊男有大男人主义的性格，而白羊女就是女汉子的形象。</p>
        summary_node = soup.find('div',class_="info").find('dd').find('p')
        res_data['summary'] = summary_node.get_text()
        print(res_data['summary'])

        return res_data
