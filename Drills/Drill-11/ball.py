import random
from pico2d import *
import game_world
import game_framework
import main_state


class Ball:
    MIN_FALL_SPEED = 50  # 1.5m/s
    MAX_FALL_SPEED = 200  # 6m/s
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1500 - 1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)
        self.on_the_brick = False

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time
        if self.on_the_brick:
            self.x += (main_state.brick.move_dir * main_state.brick.SPEED) * game_framework.frame_time

    # fill here for def stop
    def stop(self):
        self.fall_speed = 0


# fill here
class BigBall(Ball):
    MIN_FALL_SPEED = 50  # 1.5m/s
    MAX_FALL_SPEED = 200  # 6m/s
    image = None

    def __init__(self):
        if BigBall.image is None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1500 - 1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)
        self.on_the_brick = False

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
