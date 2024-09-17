def first():
    days = float(input('введите расстояние, которое спортсмен преодолел в первый день (в км): '))
    k = int(input('введите день, для рассчета дистанции: '))
    distance = days * (1.1 ** (k-1))
    print(f'дистанция на {k} день составит {distance:.3f} км')

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
    try:
        decimal = int(input('введите десятичное число (меньше 256): '))
        if decimal < 0 or decimal >= 256:
            print('введите корректное число')
        else:
            binary = bin(decimal)[2:]
            print(f'число {decimal} в двоичном коде будет выглядеть так: {binary}')
    except ValueError:
        print('ошибка. введите десятичное число')

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
    
    try:
        num = int(input('введите натуральное число: '))
        number = num
        if number <= 0:
            print('вы ввели некорректное число')
        else:
            fact = []
            divis = 2
            while number > 1:
                while number % divis == 0:
                    fact.append(divis)
                    number //= divis
                divis += 1
            
            print(f'простые можнители числа {num}: {fact}')
    except ValueError:
        print('ошибка. введите корректное число')

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


def fourth():
    
    current_population = 620000
    target_population = 1500000
    growth = 0.037
    current_year = 2021

    while current_population < target_population:
        current_population += current_population * growth
        current_year += 1
    print(f'население города превысит 1.5млн человек в {current_year} году\n')

    
    while True:
        answer = input("хотите продолжить? (да/нет) ")
        match answer.lower():
            case "да" | "lf" | "yes":
                main()
                break
            case "нет" | "ytn" | "no":
                print('ок')
                break
            case _:
                print("ошибка: введите 'да' или 'нет'")

def fifth():
    
    num = int(input('введите число, сумму нечетных делителей которого нужно найти: '))
    divis = 0
    for i in range(1, num + 1):
        if num % i == 0:
            if i % 2 != 0:
                divis += i
    print(f'сумма нечетных делителей числа {num} равна {divis}')

    while True:
        answer = input("хотите повторить? (да/нет) ")
        match answer.lower():
            case "да" | "lf" | "yes":
                fifth()
                break
            case "нет" | "ytn" | "no":
                main()
                break
            case _:
                print("ошибка: введите 'да' или 'нет'")

def main():
    print('выберите задачу: ')
    while True:
        task = input('1. пределение длины дистанции на k-й день\n2. перевод десятичного числа в двоичное\n3. разложение натурального числа на просте множители\n4. определение превышения населения\n5. сумма нечетных делителей\nвведите 0, чтобы выйти\n\n')
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
                fourth()
                break
            case "5":
                fifth()
                break
            case "0":
                print("ok")
                break
            case _:
                print("ошибка: введите '0', '1', '2', '3', '4' или '5'")

if __name__ == "__main__":
    main()