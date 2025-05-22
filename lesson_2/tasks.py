# 1
number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

if number_1 > number_2:
    print("Первое число больше второго")
elif number_1 == number_2:
    print("Числа равны")
else:
    print("Второе число больше первого")


# 2
number_3 = int(input("Введите число: "))
if (number_3 % 2 != 0):
    print("Число нечётное")
else:
    print("Число чётное")

# 3
number_4 = int(input("Введите число: "))
if (number_4 > 0):
    print("Число положительное")
elif (number_4 == 0):
    print("Число равно нулю")
else:
    print("Число отрицательное")

# 4
number_5 = int(input("Введите первое число: "))
number_6 = int(input("Введите второе число: "))
operation = input("Введите операцию (значком): ")

if (operation == "+"):
    print("Результат: " + str(number_5 + number_6))
elif (operation == "-"):
    print("Результат: " + str(number_5 - number_6))
elif (operation == "*"):
    print("Результат: " + str(number_5 * number_6))
elif (operation == "/" and number_6 != 0):
    print("Результат: " + str(number_5 / number_6))
elif (operation == "/" and number_6 == 0):
    print("Ошибка! Делить на ноль нельзя!")
else:
    pass

# 5
year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("Год високосный")
else:
    print("Год невисокосный")

# 6
time = int(input("Введите время в часах: "))
if (5 >= time >= 0):
    print("Сейчас ночь")
elif (11 >= time >= 6):
    print("Сейчас утро")
elif (17 >= time >= 12):
    print("Сейчас день")
elif (18 >= time >= 23):
    print("Сейчас вечер")
else:
    pass

# 7
password = input("Введите пароль: ")

if (password == "secret12345"):
    print("Доступ разрешён")
else:
    print("Доступ разрешён")

# 8

number_7 = int(input("Введите число: "))

if (number_7 % 3 == 0 and number_7 % 5 != 0):
    print("Fizz")
elif (number_7 % 3 != 0 and number_7 % 5 == 0):
    print("Buzz")
elif (number_7 % 3 == 0 and number_7 % 5 == 0):
    print("FizzBuzz")
else:
    print("Простое число")

# 9
figure = input("Введите фигуру: ")

if (figure == "круг"):
    rad = int(input("Введите радиус круга: "))
    square = print("Площадь круга равна: " + str(3.14 * rad ** 2))
elif (figure == "прямоугольник"):
    weight = int(input("Введите ширину прямоугольника: "))
    height = int(input("Введите длину прямоугольника: "))
    square = print("Площадь прямоугольника равна: " + str(weight * height))
elif (figure == "треугольник"):
    weight = int(input("Введите ширину треугольника: "))
    height = int(input("Введите высоту треугольника: "))
    square = print("Площадь треугольника равна: " + str(0.5 * weight * height))
else:
    pass

# 10

tempo = int(input("Введите температуру в C*: "))

print("Температура равна " + str(tempo * 9 / 5 + 32) + " Фаренгейт")
