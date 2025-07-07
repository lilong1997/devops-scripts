# 定义函数
def greet():
    print("Hello!")

# 带参数
def greet(name):
    print(f"Hello, {name}")

# 默认参数
def greet(name="Ethan"):
    print(f"Hello, {name}")

# 返回值
def add(a, b):
    return a + b

# 多个返回值（元组）
def calc(a, b):
    return a + b, a * b

# 全局变量和局部变量
count = 0

def increase():
    global count
    count += 1

# 异常处理 try/except
try:
    num = int(input("请输入数字: "))
except ValueError:
    print("你没有输入数字")

# 多种异常
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以0")
except Exception as e:
    print("其他错误", e)

# 总是执行 finally
try:
    f = open("file.txt")
except:
    print("打开失败")
finally:
    print("程序结束")



# 命令行工具参数（argparse）
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name', help='服务名')
args = parser.parse_args()

print("你输入的服务是：", args.name)


