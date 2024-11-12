class task_5:
    def __init__(self, value):
        self.value = value  # сохраняем переданное значение как атрибут объекта

    # метод для получения длины строки
    def __len__(self):
        return len(self.value)  # возвращаем количество символов в строке

    # метод для сравнения строк по количеству символов
    def __lt__(self, other):
        if isinstance(other, task_5):  # проверяем, является ли другой объект экземпляром task_5
            return len(self) < len(other)  # сравниваем длину текущей строки с длиной другой строки
        elif isinstance(other, str):  # проверяем, является ли другой объект обычной строкой
            return len(self) < len(other)  # сравниваем длину текущей строки с длиной обычной строки

        return NotImplemented  # если объект не того типа, возвращаем NotImplemented

    # метод для вывода строки
    def __str__(self):
        return self.value  # возвращаем значение строки для удобного отображения

real_str1 = task_5("Apple")
real_str2 = task_5("Яблоко")

print(real_str1 < real_str2)

print(real_str1 < "Banana")
