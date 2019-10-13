
import logging

from typing import Dict, Tuple
from scripts.core.constants import MessageEventTypes, VisualInfo
from scripts.core.fonts import Font
from scripts.global_singletons.event_hub import publisher
from scripts.ui_elements.colours import Colour
from scripts.ui_elements.palette import Palette
from scripts.ui_elements.templates.render_area import RenderArea


class MessageLog:
    """
    Store messages, and related functionality, to be shown in the message log.

    Attributes:
        message_list (List(Tuple(MessageEventTypes, string))):  list of messages and their type
        icons (Dict): Dictionary of icons to look for and the icon to show.
        is_dirty (bool): flag indicating need to draw
    """

    def __init__(self):
        # log setup
        self.message_list = []
        self.messages_to_draw = []
        self.keywords = {}
        self.icons = {}
        self.commands = {}
        self.is_dirty = True
        self.is_visible = False

        # render_area info
        render_width = int((VisualInfo.BASE_WINDOW_WIDTH / 4) * 1)
        render_height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        render_x = 50 # VisualInfo.BASE_WINDOW_WIDTH - render_width
        render_y = 100

        self.render_area = RenderArea(render_x, render_y, render_width, render_height)

        # log info
        self.edge_size = 1
        self.message_indent = 5
        #font_size = Font().message_log.size
        font_size = 12
        self.gap_between_lines = int(font_size / 3)
        self.first_message_index = 0
        self.number_of_messages_to_show = int((render_height - 2 * self.edge_size) / (font_size +
                                                                                     self.gap_between_lines))

        # *** testing
        # Use Glooey instead?
        import pyglet
        location = pyglet.resource.location("actor_template.png")
        html = "<font color=white> This is some text that goes on for a very long time and needs to be wrapped " \
               "because it is so big, (oh, here's an image!) " \
               "<img src='actor_template.png' height='12'/>" \
               "otherwise it wont all show in the window."
        label = pyglet.text.HTMLLabel(x=render_x, y=render_y, text=html, width=render_width, multiline=True,
            anchor_y='center', location=location)
        self.text = label

        logging.debug(f"MessageLog initialised.")

    def draw(self):
        """
        Draw the message log and all included text and icons
        """
        self.text.draw()
        #self.render_area.batch.draw()


        #
        # # init info for message render
        # msg_x = self.edge_size + self.message_indent
        # msg_y = self.edge_size
        # font_size = 12
        # line_count = 0
        #
        # # render the messages_to_draw
        # for line_list in self.messages_to_draw:
        #     # reset offset
        #     x_offset = 0
        #
        #     # get y position of line to write to
        #     adjusted_y = msg_y + (line_count * (font_size + self.gap_between_lines))
        #
        #     # update  line count
        #     line_count += 1
        #
        #     # pull each surface from each line_list and render to the render_area surface
        #     for message in line_list:
        #         panel_surface.blit(message, (msg_x + x_offset, adjusted_y))
        #         message_width = message.get_width()
        #         x_offset += message_width + 2  # 2 for space between words


