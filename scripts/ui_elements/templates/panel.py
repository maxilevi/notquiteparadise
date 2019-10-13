import pygame
import pyglet

from scripts.core.constants import TILE_SIZE


class Panel:
    """
    A panel for an element on the UI

    Attributes:
        x (int) = X position of the panel.
        y (int) = Y position of the panel.
        width (int) = Width of the panel.
        height (int) = Height of the panel.
        colour (Colour)= Colour of background.
        border_size (int)= Size of border. If 0 no border is drawn.
        border_colour (Colour) = Colour of the border


    """

    def __init__(self, x, y, width, height, background_colour, border_size, border_colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_size = border_size
        self.background_colour = background_colour
        self.border_colour = border_colour
        self.centre = (width / 2, height / 2)

    def draw_background(self):
        """
        Draw a panel surface, including background

        """
        self.surface.fill(self.background_colour)
        offset = self.border_size
        pygame.draw.rect(self.surface, self.background_colour,  [0 + offset,  0 + offset, self.width - offset,
                            self.height - offset], 0)

    def draw_border(self):
        """
        Draw a panel`s border if bordersize > 0
        """

        if self.border_size > 0:
            pygame.draw.rect(self.surface, self.border_colour,  [0, 0, self.width, self.height],
                             self.border_size)


class RenderArea:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprites = []
        self.batch = pyglet.graphics.Batch()

    def add(self, image, x, y, width=0, height=0):
        # create sprite
        new_sprite = pyglet.sprite.Sprite(image, x=self.x + x, y=self.y + y, batch=self.batch)

        # resize to specified sizes
        if width > 0:
            scale_x = (width / image.height)
            new_sprite.update(scale_x=scale_x)
        if height > 0:
            scale_y = (height / image.width)
            new_sprite.update(scale_y=scale_y)

        # add to list
        self.sprites.append(new_sprite)