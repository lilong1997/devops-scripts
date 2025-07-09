# main_cli.py
from .employee import add_employee_cli, list_employees, search_employee_cli, delete_employee_cli
import argparse

def main():
    # 四种操作
    parser = argparse.ArgumentParser(description="员工信息管理系统")
    parser.add_argument('--list', action='store_true', help="查看所有员工")
    parser.add_argument('--add', action='store_true', help="添加员工")
    parser.add_argument('--search', action='store_true', help="搜索员工")
    parser.add_argument('--delete', action='store_true', help="删除员工")

    # 通用字段
    parser.add_argument('--name', help="姓名")
    parser.add_argument('--age', type=int, help="年龄")
    parser.add_argument('--title', help="职位")

    args = parser.parse_args()


    if args.list:
        list_employees()
    elif args.add:
        if args.name and args.age and args.title:
            add_employee_cli(args.name, args.age, args.title)
        else:
            print("添加员工需要 --name --age --title")
    elif args.search:
        if args.name:
            search_employee_cli(args.name)
        else:
            print("搜索员工需要 --name")
    elif args.delete:
        if args.name:
            delete_employee_cli(args.name)
        else:
            print("删除员工需要 --name")
    else:
        parser.print_help


if __name__ == "__main__":
    main()