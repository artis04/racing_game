import pygame

# adds about.txt file
f = open("about.txt", "a+")
f.write("hello to this game")
f.close()


pygame.init()
# scr_width = 1650
# scr_height = 927
scr_width = 1350
scr_height = 944


win = pygame.display.set_mode((scr_width, scr_height))

pygame.display.set_caption("Racing game")

#background
# background = pygame.image.load('images/racing rack/track1.png')
background = pygame.image.load('images/racing rack/track2.png')


x = 50
y = 50
width = 16
height = 20
vel = 35

image = pygame.image.load('images/car1/unknown.png')


run = True
border = ['163 140', '133 190', '109 214', '85 288', '70 404', '76 481', '81 578', '96 681', '129 760', '178 819', '248 865', '337 890', '430 899', '546 913', '661 911', '790 914', '928 905', '1021 885', '1110 857', '1112 862', '1175 825', '1229 774', '1267 699', '1289 622', '1290 538', '1266 445', '1235 383', '1179 332', '1132 310', '1072 277', '979 264', '900 263', '831 283', '774 297', '718 316', '694 324', '682 305', '701 262', '715 218', '724 172', '710 116', '683 89', '644 69', '610 51', '533 42', '470 38', '391 39', '302 49', '246 74', '200 93', '165 123', '151 159']

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mx, my = pygame.mouse.get_pos()
        #     location = str(mx) + " " + str(my)
        #     border.append(location)
        #     print(border)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < scr_width - width:
        x += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < scr_height - height:
        y += vel

    win.fill((0, 0, 0))
    win.blit(background, (0, 0))

    pygame.draw.rect(win, (255, 99, 71), (x, y, width, height))
    pygame.display.set_mode((scr_width, scr_height)).blit(image, (0, 0))


    pygame.display.update()

pygame.quit()
