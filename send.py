from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令：
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址
to_addr = input('To: ')
# 输入SMTP服务器地址：
smtp_server = input('SMTP server: ')

# 修改邮件内容
msg = MIMEMultipart()
msg['From'] = _format_addr('Python测试者 <%s>' % from_addr)
msg['To'] = _format_addr('收件人 <%s>' % to_addr)
msg['Subject'] = Header('关于 Python SMTP 发送测试', 'utf-8').encode()

msg.attach(MIMEText("你好，我正在测试用 Python 发送邮件，希望它能够顺利送达！\n\n此邮件仅用于测试 SMTP 发送功能。", 'plain', 'utf-8'))

with open("D:/selfstudying/code/python/learn_python/file2/test.jpg", 'rb') as f:
    mime = MIMEBase('image', 'png', filename='test.png')
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()