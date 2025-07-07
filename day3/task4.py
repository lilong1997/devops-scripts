# task4
def calculate():
    try:
        num1 = int(input("请输入第一个数字："))
        num2 = int(input("请输入第二个数字："))
        method = input("请输入运算符：")
        if method == "+":
            return print(num1 + num2)
        elif method == "-":
            return print(num1 - num2)
        elif method == "*":
            return print(num1 * num2)
        elif method == "/":
            return print(num1 / num2)
        else:
            return print("非法运算符")
    except ValueError:
        print("请输入数字！")
    except ZeroDivisionError:
        print("除数不能为0")
    except Exception as e:
        print("其他错误", e)

calculate()