import os

def find_files(keyword, path="."):
    """
    在当前目录及所有子目录下查找文件名包含指定字符串的文件，并打印相对路径
    :param keyword: 要查找的文件名关键词
    :param path: 查找的起始目录（默认是当前目录）
    """
    for root, _, files in os.walk(path):  # 遍历当前目录及其所有子目录
        for file in files:
            if keyword in file:  # 如果文件名包含指定字符串
                rel_path = os.path.relpath(os.path.join(root, file), path)  # 获取相对路径
                print(rel_path)

# 运行程序
if __name__ == "__main__":
    search_keyword = input("请输入要查找的文件名关键字: ").strip()
    find_files(search_keyword)
