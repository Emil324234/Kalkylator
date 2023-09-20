import math

while True:
    print("""
    Калькулятор:
    1. Сложить 2 числа
    2. Вычесть первое из второго
    3. Перемножить два числа
    4. Разделить первое на второе
    5. Возвести в степень N первое число
    6. Найти квадратный корень из числа
    7. Найти 1 процент от числа
    8. Найти факториал из числа
    9. Выйти из программы
    """)

    choice = input("Выберите операцию (1-9): ")

    if choice == "1":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 + num2
        print("Результат: ", result)
    elif choice == "2":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num2 - num1
        print("Результат: ", result)
    elif choice == "3":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 * num2
        print("Результат: ", result)
    elif choice == "4":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 / num2
        print("Результат: ", result)
    elif choice == "5":
        num1 = float(input("Введите число: "))
        power = int(input("Введите степень: "))
        result = num1 ** power
        print("Результат: ", result)
    elif choice == "6":
        num = float(input("Введите число: "))
        result = math.sqrt(num)
        print("Результат: ", result)
    elif choice == "7":
        num = float(input("Введите число: "))
        result = num / 100
        print("Результат: ", result)
    elif choice == "8":
        num = int(input("Введите число: "))
        result = 1
        for i in range(1, num + 1):
            result *= i
        print("Результат: ", result)
    elif choice == "9":
        break
    else:
        print("Неверный выбор операции. Попробуйте снова.")