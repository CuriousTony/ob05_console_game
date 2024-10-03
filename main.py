from abc import ABC, abstractmethod
import random


class Hero(ABC):
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.attack_power = random.randint(10, 20)

    @abstractmethod
    def attack(self, target):
        pass

    def is_alive(self):
        return self.hp > 0


class Player(Hero):
    def __init__(self, name):
        super().__init__(name)

    def attack(self, target):
        target.hp -= self.attack_power
        print(f"{self.name.title()} атакует {target.name}! Остаток hp: {target.hp}.")


class Computer(Hero):
    def __init__(self, name):
        super().__init__(name)

    def attack(self, target):
        target.hp -= self.attack_power
        print(f"{self.name} дубасит игрока наотмашь!"
              f" Остаток hp составляет {target.hp}.\n")


class Game:
    def __init__(self):
        player_name = input("Введите имя своего героя: ")
        self.player = Player(player_name)
        self.computer = Computer('r2d2')

    def start(self):
        print(f"Начинается поединок между {self.player.name.title()} и "
              f"{self.computer.name}.")
        print("Да победит тот, кого осенит благодатью рандом!\n")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"Победа за {self.player.name.title()}!")
                break

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"Герой по имени {self.player.name.title()} пал жертвой рандома...")
                break


game = Game()
game.start()
