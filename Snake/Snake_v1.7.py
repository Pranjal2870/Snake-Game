'''
Snake Game_v1.7

* What's new

  New Home Screen added

'''
import pygame
import random
import os

pygame.mixer.init()
pygame.init()

# Colors(Here colours for different
white = (255, 255, 255)
blue = (24, 87, 186)
red = (255, 0, 0)
black = (0, 0, 0)
green = (110, 110, 5)
darkGreen = (0, 100, 0)

# Game Specific Variables
scr_width = 400  # Screen Width
scr_height = 400  # Screen Height
clock = pygame.time.Clock()  # Initializing clock
font = pygame.font.SysFont(None, 40)  # Creating custom font

# Creating Game Window
gameWindow = pygame.display.set_mode((scr_width, scr_height))  # Giving size of your game window
pygame.display.set_caption("Snake.exe")  # Creating Title for your Game
pygame.display.update()  # Updates the game screen


# Function to print message on Main Screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# Snake Body
def plot_snake(gameWindow, color, snk_list, snk_size):
    for x, y in snk_list:
        # pygame.draw.rect(gameWindow, color, [x, y, snk_size, snk_size])
        pygame.draw.circle(gameWindow, blue, [x, y], snk_size)  # Creating food object


def welcome():
    exit_game = False

    pygame.mixer.music.load("Snake.mp3")
    pygame.mixer.music.play()

    while not exit_game:
        gameWindow.fill(green)
        bgimg = pygame.image.load("SnakeImg.jpg")
        bgimg = pygame.transform.scale(bgimg, (scr_width, scr_height)).convert_alpha()
        gameWindow.blit(bgimg, (0, 0))

        text_screen("Press [Space] to Play", black, 59, 360)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(30)


# Main Game Loop
def gameloop():

    # Variables(Here all the necessary variable for the game are available)
    snk_x = 10  # Position of
    snk_y = 10  # Snake Head
    snk_size = 10  # Size of Snake
    food_size = 10  # Size of Food
    fps = 60  # frames pes second
    vlt_x = 0  # Initial velocity
    vlt_y = 0  # of the Snake
    vlt = 7
    score = 0  # variable for counting the score
    exit_game = False  # for exiting the game
    game_over = False  # for game over


    # Setting the position of food(This is where the position of
    # food will be decide every time it gets eaten by the snake)
    food_x = random.randint(0, scr_width)
    food_y = random.randint(0, scr_height)

    snk_list = []
    snk_lenght = 1

    # Check if High Score File exists
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            bgimg = pygame.image.load("Background.png")
            bgimg = pygame.transform.scale(bgimg, (scr_width, scr_height)).convert_alpha()
            gameWindow.blit(bgimg, (0, 0))


            text_screen("Game Over!", black, 120, 150)
            text_screen("Press Enter to Continue", black, 38, 360)

            for event in pygame.event.get():  # getting i/p from hardware
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():  # getting i/p from hardware
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:  # setting the directions
                    if event.key == pygame.K_RIGHT and vlt_x != -vlt:
                        vlt_x = vlt
                        vlt_y = 0
                        pygame.mixer.music.load("sounds_bump.mp3")
                        pygame.mixer.music.play()

                    if event.key == pygame.K_LEFT and vlt_x != vlt:
                        vlt_x = -vlt
                        vlt_y = 0
                        pygame.mixer.music.load("sounds_bump.mp3")
                        pygame.mixer.music.play()

                    if event.key == pygame.K_UP and vlt_y != vlt:
                        vlt_y = -vlt
                        vlt_x = 0
                        pygame.mixer.music.load("sounds_bump.mp3")
                        pygame.mixer.music.play()

                    if event.key == pygame.K_DOWN and vlt_y != -vlt:
                        vlt_y = vlt
                        vlt_x = 0
                        pygame.mixer.music.load("sounds_bump.mp3")
                        pygame.mixer.music.play()

            snk_x += vlt_x  # updating x and y
            snk_y += vlt_y  # position of Snake

            # Here updations related to food will take place
            if abs(snk_x - food_x) < 20 and abs(snk_y - food_y) < 20:
                score += 10  # Updating Score
                pygame.mixer.music.load("sounds_coin.mp3")
                pygame.mixer.music.play()
                food_x = random.randint(10, scr_width - 10)  # updating the position of food
                food_y = random.randint(10, scr_height - 10)  # after getting eaten by snake
                snk_lenght += 2

                if score>int(hiscore):
                    hiscore = score

            # Everything happening on the screen is being handeled here
            # gameWindow.fill(green)  # Background

            bgimg = pygame.image.load("Background.png")
            bgimg = pygame.transform.scale(bgimg, (scr_width, scr_height)).convert_alpha()
            gameWindow.blit(bgimg, (0, 0))

            text_screen("Score :" + str(score) + "  High Score:" + str(hiscore), black, 5, 5)  # Printing score on screen
            pygame.draw.circle(gameWindow, red, [food_x, food_y], food_size)  # Creating food object

            head = []  # List for creating main body of the snake
            head.append(snk_x)
            head.append(snk_y)
            snk_list.append(head)

            # Here length of the snake is managed
            if len(snk_list) > snk_lenght:
                del snk_list[0]


            # If the snake collides with itself then game should get over
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("sounds_dead.wav")
                pygame.mixer.music.play()
                # pygame.mixer.music.

            if snk_x < 0 or snk_x > scr_width or snk_y < 0 or snk_y > scr_height:
                game_over = True
                pygame.mixer.music.load("sounds_dead.wav")
                pygame.mixer.music.play()

            plot_snake(gameWindow, black, snk_list, snk_size)
        pygame.display.update()  # Updating game
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()