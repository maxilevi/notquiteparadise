from operator import mod

from scripts.ui_elements.templates.panel import Panel, RenderArea
from scripts.core.constants import VisualInfo, TILE_SIZE
from scripts.ui_elements.colours import Colour
from scripts.ui_elements.palette import Palette
from scripts.world.tile import Tile


class Camera:
    """
    Hold the visual info for the Game Map
    """

    def __init__(self):
        self.tiles_to_draw = []  # the tiles passed from the GameMap to draw
        self.is_visible = False

        self.x = 0
        self.y = 0
        self.width = 10
        self.height = 10
        self.edge_size = 3

        # setup the panel
        panel_x = 0
        panel_y = 0
        panel_width = int((VisualInfo.BASE_WINDOW_WIDTH / 4) * 3)
        panel_height = VisualInfo.BASE_WINDOW_HEIGHT
        panel_border = 2
        panel_background_colour = Palette().game_map.background
        panel_border_colour = Palette().game_map.border
        # self.panel = Panel(panel_x, panel_y, panel_width, panel_height, panel_background_colour, panel_border,
        #                    panel_border_colour)

        self.panel = RenderArea(panel_x, panel_y, panel_width, panel_height)

    def new_draw(self):
        self.panel.batch.draw()

    def update_panel_sprites(self):
        # clear previous
        self.panel.sprites = []
        import pyglet
        self.panel.batch = pyglet.graphics.Batch()

        tiles = self.tiles_to_draw
        y_pos = self.height
        x_pos = 0

        for x in range(0, len(tiles)):
            tile = tiles[x]

            if y_pos <= 0:
                y_pos = self.height
                x_pos += 1

            draw_x = x_pos * TILE_SIZE
            draw_y = y_pos * TILE_SIZE

            if tile.terrain:
                self.panel.add(tile.terrain.sprite, draw_x, draw_y, TILE_SIZE, TILE_SIZE)

            if tile.entity:
                self.panel.add(tile.entity.icon, draw_x, draw_y, TILE_SIZE, TILE_SIZE)

            if tile.aspects:
                for key, aspect in tile.aspects.items():
                    self.panel.add(aspect.sprite, draw_x, draw_y, TILE_SIZE, TILE_SIZE)

            y_pos -= 1

    def draw(self, surface):
        """
        Draw the tiles in view

        Args:
            surface(Surface): Surface to draw to

        """
        # panel background
        self.panel.surface.fill(Colour().black)
        self.panel.draw_background()

        self.draw_cameras_tiles()

        # panel border
        self.panel.draw_border()
        surface.blit(self.panel.surface, (self.panel.x, self.panel.y))

    def draw_cameras_tiles(self):
        """
        Draw the game map on the panel surface
        """
        # TODO - draw visible only
        tiles = self.tiles_to_draw

        y_pos = 0
        x_pos = 0

        for x in range(0, len(tiles)):
            tile = tiles[x]

            if y_pos >= self.height:
                y_pos = 0
                x_pos += 1

            draw_position = (x_pos * TILE_SIZE, y_pos * TILE_SIZE)

            if tile.terrain:
                self.panel.surface.blit(tile.terrain.sprite, draw_position)

            if tile.entity:
                self.panel.surface.blit(tile.entity.icon, draw_position)

            if tile.aspects:
                for key, aspect in tile.aspects.items():
                    self.panel.surface.blit(aspect.sprite, draw_position)

            y_pos += 1

