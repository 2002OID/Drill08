from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):  # 생성자 함수, __init__고정, 객체의 초기상태(속성, 속성값) 설정
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Small_Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(1, 10)

    def update(self):
        if(self.y > 60):
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

class Big_Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(1, 10)

    def update(self):
        if(self.y > 70):
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)
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
    global team
    global world
    global small_balls
    global big_balls

    running = True
    world = []
    grass = Grass()
    world.append(grass)
    #team = [Boy() for i in range(11)]
    #world += team
    sb = random.randint(0,20 + 1)
    small_balls = [Small_Ball() for i in range(sb)]
    world += small_balls
    bb = 20 - sb
    big_balls = [Big_Ball() for i in range(bb)]
    world += big_balls
def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
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
