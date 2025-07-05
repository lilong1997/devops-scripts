# guess the number
# version1
# import random
# result = random.randint(1, 100)
# try_times = 0
# game_over = False
# while game_over == False:
#     user_input = int(input("猜一个 1~100 的数字："))
#     if user_input > result:
#         print("太大了！")
#         try_times += 1
#     elif user_input < result:
#         print("太小了！")
#         try_times += 1
#     else:
#         try_times += 1
#         print("猜对了！", end="")
#         print(f"你一共猜了{try_times}次")
#         game_over = True


# version2
import random
result = random.randint(1, 100)
user_guess_list = []
try_times = 0
max_try_times = 10
while True:
    if try_times < max_try_times:
        user_guess = int(input("猜一个1~100的数字："))
        user_guess_list.append(user_guess)
        if user_guess == result:
            try_times += 1
            print(f"猜对了！你一共猜了{try_times}次，你猜过的数字有", end="")
            print(user_guess_list)
            break
        elif user_guess < result:
            try_times += 1
            print("太小了！")
        else:
            try_times += 1
            print("太大了！")
    else:
        print("你已经超过最大游戏次数")
        break