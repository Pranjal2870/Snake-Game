import pygame
import random
import os

pygame.mixer.init()

pygame.init()


# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


scr_width = 900             # Screen Width
scr_height = 600            # Screen Height
food_size = 8             # Size of Food



# Setting the position of food
clock = pygame.time.Clock()                                     # Initializing clock
font = pygame.font.SysFont(None, 55)                            # Creating custom font

# Creating Game Window
gameWindow = pygame.display.set_mode((scr_width, scr_height))   # Giving size of your game window
pygame.display.set_caption("Snake.exe")                         # Creating Title for your Game
pygame.display.update()                                         # Updates the game screen

#Background Image

bgimg = pygame.image.load("snake3.jpg")
bgimg = pygame.transform.scale(bgimg, (scr_width, scr_height))#.convert_aplha()


def text_screen(text, color, x, y):                             # Function for showing score on screen
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snk_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snk_size, snk_size])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((233,210,229))
        text_screen("Welcome To Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #pygame.mixer.music.load('')
                    #pygame.mixer.musicplay()
                    gameloop()

        pygame.display.update()
        clock.tick(20)
            

# Creating a game loop
def gameloop():
    # Game Specific Variables
    exit_game = False           # for exiting the game
    game_over = False           # for game over
    snk_x = 45                  # Position of
    snk_y = 55                  # Snake Head
    vlt_x = 0                   # Initial velocity
    vlt_y = 0                   # of the Snake
    snk_list = []
    snk_lenght = 1
    food_x = random.randint(10, scr_width/2)
    food_y = random.randint(10, scr_height/2)
    score = 0                   # variable for counting the score
    init_velocity = 5
    snk_size = 15               # Size of Snake
    fps = 20                     # frames pes second 
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)
            
            for event in pygame.event.get():           
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            
            for event in pygame.event.get():           
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:        # setting the directions
                    if event.key == pygame.K_RIGHT:
                        vlt_x = 10
                        vlt_y = 0
                    if event.key == pygame.K_LEFT:
                        vlt_x = -10
                        vlt_y = 0
                    if event.key == pygame.K_UP:
                        vlt_y = -10
                        vlt_x = 0
                    if event.key == pygame.K_DOWN:
                        vlt_y = 10
                        vlt_x = 0

            snk_x += vlt_x              # updating x and y
            snk_y += vlt_y              # position of Snake

            # Here updations related to food will take place
            if abs(snk_x - food_x + 3) < 15 and abs(snk_y - food_y + 3) < 15:
                score += 10                                                     # Updating Score
                food_x = random.randint(10, scr_width - 10)           # updating the position of food
                food_y = random.randint(10, scr_height - 10)          # after getting eaten by snake
                snk_lenght += 2


            # Everything happening on the screen is being handeled here
            gameWindow.fill(white)                          # Background
            gameWindow.blit(bgimg, (0,0))
            text_screen("Score :" + str(score), red, 5, 5)      # Printing score on screen
            pygame.draw.circle(gameWindow, red, [food_x, food_y], food_size)    # Creating food object

            head = []
            head.append(snk_x)
            head.append(snk_y)
            snk_list.append(head)

            if len(snk_list) > snk_lenght:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                #pygame.mixer.music.load('')
                #pygame.mixer.musicplay()
                
            if snk_x<0 or snk_x>scr_width or snk_y<0 or snk_y>scr_height:
                game_over = True
                #pygame.mixer.music.load('')
                #pygame.mixer.musicplay()
            pygame.draw.rect(gameWindow, black, [snk_x, snk_y, snk_size, snk_size])     # Creating Snake object
            plot_snake(gameWindow, black, snk_list, snk_size)
        pygame.display.update()                                 # Updating game
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()
