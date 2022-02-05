# ============================================================
# File name: Game_of_life.py
# Author: Hao-Wei Li
# Date created: 2019/1/6
# Date last modified: 
# Python Version: 3.6
# ============================================================
import random
from copy import deepcopy
from colorama import init, Fore, Style
init()

GAME_PLACE_LIMIT = 20

class Cell:
    # X, Y Point in map
    # _X = -1 # Initialize with impossibile value
    # _Y = -1 # Initialize with impossibile value
    # _alive = 0
    # _nieghberhoods = []
    
    def __init__(self, x, y, alive=0):
        if x > GAME_PLACE_LIMIT or y > GAME_PLACE_LIMIT:
           raise Exception("X 或 Y 超過遊戲最大限制") 

        self._X = x
        self._Y = y
        self._alive = alive
        self._nieghberhoods = []

        for xi in range(-1, 2):
            for yi in range(-1, 2):
                if self._X + xi < 0 or self._X + xi >= GAME_PLACE_LIMIT \
                    or self._Y + yi < 0 or self._Y + yi >= GAME_PLACE_LIMIT \
                    or (xi==0 and yi==0):
                    continue
                else:
                    self._nieghberhoods.append((self._X+xi, self._Y+yi))

    def __repr__(self):
        return str(self._alive)

    def __str__(self):
        return str(self._alive)

class Generations:

    _generations_iter = 0

    def __init__(self, max_iter=10):
        self.max_iter = max_iter
        self.world = World()
    
    def start(self):
        print(f" ==============  第 {self._generations_iter} 代  ==============  ")
        print(self.world)

        while self._generations_iter < self.max_iter:
            self._generations_iter += 1 # 更新世代的數字

            # 更新世界
            for y in range(len(self.world.map)):
                for x in range(len(self.world.map[y])):
                    state = sum(self.world[neighborX, neighborY]._alive for neighborX, neighborY in self.world[x, y]._nieghberhoods)

                    if state >= 4 or state ==0 or state ==1:
                        self.world[x, y] = 0
                    elif state==2:
                        pass
                    elif state == 3:
                        self.world[x, y] = 1
            # 更新 world map
            self.world.update()

            print(f" ==============  第 {self._generations_iter} 代  ==============  ")
            print(self.world)

            
class World:
    def __init__(self):
        self.map = []
        for y in range(GAME_PLACE_LIMIT):
            self.map.append([])
            for x in range(GAME_PLACE_LIMIT):
                if random.random() > 0.35:
                    self.map[y].append(Cell(x, y, 0))
                else:
                    self.map[y].append(Cell(x, y, 1))

        self.__next_map = deepcopy(self.map)
    
    def __str__(self):
        string = ""
        for y in range(len(self.map)):
            row = "  ".join(str(v) if v._alive == 0 else f"{Fore.GREEN}{v}{Style.RESET_ALL}" for v in self.map[y] )
            string = string + f"{y: >2} |  {row}\n"
        return string

    def update(self):
        self.map = deepcopy(self.__next_map)

    def __getitem__(self, coordinate):
        return self.map[coordinate[1]] [coordinate[0]]

    def __setitem__(self, coordinate, value):
        x = coordinate[0]
        y = coordinate[1]
        self.__next_map[y][x]._alive = value

if __name__ == "__main__":
    g = Generations(max_iter=100)
    g.start()
