
import logging

from typing import Tuple

import pyglet

from scripts.core.constants import UIElementTypes, SkillShapes, VisualInfo, TILE_SIZE, RenderOrder
from scripts.global_singletons.data_library import library
from scripts.ui_elements.camera import Camera
from scripts.ui_elements.entity_info import SelectedEntityInfo
from scripts.ui_elements.entity_queue import EntityQueue
from scripts.ui_elements.message_log import MessageLog
from scripts.ui_elements.skill_bar import SkillBar
from scripts.ui_elements.targeting_overlay import TargetingOverlay
from scripts.world.entity import Entity


class ElementMethods:
    """
    Methods for taking actions with ui elements

    Attributes:
        manager ():
    """

    def __init__(self, manager):
        from scripts.managers.ui_manager import UIManager
        self.manager = manager  # type: UIManager

        self.elements = {}  # list of all init'd ui elements

    def init_message_log(self):
        """
        Initialise the message log ui element.
        """
        self.elements[UIElementTypes.MESSAGE_LOG.name] = MessageLog()

    def init_entity_info(self):
        """
        Initialise the selected entity info ui element
        """
        self.elements[UIElementTypes.ENTITY_INFO.name] = SelectedEntityInfo()

    def init_targeting_overlay(self):
        """
        Initialise the targeting_overlay
        """
        self.elements[UIElementTypes.TARGETING_OVERLAY.name] = TargetingOverlay()

    def init_skill_bar(self):
        """
        Initialise the skill bar
        """
        self.elements[UIElementTypes.SKILL_BAR.name] = SkillBar()

    def init_entity_queue(self):
        """
        Initialise the entity queue
        """
        self.elements[UIElementTypes.ENTITY_QUEUE.name] = EntityQueue()

        from scripts.global_singletons.managers import turn_manager
        if turn_manager:
            self.update_entity_queue()

    def init_camera(self):
        """
        Initialise the camera
        """
        self.elements[UIElementTypes.CAMERA.name] = Camera()

    def set_element_visibility(self, element_type, visible):
        """
        Update whether an element is visible.

        Args:
            element_type (UIElementTypes): 
            visible (bool):
        """
        try:
            element = self.elements[element_type.name]
            element.is_visible = visible
        except KeyError:
            logging.debug(f"Tried to set {element_type.name} to {visible} but key doesn't exist.")

    def draw_visible_elements(self):
        """
        Draw the visible ui elements based on is_visible attribute of the element
        """
        # TODO - add handling for dirty

        for key, element in self.elements.items():
            if element.is_visible:
                element.draw()

    def set_selected_entity(self, entity):
        """
        Set the selected entity

        Args:
            entity(Entity):
        """
        self.elements[UIElementTypes.ENTITY_INFO.name].selected_entity = entity

    def set_skill_being_targeted(self, skill):
        """
        Set the skill that the player is currently targeting

        Args:
            skill (Skill):
        """
        self.elements[UIElementTypes.TARGETING_OVERLAY.name].skill_being_targeted = skill

    def set_selected_tile(self, tile):
        """
        Update the tile currently selected in the targeting overlay. Must be in the highlighted range.

        Args:
            tile(Tile):
        """
        targeting_overlay = self.get_ui_element(UIElementTypes.TARGETING_OVERLAY)

        if tile in targeting_overlay.tiles_in_range_and_fov:
            targeting_overlay.selected_tile = tile

    def set_tiles_in_targeting_overlay(self, tiles):
        """
        Set the tiles to be shown in the targeting overlay

        Args:
            tiles (list[Tiles]):
        """
        targeting_overlay = self.get_ui_element(UIElementTypes.TARGETING_OVERLAY)
        targeting_overlay.tiles_in_range_and_fov = tiles

    def get_ui_element(self, element_type):
        """
        Get UI element. Returns nothing if not found. Won't be found if not init'd.

        Args:
            element_type (UIElementTypes):

        Returns:
            any: ui element
        """
        return self.elements[element_type.name]

    def get_ui_elements(self):
        """
        Get all the ui elements

        Returns:
            list: list of ui_elements
        """
        return self.elements

    def get_skill_being_targeted(self):
        """
        Get the skill being targeted (held in targeting overlay).

        Returns:
            Skill:
        """
        targeting_overlay = self.get_ui_element(UIElementTypes.TARGETING_OVERLAY)
        return targeting_overlay.skill_being_targeted

    def update_targeting_overlays_tiles_in_range_and_fov(self):
        """
        Update list of valid tiles within range based on currently selected skill's range.
        """
        skill_being_targeted = self.get_skill_being_targeted()

        # if there is a skill being targeted
        if skill_being_targeted:

            skill_data = library.get_skill_data(skill_being_targeted.skill_tree_name, skill_being_targeted.name)
            skill_range = skill_data.range

            from scripts.global_singletons.managers import world_manager
            tiles = world_manager.FOV.get_tiles_in_range_and_fov_of_player(skill_range)

            self.set_tiles_in_targeting_overlay(tiles)

    def update_targeting_overlays_tiles_in_skill_effect_range(self):
        """
        Update the list of Tiles for those effected by the skill effect range. Based on selected skill.
        """
        # TODO - convert to a set method and set via an event
        targeting_overlay = self.get_ui_element(UIElementTypes.TARGETING_OVERLAY)

        # if there is a skill being targeted
        if targeting_overlay.skill_being_targeted:

            # clear current tiles
            targeting_overlay.tiles_in_skill_effect_range = []

            # get the skill data
            data = library.get_skill_data(targeting_overlay.skill_being_targeted.skill_tree_name,
                                          targeting_overlay.skill_being_targeted.name)

            from scripts.global_singletons.managers import world_manager
            coords = world_manager.Skill.create_shape(data.shape, data.shape_size)
            effected_tiles = world_manager.Map.get_tiles(targeting_overlay.selected_tile.x,
                                                         targeting_overlay.selected_tile.y, coords)

            targeting_overlay.tiles_in_skill_effect_range = effected_tiles

    def update_skill_bar(self):
        """
        Get the player`s known skills to show in the skill bar, up to max skills shown in bar.
        """
        skill_bar = self.get_ui_element(UIElementTypes.SKILL_BAR)

        # update info
        from scripts.global_singletons.managers import world_manager
        player = world_manager.player

        # if the player has been init'd update skill bar
        if player:
            skills = []

            for counter, skill in enumerate(player.actor.known_skills):
                if counter <= skill_bar.max_skills_in_bar:
                    skills.append(skill)

            self.set_skills_in_skill_bar(skills)

    def set_skills_in_skill_bar(self, skills_to_draw: list):
        """
        Set the skills to be drawn on the skill bar

        Args:
            skills_to_draw ():
        """
        skill_bar = self.get_ui_element(UIElementTypes.SKILL_BAR)
        render_area = skill_bar.render_area
        size_x = skill_bar.skill_size_x
        size_y = skill_bar.skill_size_y
        gap = skill_bar.gap_between_skill_icons

        # clear existing
        skill_bar.skills_to_draw = []
        skill_bar.skills_to_draw = skills_to_draw

        # starting draw positions for skills, relative to render area
        draw_x = int((skill_bar.render_area.width / 2) - (size_x / 2))
        draw_y = -size_y

        for skill in skills_to_draw:
            # add skill icon
            data = library.get_skill_data(skill.skill_tree_name, skill.name)
            image = pyglet.resource.image(data.icon)
            render_area.add_image(image, draw_x, draw_y, size_x, size_y)

            # add skill name
            render_area.add_text(skill.name, draw_x, draw_y)

            # increment draw position
            draw_y -= size_y + gap

    def update_entity_queue(self):
        """
        Get info from the turn_manager and update the entity queue to be displayed
        """
        entity_queue = self.get_ui_element(UIElementTypes.ENTITY_QUEUE)

        counter = 0
        entities_to_draw = []

        # loop entities in turn queue, up to max to show
        from scripts.global_singletons.managers import turn_manager
        for entity, time in turn_manager.turn_queue.items():
            if counter < entity_queue.max_entities_to_show:
                entities_to_draw.append(entity)

                counter += 1

            else:
                break

        self.set_entities_in_entity_queue(entities_to_draw)

    def set_entities_in_entity_queue(self, entities_to_draw: list):
        """
        Set the entities to draw in the entity queue.

        Args:
            entities_to_draw ():
        """
        entity_queue = self.get_ui_element(UIElementTypes.ENTITY_QUEUE)
        render_area = entity_queue.render_area
        size_x = entity_queue.entity_size_x
        size_y = entity_queue.entity_size_y
        gap = entity_queue.gap_between_entities

        # clear current queue
        entity_queue.entities_to_draw.clear()
        entity_queue.entities_to_draw = entities_to_draw

        # starting draw positions
        draw_x = int((entity_queue.render_area.width / 4) - 5)
        draw_y = -size_y

        for entity in entities_to_draw:
            # add entity icon
            render_area.add_image(entity.icon, draw_x, draw_y, size_x, size_y)

            # add name
            render_area.add_text(entity.name, draw_x, draw_y)

            # increment draw position
            draw_y -= size_y + gap

    def set_tiles_in_camera(self, tiles):
        """
        Set the tiles to be drawn by the camera.

        Args:
            tiles (list[Tile]): all of the tiles to draw.
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)

        # update tile list
        camera.tiles_to_draw = tiles

        # clear previous sprites
        camera.render_area.sprites = []
        camera.render_area.batch = pyglet.graphics.Batch()

        tiles = camera.tiles_to_draw
        height = camera.height
        render_area = camera.render_area
        y_pos = height
        x_pos = 0

        for x in range(0, len(tiles)):
            tile = tiles[x]

            if y_pos <= 0:
                y_pos = height
                x_pos += 1

            draw_x = x_pos * TILE_SIZE
            draw_y = y_pos * TILE_SIZE

            if tile.terrain:
                render_area.add_image(tile.terrain.sprite, draw_x, draw_y, TILE_SIZE, TILE_SIZE, RenderOrder.TERRAIN)

            if tile.entity:
                render_area.add_image(tile.entity.icon, draw_x, draw_y, TILE_SIZE, TILE_SIZE, RenderOrder.ENTITY)

            if tile.aspects:
                for key, aspect in tile.aspects.items():
                    render_area.add_image(aspect.sprite, draw_x, draw_y, TILE_SIZE, TILE_SIZE, RenderOrder.ASPECT)

            y_pos -= 1

    def is_target_pos_in_camera_edge(self, target_pos: Tuple):
        """
        Determine if target position is within the edge of the camera

        Args:
            target_pos (): x,y

        Returns:
            bool:
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)
        player_x, player_y = target_pos

        edge_start_x = camera.x
        edge_end_x = camera.x + camera.width
        edge_start_y = camera.y
        edge_end_y = camera.y + camera.height

        if edge_start_x <= player_x < edge_start_x + camera.edge_size:
            print("in left")
            return True
        elif edge_end_x >= player_x > edge_end_x - camera.edge_size:
            print("in right")
            return True
        elif edge_start_y <= player_y < edge_start_y + camera.edge_size:
            print("in up")
            return True
        elif edge_end_y >= player_y > edge_end_y - camera.edge_size:
            print("in down")
            return True
        else:
            return False

    def should_camera_move(self, start_pos: Tuple, target_pos: Tuple):
        """
        Determine if camera should move based on start and target pos and intersecting the edge of the screen.

        Args:
            start_pos (): x,y
            target_pos (): x,y

        Returns:
            bool:
        """
        start_x, start_y = start_pos
        target_x, target_y = target_pos
        camera = self.get_ui_element(UIElementTypes.CAMERA)

        edge_start_x = camera.x
        edge_end_x = camera.x + camera.width
        edge_start_y = camera.y
        edge_end_y = camera.y + camera.height

        start_pos_in_edge = self.is_target_pos_in_camera_edge(start_pos)
        target_pos_in_edge = self.is_target_pos_in_camera_edge(target_pos)

        # are we currently in the edge (e.g. edge of world)
        if start_pos_in_edge:

            # will we still be in the edge after we move?
            if target_pos_in_edge:
                dir_x = target_x - start_x
                dir_y = target_y - start_y

                # are we moving to a worse position?
                if edge_start_x <= start_x < edge_start_x + camera.edge_size:
                    # player is on the left side, are we moving left?
                    if dir_x < 0:
                        print("moving left")
                        return True
                if edge_end_x > start_x >= edge_end_x - camera.edge_size:
                    # player is on the right side, are we moving right?
                    if 0 < dir_x:
                        print("moving right")
                        return True
                if edge_start_y <= start_y < edge_start_y + camera.edge_size:
                    # player is on the up side, are we moving up?
                    if dir_y < 0:
                        print("moving up")
                        return True
                if edge_end_y > start_y >= edge_end_y - camera.edge_size:
                    # player is on the down side, are we moving down?
                    if 0 < dir_y:
                        print("moving down")
                        return True

        elif target_pos_in_edge:
            # we are moving into the edge
            return True

        else:
            return False

    def move_camera(self, move_x: int, move_y: int):
        """
        Increment camera's drawn tiles in the given direction. N.B. Physical position on screen does not change.

        Args:
            move_x (): number of tiles to move the x
            move_y (): number of tiles to move the y
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)

        from scripts.global_singletons.managers import world_manager
        game_map = world_manager.Map.get_game_map()

        # clamp function: max(low, min(n, high))
        camera.x = max(0, min(camera.x + move_x, game_map.width))
        camera.y = max(0, min(camera.y + move_y, game_map.height))

    def update_cameras_tiles_to_draw(self):
        """
        Retrieve the tiles to draw within view of the camera
        """
        camera = self.get_ui_element(UIElementTypes.CAMERA)
        coords = []

        for x in range(camera.x, camera.x + camera.width):
            for y in range(camera.y, camera.y + camera.height):
                coords.append((x, y))

        from scripts.global_singletons.managers import world_manager
        # use 0,0 to stop the camera double jumping due to converting back and forth from world and physical space
        tiles = world_manager.Map.get_tiles(0, 0, coords)
        self.set_tiles_in_camera(tiles)

