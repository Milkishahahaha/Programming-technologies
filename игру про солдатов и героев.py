''' Задание: В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный 
номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть метод 
"иду за героем", который в качестве аргумента принимает объект типа "герой". У героев есть 
метод увеличения собственного уровня. 
В основной ветке программы создается по одному герою для каждой команды. В цикле 
генерируются объекты-солдаты. Их принадлежность команде определяется случайно. Солдаты 
разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, 
принадлежащего команде с более длинным списком, увеличивается уровень. 
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран 
идентификационные номера этих двух юнитов.
 (Написать класс, содержащий методы реализующие игру)'''

import random

class Unit:
    ID = 0

    def __init__(self, team):
        Unit.ID += 1
        self.id = Unit.ID
        self.team = team


class Soldier(Unit):
    def __init__(self, team):
        super().__init__(team)
        self.hero = None

    def follow_hero(self, hero):
        if self.team == hero.team:
            self.hero = hero
            print(f"Солдат {self.id} следует за героем {hero.id}")
        else:
            print("Нельзя следовать за героем другой команды")


class Hero(Unit):
    def __init__(self, team):
        super().__init__(team)
        self.level = 1

    def level_up(self):
        self.level += 1
        print(f"Герой {self.id} повысил уровень до {self.level}")


class Game:
    def __init__(self):
        self.hero1 = Hero(1)
        self.hero2 = Hero(2)

        self.team1 = []
        self.team2 = []

    def create_soldiers(self, count):
        for _ in range(count):
            team = random.choice([1, 2])
            soldier = Soldier(team)
            if team == 1:
                self.team1.append(soldier)
            else:
                self.team2.append(soldier)

    def play(self):
        print(f"Солдаты команды 1: {len(self.team1)}")
        print(f"Солдаты команды 2: {len(self.team2)}")

        if len(self.team1) > len(self.team2):
            self.hero1.level_up()
        elif len(self.team2) > len(self.team1):
            self.hero2.level_up()
        else:
            print("Команды равны по численности")

        if self.team1:
            soldier = self.team1[0]
            soldier.follow_hero(self.hero1)
            print(f"ID героя: {self.hero1.id}, ID солдата: {soldier.id}")

game = Game()
game.create_soldiers(10)
game.play()
