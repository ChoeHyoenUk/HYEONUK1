import random
from pico2d import *
import game_world
import game_framework
import main_state


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, 1837 - 1), random.randint(0, 1109 - 1)
        self.hp = 50

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.cx, self.cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(self.cx, self.cy)

    def update(self):
        pass
    # fill here for def stop

    def stop(self):
        pass

    def set_background(self, bg):
        self.bg = bg
        self.x = self.x
        self.y = self.y


# fill here
class BigBall(Ball):
    image = None

    def __init__(self):
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1837 - 1), 1109
        self.hp = 100

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
