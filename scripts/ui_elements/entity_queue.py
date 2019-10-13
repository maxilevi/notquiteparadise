
import logging
import pygame

from typing import List, Tuple
from scripts.core.constants import VisualInfo
from scripts.core.fonts import Font
from scripts.ui_elements.palette import Palette
from scripts.ui_elements.templates.render_area import RenderArea


class EntityQueue:
    """
    Entities listed in the turn manager.
    """
    def __init__(self):
        # setup info
        self.entity_size_x = 64
        self.entity_size_y = 64
        self.entities_to_draw = []  # type: List[Tuple]  # (image, str)
        self.gap_between_entities = 2
        self.is_visible = False

        # setup the render_area
        render_width = int(self.entity_size_x * 1.5)
        render_height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        render_x = VisualInfo.BASE_WINDOW_WIDTH - (render_width * 2)
        render_y = VisualInfo.BASE_WINDOW_HEIGHT - (self.entity_size_y / 2)

        self.render_area = RenderArea(render_x, render_y, render_width, render_height)

        # defined here due to dependency on render_area
        self.max_entities_to_show = int(render_height / (self.entity_size_y + self.gap_between_entities))

        logging.debug(f"EntityQueue initialised.")

    def draw(self):
        """
        Draw the entity queue
        """
        self.render_area.batch.draw()
