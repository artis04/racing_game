import pygame
import math


pygame.init()
# scr_width = 1650 # --> using for first track
# scr_height = 927
scr_width = 1350
scr_height = 944

win = pygame.display.set_mode((scr_width, scr_height))

# creates title of window
pygame.display.set_caption("Racing game")

# tracks
# background = pygame.image.load('images/racing_track/track1.png')
background = pygame.image.load('images/racing_track/track2.png')

# x and y coordinates for player car
x = 593
y = 802
max_speed = 30  # Max speed for the car
back_max_speed = 10  # Max reverse speed for the car
speed = 0  # Starting speed
angle = 0  # Starting angle of the car
angle_attack = 8  # Angle attack pressing left/right arrow (degrees)
laps = 0  # Lap count start
speed_increase = 3.3  # How fast car increases speed
onetime = 0  # Thing for cars sound
ticks = 0  # Game ticks for lap count


car_image = pygame.image.load('images/cars/car1.png').convert()  # takes car image from images/cars/car1.png
car_image.set_colorkey((0, 0, 0))  # removes black background from image

car1_sound = pygame.mixer.Sound("sound/cars/car1/boost.wav")  # Loads car sound as car1_sound
music2 = pygame.mixer.music.load("sound/music/music2.wav")  # Loads background music
pygame.mixer.Sound.set_volume(car1_sound, 0.1)  # Sets volume for car1 sound
pygame.mixer.music.set_volume(0.01)  # Sets volume for music
pygame.mixer.music.play(-1)  # Plays background music

border = ['163 140', '133 190', '109 214', '85 288', '70 404', '76 481', '81 578', '96 681', '129 760', '178 819',
          '248 865', '337 890', '430 899', '546 913', '661 911', '790 914', '928 905', '1021 885', '1110 857',
          '1112 862', '1175 825', '1229 774', '1267 699', '1289 622', '1290 538', '1266 445', '1235 383', '1179 332',
          '1132 310', '1072 277', '979 264', '900 263', '831 283', '774 297', '718 316', '694 324', '682 305',
          '701 262', '715 218', '724 172', '710 116', '683 89', '644 69', '610 51', '533 42', '470 38', '391 39',
          '302 49', '246 74', '200 93', '165 123', '151 159']
# border list is points (x and y) where should be outside border


def move(x, y, speed, angle):  # Calculates where should be car in next frame (x and y), depending on angle and speed

    new_y = y - math.sin(angle) * speed
    new_x = x + math.cos(angle) * speed
    return new_x, new_y

def border_hit(x, y):  # if hits border then returns True, else False
    pass

run = True
while run:  # Loops pygame
    pygame.time.delay(100)
    ticks += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # For testing only, when you press on screen somewhere
            mx, my = pygame.mouse.get_pos()       # it prints x and y coordinates
            location = str(mx) + " " + str(my)
            # border.append(location)
            print(location)

    keys = pygame.key.get_pressed()  # On arrow keys triggered
    if keys[pygame.K_LEFT]:  # On left arrow key triggered
        if speed > 0:
            angle += angle_attack  # If speed is more than 0 then increases angle for car
        elif speed < 0:
            angle -= angle_attack  # If speed is less than 0 then reduce angle for car
        # if speed == 0 then nothing happens
        if angle > 360:  # in case angle reaches 360 degrees, then it goes back to 0
            angle = 0

    if keys[pygame.K_RIGHT]:  # On right arrow key triggered
        if speed > 0:
            angle -= angle_attack  # If speed is more than 0 then reduces cars angle
        elif speed < 0:
            angle += angle_attack  # If speed is less than 0 then increases angle for car

        if angle < -360:  # In case angle reaches -360 degrees, then it goes back to 0
            angle = 0


    if keys[pygame.K_UP] and y > 0:

        if onetime == 0:  # This prevents spam sound if Up arrow key is pressed and hold
            pygame.mixer.Sound.stop(car1_sound)  # Stop previous sound effect
            pygame.mixer.Sound.play(car1_sound)  # Start sound effect
            onetime = 1  # prevents spam sound

        if not speed > max_speed:  # If speed is less than max speed, then it increases speed value by "speed_increase" variable
            speed += speed_increase

    if keys[pygame.K_DOWN] and y < scr_height:  # On down key pressed
        if not speed < -back_max_speed:  # If speed is more than max back speed then reduce speed by 3
            speed -= 3

    if not keys[pygame.K_DOWN] and not keys[pygame.K_UP] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        if speed > 0:  # if non of arrow keys are pressed, then reduce speed until it is 0
            speed -= 0.5
        elif speed < 0:
            speed += 0.5
        else:
            speed = 0

    if not keys[pygame.K_UP]:  # if up arrow key is pressed stop car sound and restart spam prevention
        onetime = 0
        pygame.mixer.Sound.stop(car1_sound)

    # Display update
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))

    surf = pygame.transform.rotate(car_image, angle)  # shows car with correct angle

    radians = angle * math.pi / 180  # Calculates from degrees to radians (because package math uses radians)
    xy = move(x, y, speed, radians)  # calls "move" function and gives x, y coordinates, speed and angle

    y = xy[1]  # from "move" function gets next frame y location
    x = xy[0]  # from "move" function gets next frame x location
    win.blit(surf, (x, y))  # places car at x and y coordinates
    if x < 750 and x >= 717 and y >= 737 and y <= 909 and ticks > 60:
        # checks if you pass finish line and over 60 ticks have passed
        ticks = 0  # restarts ticks to 0
        print("Finish line")
        laps += 1  # add 1 more lap to count
        print("Laps ", laps)  # Prints lap count



    pygame.display.update()  # updates display

pygame.quit()  # quits pygame
