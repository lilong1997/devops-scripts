employees = []

def add_employee():
    name = input("name: ")
    age = int(input("age: "))
    title = input("title: ")
    employee = {'name': name, 'age': age, "title": title}
    employees.append(employee)

def list_employees():
    if not employees:
        print("no empolyee at this time")
    for employee in employees:
        name = employee["name"]
        age = employee["age"]
        title = employee["title"]
        print(f"name: {name}, age: {age}, title: {title}")

def search_employee():
    target_name = input("input the name you are searching: ")
    found = False
    for employee in employees:
        if employee["name"] == target_name:
            found = True
            print("name: ", employee["name"])
            print("age: ", employee["age"])
            print("title: ", employee["title"])
    if not found:
        print("employee not found")

def delete_employee():
    target_name = input("input the name you are deleting: ")
    found = False
    for employee in employees:
        if employee["name"] == target_name:
            found = True
            employees.remove(employee)
            print("employee deleted successfully")
    if not found:
        print("employee not found")

while True:
    print("欢迎使用员工信息管理系统！\n" \
    "1. 添加员工 \n" \
    "2. 查看所有员工 \n" \
    "3. 搜索员工 \n" \
    "4. 删除员工 \n" \
    "5. 退出系统 \n")
    user_input = int(input("请输入操作编号："))
    if user_input == 1:
        add_employee()
    elif user_input == 2:
        list_employees()
    elif user_input == 3:
        search_employee()
    elif user_input == 4:
        delete_employee()
    elif user_input == 5:
        break
    else:
        print("输入错误，请重新输入！")