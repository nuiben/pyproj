import pygame
from pygame.locals import *

# Pygame Initialization
pygame.init()
pygame.display.set_caption('Promodoro Timer')
catppucin_cat = pygame.transform.scale(pygame.image.load("catppuccin.png"), (64, 64))
#cat_64 = pygame.image.load('catppuccin_64.png')
nyan_cat = pygame.transform.scale(pygame.image.load("nyan.png"), (64, 64))
timer = pygame.image.load('promodoro_01.png')

pygame.display.set_icon(timer)

# Catppuccin Colors
pink = (243, 188, 230)  # F3BCE6
yankees_blue = (36, 39, 58)  # 24273A
lavender = (194, 157, 241)  # C29DF1

# Time Values
clock = pygame.time.Clock()

# Clickable Catppucin
pygame.mouse.set_pos(128, 150)
mouse_pos = pygame.mouse.get_pos()
# cat_position = cat.get_rect()
cat_position = Rect(150, 150, 64, 64)
cat_position.collidepoint(mouse_pos)

# Set up the display
default_font_size = 30
display_height = 300
display_width = 400
gameDisplay = pygame.display.set_mode((display_width, display_height))


def display_cat(cat):
    gameDisplay.blit(cat, (
    (display_width / 2) - 32, display_height * 0.5))  # Promodoro_05 is 64x64: -32 is centering the image.


# Function to display text
def display_text(text, x, y, size):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, lavender)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)


# Function for Pomodoro timer
def pomodoro_timer(task_name):
    # 25, 10, 25
    timeline = ["25 minute promodoro", "5 minute break"] * 3 + ["25 minute promodoro", "15 minute break"]

    for stage in timeline:
        if "promodoro" in stage:
            task_status = f"Task: {task_name}"
            current_cat = nyan_cat
        else:
            task_status = "Break time"
            current_cat = catppucin_cat
        minutes = int(stage.split()[0]) - 1
        seconds = 60

        pygame.time.set_timer(pygame.USEREVENT, 1000)

        # NEW COUNTDOWN LOOP
        run = True
        while run:
            for event in pygame.event.get():
                if minutes == 0 and seconds == 0:
                    run = False
                #print('Event: ' + str(event.type))
                if event.type == pygame.USEREVENT:
                    if seconds > 0:
                        seconds -= 1  # print('{}:{}'.format(minutes, seconds))
                    gameDisplay.fill(yankees_blue)

                    # Display the Task input by the User
                    display_text(task_status, display_width / 2, display_height * 0.1, default_font_size)

                    # Display the Current Stage (Promodoro, Long Break, or Short Break)
                    display_text("Stage: " + stage, display_width / 2, display_height * 0.8, 17)
                    display_cat(current_cat)

                    if seconds < 1 and minutes > 0:
                        seconds = 60
                        minutes -= 1
                        display_text(f"{'%02d' % (minutes + 1)}:00", display_width / 2, display_height / 3,
                                     default_font_size + 2)
                    else:
                        display_text(f"{'%02d' % minutes}:{'%02d' % seconds}", display_width / 2,
                                     display_height / 3, default_font_size + 2)
                elif event.type == MOUSEBUTTONDOWN:
                    # mouse_pos = event.pos  # Now it will have the coordinates of click point.
                    # print('Cat Position: {}\nMouse Position {}'.format(cat_position, mouse_pos))
                    if cat_position.collidepoint(event.pos):
                        print('meow')
                        # Need this to pause the timer
                elif event.type == pygame.QUIT:
                    run = False
                pygame.display.update()
                clock.tick(60)


if __name__ == "__main__":
    # task = input("Enter the task name: ")
    task = 'Promodoro'
    pomodoro_timer(task)
    pygame.quit()
    quit()
