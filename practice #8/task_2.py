class task_2:
    def __init__(self, a, b, c): 
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
            # значение сторон сброшено из-за неверного ввода
            if isinstance(self.a, (int, float)) or isinstance(self.b, (int, float)) or isinstance(self.c, (int, float)):
                return "отрицательные числа нельзя"
            else:
                return "нужны только числа" 
        # проверка неравенства треугольника
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "можно построить треугольник"
        else:
            return "нельзя построить треугольник"

triangle_checker1 = task_2(int(input().split(' ',',')))
print(triangle_checker1.is_triangle())
