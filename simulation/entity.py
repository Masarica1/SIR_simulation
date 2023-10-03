import pygame
import random
import json


with open('setting.json', 'r') as file:
    data = json.load(file)

window_h = data['height']
window_w = data['width']
window = pygame.display.set_mode((window_w, window_h))

# color
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (127, 127, 127)

# size
size = data['size']


def speed_setting(x_dir: bool, y_dir: bool):
    vel = [0, 0]

    if x_dir:
        vel[0] = random.choice(range(3, 10))
    else:
        vel[0] = -random.choice(range(3, 10))
    if y_dir:
        vel[1] = random.choice(range(3, 10))
    else:
        vel[1] = -random.choice(range(3, 10))
    return vel


class Person(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.vel = [random.choice(range(-10, 10)), random.choice(range(-10, 10))]

    def update(self):
        self.rect.move_ip(self.vel[0], self.vel[1])

        if self.rect.x < 0:
            self.rect.x = 0
            self.vel = speed_setting(True, random.choice([True, False]))
        elif self.rect.right > window_w:
            self.rect.right = window_w
            self.vel = speed_setting(False, random.choice([True, False]))
        if self.rect.y < 0:
            self.rect.y = 0
            self.vel = speed_setting(random.choice([True, False]), True)
        elif self.rect.bottom > window_h:
            self.rect.bottom = window_h
            self.vel = speed_setting(random.choice([True, False]), False)


class Suspicious(Person):
    def __init__(self):
        super().__init__()
        pygame.draw.circle(self.image, BLUE, (size/2, size/2), size/2)
        self.rect.center = [random.choice(range(window_w)), random.choice(range(window_h))]

    def infection_check(self):
        collide_list = pygame.sprite.spritecollide(self, infected_group, False)
        for _ in collide_list:
            if random.choice(range(data['p_infection'])) == 1:
                # noinspection PyTypeChecker
                suspicious_group.remove(self)
                # noinspection PyTypeChecker
                infected_group.add(Infected(self.rect.center, self.vel))


class Infected(Person):
    def __init__(self, center, vel):
        super().__init__()
        self.image = pygame.Surface((size*6, size*6), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.vel = vel
        self.rect.center = center

        pygame.draw.circle(self.image, (255, 0, 0, 63), (size*3, size*3), size*3)
        pygame.draw.circle(self.image, RED, (size*3, size*3), size/2)

    def update(self):
        super().update()

        if random.choice(range(data['p_recovery'] * 60)) == 1:
            # noinspection PyTypeChecker
            recovered_group.add(Recovered(self.rect.center, self.vel))
            # noinspection PyTypeChecker
            infected_group.remove(self)


class Recovered(Person):
    def __init__(self, center, vel):
        super().__init__()
        self.vel = vel

        pygame.draw.circle(self.image, GRAY, (size/2, size/2), size/2)

        self.rect.center = center


# entity setting
suspicious_group = pygame.sprite.Group()
infected_group = pygame.sprite.Group()
recovered_group = pygame.sprite.Group()

for i in range(data['population'] - data['initial_infectious']):
    # noinspection PyTypeChecker
    suspicious_group.add(Suspicious())

for i in range(data['initial_infectious']):
    # noinspection PyTypeChecker
    infected_group.add(Infected([random.choice(range(window_w)), random.choice(range(window_h))],
                                [random.choice(range(-10, 10)), random.choice(range(-10, 10))]))
