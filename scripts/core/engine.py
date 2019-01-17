import pygame

from scripts.core.constants import PALETTE_BACKGROUND, TILE_SIZE, GameStates, DEBUG_FONT
from scripts.core.global_data import world_manager, game_manager, entity_manager, turn_manager
from scripts.core.input import get_input, handle_input
from scripts.core.intialisers import initialise_game

main_surface = None


def main():
    """The container for the game init and game loop"""

    global main_surface

    main_surface = initialise_game()
    game_loop()

    # we've left the game loop so now leave the game
    pygame.quit()  # clean up pygame resources
    raise SystemExit  # exit window and python


def game_loop():

    # TODO enforce loop timestep
    while not game_manager.game_state == GameStates.EXIT_GAME:

        if game_manager.game_state == GameStates.PLAYER_TURN:
            # HANDLE INPUT
            # determine the action to take from the input with the context of the game state
            input_values = get_input()
            handle_input(input_values)

        elif game_manager.game_state == GameStates.ENEMY_TURN:
            turn_manager.turn_holder.ai.take_turn()

        # HANDLE UPDATE
        game_manager.event_hub.update()

        # DRAW
        draw_game()


def draw_game():
    global main_surface

    main_surface.fill(PALETTE_BACKGROUND)

    draw_map(world_manager.game_map)
    draw_entities()
    draw_debug_info()

    # update the display
    pygame.display.flip()


def draw_map(map):

    for x in range(0, map.width):
        for y in range(0, map.height):
            tile_position = (x * TILE_SIZE, y * TILE_SIZE)
            main_surface.blit(map.tiles[x][y].sprite, tile_position)  # Yes, it is [y][x] - don't forget it!


def draw_entities():
    for entity in entity_manager.entities:
        main_surface.blit(entity.sprite, (entity.x * TILE_SIZE, entity.y * TILE_SIZE))


def draw_debug_info():
    info_to_display = f"The current time is:{turn_manager.time}"
    DEBUG_FONT.render_to(main_surface, (0, 0), info_to_display, (0, 0, 0))


if __name__ == "__main__":  # prevents being run from other modules
    main()
