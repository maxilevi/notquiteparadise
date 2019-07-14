from scripts.core.constants import MessageEventTypes, LoggingEventTypes, TargetTags, SkillEffectTypes
from scripts.events.logging_events import LoggingEvent
from scripts.events.message_events import MessageEvent
from scripts.global_singletons.data_library import library
from scripts.global_singletons.event_hub import publisher
from scripts.skills.skill_effects.skill_effect import SkillEffect
from scripts.world.terrain.floor import Floor
from scripts.world.terrain.terrain import Terrain
from scripts.world.terrain.wall import Wall


class ChangeTerrainSkillEffect(SkillEffect):
    """
    SkillEffect to change the terrain of a tile
    """

    def __init__(self, owner):
        super().__init__(owner, "change_terrain", "This is the Manipulate Terrain effect",
                         SkillEffectTypes.CHANGE_TERRAIN)

    def trigger(self, terrain_to_change):
        """
        Trigger the effect; check tags and then, if all True, apply the effect

        Args:
            terrain_to_change (Terrain):
        """
        super().trigger()

        tags_checked = {}  # bool list of tags checked
        tile = terrain_to_change.owner
        terrain = terrain_to_change
        starting_terrain_name = terrain.name

        from scripts.global_singletons.managers import world_manager
        target_type = world_manager.Skill.get_target_type(terrain)

        data = library.get_skill_effect_data(self.owner.skill_tree_name, self.owner.name, self.skill_effect_type)

        # check the type is correct, then that the tags match
        if target_type == data.required_target_type:

            # assess all tags
            for tag in data.required_tags:
                tags_checked[tag] = world_manager.Map.tile_has_tag(tile, tag)

            # if all tags came back true apply the change
            if all(value for value in tags_checked.values()):
                world_manager.Map.set_terrain_on_tile(tile, data.new_terrain)

                # success message
                entity = self.owner.owner.owner
                msg = f"{entity.name} changed the {starting_terrain_name} to {tile.terrain.name}."
                publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

            else:
                # log why
                log_string = f"-> target tags incorrect; tag results:{tags_checked}"
                publisher.publish(LoggingEvent(LoggingEventTypes.WARNING, log_string))
        else:
            # confirm can't do it
            msg = f"You can't do that there!"
            publisher.publish(MessageEvent(MessageEventTypes.BASIC, msg))

            # log why
            log_string = f"-> target type incorrect; selected:{target_type}, needed:{data.required_target_type}"
            publisher.publish(LoggingEvent(LoggingEventTypes.WARNING, log_string))