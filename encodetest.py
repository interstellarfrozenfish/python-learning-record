import gzip
from urllib import request

URL = "https://api.weatherapi.com/v1/current.xml?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no"

def get_data(url):
    req = request.Request(url)
    req.add_header("Accept-Encoding", "gzip")  # 确保服务器返回 gzip
    with request.urlopen(req) as f:
        if f.info().get("Content-Encoding") == "gzip":
            print("🔍 发现 gzip 压缩，正在解压...")
            data = gzip.decompress(f.read())  # 解压缩数据
        else:
            data = f.read()
    return data.decode("utf-8", errors="ignore")  # 忽略无法解码的字符

data = get_data(URL)
print(data[:500])  # 预览前 500 个字符，看看是否解码成功
print("OK")  # 如果输出 OK，则表示解码成功  