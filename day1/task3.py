# task3
grade1 = int(input("grade1"))
grade2 = int(input("grade2"))
grade3 = int(input("grade3"))
ave_grade = (grade1 + grade2 + grade3) / 3
print(ave_grade)
if ave_grade >= 60:
    print("pass the exam")
else:
    print("faild to pass")