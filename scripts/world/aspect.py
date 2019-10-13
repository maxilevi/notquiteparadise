from scripts.core.constants import TILE_SIZE, TargetTags
from scripts.global_singletons.data_library import library
from scripts.world.tile import Tile


class Aspect:
    """
    An Aspect of a Tile, such as smoke or fire
    
    Attributes:
        owner(Tile):
        blocks_movement(bool):
        blocks_sight(bool):
        sprite(pygame.Sprite):
        name(str):
        
    """
    def __init__(self, owner, aspect_name, duration=None):
        # TODO - should aspects be logged on a central list, like afflictions?

        self.owner = owner  # type: Tile
        self.name = aspect_name
        self.duration = duration

        data = library.get_aspect_data(aspect_name)

        self.blocks_movement = data.blocks_movement
        self.blocks_sight = data.blocks_sight

        import pyglet
        self.sprite = pyglet.resource.image("world/" + data.sprite)

    @property
    def x(self):
        """
        Get the tile_x of the Aspect.

        Returns:

        """
        return self.owner.x

    @property
    def y(self):
        """
        Get the tile_y of the Aspect.

        Returns:

        """
        return self.owner.y

    def trigger(self):
        """
        Trigger any effects for the aspects
        """
        data = library.get_aspect_data(self.name)

        # apply any effects
        for effect_name, effect_data in data.effects.items():
            from scripts.global_singletons.managers import world_manager
            effect = world_manager.Skill.create_effect(self, effect_data.effect_type)
            effect.trigger([self.owner])
