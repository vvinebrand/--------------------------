import math

def first():
    price = float(input('введите стоимость килограмма конфет: '))
    for kg in range(1, 11):
        cost = price * kg
        print(f'стоимость {kg}кг конфет: {cost:.1f} руб.')
    
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
    x = int(input('введите значение х: '))
    a = int(input('введите значение a: '))
    n = int(input('введите значение n: '))

    left_side = pow(a, x)

    right_side = 0
    for i in range(n + 1):
        right_side += ((x * math.log(a)) ** i)/math.factorial(i)
    
    print(f'\nлевая часть: {left_side:.6f}\nправая часть: {right_side:.6f}')
    if math.isclose(left_side, right_side, rel_tol=1e-10):
        print('равенство выполнено')
    else:
        print('равенство не выполнено')
    
    while True:
        answer = input("хотите повторить? (да/нет) ")
        match answer.lower():
            case "да" | "lf" | "yes":
                second()
                break
            case "нет" | "ytn" | "no":
                main()
                break
            case _:
                print("ошибка: введите 'да' или 'нет'")


def third():
    total_time = 0
    while True:
        time = input('введите время обработки каждой детали на трех станках (формат: станок1 станок2 станок3): ')
        if time.strip() == '':
            break

        try:
            times = list(map(float, time.split()))
            if len(times) != 3:
                print('ошибка. нужно ввести ровно три числа')
                continue
            sum_times = sum(times)
            total_time += sum_times
        except ValueError:
            print('ошибка. введите корректные числа')
    print(f'общее время обработки всех деталей равна {total_time:.2f}')

    while True:
        answer = input("хотите повторить? (да/нет) ")
        match answer.lower():
            case "да" | "lf" | "yes":
                third()
                break
            case "нет" | "ytn" | "no":
                main()
                break
            case _:
                print("ошибка: введите 'да' или 'нет'")



def main():
    print('выберите задачу: ')
    while True:
        task = input('1. вывод стоимости конфет\n2. проверка равенства\n3. подсчет времени обработки\nвведите 0, чтобы выйти\n\n')
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
            case "0":
                print("ok")
                break
            case _:
                print("ошибка: введите '0', '1', '2' или '3''")

if __name__ == "__main__":
    main()