import random
import time
import pygame
from pygame.color import THECOLORS

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

SNAKE_SPEED = 30


def play_snake(continue_game=True):
    print("It's a simple snake game, use arrow-buttons to move, else you can increase your speed by pressing '+' or "
          "'-'.")
    time.sleep(5)
    pygame.init()
    dis = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake game by Wesson')

    def message(text, color):
        font_style = pygame.font.Font('font/centurygothic_bold.ttf', 20)
        return font_style.render(text, True, color)

    def your_score(score):
        value = pygame.font.Font('font/centurygothic.ttf', 20).render("Score: " + str(score), True, THECOLORS['green2'])
        dis.blit(value, [10, 0])

    def our_snake(snake_block, snake_list):
        for i in snake_list:
            pygame.draw.rect(dis, THECOLORS['blue'], [i[0], i[1], snake_block, snake_block])

    def get_food_coordinates() -> tuple[float, float]:
        food_x = round(random.randrange(1, WINDOW_WIDTH - 10) / 10.0) * 10.0
        food_y = round(random.randrange(1, WINDOW_HEIGHT - 10) / 10.0) * 10.0
        return food_x, food_y

    def is_food_inside_snake(snake_list: list[list[int, int]], food_x: float, food_y: float) -> bool:
        for snake_block in snake_list:
            if snake_block[0] == food_x and snake_block[1] == food_y:
                return True
        return False

    def game_loop():
        nonlocal continue_game
        running = True
        game_close = False
        clock = pygame.time.Clock()
        continue_game = True

        change_to = 'STAY'
        direction = 'STAY'
        snake_speed = SNAKE_SPEED

        x1, y1 = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
        x1_change, y1_change = 0, 0

        food_x, food_y = get_food_coordinates()

        snake_list = []
        length_of_snake = 1

        while running:

            while game_close:
                dis.fill(THECOLORS['grey11'])
                dis.blit(message('Game over!', THECOLORS['red2']), [340, 255])
                dis.blit(message('Press "C" to play again or press "Q" to quit', THECOLORS['red2']), [190, 285])
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
                            dis.blit(message('Starting new game...', THECOLORS['red2']), [300, 275])
                            pygame.display.update()
                            time.sleep(2)
                            continue_game = True
                            return None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continue_game = False
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'
                    if event.key == pygame.K_EQUALS:
                        if snake_speed + 4 <= 60:
                            snake_speed += 4
                    if event.key == pygame.K_MINUS:
                        if snake_speed - 4 >= 0:
                            snake_speed -= 4

            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'

            if direction == 'UP':
                x1_change = 0
                y1_change = -10
            if direction == 'DOWN':
                x1_change = 0
                y1_change = 10
            if direction == 'LEFT':
                x1_change = -10
                y1_change = 0
            if direction == 'RIGHT':
                x1_change = 10
                y1_change = 0

            if x1 >= WINDOW_WIDTH or x1 < 0 or y1 >= WINDOW_HEIGHT or y1 < 0:
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
                food_x, food_y = get_food_coordinates()
                length_of_snake += 1
                while True:
                    if is_food_inside_snake(snake_list, food_x, food_y):
                        food_x, food_y = get_food_coordinates()
                        length_of_snake += 1
                        continue
                    break

            clock.tick(snake_speed)  # snake speed

    while continue_game:
        game_loop()

    pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    play_snake()
