import pygame

from scripts.components.actor import Actor
from scripts.components.combatant import Combatant
from scripts.core.constants import EventTopics, SPRITE_PLAYER, GameStates
from scripts.events.entity_handler import EntityHandler
from scripts.events.logging_handler import LoggingHandler
from scripts.events.message_handler import MessageHandler
from scripts.events.game_handler import GameHandler
from scripts.core.global_data import game_manager, world_manager, entity_manager, turn_manager
from scripts.entities.entity import Entity


def initialise_game():
    """
    Init the game's required info
    """

    pygame.init()

    initialise_event_handlers()

    world_manager.create_new_map(50, 30)  # TODO remove magic numbers

    player = Entity(0, 0, SPRITE_PLAYER, "player", actor=Actor(), combatant=Combatant(), sight_range=5)
    # TODO move  to player creation  method

    entity_manager.add_player(player)

    entity_manager.create_actor(0, 3, "orc_fighter")  # TODO remove- test only

    game_manager.update_game_state(GameStates.PLAYER_TURN) # TODO remove when main menu is starting point
    turn_manager.turn_holder = player


def initialise_event_handlers():
    game_handler = GameHandler(game_manager.event_hub)
    game_handler.subscribe(EventTopics.GAME)

    message_handler = MessageHandler(game_manager.event_hub)
    message_handler.subscribe(EventTopics.MESSAGE)

    logging_handler = LoggingHandler(game_manager.event_hub)
    logging_handler.subscribe(EventTopics.LOGGING)

    entity_handler = EntityHandler(game_manager.event_hub)
    entity_handler.subscribe(EventTopics.ENTITY)
