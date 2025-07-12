# employee.py
from ..storage import load_data, save_data

def add_employee(data: list, info: dict) -> None:
    data.append(info)


def list_employees(data: list) -> list:
    return data


def search_employee(data: list, name: str) -> tuple:       
    for employee in data:
        if employee['name'] == name:
            return employee, True
    return None, False

def delete_employee(data: list, name: str) -> tuple:
    for i, employee in enumerate(data):
        if employee['name'] == name:
            del data[i]
            return data, True
    return data, False

def update_employee(data: list,name: str, info: dict) -> tuple:
    for emp in data:
        if emp['name'] == name:
            update_fields = ['age', 'title', 'email']
            update = False
            for field in update_fields:
                if field in info and info[field]:
                    emp[field] = info[field]
            return data, True
    return data, False

def filter_by_title(data: list, title: str) -> tuple:
    result = []
    for emp in data:
        if emp['title'] == title:
            result.append(emp)
    if result:
        return result, True
    else:
        return result, False