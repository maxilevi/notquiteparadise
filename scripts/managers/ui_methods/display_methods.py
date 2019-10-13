
import pyglet
from typing import Tuple
from scripts.core.constants import VisualInfo


class DisplayMethods:
    """
    Methods for handling display

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        self.init_resource_config()

        from scripts.managers.ui_manager import UIManager
        self.manager = manager  # type: UIManager

        self.desired_width = VisualInfo.BASE_WINDOW_WIDTH
        self.desired_height = VisualInfo.BASE_WINDOW_HEIGHT
        # TODO - allow for selection by player but only multiples of base (16:9)
        self.screen_scaling_mod_x = self.desired_width // VisualInfo.BASE_WINDOW_WIDTH
        self.screen_scaling_mod_y = self.desired_height // VisualInfo.BASE_WINDOW_HEIGHT

        self.window = self.init_window()

        # import pygame
        # self.window = pygame.display.set_mode((self.desired_width, self.desired_height))
        # self.main_surface = pygame.Surface((VisualInfo.BASE_WINDOW_WIDTH, VisualInfo.BASE_WINDOW_HEIGHT))

    def init_window(self):
        window = pyglet.window.Window(self.desired_width, self.desired_height, "Not Quite Paradise", resizable=False)
        window.set_minimum_size(VisualInfo.BASE_WINDOW_WIDTH, VisualInfo.BASE_WINDOW_HEIGHT)
        # window.set_location(centre_x, centre_y) # move to centre
        # set window icon
        # icon1 = pyglet.image.load('16x16.png')
        # icon2 = pyglet.image.load('32x32.png')
        # window.set_icon(icon1, icon2)

        return window

    def init_resource_config(self):
        pyglet.resource.path = ["C:/Users/Gabriel/Documents/NotQuiteParadise/assets",
            "C:/Users/Gabriel/Documents/NotQuiteParadise/assets/actor"]
        pyglet.resource.reindex()

    def get_screen_scaling_mod(self):
        """
        Get the screen scaling modifier

        Returns:
            Tuple[int,int]
        """
        return self.screen_scaling_mod_x, self.screen_scaling_mod_y

    def get_main_surface(self):
        """
        Get the main surface where all draws eventually go.

        Returns:
            pygame.Surface:
        """
        return self.main_surface

    def get_desired_resolution(self):
        """
        Get the desired resolution

        Returns:
            Tuple[int, int]: (width, height)
        """
        return self.desired_width, self.desired_height

    def get_window(self):
        """
        Get the window

        Returns:

        """
        return self.window