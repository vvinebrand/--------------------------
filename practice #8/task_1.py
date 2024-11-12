class soda:
    def __init__(self, additive=None):
        # инициализация класса soda с добавкой
        self.additive = additive  # сохраняем добавку в атрибуте класса

    def show_my_drink(self):
        # метод для отображения типа газировки
        if self.additive:  # проверяем, есть ли добавка
            print(f"Газировка и {self.additive}")  # выводим сообщение с добавкой
        else:
            print("Обычная газировка")  # выводим сообщение для обычной газировки

soda1 = soda(input())
soda1.show_my_drink() 

