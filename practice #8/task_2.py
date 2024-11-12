class TriangleChecker:
    def __init__(self, a, b, c):
        # инициализация класса TriangleChecker с тремя сторонами
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
            # проверка, являются ли все стороны числами
            if a > 0 and b > 0 and c > 0:
                # проверка, положительные ли числа
                self.a = a  # сохраняем первую сторону
                self.b = b  # сохраняем вторую сторону
                self.c = c  # сохраняем третью сторону
            else:
                self.a = self.b = self.c = None  # сбрасываем значения, если есть отрицательные
        else:
            self.a = self.b = self.c = None  # сбрасываем значения, если не числа

    def is_triangle(self):
        # метод для проверки возможности построения треугольника
        if self.a is None:
            # если значение сторон сброшено из-за неверного ввода
            if isinstance(self.a, (int, float)) or isinstance(self.b, (int, float)) or isinstance(self.c, (int, float)):
                # если хотя бы одно значение было числом
                return "С отрицательными числами ничего не выйдет!"  # возвращаем сообщение о отрицательных числах
            else:
                return "Нужно вводить только числа!"  # возвращаем сообщение о неверном типе данных
        # проверка неравенства треугольника
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Ура, можно построить треугольник!"  # возвращаем сообщение о возможности построения треугольника
        else:
            return "Жаль, но из этого треугольник не сделать."  # возвращаем сообщение о невозможности построения

triangle_checker1 = TriangleChecker(int(input().split(' ',',')))  # создаем объект с тремя положительными числами
print(triangle_checker1.is_triangle())  # выводит: Ура, можно построить треугольник!
