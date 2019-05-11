"""
The entry-point for the Snake game written in python.

Developed by JHEBOI Tech.
"""

def main():
    """
    The entry point for this solution.
    :return:    Nothing.
    """
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