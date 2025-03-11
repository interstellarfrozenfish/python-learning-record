from xml.parsers.expat import ParserCreate
from urllib import request

class DefaultSaxHandler(object):
    def __init__(self):
        self.data = {
            'city': None,
            'weather': {
                'condition': None,
                'temperature': None,
                'wind': None
            }
        }
        self.current_tag = None

    def start_element(self, name, attrs):
        self.current_tag = name
        print('sax:end_element: %s, attrs: %s' % (name, str(attrs)))
    
    def end_element(self, name):
        self.current_tag = None
        print('sax:end_element: %s' % name)    

    def char_data(self, text):
        text = text.strip()
        if not text:
            return
        print('sax:char_data: %s' % text)

        if self.current_tag == 'name':
            self.data['city'] = text
        elif self.current_tag == 'text':
            self.data['weather']['condition'] = text
        elif self.current_tag == 'temp_c':
            self.data['weather']['temperature'] = float(text)
        elif self.current_tag == 'wind_kph':
            self.data['weather']['wind'] = float(text)

def parseXml(xml_str):
    # print(xml_str)
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return handler.data

# 测试:
URL = 'https://api.weatherapi.com/v1/current.xml?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'

print('OK')