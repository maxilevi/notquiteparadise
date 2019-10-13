
from scripts.world.terrain.terrain import Terrain


class Wall(Terrain):
    """
    Wall tile, blocks movement and sight.
    """
    def __init__(self):
        super().__init__()
        self.blocks_movement = True
        self.blocks_sight = True
        self.name = "wall tile"
        import pyglet
        self.sprite = pyglet.resource.image("world/placeholder/_testWall.png")  # TODO - amend to hold in library
