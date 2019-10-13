
import logging

from scripts.core.constants import VisualInfo
from scripts.ui_elements.templates.render_area import RenderArea


class SkillBar:
    """
    Get and hold the info for the skill section
    """

    def __init__(self):
        # setup info
        self.max_skills_in_bar = 5
        self.skill_size_x = 64
        self.skill_size_y = 64
        self.is_visible = False
        self.skills_to_draw = []

        # render_area info
        render_width = int(self.skill_size_x * 1.5)
        render_height = int(VisualInfo.BASE_WINDOW_HEIGHT / 2)
        render_x = VisualInfo.BASE_WINDOW_WIDTH - render_width
        render_y = int(VisualInfo.BASE_WINDOW_HEIGHT - (self.skill_size_y / 2))

        self.render_area = RenderArea(render_x, render_y, render_width, render_height)

        self.gap_between_skill_icons = int((render_height - (self.max_skills_in_bar * self.skill_size_y)) /
                                           self.max_skills_in_bar)

        logging.debug(f"SkillBar initialised.")

    def draw(self):
        """
        Draw the skill bar
        """
        self.render_area.batch.draw()



