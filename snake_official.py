import pygame, sys
import random
import menus


pygame.init()
grid = pygame.image.load(r"C:\Users\yaoki\Downloads\menu images\green grid1.png")
apple = pygame.image.load(r"C:\Users\yaoki\Downloads\menu images\apple.png")
apple = pygame.transform.scale(apple, (40, 40))
grid = pygame.transform.scale(grid, (500, 500))
window = pygame.display.set_mode((500,500))
window.blit(grid, (0, 0))
pygame.display.set_caption("Snake")
speed = pygame.time.Clock()
 

# game over menu
def game_over(length):
    menus.display_all_end(window, length)
    
# quits pygame
def exit_game():
    pygame.quit()
    sys.exit()

# quit pygames
def pause(p):
    if p:
        p = False
    else:
        p = True
 
# main functionality
def game():
    retry = True
    quit_but = True
    while retry:
        direction = 'left'
        x = 300
        y = 200
     
        snake = []
        length = 1
        
        food_x = round(random.randrange(0, 480) / 20.0) * 20.0
        food_y = round(random.randrange(0, 480) / 20.0) * 20.0
        
        if quit_but:
            menus.main_menu(window)
            
        running = True
        while running:

            for event in pygame.event.get():
                # if player clicks the x, the game quits
                if event.type == pygame.QUIT:
                    exit()
                
                # if a key is pressed, find out what key it is
                if event.type == pygame.KEYDOWN:
                    # the snake cannot move in the opposite direction, so check
                    # the existing direction before assigning a new one
                    # for some reason up and down are reversed, so the opposite
                    # key is added
                    if event.key == pygame.K_UP and (direction != "down"):
                        direction = 'down'
                    elif event.key == pygame.K_DOWN and (direction != "up"):
                        direction = 'up'
                    elif event.key == pygame.K_LEFT and (direction != "right"):
                        direction = 'left'
                    elif event.key == pygame.K_RIGHT and (direction != "left"):
                        direction = 'right'
                    elif event.key == pygame.K_ESCAPE:
                        pause(p)

                
                # check if quit button pressed in game over menu
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if menus.check_quit_clicked(mx, my):
                        quit_but = True
                        retry = True
                        running = False
                    elif menus.check_retry_clicked(mx, my):
                        retry = True
                        running = False
                        quit_but = False
                        

            # moves snake in the current direction
            if direction == "left":
                x -= 20
            elif direction == "right":
                x += 20
            elif direction == "up":
                y += 20
            elif direction == "down":
                y -= 20


            # draw the picnic background
            window.blit(grid, (0, 0))

            # draw the apple food
            window.blit(apple, [food_x, food_y, 20, 20])

            # add the new x, y coordinate to the snake
            snake.append([x, y])

            # delete the last block in the snake, moving it forward
            if len(snake) > length:
                del snake[0]

            # check to see if snake head out of bounds
            if x < 0 or x >= 500 or y < 0 or y >= 500:
                game_over(length)

            # Check to see if snake head touches the body
            for s in snake[:-1]:
                if s == [x, y]:
                    game_over(length)
        
            # draw a square for each block of the snake
            for s in snake:
                pygame.draw.rect(window, "pink", [s[0], s[1], 20, 20])
     
            
            # if the snake head is in the same position as food, make a new food location
            if menus.img_clicked(apple, x, y, (food_x, food_y)):
                length += 1
                # create a random food location, taking into account
                # the size of the snake a food scale
                food_x = round(random.randrange(0, 480) / 20.0) * 20.0
                food_y = round(random.randrange(0, 480) / 20.0) * 20.0

            #prints the score on the screen
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render(f'Score: {length - 1}', True, "white")
            rectangle = text.get_rect()
            window.blit(text, rectangle) 
            # how fast the snake moves
            speed.tick(8)

            # update the display
            pygame.display.update()
 
game()
