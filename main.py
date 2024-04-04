# Задача: Разработать простую игру, где игрок может использовать
# различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом,
# чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.
#
# Исходные данные:
#
# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
#
# Шаг 1: Создайте абстрактный класс для оружия
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
# Шаг 2: Реализуйте конкретные типы оружия
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow.
# Каждый из этих классов реализует метод attack() своим уникальным способом.
#
# Шаг 3: Модифицируйте класс Fighter
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
# Добавьте метод changeWeapon(), который позволяет изменить оружие бойца.
#
# Шаг 4: Реализация боя
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
#
# Требования к заданию:
# Код должен быть написан на Python.
# Программа должна демонстрировать применение принципа открытости/закрытости:
# новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# Программа должна выводить результат боя в консоль.
# Пример результата:
## Боец выбирает меч.
## Боец наносит удар мечом.
## Монстр побежден!
## Боец выбирает лук.
## Боец наносит удар из лука.
## Монстр побежден!

from abc import ABC, abstractmethod
class Weapon(ABC):
    # абстрактрый класс для оружия
    @abstractmethod
    def attack(self):
        pass

    def get_type(self):
        pass

class Sword(Weapon):
    # меч
    def attack(self):
        print("наносит удар мечом")
        return 20

    def get_type(self):
        return "меч"

class Bow(Weapon):
    # лук
    def attack(self):
        print("стреляет из лука")
        return 10

    def get_type(self):
        return "лук"

class Fighter():
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon
        print(f"Новый боец {self.name} с оружием {weapon.get_type()}")


    def changeWeapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"{self.name} выбирает {new_weapon.get_type()}")

    def attack(self):
        print(f"{self.name} атакует:")
        return self.weapon.attack()

class Monster():
    def __init__(self, health):
        self.health = health

    def attack(self):
        print("Монстр нападает!")

def battle(fighter, monster):
    print("Битва!")
    monster.attack()
    while monster.health > 0:
        counter = f01.attack()
        monster.health -= counter
        if monster.health == 40:
            f01.changeWeapon(Bow())

    if monster.health <= 0:
        print(f"Монстр побежден!")


f01 = Fighter("Добрыня", Sword())
m01 = Monster(100)

battle(f01, m01)