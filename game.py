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
vel = 20

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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

    pygame.display.update()

pygame.quit()
