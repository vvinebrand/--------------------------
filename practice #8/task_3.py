class KgToPounds:
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
            raise ValueError('Килограммы задаются только числами')  # выбрасываем ошибку, если значение некорректно

    def to_pounds(self):
        # метод для перевода килограммов в фунты
        return self.__kg * 2.205  # возвращаем значение в фунтах


# Пример использования:
kg_to_pounds = KgToPounds(int(input()))  # создаем объект с 10 килограммами
print(kg_to_pounds.to_pounds())  # выводит: 22.05

print(kg_to_pounds.kg)  # выводим текущее значение килограммов: 10

kg_to_pounds.kg = int(input())  # изменяем значение на 15 килограммов
print(kg_to_pounds.kg)  # выводим текущее значение килограммов: 15
print(kg_to_pounds.to_pounds())  # выводит: 33.075
