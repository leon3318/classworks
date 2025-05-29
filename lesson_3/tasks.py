# 1
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# 2
string = input("Введите строку: ")
for i in string:
    print(i)

# 3
num = int(input("Введите число: "))
for i in range(1, 16):
    print(num, "умножить на", i, "равно", num*i)

# 4
sum_2 = 0
num_2 = int(input("Введите число: "))
for i in range(1, num_2 + 1):
    if (i % 2 != 0):
        continue
    sum_2 += i
print(sum_2)

# 5
n = int(input("Введите число: "))
sum_3 = 0
i = 1
while (i <= n):
    if (i % 3 == 0):
        sum_3 += i
    i += 1
print(sum_3)

# 6
num_3 = int(input("Введите число: "))
if (num_3 > 1):
    for i in range(2, int(num_3 / 2 + 1)):
        if (num_3 % i == 0):
            print("Число не является простым!")
            break
    else:
        print("Число простое!")
else:
    print("Число должно быть больше 1")
