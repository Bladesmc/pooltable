import pygame, sys, math
import ball

#TODO: fix mospos/ballpos calls

pygame.init()

# CONSTANTS
x = 0
y = 1
size = width, height = 360, 720
font = pygame.font.SysFont("Arial", 15)
clock = pygame.time.Clock()
green = 34, 139, 34
white = 255, 255, 255
red = 255, 0, 0

#BALLS
cueball = ball.Ball()
cueballpos = cueball.get_pos()
ball1 = ball.Ball()
ball1.set_pos([width/2, 100])
ball1pos = ball1.get_pos()

# BALL LIST
ball_list = [cueball, ball1]
ball_pos_list = [cueballpos, ball1pos]

# CHANGEABLE VARIABLES
decel = cueball.get_decel_int()
hitdb = 0
ballsize = 10

screen = pygame.display.set_mode(size)
# ball = pygame.draw.circle(screen, white, ballpos, ballsize)
pwr = 3
pwrup = 0
xd = 0
yd = 0
pygame.mouse.set_visible(False)
db = False


while True:
    if pwrup == 0: mospos = pygame.mouse.get_pos()

    xd = mospos[x] - cueballpos[x]
    yd = mospos[y] - cueballpos[y]

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and hitdb == 0:
                pwrup = 1
            elif event.key == pygame.K_F3:
                db = not db
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and hitdb == 0:
                cueball.set_velo(xd, yd, pwr)

            hitdb = 1
            pwr = 3
            pwrup = 0


    if pwrup == 1 and pwr < 10: pwr = pwr + 1

    if cueball.get_velo() == [0, 0]: hitdb = 0

    pwrtxt = font.render("pwr: " + str(pwr), False, white)
    xdc = font.render("xd: " + str(xd), False, white)
    ydc = font.render("yd: " + str(yd), False, white)
    hdbt = font.render("hdb:" + str(hitdb), False, white)

    screen.fill(green)
    if db == True:
        screen.blit(hdbt, (0,0))
        screen.blit(xdc, (0, 40))
        screen.blit(ydc, (0, 50))
        screen.blit(pwrtxt, (0, 60))
        pygame.draw.line(screen, white, cueballpos, ball1pos)

    # Collisions
    # For loop that goes through each ball and checks to see if another ball is within 5 pixels (ballsize/2)
    for b in ball_list:
        current = b.get_pos()
        for other in ball_list:
            # Compare current position to other balls
            if other is not b:
                loc = other.get_pos()
                currentxd = current[x] - loc[x]
                currentyd = current[y] - loc[y]
                if (currentxd <= 5 and currentxd >= -5) and (currentyd <= 5 and currentyd >= -5):
                    b.set_velo(currentxd, currentyd, 5)
                    print("current d: " + str(currentxd) + ", " + str(currentyd))


    # Get the ball positions for this frame
    #   Cue
    cueballpos = cueball.get_pos()
    #   Ball1
    ball1pos = ball1.get_pos()

    # Draw the balls
    #   Cue
    pygame.draw.circle(screen, white, cueballpos, ballsize)
    #   Ball 1
    pygame.draw.circle(screen, red, ball1pos, ballsize)

    # Draw the power indicator
    pygame.draw.circle(screen, red, mospos, pwr)

    pygame.display.flip()
    clock.tick(60)