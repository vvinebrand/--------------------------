class task_3:
    def __init__(self, kg):
        # инициализация с заданным значением в килограммах
        self.__kg = kg  # защищенное поле для хранения килограммов

    @property
    def kg(self):
        # декоратор property для получения значения кг
        return self.__kg  # возвращаем текущее значение кг

    @kg.setter
    def kg(self, new_kg):
        # декоратор setter для изменения значения кг
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg  # если значение корректно, присваиваем новое значение
        else:
            raise ValueError('килограммы задаются только числами')  # ошибка, если значение некорректно

    def to_pounds(self):
        # метод для перевода килограммов в фунты
        return self.__kg * 2.205  # возвращаем значение в фунтах

kg_to_pounds = task_3(int(input()))
print(kg_to_pounds.to_pounds())

print(kg_to_pounds.kg)

kg_to_pounds.kg = int(input())
print(kg_to_pounds.kg)
print(kg_to_pounds.to_pounds())
