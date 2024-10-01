import random

def first():
    num = [random.randint(1, 10) for _ in range(5)]
    sq_num = [x**2 for x in num]
    print(f'\nисходный список: {num}, квадраты: {sq_num}')

    print('\nхотите повторить?\n')
    choice = input()
    match choice:
        case 'да' | 'lf' | 'yes' | 'нуы':
            first()
        case 'нет' | 'ytn' | 'no' | 'тщ':
            main()

def second():
    # num = [random.randint(1, 10) for _ in range(10)]
    num = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7]
    dublicates = [x for x in set(num) if num.count(x) > 1]
    print(f'\nисходный список: {num}, дубликаты: {dublicates}')

    print('\nхотите повторить?\n')
    choice = input()
    match choice:
        case 'да' | 'lf' | 'yes' | 'нуы':
            second()
        case 'нет' | 'ytn' | 'no' | 'тщ':
            main()

def third():
    list1 = [random.randint(1, 10) for _ in range(10)]
    list2 = [random.randint(1, 10) for _ in range(10)]
    list3 = [x for x in list2 if x not in list1]
    print(f'\nпервый список: {list1}\nвторой список: {list2}\nтретий список: {list3}\n')

    print('хотите повторить?\n')
    choice = input()
    match choice:
        case 'да' | 'lf' | 'yes' | 'нуы':
            third()
        case 'нет' | 'ytn' | 'no' | 'тщ':
            main()

def fourth():
    num = [random.randint(10, 20) for _ in range(10)]
    print(f'\nисходный список: {num}\n')
    if 20 in num:
        num[num.index(20)] = 200
    print(f'исправленный список: {num}\n')

    print('хотите повторить?\n')
    choice = input()
    match choice:
        case 'да' | 'lf' | 'yes' | 'нуы':
            fourth()
        case 'нет' | 'ytn' | 'no' | 'тщ':
            main()

def fifth():
    num = [random.randint(1, 20) for _ in range(10)]
    print(f'исходный список: {num}')
    nums_list = []
    for numbers in num:
        if numbers % 2 == 0:
            nums_list.append(numbers)
        if numbers == 15:
            break
    print("чётные числа из списка: " + ", ".join(map(str,nums_list)))
    
    print('\nхотите повторить?\n')
    choice = input()
    match choice:
        case 'да' | 'lf' | 'yes' | 'нуы':
            fifth()
        case 'нет' | 'ytn' | 'no' | 'тщ':
            main()

def main():
    print("1.замена значений элементов в списке на их квадраты. \n2. вывод на экран значения, которые в сипске более одного раза. \n3. составление третьего списка, в который входят такие эл-ты второго списка, которые не входят в первый список. \n4. замена значения 20 на 200 в списке. \n5. вывод четных чисел из заданного списка и останавливается, если встречает число 15.\n введите 0 чтобы выйти\n")
    choice = int(input("Введите нужный номер: "))

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
            print("ок")

if __name__ == "__main__":
    main()