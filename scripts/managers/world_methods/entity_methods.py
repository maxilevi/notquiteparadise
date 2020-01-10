from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import logging
import math
import pygame
import tcod
import scipy.spatial
from scripts.components.actor import Actor
from scripts.components.combatant import Combatant
from scripts.components.homeland import Homeland
from scripts.components.race import Race
from scripts.components.savvy import Savvy
from scripts.core.constants import TILE_SIZE
from scripts.core.library import library
from scripts.world.components import IsPlayer, Position, Blocking, Resources
from scripts.world.entity import Entity
from scripts.world.tile import Tile

if TYPE_CHECKING:
    from typing import List
    from scripts.managers.world_manager import WorldManager


class EntityMethods:
    """
    Queries relating to entities.

    Attributes:
        manager(WorldManager): the manager containing this class.
    """

    def __init__(self, manager):
        self.manager = manager  # type: WorldManager

    ############### GET ENTITY ###################

    def get_blocking_entity(self, tile_x, tile_y):
        """

        Args:
            tile_x:
            tile_y:

        Returns:
            Entity: returns entity if there is one, else None.
        """
        # TODO - change to just get the entity
        tile = self.manager.Map.get_tile((tile_x, tile_y))
        entity = tile.entity

        if entity:
            if entity.blocks_movement:
                return entity

        return None

    def get_entity_in_fov_at_tile(self, tile_x, tile_y):
        """
        Get the entity at a target tile

        Args:
            tile_x: x of tile
            tile_y: y of tile

        Returns:
            entity: Entity or None if no entity found
        """
        tile = self.manager.Map.get_tile((tile_x, tile_y))
        entity = tile.entity

        if entity:
            if self.manager.FOV.is_tile_in_fov(tile_x, tile_y):
                return entity

        return None

    def get_player(self):
        """
        Get the player.

        Returns:
            int: Entity ID
        """
        for entity, flag in self.manager.World.get_component(IsPlayer):
            return entity

    def get_entity(self, unique_component) -> int:
        """
        Get a single entity that has a component. If multiple entities have the given component only the first found
        is returned.

        Args:
            unique_component ():

        Returns:
            int: Entity ID.
        """
        entities = []
        for entity, flag in self.manager.World.get_component(unique_component):
            entities.append(entity)

        if len(entities) != 1:
            logging.warning(f"Tried to get an entity with {unique_component} component but found {len(entities)} "
                            f"entities with that component.")

        return entities[0]

    def get_entities(self, component1, component2=None, component3=None) -> List[int]:
        """
        Get entities with the specified components.

        Args:
            component1 ():
            component2 ():
            component3 ():

        Returns:
            List[int]: List of Entity IDs
        """
        entities = []

        if not component2 and not component3:
            for entity, c1 in self.manager.World.get_component(component1):
                entities.append(entity)
        elif component2 and not component3:
            for entity, (c1, c2) in self.manager.World.get_components(component1, component2):
                entities.append(entity)
        elif component2 and component3:
            for entity, (c1, c2, c3) in self.manager.World.get_components(component1, component2, component3):
                entities.append(entity)

        return entities

    def get_entitys_component(self, entity, component):
        """
        Get an entity's component.

        Args:
            entity ():
            component ():

        Returns:

        """
        if self.manager.World.has_component(entity, component):
            return self.manager.World.component_for_entity(entity, component)

    ############## ENTITY CREATION ################

    def remove_entity(self, entity: int):
        """
        Queues entity for removal from the world. Happens at the next run of World.process.

        Args:
            entity:
        """
        self.manager.World.delete_entity(entity)

    def create_entity(self, components: List = []) -> int:
        """
        Use each component in a list of components to create an entity

        Args:
            components ():
        """
        world = self.manager.World
        entity = world.create_entity()

        for component in components:
            world.add_component(entity, component)

        return entity

    ############## LOCATION QUERIES ##############

    @staticmethod
    def get_euclidean_distance_between_entities(start_entity, target_entity):
        """
        get distance from an entity towards another entity`s location

        Args:
            start_entity (Entity):
            target_entity (Entity):

        Returns:
            float: straight line distance

        """
        dx = target_entity.x - start_entity.x
        dy = target_entity.y - start_entity.y
        return math.sqrt(dx ** 2 + dy ** 2)

    @staticmethod
    def get_chebyshev_distance_between_tiles(start_tile, end_tile):
        """
        get distance from a Tile towards another Tile`s location

        Args:
            start_tile (Tile):
            end_tile (Tile):

        Returns:
            int: distance in tiles

        """
        start_tile_position = [start_tile.x, start_tile.y]
        target_tile_position = [end_tile.x, end_tile.y]
        return scipy.spatial.distance.chebyshev(start_tile_position, target_tile_position)

    def get_direction_between_entities(self, start_entity, target_entity):
        """
        Get direction from an entity towards another entity`s location. Respects blocked tiles.

        Args:
            start_entity (Entity):
            target_entity (Entity):

        """
        log_string = f"{start_entity.name} is looking for a direct path to {target_entity.name}."
        logging.debug(log_string)

        direction_x = target_entity.x - start_entity.x
        direction_y = target_entity.y - start_entity.y
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)

        direction_x = int(round(direction_x / distance))
        direction_y = int(round(direction_y / distance))

        tile_is_blocked = self.manager.Map.is_tile_blocking_movement(start_entity.x + direction_x,
                                                                     start_entity.y + direction_y)

        if not (tile_is_blocked or self.get_blocking_entity(start_entity.x + direction_x,
                                                            start_entity.y + direction_y)):
            log_string = f"{start_entity.name} found a direct path to {target_entity.name}."
            logging.debug(log_string)

            return direction_x, direction_y
        else:
            log_string = f"{start_entity.name} did NOT find a direct path to {target_entity.name}."
            logging.debug(log_string)

            return start_entity.x, start_entity.y

    def get_a_star_direction_between_entities(self, start_entity, target_entity):
        """
        Use a* pathfinding to get a direction from one entity to another
        Args:
            start_entity:
            target_entity:

        Returns:

        """
        max_path_length = 25
        game_map = self.manager.game_map
        entities = []
        # TODO - update to use ECS
        for ent, (pos, blocking) in self.manager.World.get_components(Position, Blocking):
            entities.append(ent)
        entity_to_move = start_entity
        target = target_entity

        log_string = f"{entity_to_move.name} is looking for a path to {target.name} with a*"
        logging.debug(log_string)

        # Create a FOV map that has the dimensions of the map
        fov = tcod.map_new(game_map.width, game_map.height)

        # Scan the current map each turn and set all the walls as unwalkable
        for y1 in range(game_map.height):
            for x1 in range(game_map.width):
                tcod.map_set_properties(fov, x1, y1, not game_map.tiles[x1][y1].blocks_sight,
                                        not game_map.tiles[x1][y1].blocks_movement)

        # Scan all the objects to see if there are objects that must be navigated around
        # Check also that the object isn't self or the target (so that the start and the end points are free)
        # The AI class handles the situation if self is next to the target so it will not use this A* function
        # anyway
        for entity in entities:
            if entity.blocks_movement and entity != entity_to_move and entity != target:
                # Set the tile as a wall so it must be navigated around
                tcod.map_set_properties(fov, entity.x, entity.y, True, False)

        # Allocate a A* path
        # The 1.41 is the normal diagonal cost of moving, it can be set as 0.0 if diagonal moves are prohibited
        my_path = tcod.path_new_using_map(fov, 1.41)

        # Compute the path between self`s coordinates and the target`s coordinates
        tcod.path_compute(my_path, entity_to_move.x, entity_to_move.y, target.x, target.y)

        # Check if the path exists, and in this case, also the path is shorter than max_path_length
        # The path size matters if you want the monster to use alternative longer paths (for example through
        # other rooms) if for example the player is in a corridor
        # It makes sense to keep path size relatively low to keep the monsters from running around the map if
        # there`s an alternative path really far away
        if not tcod.path_is_empty(my_path) and tcod.path_size(my_path) < max_path_length:
            # Find the next coordinates in the computed full path
            x, y = tcod.path_walk(my_path, True)

            # convert to direction
            direction_x = x - entity_to_move.x
            direction_y = y - entity_to_move.y

            log_string = f"{entity_to_move.name} found an a* path to {target.name}..."
            log_string2 = f"-> will move from [{entity_to_move.x},{entity_to_move.y}] towards [{x},{y}] in direction " \
                          f"[{direction_x},{direction_y}]"
            logging.debug(log_string)
            logging.debug(log_string2)

        else:
            # no path found return no movement direction
            direction_x, direction_y = 0, 0
            log_string = f"{entity_to_move.name} did NOT find an a* path to {target.name}."
            logging.debug(log_string)

        # Delete the path to free memory
        tcod.path_delete(my_path)
        return direction_x, direction_y

    ############### COMPONENT MANAGEMENT ##########

    def spend_time(self, entity: int, time_spent: int):
        """
        Add time_spent to the entity's total time spent.

        Args:
            entity ():
            time_spent ():
        """
        resources = self.manager.World.component_for_entity(entity, Resources)
        resources.time_spent += time_spent
