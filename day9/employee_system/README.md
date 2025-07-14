# employee_system

一个基于 Python 构建的简单员工信息管理 CLI 工具。支持添加、查询、搜索、删除员工。

## 使用方法

```bash
python -m employee_system.main_cli --add --name 张三 --age 28 --title 运维
python -m employee_system.main_cli --list


---

### ✅ 2. 支持 pip 安装（变成 `emp` 命令）

只需运行以下命令：

```bash
pip install -e .

然后你就可以在命令行直接运行：

emp --list
