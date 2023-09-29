import pygame
import csv

import entity
pygame.init()


class Time:
    timer = 0

    clock = pygame.time.Clock()
    event_1 = pygame.USEREVENT + 1
    pygame.time.set_timer(event_1, 1000)


def write():
    with open('record.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            len(entity.suspicious_group) / entity.number_s,
            len(entity.infected_group) / entity.number_s,
            len(entity.recovered_group) / entity.number_s
        ])


with open('record.csv', 'w', newline=''):
    pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == Time.event_1:
            for i in entity.infected_group:
                i.recover_time -= 1
            write()

            Time.timer += 1

    entity.window.fill((255, 255, 255))

    entity.suspicious_group.draw(entity.window)
    entity.suspicious_group.update()

    for s in entity.suspicious_group:
        s.infection_check()

    entity.infected_group.draw(entity.window)
    entity.infected_group.update()
    entity.recovered_group.draw(entity.window)
    entity.recovered_group.update()

    pygame.display.update()
    Time.clock.tick(60)
pygame.quit()
