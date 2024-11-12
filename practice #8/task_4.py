# определяем класс Nikola
class task_4:
    # определяем инициализатор с параметрами имя и возраст
    def __init__(self, name, age):
        # проверяем, если имя не "Николай"
        if name != "николай":
            # присваиваем имя, если оно не Николай
            self.name = f"я не {name}, а Николай"
        else:
            # присваиваем имя без изменений
            self.name = name
        
        # сохраняем возраст
        self.age = age

        # запрещаем добавление новых атрибутов экземпляра
        # для этого переопределим __setattr__
    def __setattr__(self, key, value):
        # если ключ не "name" или "age", генерируем исключение
        if key not in ['name', 'age']:
            raise AttributeError(f"нельзя добавлять атрибут '{key}'")
        # устанавливаем атрибут, если он разрешен
        super().__setattr__(key, value)

nikolai = task_4("Леон", 25)
nikolai1 = task_4("Николай", 33)

print(nikolai.name)
print(nikolai1.name)
print(nikolai.age)

try:
    nikolai.parentage = "Маратович"
except AttributeError as e:
    print(e)