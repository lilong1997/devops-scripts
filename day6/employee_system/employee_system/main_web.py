from flask import Flask, request, jsonify
from .storage import load_data, save_data

app = Flask(__name__)

@app.route('/employees', methods=['GET'])
def get_employees():
    data = load_data()
    return jsonify(data)

@app.route('/employees', methods=['POST'])
def add_employee():
    info = request.get_json()
    required_fields = ['name', 'age', 'title', 'email']
    if not all(field in info and info[field] for field in required_fields):
            return jsonify({'msg': '添加员工必须包含name, age, title, email'}), 400
    data = load_data()
    data.append(info)
    save_data(data)
    return jsonify({'msg': '添加成功！'})

@app.route('/employees/<name>', methods=['PUT'])
def update_employee(name):
    data = load_data()
    info = request.get_json()
    for emp in data:
        if emp['name'] == name:
            if 'age' in info and info['age']:
                emp['age'] = info['age']
            if 'title' in info and info['title']:
                emp['title'] = info['title']
            if 'email' in info and info['email']:
                emp['email'] = info['email']
            save_data(data)
            return jsonify({'msg': '更新员工信息成功'})
    return jsonify({'msg': '查无此人'}), 404

@app.route('/employees/title/<title>', methods=['GET'])
def filter_by_title(title):
    data = load_data()
    result = []
    for emp in data:
        if emp['title'] == title:
            result.append(emp)
    if result:
        return jsonify(result)
    else:
        return jsonify({'msg': '查无此人'}), 404

@app.route('/employees/<name>', methods=['GET'])
def search_employee(name):
    data = load_data()
    for emp in data:
        if emp['name'] == name:
            return jsonify(emp)
    return jsonify({'msg': '查无此人'}), 404

@app.route('/employees/<name>', methods=['DELETE'])
def delete_employee(name):
    data = load_data()
    for i, emp in enumerate(data):
        if emp['name'] == name:
            del data[i]
            save_data(data)
            return jsonify({'msg': '删除成功'})
    return jsonify({'msg': '查无此人'}), 404

@app.route('/ping', methods=['GET'])
def print_pong():
    return jsonify({'msg': 'pong'})

if __name__ == "__main__":
    app.run(debug=True)