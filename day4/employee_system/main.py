# main.py
from employee import add_employee, list_employees, search_employee, delete_employee

while True:
    print("欢迎使用员工信息管理系统")
    print("1. 添加员工\n2. 查看所有员工\n3. 搜索员工\n4. 删除员工\n5. 退出")
    choice = input("请输入操作编号：")
    if choice == "1":
        add_employee()
    elif choice == "2":
        list_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        break
    else:
        print("无效输入")