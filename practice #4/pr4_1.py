def first():
    filename = input("введите имя файла (с расширением, например, 'example.txt'): ")
    with open(filename, 'w', encoding = 'utf-8') as file:
        while True:
            us_in = input("введите строку, котору хотите записать в файл (пустая строка для выхода): ")
            if us_in == "":
                break
            file.write(us_in + '\n')
    main()

def second():
    filename = input("введите имя существующего файла (с расширением, например, 'example.txt'): ")
    try:
        with open(filename, 'r', encoding='utf-8') as infile: #r - открываем файл для чтения
            lines = infile.readlines()
        with open(filename, 'w', encoding='utf-8') as outfile: #w - открываем файл для записи
            for index, line in enumerate(lines, start=1):
                clean = line.rstrip()
                outfile.write(f"{index}. {clean}\n")
    except FileNotFoundError:
        print(f"файла {filename} не существует")
    main()

def third():
    filename = input("введите имя существующего файла (с расширением, например, 'example.txt'): ")
    lines_per_file = int(input("введите кол-во строк в каждом файле: "))
    try:
        with open(filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        counter = 1
        for i in range(0, len(lines), lines_per_file): #создание последовательности индексов с 0 до len(lines) с шагом lines_per_file
            chunk = lines[i:i + lines_per_file] #создаем подсписок chunck, содержащий lpf строк, начиная с i при помощи среза
            outfilename = f'{counter}.txt' #имя файла для вывода
            counter += 1
            with open(outfilename, 'w', encoding='utf-8') as outfile: #открываем файл в режиме записи (будет закрыт автоматически)
                outfile.writelines(chunk) #записываем все строки из chunk в файл
    except FileNotFoundError:
        print(f"файл {filename} не найден")
    main()

def fourth():
    infiles = input("введите имена файлов для объединения, разделенные запятыми (с расширением, например, 'example.txt'): ").split(',')
    infiles = [file.strip() for file in infiles] #file.strip удаляет все пробелы или другие символы. итерируемся по существующему списку
    outfilename = 'combined.txt'
    try:
        with open(outfilename, 'w', encoding='utf-8') as outfile:
            for filename in infiles:
                try:
                    with open(filename, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content)
                except FileNotFoundError:
                    print(f"файл {filename} не найден")
                except Exception as e:
                    print(f"произошла ошибка при чтении файла '{filename}': {e}")
    except Exception as e:
        print(f"произошла ошибка при записи в файл: {e}")
    main()

def fifth():
    filename = input("введите имя файла (с расширением, например, 'example.txt'): ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        choice = input("вы хотите вывести первые или последние строки? (введите 'первые' или 'последние'): ").strip().lower()
        num_lines = int(input("сколько строк вывести (например, 1 для первой или последней): "))
        if num_lines > len(lines) or num_lines < 1:
            print(f"файл содержит только {len(lines)} строк. пожалуйста, введите число от 1 до {len(lines)}.")
        else:
            match choice:
                case 'первые':
                    print("\nпервые строки файла:")
                    for i in range(num_lines):
                        print(lines[i].strip())
                case 'последние':
                    print("\nпоследние строки файла:")
                    for i in range(-num_lines, 0):
                        print(lines[i].strip())
                case _:
                    print("Неверный выбор. Пожалуйста, введите 'первые' или 'последние'.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден. Проверьте имя файла и попробуйте снова.")
    except ValueError:
        print("Пожалуйста, введите правильное число.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def main():
    print("\n1.записать в файл вводимые данные. \n2.нумерация строк в файле. \n3.разделить файл на части. \n4.объединение файлов. 5. доп.задачи \nвведите 0 чтобы выйти\n")
    choice = int(input("введите нужный номер: "))

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