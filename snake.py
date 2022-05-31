import random
import time
import pygame
from pygame.color import THECOLORS


def play_snake(continue_game=True):
    pygame.init()
    dis = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snake game by Wesson')

    def message(text, color):
        font_style = pygame.font.SysFont('centurygothic', 30, True)
        return font_style.render(text, True, color)

    def your_score(score):
        value = pygame.font.SysFont('centurygothic', 20).render("Score: " + str(score), True, THECOLORS['green2'])
        dis.blit(value, [10, 0])

    def game_loop():
        nonlocal continue_game
        running = True
        game_close = False
        clock = pygame.time.Clock()
        continue_game = True

        x1, y1 = 400, 300
        x1_change, y1_change = 0, 0

        food_x = round(random.randrange(1, 790) / 10.0) * 10.0
        food_y = round(random.randrange(1, 590) / 10.0) * 10.0

        snake_list = []
        length_of_snake = 1

        def our_snake(snake_block, snake_list):
            for i in snake_list:
                pygame.draw.rect(dis, THECOLORS['blue'], [i[0], i[1], snake_block, snake_block])

        while running:

            while game_close:
                dis.fill(THECOLORS['grey11'])
                dis.blit(message('Game over!', THECOLORS['red2']), [310, 240])
                dis.blit(message('Press "C" to play again or press "Q" to quit', THECOLORS['red2']), [110, 275])
                your_score(length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        game_close = False
                        continue_game = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            running = False
                            game_close = False
                            continue_game = False
                        if event.key == pygame.K_c:
                            dis.fill(THECOLORS['grey11'])
                            dis.blit(message('Starting new game...', THECOLORS['red2']), [260, 268])
                            pygame.display.update()
                            time.sleep(2)
                            continue_game = True
                            return None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    continue_game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and x1_change != 10:
                        x1_change = -10
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT and x1_change != -10:
                        x1_change = 10
                        y1_change = 0
                    elif event.key == pygame.K_DOWN and y1_change != -10:
                        x1_change = 0
                        y1_change = 10
                    elif event.key == pygame.K_UP and y1_change != 10:
                        x1_change = 0
                        y1_change = -10
            if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change

            dis.fill(THECOLORS['grey11'])
            pygame.draw.rect(dis, THECOLORS['red'], [food_x, food_y, 10, 10])

            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            our_snake(10, snake_list)
            your_score(length_of_snake - 1)

            pygame.display.update()

            if x1 == food_x and y1 == food_y:
                food_x = round(random.randrange(0, 790) / 10.0) * 10.0
                food_y = round(random.randrange(0, 590) / 10.0) * 10.0
                length_of_snake += 1

            clock.tick(15)  # snake speed

    while continue_game:
        game_loop()

    pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    play_snake()
