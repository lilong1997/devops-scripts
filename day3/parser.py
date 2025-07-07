# argparse 的4个核心步骤
import argparse # 第1步：导入模块
# 第2步：创建ArgumentParser对象
parser = argparse.ArgumentParser()

# 第3步：定义需要的命令行参数
parser.add_argument('--name', help='服务名称')
parser.add_argument('--port', type=int, help='端口号')

# 解析参数（重要）
args = parser.parse_args()

# 使用参数
print("服务名： ", args.name)
print("端口：", args.port)


