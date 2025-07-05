# task5
word = "hello world"
result = {}
for i in word:
    if i in result:
        result[i] += 1;
    else:
        result[i] = 1
for key, value in result.items():
    print(f"{key}: {value}")
