# task5
service = {
    'nginx': 'running',
    'redis': 'stopped',
    'docker': 'running'
}



def check_services():
    for key, value in service.items():
        print(f"服务名：{key}，运行状态：{value}")

def check_service(name):
    if name in service:
        status = service[name]
        print(f"服务名：{name}，运行状态：{status}")
    else:
        print("服务未找到")



check_services()

name = input("请输入服务名：").lower
check_service(name)