"""
The entry-point for the Snake game written in python.

Developed by JHEBOI Tech.
"""

# Additional required modules

import pygame

# define a main function
def main():
    """
    The entry point for this solution.
    :return:    Nothing.
    """
    # initialize the pygame module
    pygame.init()

    #set logo
    logo = pygame.image.load("JHE_logo.png")
    pygame.display.set_icon(logo)
    # set caption text
    pygame.display.set_caption("JHEBOI SNAKE")

    # initialize screen and size
    screen = pygame.display.set_mode((640, 480))

    # define variable to control main loop
    running = True

    # main loop
    while running:
        # event handler, gets all events from queue
        for event in pygame.event.get():
            # quit event to exit loop
            if event.type == pygame.QUIT:
                running = False

    if __debug__:
        # Anything inside this if statement and others after it will only be run
        # if the python program is in debug mode. To run this program so that these
        # print statements don't occur, run python with the -O option which enables
        # optimisation mode. i.e.
        # `python3 -O __main__.py
        print("Welcome to snake!")

if __name__ == "__main__":
    # Run the main function to kick off the game.
    main()