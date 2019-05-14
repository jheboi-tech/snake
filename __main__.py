"""
The entry-point for the Snake game written in python.

Developed by JHEBOI Tech.
"""

import kivy
from random import randint

kivy.require('1.10.1')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty, ListProperty
from kivy.properties import BooleanProperty, OptionProperty
from kivy.properties import ReferenceListProperty
from kivy.graphics import Rectangle, Ellipse
from kivy.core.window import Window

_INITIAL_LENGTH = 3

_KEY_LEFT = (276, 80)
_KEY_UP = (273, 82)
_KEY_RIGHT = (275, 79)
_KEY_DOWN = (274, 81)

class Playground(Widget):
    """Children widgets containers."""
    fruit = ObjectProperty(None)
    snake = ObjectProperty(None)

    # Grid Parameters
    col_number = 16
    row_number = 9

    # Game variables
    score = NumericProperty(0)
    turn_counter = NumericProperty(0)
    fruit_rhythm = NumericProperty(0)

    # User input handling
    touch_start_pos = ListProperty()
    action_triggered = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(Playground, self).__init__(**kwargs)
        Window.bind(on_key_up=self._keyup)
        Window.bind(on_key_down=self._keydown)

    def _keyup(self, *args):
        signature = args[1:3]
        key = self._get_key_press(signature)

    def _keydown(self, *args):
        signature = args[1:3]
        key = self._get_key_press(signature)
        self.snake.set_direction(key)

    def _get_key_press(self, signature):
        if signature == _KEY_UP:
            return "Up"
        elif signature == _KEY_DOWN:
            return "Down"
        elif signature == _KEY_LEFT:
            return "Left"
        elif signature == _KEY_RIGHT:
            return "Right"
        else:
            return ""

    def start(self):
        self.new_snake()

        # Start the update loop
        self.update()

    def reset(self):
        self.turn_counter = 0
        self.score = 0

        self.snake.remove()
        self.fruit.remove()

    def new_snake(self):
        start_coord = (
            randint(2, self.col_number - 2), randint(2, self.row_number - 2)
        )

        self.snake.set_position(start_coord)

        rand_index = randint(0, 3)
        start_direction = ["Up", "Down", "Left", "Right"][rand_index]

        # Set random direction.
        self.snake.set_direction(start_direction)

    def pop_fruit(self, *args):
        random_coord = [
            randint(1, self.col_number), randint(1, self.row_number)
        ]

        snake_space = self.snake.get_full_position()

        # if the coordinates are on a cell occupied by the snake, re-draw.
        while random_coord in snake_space:
            random_coord = [
                randint(2, self.col_number - 1), randint(2, self.row_number - 1)
            ]

        self.fruit.pop(random_coord)

    def is_defeated(self):
        snake_position = self.snake.get_position()

        if snake_position in self.snake.tail.blocks_positions:
            return True

        if (
                (snake_position[0] > self.col_number) or
                (snake_position[0] < 1) or
                (snake_position[1] > self.row_number) or
                (snake_position[1] < 1)
        ):
            return True

        return False

    def update(self, *args):

        self.snake.move()

        if self.is_defeated():
            self.reset()
            self.start()
            return

        if self.fruit.is_on_board():
            if self.snake.get_position() == self.fruit.pos:
                # if so, remove the fruit and increment score and tail size
                self.fruit.remove()
                self.score += 1
                self.snake.tail.size += 1
        else:
            self.pop_fruit()

        # Increment turn counter.
        self.turn_counter += 1

        Clock.schedule_once(self.update, 0.2)


class Snake(Widget):
    """Children widgets containers."""
    head = ObjectProperty(None)
    tail = ObjectProperty(None)

    def move(self):
        next_tail_pos = list(self.head.position)
        self.head.move()
        self.tail.add_block(next_tail_pos)

    def remove(self):
        self.head.remove()
        self.tail.remove()

    def set_position(self, position):
        self.head.position = position

    def get_position(self):
        return self.head.position

    def get_full_position(self):
        return self.head.position + self.tail.blocks_positions

    def set_direction(self, direction):
        print("Facing: {}".format(direction))
        self.head.direction = direction

    def get_direction(self):
        return self.head.direction


