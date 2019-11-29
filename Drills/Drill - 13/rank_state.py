import main_state
from pico2d import *
import json
import game_framework
import game_world
import world_build_state

name = "RankState"
font = None


def enter():
    global font
    main_state.time.sort(reverse=True)
    font = load_font('ENCR10B.TTF', 20)


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_world.save()

def update():
    pass

def draw():
    global font
    clear_canvas()
    if len(main_state.time) < 10:
        for i in range(len(main_state.time)):
            font.draw(10, 800 - (20 * i), '%3.2f' % main_state.time[i], (0, 0, 0))
    else:
        for i in range(10):
            font.draw(10, 800 - (20*i), '%3.2f' % main_state.time[i], (0, 0, 0))
    update_canvas()
