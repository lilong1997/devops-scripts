import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--name",type=str, help="服务名")
args = parser.parse_args()
print(args.name)