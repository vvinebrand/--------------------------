def first():
    height, weight = map(int, input('введите свой рост и вес через пробел: ').split( ))
    ideal_weight = height-100
    if weight>ideal_weight:
        print(f"ваш идеальный вес: {ideal_weight}. Сейчас вы весите больше")
    elif weight==ideal_weight:
        print(f"ваш идеальный вес: {ideal_weight}. Все гуд")
    else:
        print(f"ваш идеальный вес: {ideal_weight}. Вы весите меньше")

def second():
    a = float(input("введите длину первой стороны: "))
    b = float(input("введите длину второй стороны: "))
    c = float(input("введите длину третьей стороны: "))

    if a == b == c:
        print("треугольник равносторонний")
    elif a == b or b == c or a == c:
        print("треугольник равнобедренный")
    else:
        print("треугольник разносторонний")

def third():
    a = float(input("введите первое число: "))
    b = float(input("введите второе число: "))
    c = float(input("введите третье число: "))

    print("модифицированные числа:")
    match (a, b, c):
        case (1, y, z):
            print(2, y / 2, z / 2)
        case (x, 1, z):
            print(x / 2, 2, z / 2)
        case (x, y, 1):
            print(x / 2, y / 2, 2)
        case (x, y, z):
            print(x / 2, y / 2, z / 2)

def fourth():
    year = int(input("введите год: "))

    match year:
        case year if year % 400 == 0:
            print(f"{year} - високосный год")
        case year if year % 100 == 0:
            print(f"{year} - невисокосный год")
        case year if year % 4 == 0:
            print(f"{year} - високосный год")
        case _:
            print(f"{year} - невисокосный год")

def fifth():
    number = int(input("введите число: "))

    match number % 2:
        case 0:
            print(f"{number} - чётное число")
        case _:
            print(f"{number} - нечётное число")

def main():
    print("Выберите задание:")
    print("1. вычисление оптимального веса")
    print("2. определение вида треугольника")
    print("3. замена чётных значений на их частное от деления на 2, а единицы - на 2")
    print("4. определение, является ли год високосным")
    print("5. проверка на чётность числа")

    choice = int(input("введите номер задания: "))

    match choice:
        case 1:
            first()
        case 2:
            second()
        case 3:
            third()
        case 4:
            fourth()
        case 5:
            fifth()
        case _:
            print("ошибка. введите номер задания")

if __name__ == "__main__":
    main()