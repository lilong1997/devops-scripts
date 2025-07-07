# employee.py
from storage import load_data, save_data

def add_employee():
    employees = load_data()
    name = input("请输入姓名：")
    age = int(input("请输入年龄："))
    title = input("请输入职位：")
    new_employee = {'name': name, 'age': age, 'title': title}
    employees.append(new_employee)
    save_data(employees)
    print(f"添加员工 {name} 成功！")

def add_employee_cli(name, age, title):
    employees = load_data()
    new_employee = {'name': name, 'age': age, 'title': title}
    employees.append(new_employee)
    save_data(employees)
    print(f"添加员工 {name} 成功！")

def list_employees():
    employees = load_data()
    if not employees:
        print("现在还没有员工记录在案")
    else:
        for i, employee in enumerate(employees, start=1):
            name = employee['name']
            age = employee['age']
            title = employee['title']
            print(f"{i}. 姓名： {name}，年龄： {age}，职位： {title}")


def search_employee():
    employees = load_data()
    input_name = input("请输入你想搜索的员工姓名：")
    if not employees:
        print("现在还没有员工记录在案")
    else:
        found = False
        for employee in employees:
            if employee['name'] == input_name:
                found = True
                age = employee['age']
                title = employee['title']
                print(f"姓名：{input_name}，年龄： {age}，职位： {title}")
        if not found:
            print("查无此人")

def search_employee_cli(name):
    employees = load_data()
    
    if not employees:
        print("现在还没有员工记录在案")
    else:
        found = False
        for employee in employees:
            if employee['name'] == name:
                found = True
                age = employee['age']
                title = employee['title']
                print(f"姓名：{name}，年龄： {age}，职位： {title}")
        if not found:
            print("查无此人")

def delete_employee():
    employees = load_data()
    input_name = input("请输入你想删除的员工姓名：")
    if not employees:
        print("现在还没有员工记录在案")
    else:
        found = False
        for i, employee in enumerate(employees):
            if employee['name'] == input_name:
                found = True
                del employees[i]
                save_data(employees)
                print(f"删除员工 {input_name} 成功")
                break
        if not found:
            print("查无此人")

def delete_employee_cli(name):
    employees = load_data()
    if not employees:
        print("现在还没有员工记录在案")
    else:
        found = False
        for i, employee in enumerate(employees):
            if employee['name'] == name:
                found = True
                del employees[i]
                save_data(employees)
                print(f"删除员工 {name} 成功")
                break
        if not found:
            print("查无此人")