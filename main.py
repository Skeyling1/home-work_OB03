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

animals = [Reptile("Snake", 10, "mice"), Mammal("Sheep", 1, "grass"), Bird("Crow", 105, "porridge")]

def animal_sound(animals):
    for i in animals:
        i.make_sound()

animal_sound(animals)

class Zoo:
    def __init__(self):
        self.animals = animals
        self.employee = employee
    def add_employee(self, new_employee):
        employee.append(new_employee)
    def add_animal(self, new_animal):
        animals.append(new_animal)
# Должны быть методы для добавления животных и сотрудников в зоопарк.


class ZooKeeper:
    def __init__(self, name):
        self.name = name
    def feed_animal(self, which_animal):
        print(animals[which_animal].name, "was fed by", self.name, "with", animals[which_animal].food)

class Veterinarian:
    def __init__(self, name):
        self.name = name
    def heal_animal(self, which_animal):
        print(animals[which_animal].name, "was healed by", self.name)

employee = [Veterinarian("Joane"), ZooKeeper("Alex")]

print("")
employee[1].feed_animal(1)
employee[0].heal_animal(2)
employee[1].feed_animal(0)

print("\na new person and a new animal were added, let's see what they do:")
new_emp = ZooKeeper("Barbara")
new_anim = Bird("Pigeon", 2, "sunflower grains")

Z1 = Zoo()
Z1.add_animal(new_anim)
Z1.add_employee(new_emp)

employee[2].feed_animal(3)


# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл
# и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

