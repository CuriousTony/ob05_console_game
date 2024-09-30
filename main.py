import random


class Hero:
    def __init__(self, name, health=100, attack_power=random.randint(15,40)):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютерный противник")

    def start(self):
        print("Начало игры!")
        while self.player.is_alive() and self.computer.is_alive():
            # Игрок атакует
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} побеждает!")
                break
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")

            # Компьютер атакует
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} побеждает!")
                break
            print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")


if __name__ == "__main__":
    game = Game()
    game.start()
