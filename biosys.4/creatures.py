from random import randint
from typing import NamedTuple
from numpy import sqrt


class pos(NamedTuple):
    x: float
    y: float


class property(NamedTuple):
    level: int
    position: pos
    speed: float
    color: tuple


'''
    level define:
        0 : plants
        1,2,...,6 : animals
        -1 : microbes
'''


class organism():
    def __init__(self, level: int) -> None:
        self.level = level
        self.speed = level * 1.2
        self.energy = 500 - level * 10
        self.alive = True
        if level == 0:
            self.color = (40, 255, 40)
        elif level == -1:
            self.color = (0, 0, 159)
        else:
            self.color = (level * 40, 30, 20)

    def setPosition(self, position: pos = (randint(0, 100), randint(0, 100))) -> None:
        self.position: pos = position

    def setFood(self, foods: list = [0]) -> None:
        self.foods = foods

    def catch(self, food):
        foodpos = food.getDatas()[0]
        dx = foodpos.x - self.position.x
        dy = foodpos.y - self.position.y
        dist = sqrt((dx ** 2 + dy ** 2))
        if dist > self.speed:
            x = self.speed * dx / dist + self.position.x
            y = self.speed * dy / dist + self.position.y
            self.energy -= self.speed * 0.1
        else:
            x = foodpos.x
            y = foodpos.y
            self.energy -= dist * 0.1
        if dist <= 5:
            self.energy += self.level * 2
        self.position = pos(x, y)

    def flee(self, enemy):
        enemypos = enemy.getDatas()[0]
        dx = self.position.x - enemypos.x
        dy = self.position.y - enemypos.y
        dist = sqrt((dx ** 2 + dy ** 2))
        if dist == 0:
            x = randint(-self.level, self.level) + self.position.x
            y = randint(-self.level, self.level) + self.position.y
        else:
            x = self.speed * dx / dist + self.position.x
            y = self.speed * dy / dist + self.position.y
        if dist <= 5:
            self.energy -= enemy.getDatas()[3] * 3
        self.energy -= self.speed * 0.1
        self.position = pos(x, y)

    def getDatas(self) -> tuple:
        if self.energy < self.level * 5:
            self.alive = False
        return (self.position, self.energy, self.color, self.level, self.alive)
