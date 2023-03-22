import pygame
import random

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game with Enemy Snake")


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)


font_style = pygame.font.SysFont(None, 50)

block_size = 10

clock = pygame.time.Clock()



def message(msg, color):

    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])


def draw_snake(block_size, snake_List):

    for x in snake_List:
        pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])


def gameLoop():

    game_over = False
    game_close = False


    lead_x = screen_width / 2
    lead_y = screen_height / 2
    lead_x_change = 0
    lead_y_change = 0

    enemy_x = random.randrange(0, screen_width - block_size, block_size)
    enemy_y = random.randrange(0, screen_height - block_size, block_size)
    enemy_x_change = 0
    enemy_y_change = 0


    snake_List = []
    Length_of_snake = 1


    food_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update(
                snake_List + [food_x, food_y, block_size, block_size] + [enemy_x, enemy_y, block_size, block_size])


            for event in pygame.event.get():
                print(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0


        if lead_x > enemy_x:
            enemy_x_change = block_size
        elif lead_x < enemy_x:
            enemy_x_change = -block_size
        elif lead_y > enemy_y:
            enemy_y_change = block_size
        elif lead_y < enemy_y:
            enemy_y_change = -block_size


        if enemy_x >= screen_width - block_size or enemy_x < 0 or enemy_y >= screen_height - block_size or enemy_y < 0:
            enemy_x_change = -enemy_x_change
            enemy_y_change = -enemy_y_change


        for x in snake_List:
            if x == [enemy_x, enemy_y]:
                game_close = True


        if lead_x >= screen_width or lead_x < 0 or lead_y >= screen_height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change


        enemy_x += enemy_x_change
        enemy_y += enemy_y_change

        screen.fill(white)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])
        snake_Head = []
        snake_Head.append(lead_x)
        snake_Head.append(lead_y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]


        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(block_size, snake_List)
        pygame.draw.rect(screen, black, [enemy_x, enemy_y, block_size, block_size])
        pygame.display.update()


        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
            Length_of_snake += 1

   
        clock.tick(15)


gameLoop()
pygame.quit()
