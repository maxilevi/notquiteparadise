
from scripts.world.terrain.terrain import Terrain


class Floor(Terrain):
    """
    Floor tile, doesnt block movement or sight
    """
    def __init__(self):
        super().__init__()
        self.name = "floor tile"
        import pyglet
        self.sprite = pyglet.resource.image("world/placeholder/_test.png")
