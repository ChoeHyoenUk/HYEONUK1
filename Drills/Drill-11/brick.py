from pico2d import *
import game_framework
import random


class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.SPEED = 300  # 9m/s
        self.move_dir = -1
        self.x, self.y = 600, 200

    def update(self):
        self.x += (self.move_dir * self.SPEED) * game_framework.frame_time

        if self.x > (1500-90) or self.x < 90:
            self.move_dir *= -1

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
         return self.x - 90, self.y - 20, self.x + 90, self.y + 20