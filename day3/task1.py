# task1
def is_even(n):
    if n % 2 == 0:
        result = True
    else:
        result = False
    return result

try:
    n = int(input())
    result = is_even(n)
    print(result)
except ValueError:
    print("请输入数字")
