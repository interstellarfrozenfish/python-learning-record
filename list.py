import os
import stat
import time

def list_dir_l(path="."):
    """ 模拟 `dir -l` 命令，列出文件详细信息 """
    try:
        # 获取当前目录下的所有文件和目录
        files = os.listdir(path)
    except FileNotFoundError:
        print(f"错误: 目录 '{path}' 不存在")
        return
    except PermissionError:
        print(f"错误: 无法访问 '{path}'")
        return

    print(f"总计: {len(files)}")
    
    for file in files:
        file_path = os.path.join(path, file)
        
        # 获取文件状态信息
        file_stat = os.stat(file_path)
        
        # 获取文件权限
        permissions = stat.filemode(file_stat.st_mode)
        
        # 获取文件大小
        size = file_stat.st_size
        
        # 获取修改时间
        mod_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_stat.st_mtime))
        
        # 判断是否是目录
        if os.path.isdir(file_path):
            file = f"\033[34m{file}\033[0m"  # 让目录名变蓝色（仅限支持 ANSI 颜色的终端）

        print(f"{permissions}  {size:10}  {mod_time}  {file}")

# 运行程序
if __name__ == "__main__":
    list_dir_l()  # 列出当前目录的文件信息
