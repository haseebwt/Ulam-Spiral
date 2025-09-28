# Importing pygame module and the class
import pygame
import generate

# initiate pygame
pygame.init()

# create the display surface object
width, height = 1920, 1080
canvas = pygame.display.set_mode((width, height))

# Set title
pygame.display.set_caption('Ulam Spiral')

# Clock speed
clock = pygame.time.Clock()

# Fill the scree with white color
canvas.fill("lightgrey")

# start from center
pos_x = width/2
pos_y = height/2

# previous
prev_x = width/2
prev_y = height/2

# Define the font
face = '/usr/share/fonts/TTF/MononokiNerdFontMono-Regular.ttf'
font = pygame.font.Font(face, 18)

# Drawer
draw = pygame.draw

# Reference
func = generate.Generate(5, pos_x, pos_y)

# Setting the state of program
running = True

# Creating a while loop
while running:
    # Loading the keys pressed in an array
    keys = pygame.key.get_pressed()

    # Iterating over all the events received from
    for event in pygame.event.get():

        # If the type of the event is quit
        # then setting the run variable to false
        if event.type == pygame.QUIT:
            running = False

        # If key pressed is X, kill the program!
        elif keys[pygame.K_x]:
            running = False

    # Getting the steps
    step = generate.step

    # Checking for prime
    check = generate.Generate.is_prime(step)

    # Drawing the line or num
    # func.draw_num(font, canvas, prev_x, prev_y)
    func.draw_line(pos_x, pos_y, step, check, draw, canvas, func)

    # Incrementing the number
    generate.Generate.change()

    # Draws the surface object to the screen.
    pygame.display.update()

    # framerate of the animation
    clock.tick(60)
