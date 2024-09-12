import math

def first():
    print("введите три числа для вычисления выражения:")

    while True:
        try:
            a = float(input("a: "))
            b = float(input("b: "))
            f = float(input("f: "))
            break
        except ValueError:
            print("ошибка: введите числа")

    result = (a + b - f / a) + f * a * a - (a + b)
    print(f"результат выражения: {result:.3f}")

    while True:
        answer = input("хотите повторить? (да/нет) ")
        match answer.lower():
            case "да" | "lf" | "yes":
                first()
                break
            case "нет" | "ytn" | "no":
                main()
                break
            case _:
                print("ошибка: введите 'да' или 'нет'")

def second():
    print("программа определяет, принадлежит ли точка с координатами (x, y) заштрихованной области")

    while True:
        try:
            x = float(input("введите значение x: "))
            y = float(input("введите значение y: "))
            break
        except ValueError:
            print("ошибка: введите числа")

    if y >= 0.5 and y <= math.sin(x):
        print(f"точка с координатами ({x}, {y}) принадлежит заштрихованной области")
    else:
        print(f"точка с координатами ({x}, {y}) не принадлежит заштрихованной области")

    while True:
        answer = input("хотите проверить другую точку? (да/нет) ")
        match answer.lower():
            case "да" | "lf" | "yes":
                second()
                break
            case "нет" | "ytn" | "no":
                main()
                break
            case _:
                print("ошибка: введите 'да' или 'нет'.")

def third():
    while True:
        try:
            a = float(input("введите длину стороны a: "))
            b = float(input("введите длину стороны b: "))
            c = float(input("введите длину стороны c: "))
            break
        except ValueError:
            print("ошибка: пожалуйста, введите числа")

    cos_a = (b**2 + c**2 - a**2) / (2 * b * c)
    cos_b = (a**2 + c**2 - b**2) / (2 * a * c)
    cos_c = (a**2 + b**2 - c**2) / (2 * a * b)

    match (cos_a, cos_b, cos_c):
        case (cos_a, cos_b, cos_c) if cos_a < 0 or cos_b < 0 or cos_c < 0:
            print(f"треугольник со сторонами {a}, {b}, {c} является тупоугольным")
        case (cos_a, cos_b, cos_c) if abs(cos_a - 0) < 1e-9 or abs(cos_b - 0) < 1e-9 or abs(cos_c - 0) < 1e-9:
            print(f"треугольник со сторонами {a}, {b}, {c} является прямоугольным")
        case _:
            print(f"треугольник со сторонами {a}, {b}, {c} является остроугольным")

    while True:
        answer = input("хотите проверить другой треугольник? (да/нет) ")
        match answer.lower():
            case "да":
                third()
                break
            case "нет":
                main()
                break
            case _:
                print("ошибка: пожалуйста, введите 'да' или 'нет'")

def main():
    print("выберите задачу:")
    while True:
        task = input("1. вычислить выражение\n2. проверить точку\n3. определить треугольник\n4. выход\n")
        match task:
            case "1":
                first()
                break
            case "2":
                second()
                break
            case "3":
                third()
                break
            case "4":
                print("ок")
                break
            case _:
                print("ошибка: введите '1', '2', '3' или '4'")

if __name__ == "__main__":
    main()
