from flask import Flask, request, jsonify
from .storage import load_data, save_data
from .employee.logic import add_employee, list_employees, search_employee, delete_employee, update_employee, filter_by_title
from .employee.schemas import Employee, UpdateEmployee 
from pydantic import ValidationError

app = Flask(__name__)

@app.route('/employees', methods=['GET'])
def get_employees_view():
    data = load_data()
    result = list_employees(data)
    return jsonify(result)

@app.route('/employees', methods=['POST'])
def add_employee_view():
    try:
        info = request.get_json()
        emp = Employee(**info)
    except ValidationError as e:
        return jsonify({'msg': '数据验证失败', 'details': e.errors()}), 400
    data = load_data()
    add_employee(data, emp.model_dump())
    save_data(data)
    return jsonify({'msg': '添加成功！'})

@app.route('/employees/<name>', methods=['PUT'])
def update_employee_view(name):
    try:
        info = request.get_json()
        emp = UpdateEmployee(**info)
    except ValidationError as e:
        return jsonify({'msg': '数据校验失败', 'details': e.errors()}), 400
    
    data = load_data()
    update_data = {k: v for k, v in emp.model_dump().items if v is not None}
    new_data, success = update_employee(data, name, update_data)
    save_data(new_data)
    if success:
        return jsonify({'msg': '更新员工信息成功'})
    else:
        return jsonify({'msg': '查无此人'}), 404

@app.route('/employees/title/<title>', methods=['GET'])
def filter_by_title_view(title):
    data = load_data()
    result, success = filter_by_title(data, title)
    if success:
        return jsonify(result)
    else:
        return jsonify({'msg': '查无此人'}), 404

@app.route('/employees/<name>', methods=['GET'])
def search_employee_view(name):
    data = load_data()
    result, success = search_employee(data, name)
    if success:
        return jsonify(result)
    else:
        return jsonify({'msg': '查无此人'}), 404

@app.route('/employees/<name>', methods=['DELETE'])
def delete_employee_view(name):
    data = load_data()
    new_data, success = delete_employee(data, name)
    save_data(new_data)
    if success:
        return jsonify({'msg': '删除成功'})
    else:
        return jsonify({'msg': '查无此人'}), 404

@app.route('/ping', methods=['GET'])
def print_pong_view():
    return jsonify({'msg': 'pong'})

if __name__ == "__main__":
    app.run(debug=True)