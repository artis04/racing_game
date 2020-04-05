import pygame
import math

cos = math.cos

# creates size of window
pygame.init()
# scr_width = 1650
# scr_height = 927
scr_width = 1350
scr_height = 944

win = pygame.display.set_mode((scr_width, scr_height))

# creates title of window
pygame.display.set_caption("Racing game")

#background
# background = pygame.image.load('images/racing rack/track1.png')
background = pygame.image.load('images/racing rack/track2.png')

# x and y coordinates for player car
x = 712
y = 823
speed_y = 0
speed_x = 3
speed = 0
angle = 0
angle_attack = 8


# image = pygame.image.load('images/car1/unknown.png')
# image = win.blit(pygame.image.load('images/car1/car1.png'), (x, y))
start = 712, 823  # start position on screen
image_surf = pygame.image.load('images/car1/car1.png').convert()  # create variable with image
image_surf.set_colorkey((0, 0, 0))  # removes black background from image
# win.blit(image_surf, start)

xy = start

run = True
border = ['163 140', '133 190', '109 214', '85 288', '70 404', '76 481', '81 578', '96 681', '129 760', '178 819', '248 865', '337 890', '430 899', '546 913', '661 911', '790 914', '928 905', '1021 885', '1110 857', '1112 862', '1175 825', '1229 774', '1267 699', '1289 622', '1290 538', '1266 445', '1235 383', '1179 332', '1132 310', '1072 277', '979 264', '900 263', '831 283', '774 297', '718 316', '694 324', '682 305', '701 262', '715 218', '724 172', '710 116', '683 89', '644 69', '610 51', '533 42', '470 38', '391 39', '302 49', '246 74', '200 93', '165 123', '151 159']

def move(x, y, speed, angle):
    mathCos =  math.cos(angle)
    mathSin = math.sin(angle)

    new_y = y - mathSin * speed
    new_x = x + mathCos * speed



    return new_x, new_y

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
    # on event pressed X quit the game
        if event.type == pygame.QUIT:
            run = False

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mx, my = pygame.mouse.get_pos()
        #     location = str(mx) + " " + str(my)
        #     border.append(location)
        #     print(border)


    # on arrow keys pressed event
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed_x:
        x -= speed_x
        angle += angle_attack
        speed_x = -1
        if angle > 360:
            angle = 0

    if keys[pygame.K_RIGHT] and x < scr_width:
        x += speed_x
        angle -= angle_attack
        if angle < -360:
            angle = 0
        speed_x = 1


    if keys[pygame.K_UP] and y > 0:

        result = speed_y * cos(angle)
        print('angle ', angle)
        print(result)
        if not speed > 30:
            speed += 3.3

    if keys[pygame.K_DOWN] and y < scr_height:
        if not speed < -10:
            speed -= 3

    if not keys[pygame.K_DOWN] and not keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        if speed > 0:
            speed -= 0.5
        elif speed < 0:
            speed += 0.5
        else:
            speed = 0


    # update display
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))


    # create a car
    # win.blit(pygame.image.load('images/car1/car1.png'), (x, y))

    surf = pygame.transform.rotate(image_surf, angle)



    radians = angle * math.pi / 180
    xy = move(x, y, speed, radians)


    y = xy[1]
    x = xy[0]
    win.blit(surf,(x, y))




    pygame.display.update()

pygame.quit()
