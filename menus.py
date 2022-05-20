import pygame, sys

grid_img = pygame.image.load(r"C:\Users\yaoki\Downloads\menu images\green grid1.png")

pygame.font.init()
my_font = pygame.font.SysFont('freesansbold.ttf', 32)

# get end game images
quit_img = pygame.image.load(r"C:\Users\yaoki\Downloads\menu images\game over menu images\cropped quit.png")
retry_img = pygame.image.load(r"C:\Users\yaoki\Downloads\menu images\game over menu images\cropped retry.png")
gover_img = pygame.image.load(r"C:\Users\yaoki\Downloads\menu images\game over menu images\hi low score.png")

# get main menu images
play_img = pygame.image.load(r"C:\Users\yaoki\Downloads\menu images\start menu images\play.png")
how_img = pygame.image.load(r"C:\Users\yaoki\Downloads\menu images\start menu images\how to.png")
how_to_img = pygame.image.load(r"C:\Users\yaoki\Downloads\menu images\start menu images\how to screen.png")
title_img = pygame.image.load(r"C:\Users\yaoki\Downloads\menu images\start menu images\title.png")
exit_img = pygame.image.load(r"C:\Users\yaoki\Downloads\menu images\start menu images\exit.png")

# resize images
gover_img = pygame.transform.scale(gover_img, (300, 300))
quit_img = pygame.transform.scale(quit_img, (150, 85))
retry_img = pygame.transform.scale(retry_img, (150, 85))
play_img = pygame.transform.scale(play_img, (200, 65))
how_img = pygame.transform.scale(how_img, (175, 50))
how_to_img = pygame.transform.scale(how_to_img, (350, 425))
grid_img = pygame.transform.scale(grid_img, (500, 500))
title_img = pygame.transform.scale(title_img, (300, 200))
exit_img = pygame.transform.scale(exit_img, (130, 50))

################################## functions ##################################

def img_clicked(img, x, y, top_left):     # generalized button/img clicked function
    if img.get_rect(topleft = top_left).collidepoint(x, y):
        return True
    return False

def display_bg(window):            # display start/play button
    window.blit(grid_img, (0, 0))

############################# start menu functions #############################
def display_title(window):            # display title
    window.blit(title_img, (90, 50))
    
def display_start(window):            # display start/play button
    window.blit(play_img, (150, 300))

def display_how(window):              # display how to button
    window.blit(how_img, (162, 375))

def display_how_screen(window):       # display how to
    window.blit(how_to_img, (90, 50))

def display_exit(window):
    window.blit(exit_img, (185, 430))

def display_all_main(window):         # display main menu functions
    display_bg(window)
    display_exit(window)
    display_title(window)
    display_how(window)
    display_start(window)

def check_start_clicked(x, y):  # check if start/play button clicked
    return img_clicked(play_img, x, y, (150, 300))

def check_exit_clicked(x, y):  # check if start/play button clicked
    return img_clicked(exit_img, x, y, (185, 430))

def check_how_clicked(window, x, y):    # check if how to button clicked
    if img_clicked(how_img, x, y, (162, 375)):
        display_how_screen(window)
        return True
    return False

def check_how_to_clicked(window, x, y): # check if how to button clicked
    if img_clicked(how_to_img, x, y, (90, 50)):
        display_all_main(window)
        return False
    return True

def main_menu(window):
    display_all_main(window)
    how, run = False, True
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                x, y = event.pos
                if how: # if how to button clicked, check if how to screen clicked
                    how = check_how_to_clicked(window, x, y)
                elif check_start_clicked(x, y): # if strt clicked, start game
                    run = False  
                elif check_exit_clicked(x, y):  # if exit button clicked, exit
                    pygame.quit()
                    sys.exit()
                how = check_how_clicked(window, x, y)   # check if how to button clicked
        pygame.display.update()
      
        
############################## end menu functions ##############################
def display_end(window):              # display end menu with high score and current score
    window.blit(gover_img, (100, 100))

def display_retry(window):            # display retry button
    window.blit(retry_img, (250, 300))

def display_quit(window):             # display quit button
    window.blit(quit_img, (100, 300))

def display_all_end(window, length):    # display entire game over menu
    display_bg(window)
    display_end(window)
    display_retry(window)
    display_quit(window)

    #prints the current score on the screen
    font = pygame.font.Font('freesansbold.ttf', 40)
    text = font.render(f'{length - 1}', True, "white")
    rectangle = text.get_rect(topleft = (230, 215))
    window.blit(text, rectangle)

    # prints high score
    text = font.render(f'{20}', True, "white")
    rectangle = text.get_rect(topleft = (220, 150))
    window.blit(text, rectangle)
def check_quit_clicked(x, y):   # check if quit button clicked
    return img_clicked(quit_img, x, y, (100, 300))

def check_retry_clicked(x, y):  # check if retry button clicked
    return img_clicked(retry_img, x, y, (250, 300))

