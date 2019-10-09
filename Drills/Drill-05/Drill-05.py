from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def move(p1, p2):
    # fill here
    print((p1[0],p1[1]),(p2[0],p2[1]))
    global M_x, M_y
    global dir, stop_dir

    if p1[0] < p2[0]:
        dir = 1
        stop_dir = 3
    elif p1[0] > p2[0]:
        dir = -1
        stop_dir = 2

    global character
    global x, y

    for i in range(0, 100 + 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        cursor.draw(M_x, M_y)
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        if dir == 1:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif dir == -1:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()

    character.clip_draw(frame * 100, 100 * 1, 100, 100, p2[0], p2[1])
    if dir == 1:
        dir -= 1
    elif dir == -1:
        dir += 1


def handle_events():
    # fill here
    global running
    global x, y
    global M_x, M_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            M_x, M_y = event.x, KPU_HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            move((x, y), (event.x - 25, (KPU_HEIGHT - 1 - event.y) + 25))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


# fill here
open_canvas(KPU_WIDTH, KPU_HEIGHT)
hide_cursor()

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
M_x, M_y = x, y
dir = 0
stop_dir = 3
frame = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if stop_dir == 2:
        character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    elif stop_dir == 3:
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
    cursor.draw(M_x, M_y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()
