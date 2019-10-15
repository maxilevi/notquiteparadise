
import pyglet

from scripts.core.constants import RenderOrder


class RenderArea:
    """
    A set area in which to render
    """
    def __init__(self, screen_x: int, screen_y: int, width: int, height: int):
        """

        Args:
            screen_x (): The screen x position to show start drawing the render_area.
            screen_y (): The screen y position to show start drawing the render_area.
            width (): Width of the render_area.
            height (): Height of the render_area.
        """
        self.x = screen_x
        self.y = screen_y
        self.width = width
        self.height = height
        self.sprites = []
        self.batch = pyglet.graphics.Batch()

    def add_image(self, image: pyglet.image, x: int, y: int, width: int = 0, height: int = 0, render_order:
    RenderOrder = RenderOrder.BACKGROUND):
        """
        Add image to the render_area.

        Args:
            render_order ():
            image (): image to show in the render_area.
            x (): x within the render_area.
            y ():  y within the render_area
            width (): desired width of the image.
            height ():  desired height of the image.
        """
        # set the order
        if render_order == RenderOrder.TEXT:
            group = RenderOrder.TEXT.value - 1
        else:
            group = render_order.value

        # create sprite
        image_group = pyglet.graphics.OrderedGroup(group)
        new_sprite = pyglet.sprite.Sprite(image, x=self.x + x, y=self.y + y, batch=self.batch, group=image_group)

        # resize to specified sizes
        if width > 0:
            scale_x = (width / image.height)
            new_sprite.update(scale_x=scale_x)
        if height > 0:
            scale_y = (height / image.width)
            new_sprite.update(scale_y=scale_y)

        # add to list
        self.sprites.append(new_sprite)

    def add_text(self, text, x: int, y: int,):
        """
        Add text to the render_area
        Args:
            text ():
            x ():
            y ():
        """
        # create sprite
        text_group = pyglet.graphics.OrderedGroup(RenderOrder.TEXT.value)
        new_text = pyglet.text.Label(text=text,  x=self.x + x, y=self.y + y, batch=self.batch, group=text_group)

        # add to list
        self.sprites.append(new_text)