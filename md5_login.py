import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    # for k, v in db.items():
    #     if k == user:
    #         md5 = hashlib.md5()
    #         md5.update(password.encode('utf-8'))
    #         if md5.hexdigest() == v:
    #             return True
    #         else:
    #             return False
     # 直接获取用户的存储哈希
    stored_hash = db.get(user)
    if stored_hash is None:
        return False  # 用户不存在，直接返回 False
    
    # 计算输入密码的 MD5
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    
    # 比较哈希值
    return md5.hexdigest() == stored_hash
    

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')