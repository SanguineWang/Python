import urllib.request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
       #方法1
        response =  urllib.request.urlopen(url)
        if response.getcode()!=200:
            return None

        return response.read()

    def download1(self, url):
        # 方法二
        request = urllib.request.Request(url)
        request.add_header("user-agent", "Mozilia/0.5")
        response2 = urllib.request.urlopen(url)
        print(response2.getcode())
        print(len(response2.read()))
        if response2.getcode() != 200:
            return None
        return response2.read()