class SnakeHead(Widget):
    """Representation on the 'grid' of the Playground"""
    direction = OptionProperty(
        "Right", options=["Up", "Down", "Left", "Right"])
    x_position = NumericProperty(0)
    y_position = NumericProperty(0)
    position = ReferenceListProperty(x_position, y_position)

    # Representation on the canvas.
    points = ListProperty([0] * 6)
    object_on_board = ObjectProperty(None)
    state = BooleanProperty(False)

    def is_on_board(self):
        return self.state

    def remove(self):
        if self.is_on_board():
            self.canvas.remove(self.object_on_board)
            self.object_on_board = ObjectProperty(None)
            self.state = False

    def show(self):
        with self.canvas:
            x = (self.x_position - 1) * self.width
            y = (self.y_position - 1) * self.height
            coord = (x , y)
            size = (self.width, self.height)

            if not self.is_on_board():
                self.object_on_board = Rectangle(pos=coord, size=size, )
                self.state = True  # Object is on board.
            else:
                # if object is already on board, delete the
                # current object and draw a new one.
                self.canvas.remove(self.object_on_board)
                self.object_on_board = Rectangle(pos=coord, size=size)

    def move(self):

        if self.direction == "Right":
            self.x_position += 1
        elif self.direction == "Left":
            self.x_position -= 1
        elif self.direction == "Up":
            self.y_position += 1
        elif self.direction == "Down":
            self.y_position -= 1

        self.show()


class SnakeTail(Widget):
    # Tail length, in number of blocks.
    size = NumericProperty(_INITIAL_LENGTH)

    # Blocks position on the Playground's grid.
    blocks_positions = ListProperty()

    # Blocks objects drawn on the canvas.
    tail_blocks_objects = ListProperty()

    def remove(self):
        # Reset the size if some fruits were eaten.
        self.size = _INITIAL_LENGTH

        # Remove every block of the tail from the
        # canvas this is why we don't need a
        # is_on_board() here.
        for block in self.tail_blocks_objects:
            self.canvas.remove(block)

        # empty the lists.
        self.blocks_positions = []
        self.tail_blocks_objects = []

    def add_block(self, pos):
        self.blocks_positions.append(pos)

        if len(self.blocks_positions) > self.size:
            self.blocks_positions.pop(0)

        with self.canvas:
            for block_pos in self.blocks_positions:
                x = (block_pos[0] - 1) * self.width
                y = (block_pos[1] - 1) * self.height
                coord = (x, y)
                block = Rectangle(pos=coord, size=(self.width, self.height))

                self.tail_blocks_objects.append(block)

                # Control the number of blocks in the list
                # and remove from the canvas if necessary.
                if len(self.tail_blocks_objects) > self.size:
                    last_block = self.tail_blocks_objects.pop(0)
                    self.canvas.remove(last_block)


class Fruit(Widget):
    # constants used to compute the fruit_rhythm.
    # TODO: Maybe remove these??
    duration = NumericProperty(10)
    interval = NumericProperty(3)

    # Representation on the canvas.
    object_on_board = ObjectProperty(None)
    state = BooleanProperty(False)

    def is_on_board(self):
        return self.state

    def remove(self, *args):
        if self.is_on_board():
            self.canvas.remove(self.object_on_board)
            self.object_on_board = ObjectProperty(None)
            self.state = False

    def pop(self, pos):
        self.pos = pos

        with self.canvas:
            x = (pos[0] - 1) * self.size[0]
            y = (pos[1] - 1) * self.size[1]
            coord = (x, y)

            # storing the representation and update the state of the object
            self.object_on_board = Ellipse(pos=coord, size=self.size)
            self.state = True


class SnakeApp(App):
    game_engine = ObjectProperty(None)

    def on_start(self):
        self.game_engine.start()

    def build(self):
        self.game_engine = Playground()
        return self.game_engine


if __name__ == '__main__':
    SnakeApp().run()
