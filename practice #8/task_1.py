class task_1:
    def __init__(self, additive=None):# self ссылается на текущий экземпляр класса. 
        # используется для доступа к атрибутам и методам этого экземпляра внутри определения методов класса
        # инициализация класса soda с добавкой
        self.additive = additive  # сохраняем добавку в атрибуте класса

    def show_my_drink(self):
        # метод для отображения типа газировки
        if self.additive:  # проверка добавки
            print(f"газировка и {self.additive}")
        else:
            print("обычная газировка")

soda1 = task_1(input())
soda1.show_my_drink()

