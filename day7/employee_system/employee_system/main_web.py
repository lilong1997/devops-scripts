from flask import Flask, request, jsonify
from .storage import load_data, save_data
from .employee.logic import add_employee, list_employees, search_employee, delete_employee, update_employee, filter_by_title

app = Flask(__name__)

@app.route('/employees', methods=['GET'])
def get_employees_view():
    data = load_data()
    result = list_employees(data)
    return jsonify(result)

@app.route('/employees', methods=['POST'])
def add_employee_view():
    info = request.get_json()
    required_fields = ['name', 'age', 'title', 'email']
    if not all(field in info and info[field] for field in required_fields):
            return jsonify({'msg': '添加员工必须包含name, age, title, email'}), 400
    data = load_data()
    add_employee(data, info)
    save_data(data)
    return jsonify({'msg': '添加成功！'})

@app.route('/employees/<name>', methods=['PUT'])
def update_employee_view(name):
    data = load_data()
    info = request.get_json()
    new_data, success = update_employee(data, name, info)
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