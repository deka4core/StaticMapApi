import os
import sys

import pygame
import requests

map_request = "http://static-maps.yandex.ru/1.x/"
ll = list(map(float, input("Введите координаты в формате (x,y): ").split(',')))
spn = float(input("Введите коэффициент масштабирования: "))
map_file = "map.png"


def do_map(spn, ll, map_file):
    params = {"ll": ','.join(list(map(str, ll))),
              "spn": f"{spn},{spn}",
              "l": "map"}
    response = requests.get(map_request, params=params)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    # Запишем полученное изображение в файл.
    with open(map_file, "wb") as file:
        file.write(response.content)


do_map(spn, ll, map_file)
# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                spn = spn * 2 if spn * 2 <= 50 else spn
            elif event.key == pygame.K_PAGEDOWN:
                spn = spn / 2 if spn / 2 >= 0.002 else spn
            elif event.key == pygame.K_UP:
                ll[1] = ll[1] + spn * 2 if ll[1] + spn * 2 < 85 else ll[1]
            elif event.key == pygame.K_DOWN:
                ll[1] = ll[1] - spn * 2 if ll[1] - spn * 2 > -85 else ll[1]
            elif event.key == pygame.K_LEFT:
                ll[0] = ll[0] - spn * 2 if ll[0] - spn * 2 > -180 else ll[0]
            elif event.key == pygame.K_RIGHT:
                ll[0] = ll[0] + spn * 2 if ll[0] + spn * 2 < 180 else ll[0]
            do_map(spn, ll, map_file)

    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))
    # Переключаем экран, и ждем закрытия окна.
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
# Удаляем за собой файл с изображением.
os.remove(map_file)