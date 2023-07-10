import platform
import sys
import os


def show_env():
    s = platform.platform()
    print("当前系统：", s)
    p = sys.path
    print("当前安装路径：", p)
    op = os.getcwd()
    print("当前代码路径：", op)
    print("Python版本信息：", sys.version_info)


# 进行模块的单元测试
if __name__ == "__main__":
    show_env()
