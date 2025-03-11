import re

def name_of_email(addr):
    result = re.match(r'^<?(\w+\s*\w*)>?\s*\w*@\w+\.\w+$', addr)
    if result:
        return result.group(1)
    else:
        return None

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')