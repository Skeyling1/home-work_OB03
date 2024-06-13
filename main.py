# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food
    def make_sound(self):
        print(f"{self.name} make a sound 'kar-kar'")
    def eat(self):
        print(f"{self.name} eat {self.food}")

class Mammal(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food
    def make_sound(self):
        print(f"{self.name} make a sound 'be-e-e!'")
    def eat(self):
        print(f"{self.name} eat {self.food}")

class Reptile(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food
    def make_sound(self):
        print(f"{self.name} make no sound")
    def eat(self):
        print(f"{self.name} eat {self.food}")

# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.

animals = [Reptile("Snake", 10, "mise"), Mammal("Sheep", 1, "grass"), Bird("Crow", 105, "porridge")]

def animal_sound(animals):
    for i in animals:
        i.make_sound()

animal_sound(animals)


# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

class Zoo:
    pass


# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class ZooKeeper:
    pass# (например, `feed_animal()` для `ZooKeeper`

class Veterinarian:
    pass # `heal_animal()` для `Veterinarian`).


# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл
# и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

