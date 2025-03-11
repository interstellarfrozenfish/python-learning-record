from urllib.request import Request, urlopen


def get_data(url):
    '''    GET请求到指定的页面    :return:HTTP响应    '''    
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'        }
    req = Request(url, headers=headers)
    with urlopen(req, timeout=10) as f:
        data = f.read()
        print(f'Status: {f.status} {f.reason}')
        print()
    return data.decode('utf-8')


class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.__parsedata = ''  # 设置一个空的标志位        
        self.info = {'name':[], 'time':[], 'location':[]}

    def handle_starttag(self, tag, attrs):
        if('class', 'event-title') in attrs:
            self.__parsedata = 'name'        
        if tag == 'time':
            self.__parsedata = 'time'       
        if('class', 'event-location') in attrs:
            self.__parsedata = 'location'    
def handle_endtag(self, tag):
        self.__parsedata = ''    
def handle_data(self, data):
        if self.__parsedata == 'name':
            self.info['name'].append(data)
        if self.__parsedata == 'time':
            self.info['time'].append(data)
        if self.__parsedata == 'location':
            self.info['location'].append(data)

def main():
    parser = MyHTMLParser()
    URL = 'https://www.python.org/events/python-events/'    
    data = get_data(URL)
    parser.feed(data)
    num = len(parser.info['location'])

    for i in range(num):
        str = ''        
        str += '会议名称:' + parser.info['name'][i]+'\n'        
        str += '会议时间:' + parser.info['time'][i*2]+' '+parser.info['time'][i*2+1]+'\n'        
        str += '会议地点:' + parser.info['location'][i]+'\n'        
        print(str+'\n')

if __name__ == '__main__':
    main()
