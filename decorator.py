import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return result
    return wrapper

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call')
        result = func(*args, **kw)
        print('end call')
        return result
    return wrapper

def log1(text = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if text:
                print('%s %s():' % (text, func.__name__))
            else:
                print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


# 测试

@log
@metric
@log1('execute')
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@log
@metric
@log1('execute')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')