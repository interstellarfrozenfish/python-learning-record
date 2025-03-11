args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc,报错：
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc,且至少指定了一个文件：
    case ['gcc', file1, *files]:
        print('gcc comolie: ' + file1 + ',' + ','.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
