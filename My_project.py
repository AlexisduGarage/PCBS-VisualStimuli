import random
import pygame

N_TRIALS = 15 
MIN_WAIT_TIME = 2000
MAX_WAIT_TIME = 3000
MIN_RESPONSE_DELAY = 150
MAX_RESPONSE_DELAY = 500
DURATION_STIM = 32

def create_window():
    screen = pygame.display.set_mode((1280, 960))
    pygame.mouse.set_visible(False)
    return screen


def clear_screen(screen):
    screen.fill(pygame.Color('black'))
    pygame.display.flip()


def display_instruction(screen, x, y, direction):
    pygame.font.init()
    myfont = pygame.font.SysFont(pygame.font.get_default_font(), 40)
    line1 = myfont.render("Place your "+str(direction)+" hand on the space bar", 1, pygame.Color('white'))
    line2 = myfont.render("Your task: When you see a rectangle, press the space bar as quickly as possible.", 1, pygame.Color('white'))
    line3 = myfont.render("Press it now to start!", 1, pygame.Color('white'))
    screen.blit(line1, (x, y - 120))
    screen.blit(line2, (x, y -60))
    screen.blit(line3, (x, y))
    pygame.display.flip()

def warning(screen, x, y):
    pygame.font.init()
    myfont = pygame.font.SysFont(pygame.font.get_default_font(), 40)
    line = myfont.render("Ready", 1, pygame.Color('white'))
    screen.blit(line, (x - 30, y))
    pygame.display.flip()

def present_rectangle(screen, x, y, color):
    pygame.draw.rect(screen, color, (x + 60, y - 40, 120, 80))
    pygame.display.flip()
    pygame.time.delay(DURATION_STIM)


def wait_for_keypress():
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_pressed = True


def measure_reaction_time(max_response_delay, min_response_delay):
    button_pressed = False
    no_response= "NR"
    escape = False
    response_delay_elapsed = False
    anticipatory_response = False
    reaction_time = 0
    pygame.event.clear()  
    t0 = pygame.time.get_ticks()

    while not button_pressed and not escape and not response_delay_elapsed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    escape = True
                    break
                if event.key == pygame.K_SPACE:
                    reaction_time = pygame.time.get_ticks() - t0
                    button_pressed = True
                    if reaction_time < min_response_delay:
                        anticipatory_response = True
                
            if event.type == pygame.QUIT:
                escape = True
                break

        if reaction_time > max_response_delay:
            response_delay_elapsed = True

    if escape or anticipatory_response == True:
        return None
    else:
        return reaction_time
        

def save_data(waiting_times, position, reaction_times, filename):
    with open(str(filename), 'wt') as f:
        f.write('Wait,Position,RT\n')
        for wt, posit, rt in zip(waiting_times, position,reaction_times): 
            f.write(f"{wt},{posit},{rt}\n")

def block(block_number, hand):
    screen = create_window()
    r = screen.get_rect()
    W, H = r.width, r.height
    center_x = W // 2
    center_y = H // 2

    waiting_times = []
    reaction_times = []
    positions = []

    display_instruction(screen, 20, center_y, hand)
    wait_for_keypress()
    clear_screen(screen)

    pygame.time.delay(1000)

    for i_trial in range(N_TRIALS):
        clear_screen(screen)

        warning(screen, center_x, center_y)
        pygame.time.delay(1000)
        clear_screen(screen)

        waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
        pygame.time.delay(waiting_time)

        rect_x_position = random.choice([160,2*160,3*160,4*160,5*160,6*160])
        position = rect_x_position - 640

        present_rectangle(screen, rect_x_position, center_y, pygame.Color('white'))
        clear_screen(screen)

        reaction_time = measure_reaction_time(MAX_RESPONSE_DELAY, MIN_RESPONSE_DELAY)
        if reaction_time is None:
            break

        waiting_times.append(waiting_time)
        reaction_times.append(reaction_time)
        positions.append(position)
        print(i_trial, waiting_time, position, reaction_time)

    save_data(waiting_times, positions, reaction_times, "block"+str(block_number)+"-"+str(hand))
    


##### main
pygame.init()

block(1, "right")
block(2, "left")

pygame.quit()
