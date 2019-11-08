import game_framework
from pico2d import *

import game_world

# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class FlyState:

    @staticmethod
    def enter(bird, event):
        bird.velocity = RUN_SPEED_PPS
        bird.fly_dir = 1
        # fill here


    @staticmethod
    def exit(bird, event):
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        # fill here
        bird.x += bird.velocity * bird.fly_dir * game_framework.frame_time

        if 92 > bird.x or 1600-92 < bird.x:
            bird.fly_dir *= -1

    @staticmethod
    def draw(bird):
        if bird.fly_dir == 1:
            bird.image.clip_draw(int(bird.frame) * 184, 338, 183, 169, bird.x, bird.y)
        else:
            bird.image. clip_composite_draw(int(bird.frame) * 184, 338, 183, 169, 0, 'h', bird.x, bird.y, 183, 169)


class Bird:

    def __init__(self):
        self.x, self.y = 100, 450
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird_animation.png')
        # fill here
        self.fly_dir = 0
        self.velocity = 0
        self.frame = 0
        self.cur_state = FlyState
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)