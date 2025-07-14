import pytest
from employee_system.main_web import app
import json

@pytest.fixture
def client():
    # 清空数据文件
    with open('data.json', 'w') as f:
        json.dump([], f)

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_employee_ping(client):
    res = client.get('/ping')
    assert res.status_code == 200
    assert res.get_json() == {'msg': 'pong'}

def test_employee_get_employees(client):
    res = client.get('/employees')
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_employee_add_employee(client):
    payload = {
        'name': 'Jeff',
        'age': 30,
        'title': 'cto',
        'email': 'jeff@qq.com'
    }
    res = client.post('/employees', json=payload)
    assert res.status_code == 200
    assert res.json['msg'] == '添加成功！'

def test_employee_add_employee_field(client):
    payload = {
        'name': 'Zari',
        'age': 33,
        'title': 'front'
        # 缺少email
    }

    res = client.post('/employees', json=payload)
    assert res.status_code == 400
    assert '数据验证失败' in res.json['msg']

def test_employee_add_employee_invalid_email(client):
    payload = {
        'name': 'Zoe',
        'age': 35,
        'title': 'front',
        # email格式不对
        'email': 'not-an-email'
    }

    res = client.post('/employees', json=payload)
    assert res.status_code == 400
    assert res.json['msg'] == '数据验证失败'

def test_employee_search_employee(client):
    payload = {
        'name': 'Tom',
        'age': 29,
        'title': 'coo',
        'email': 'tom@qq.com'
    }

    client.post('/employees', json=payload)

    res = client.get('/employees/Tom')
    assert res.status_code == 200
    assert isinstance(res.json, dict)

def test_employee_search_employee_nonexist(client):
    payload = {
        'name': 'Tfboy',
        'age': 57,
        'title': 'coo',
        'email': 'tfboy@qq.com'
    }

    client.post('/employees', json=payload)

    res = client.get('/employees/Tfboys')
    assert res.status_code == 404
    assert res.json['msg'] == '查无此人'


def test_employee_update_employee(client):
    payload = {
        'name': 'Ethan',
        'age': 35,
        'title': 'ops',
        'email': 'ethan@qq.com'
    }

    client.post('/employees', json=payload)

    update = {
        'title': 'ops-admin'
    }

    res = client.put('/employees/Ethan', json=update)
    assert res.status_code == 200
    assert res.json['msg'] == '更新员工信息成功'

def test_employee_filter_by_title(client):
    client.post('/employees', json={
            'name': 'Eason',
            'age': 29,
            'title': 'security',
            'email': 'eason@qq.com'
        })

    client.post('/employees', json={
            'name': 'Jerry',
            'age': 28,
            'title': 'security',
            'email': 'jerry@qq.com'
        })

    res = client.get('/employees/title/security')
    assert res.status_code == 200
    assert isinstance(res.json, list)
    assert len(res.json) >= 2

    res2 = client.get('/employees/title/nonexisttitle')
    assert res2.status_code == 404
    assert res2.json['msg'] == '没有这个职位'

def test_employee_delete_employee(client):
    client.post('/employees', json={
            'name': 'Easy',
            'age': 29,
            'title': 'security',
            'email': 'ethan@qq.com'
        })

    client.post('/employees', json={
            'name': 'Tech',
            'age': 28,
            'title': 'security',
            'email': 'tom@qq.com'
        })
    
    res = client.delete('/employees/Tech')
    assert res.status_code == 200
    assert res.json['msg'] == '删除成功'

    res2 = client.delete('/employees/Tech')
    assert res2.status_code == 404
    assert res2.json['msg'] =='查无此人'