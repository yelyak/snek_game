import asyncio
import pygame
import time
import buttons
from snake import Snake
from fruit import Fruit

screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.init()
clock = pygame.time.Clock()

continue_img = pygame.image.load("continue.png")
exit_img = pygame.image.load("leave.png")

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
blue = pygame.Color(0,0,255)
yellow = pygame.Color(255,255,0)
green = pygame.Color(0,255,0)
orange = pygame.Color(255,100,10)
purple = pygame.Color(240,0,255)
pink = pygame.Color(255,100,180)

async def main():

    snake = Snake()
    fruit = Fruit(screen_width, screen_height)

    score = 0
    speed = 10

    continue_button = buttons.Button(20, 400, continue_img, 0.2)
    exit_button = buttons.Button(620, 400, exit_img, 0.2)
    show_buttons = False
    has_won = False


    def fruit_eaten():
        if snake.head[0] == fruit.location[0] and snake.head[1] == fruit.location[1]:
            global score
            score += 1
            return True
        else:
            return False

    def show_score(self, color, font, size):
        score_font = pygame.font.SysFont(font,size)
        score_surface = score_font.render(f"Score: {score}", True, color)
        score_rect = score_surface.get_rect()
        screen.blit(score_surface, score_rect)

    def win():
        global show_buttons
        win_font = pygame.font.SysFont("arial", 50)
        win_surface = win_font.render(f"Congrats! Your Score: {score}", True, blue)
        win_rect = win_surface.get_rect()
        win_rect.midtop = (screen_width / 2, screen_height / 4)
        screen.blit(win_surface, win_rect)
        pygame.display.flip()

        show_buttons = True
        while show_buttons:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            if continue_button.draw(screen):
                show_buttons = False

            if exit_button.draw(screen):
                pygame.quit()
                quit()

            pygame.display.update()

        # clearing screen??
        screen.fill(black)
        for block in snake.body:
            pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], 10, 10))
        pygame.draw.rect(screen, pink, pygame.Rect(fruit.location[0], fruit.location[1], 10, 10))
        show_score(1, white, "arial", 25)
        pygame.display.update()

    def death():
        death_font = pygame.font.SysFont("arial",50)
        death_surface = death_font.render(f"Game Lost! Your Score: {score}", True, red)
        death_rect = death_surface.get_rect()
        death_rect.midtop = (screen_width / 2, screen_height / 4)
        screen.blit(death_surface, death_rect)
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        quit()

    run = True
    while run:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction = 'RIGHT'
                elif event.key == pygame.K_UP:
                    snake.change_direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    snake.change_direction = 'DOWN'
            if event.type == pygame.QUIT:
                quit()

        snake.move()


        for block in snake.body:
            pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], 10, 10))

        pygame.draw.rect(screen, pink, pygame.Rect(fruit.location[0], fruit.location[1], 10, 10))

        if fruit_eaten():
            fruit.randomize_location(screen_width, screen_height)
            snake.add_length(True)
        else:
            snake.add_length(False)

        if snake.hit_body() or snake.hit_wall(screen_width, screen_height):
            death()

        if (score >= 10 and not has_won):
            has_won = True  # Update the flag when the player wins
            win()

        if score > 10:
            speed = 20

        if score > 20:
            speed = 30

        if score > 30:
            speed = 40

        if score > 40:
            speed = 50

        if score > 50:
            speed = 60

        if score > 55:
            speed = 65

        if score > 100:
            speed = 75

        if score > 150:
            speed = 80

        if score > 200:
            speed = 90

        show_score(1, white, "arial", 25)
        pygame.display.update()
        clock.tick(speed)
        await asyncio.sleep(0)

asyncio.run(main())
