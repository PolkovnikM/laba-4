print("1. СТРАТЕГИЯ: Выбор оружия в шутере")


class Weapon:
    def shoot(self):
        pass


class Pistol(Weapon):
    def shoot(self):
        return "(Урон: 10, Точность: 90%)"


class Shotgun(Weapon):
    def shoot(self):
        return "(Урон: 50, Разброс: широкий)"


class SniperRifle(Weapon):
    def shoot(self):
        return "(Урон: 100, Прицел: x8)"


class Player:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def pick_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} взял {weapon.__class__.__name__}")

    def attack(self):
        if self.weapon:
            return self.weapon.shoot()
        return "Без оружия! (Урон: 5)"

player = Player("Солдат")
player.pick_weapon(Pistol())
print("Атака:", player.attack())
player = Player("Пехотинец")
player.pick_weapon(Shotgun())
print("Атака:", player.attack())
player = Player("Снайпер")
player.pick_weapon(SniperRifle())
print("Атака:", player.attack())