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
elif (operation == "/"):
    if (number_6 == 0):
        print("Ошибка! На ноль делить нельзя!")
    else:
        print("Результат: " + str(number_5 / number_6))
else:
    print("Некорректная операция!")

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
    print("Некорректное время!")

# 7
password = input("Введите пароль: ")

if (password == "secret12345"):
    print("Доступ разрешён")
else:
    print("Доступ запрещён")

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
    rad = float(input("Введите радиус круга: "))
    print("Площадь круга равна: " + str(round(3.14 * rad ** 2), 2))
elif (figure == "прямоугольник"):
    weight = float(input("Введите ширину прямоугольника: "))
    height = float(input("Введите длину прямоугольника: "))
    print("Площадь прямоугольника равна: " + str(round(weight * height), 2))
elif (figure == "треугольник"):
    weight = float(input("Введите ширину треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    print("Площадь треугольника равна: " +
          str(round(0.5 * weight * height), 2))
else:
    print("Неизвестные фигура!")

# 10

tempo = int(input("Введите температуру в C*: "))

print("Температура равна " + str(tempo * 9 / 5 + 32) + " Фаренгейт")
