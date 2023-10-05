from pico2d import *


# Game object class here
class Grass:
    def __init__(self):     #생성자 함수, __init__고정, 객체의 초기상태(속성, 속성값) 설정
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    running = True
    grass = Grass()


def update_world():
    pass


def render_world():
    clear_canvas()
    grass.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()
# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
