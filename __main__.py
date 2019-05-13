"""
The entry-point for the Snake game written in python.

Developed by JHEBOI Tech.
"""

import kivy

kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
