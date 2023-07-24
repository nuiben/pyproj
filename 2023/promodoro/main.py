import pygame

# Pygame Initialization
pygame.init()

# Catppuccin Colors
pink = (243,188,230) #F3BCE6
yankees_blue = (36, 39, 58) #24273A
lavender = (194, 157, 241) #C29DF1

# Time Values
clock = pygame.time.Clock()

# Set up the display
display_height = 250
display_width = 400
gameDisplay = pygame.display.set_mode((display_width, display_height))


# Function to display text
def display_text(text, x, y):
    font = pygame.font.Font(pygame.font.match_font('arial'), 20)
    text_surface = font.render(text, True, lavender)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)


# Function for Pomodoro timer
def pomodoro_timer(task_name):
    timeline = ["25 minute promodoro", "5 minute break"] * 4 + ["25 minute break"]

    for stage in timeline:
        if "promodoro" in stage:
            task_status = f"Task: {task_name}"
        else:
            task_status = "Break time"
        minutes = int(stage.split()[0])-1
        seconds = 60

        pygame.time.set_timer(pygame.USEREVENT, 1000)

        #NEW COUNTDOWN LOOP
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    minutes_text = str(minutes).rjust(3)
                    seconds -= 1 #print('{}:{}'.format(minutes, seconds))
                    gameDisplay.fill(yankees_blue)

                    #Display the Task input by the User
                    display_text(task_status, display_width / 2, display_height * 0.1)

                    #Display the Current Stage (Promodoro, Long Break, or Short Break)
                    display_text("Stage: " + stage, display_width / 2, display_height * 0.9)

                    if seconds < 1 and minutes != 0:
                        seconds = 60
                        minutes -= 1
                        display_text(f"{'%02d' % (minutes+1)}:00", display_width / 2, display_height / 3)
                    else:
                        display_text(f"{'%02d' % minutes}:{'%02d' % seconds}", display_width / 2,
                                     display_height / 3)
                elif event.type == pygame.QUIT:
                    run = False
                pygame.display.update()
                clock.tick(60)


if __name__ == "__main__":
    #task = input("Enter the task name: ")
    task = 'Promodoro'
    pomodoro_timer(task)
    pygame.quit()
    quit()