
from scripts.ui_elements.templates.render_area import RenderArea
from scripts.core.constants import VisualInfo


class Camera:
    """
    Hold the visual info for the Game Map
    """

    def __init__(self):

        self.tiles_to_draw = []  # the tiles passed from the GameMap to draw
        self.is_visible = False

        self.x = 0  # game map tile_x
        self.y = 0  # game map tile_x
        self.width = 10  # in tiles
        self.height = 10  # in tiles
        self.edge_size = 3  # in tiles

        # setup the render_area
        render_x = 0
        render_y = 0
        render_width = int((VisualInfo.BASE_WINDOW_WIDTH / 4) * 3)
        render_height = VisualInfo.BASE_WINDOW_HEIGHT

        self.render_area = RenderArea(render_x, render_y, render_width, render_height)

    def draw(self):
        """
        Draw the ui element
        """
        self.render_area.batch.draw()