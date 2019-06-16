from scripts.core.constants import LoggingEventTypes, EventTopics, GameEventTypes, GameStates, EntityEventTypes
from scripts.global_instances.event_hub import publisher
from scripts.global_instances.managers import game_manager, ui_manager, world_manager
from scripts.events.logging_events import LoggingEvent
from scripts.events.pub_sub_hub import Subscriber


class UiHandler(Subscriber):
    """
    Handle events that effect the UI
    """
    def __init__(self, event_hub):
        Subscriber.__init__(self, "ui_handler", event_hub)
        # TODO - all UI functionality to watch events and update UI in response

    def run(self, event):
        """
        Process the events
        """

        # log that event has been received
        log_string = f"{self.name} received {event.topic}:{event.type}"
        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, log_string))

        # if an entity acts then hide the entity info
        if event.topic == EventTopics.ENTITY:
            if "entity_info" in ui_manager.visible_elements:
                self.hide_entity_info()

            if event.type == EntityEventTypes.LEARN:
                ui_manager.skill_bar.update_skill_icons_to_show()

        if event.topic == EventTopics.GAME:
            if event.type == GameEventTypes.CHANGE_GAME_STATE:

                # if changing to targeting mode then turn on targeting overlay
                if event.new_game_state == GameStates.TARGETING_MODE:
                    # get info for initial selected tile
                    player = world_manager.player
                    tile = world_manager.Map.get_tile(player.x, player.y)

                    # set the info needed to draw the overlay
                    ui_manager.targeting_overlay.set_skill_being_targeted(event.skill_to_be_used)
                    ui_manager.targeting_overlay.update_tiles_to_highlight()
                    ui_manager.targeting_overlay.set_selected_tile(tile)

                    # show the entity info
                    entity = world_manager.Entity.get_blocking_entity_at_location(tile.x, tile.y)
                    ui_manager.entity_info.set_selected_entity(entity)

                    # show the overlay
                    ui_manager.targeting_overlay.set_visibility(True)

                elif game_manager.previous_game_state.TARGETING_MODE:
                    ui_manager.targeting_overlay.set_visibility(False)

    @staticmethod
    def hide_entity_info():
        """
        Hide the entity info panel
        """
        ui_manager.entity_info.set_visibility(False)
        log_string = f"Entity info hidden."
        publisher.publish(LoggingEvent(LoggingEventTypes.INFO, log_string))