import game_framework
from pico2d import *
import main_state
import threading

name = "PauseState"
image = None
draw_pause_image = True
IsTimerRun = False


def draw_timer():
    global draw_pause_image
    global image
    timer = threading.Timer(0.5, draw_timer)

    if draw_pause_image:
        draw_pause_image = False
    else:
        draw_pause_image = True
    timer.start()
    pass


def enter():
    global image
    global IsTimerRun
    image = load_image('pause.png')
    if not IsTimerRun:
        IsTimerRun = True
        draw_timer()


def exit():
    global image
    del image


def update():
    pass


def draw():
    global image
    global draw_pause_image

    clear_canvas()
    main_state.grass.draw()
    main_state.boy.draw()

    if draw_pause_image:
        image.draw(400, 300, 300, 300)

    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            game_framework.pop_state()
    pass


def pause(): pass


def resume(): pass
