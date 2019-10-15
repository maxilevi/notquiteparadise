
import cProfile
import io
import logging
import pstats
import glooey
import pygame
import pyglet

from pyglet.window import FPSDisplay
from scripts.core.constants import GameStates
from scripts.global_singletons.managers import world_manager, game_manager, turn_manager, ui_manager, debug_manager, \
    input_manager
from scripts.global_singletons.event_hub import event_hub
from scripts.core.initialisers import initialise_game, initialise_event_handlers, initialise_logging


# Project Wide to do list...
# TODO - create global tooltip method - some relevant code in old message `log -
#  when object created needs a tooltip: pass the rect and create link to a tooltip obj (ui_man?) to store and refer
#  back to. Needs to be able to get updated strings (info not always static) and updated positions
# TODO - swap out nose for pytest
# TODO - change from use fps for timing to delta time
# TODO - draw dirty for map section (use an array to store ref to dirty x,y OR dirty flag on each tile)
# TODO - remember window position and resume at that place
# TODO - move assignation of Owner to the init
# TODO - Review closure
#  https://en.wikipedia.org/wiki/Closure_(computer_programming)
# TODO - Review compression example
#  https://gist.github.com/brianbruggeman/61199d1ddbbf220a4b5cc528da13b5c8
# TODO - move the docstring annotations to the function line, then install mypy
# TODO - use seed for RNG
# TODO - new lighting system
#  entities create light, sight range shows light in range
# TODO - stats json needs icons assigning



def main():
    """
    The container for the game initialisation and game loop
    """
    # initialise logging
    initialise_logging()

    # initialise profiling
    # TODO - set to turn off for production builds
    profiler = cProfile.Profile()
    profiler.enable()

    # **** setting up during migration
    ui_manager.Element.init_camera()
    ui_manager.Element.init_entity_queue()
    ui_manager.Element.init_skill_bar()
    ui_manager.Element.init_message_log()


    # initialise the game
    #initialise_ui_elements()
    initialise_event_handlers()
    initialise_game()

    # *** during migration only
    ui_manager.Element.update_cameras_tiles_to_draw()
    turn_manager.build_new_turn_queue()
    ui_manager.Element.update_entity_queue()
    ui_manager.Element.update_skill_bar()

    # run the game
    #game_loop()

    window = ui_manager.Display.get_window()
    fps_display = FPSDisplay(window)

    # glooey gui
    batch = pyglet.graphics.Batch()
    group = pyglet.graphics.OrderedGroup(98)
    gui = glooey.Gui(window=window, batch=batch, group=group)

    # box with buttons
    # vbox = glooey.VBox()
    # vbox.alignment = "center"
    # from scripts.ui_elements.message_log import MyTitle
    # title = MyTitle("What... question")
    # vbox.add(title)
    #from scripts.ui_elements.message_log import MyButton
    # buttons = [MyButton("BUtton 1","Ans1"), MyButton("button2", "Ans2")]
    #
    # for button in buttons:
    #     vbox.add(button)

    # gui.add(vbox)

    #print(f"Window:{window.width},{window.height}; GUI:{gui.width, gui.height}")
    window_width, window_height = 1280, 720
    board = glooey.Board()
    board.size_hint = window_width, window_height
    #board.alignment = "fill"
    gui.add(board)

    from scripts.ui_elements.templates.menu_scroll_box import MenuScrollBox
    scrollbox = MenuScrollBox()
    scroll_width, scroll_height = 400, 200
    scrollbox.size_hint = scroll_width, scroll_height
    board.add(scrollbox, right=window_width, bottom=0)

    text = "test"
    label = glooey.Label(text, line_wrap=300)
    label.alignment = "center"
    scrollbox.add(label)





    # button with click
    # button = MyButton("Click here!", "Working")
    # gui.add(button)


    # Set up window events
    @window.event
    def on_draw():
        window.clear()
        ui_manager.Element.draw_visible_elements()
        fps_display.draw()  # TODO - move to debug
        batch.draw()  # TODO - remove after testing glooey

    # @window.event
    # def on_mouse_press(x, y, button, modifiers):
    #     print(f"{button} pressed at ({x},{y})")
    #     # input_manager

    @window.event
    def on_key_press(symbol, modifiers):
        print(f"{symbol} was pressed.")
        # input_manager

    @window.event
    def on_key_release(symbol, modifiers):
        pass
        # input manager

    # @window.event
    # def on_mouse_scroll(x, y, scroll_x, scroll_y):
    #     print(f"Mouse scrolled {scroll_y} click.")

    # set up the scheduled update
    def update(dt):
        # input_manager.update()
        # game_manager.update()
        # debug_manager.update()
        # world_manager.update()
        # ui_manager.update()
        event_hub.update()
        # turn_manager.turn_holder.ai.take_turn() # TODO - move to event

    # All events received on the window to be printed to the console
    window.push_handlers(pyglet.window.event.WindowEventLogger())

    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 120.0)

    # enter app loop, exit when all windows closed
    pyglet.app.run()

    # we've left the game loop so now close everything down
    profiler.disable()
    dump_profiling_data(profiler)
    logging.shutdown()  # clear logging resources
    pygame.quit()  # clean up pygame resources
    raise SystemExit  # exit window and python


def game_loop():
    """
    The core game loop, handling input, rendering and logic.
    """
    while not game_manager.game_state == GameStates.EXIT_GAME:

        # limit frames
        game_manager.internal_clock.tick(60)

        if game_manager.game_state == GameStates.ENEMY_TURN:
            turn_manager.turn_holder.ai.take_turn()

        # HANDLE UPDATE
        input_manager.update()
        game_manager.update()
        debug_manager.update()
        world_manager.update()
        ui_manager.update()
        event_hub.update()

        # DRAW
        debug_manager.draw()
        ui_manager.Element.draw_visible_elements()


# TODO - move to debug manager
def dump_profiling_data(profiler):
    """
    End profiling
    Args:
        profiler: The profiler
    """

    # dump the profiler stats
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats("cumulative")
    ps.dump_stats("logs/profiling/profile.dump")

    # convert profiling to human readable format
    import datetime
    date_and_time = datetime.datetime.utcnow()

    # TODO - add version number to profile logs
    out_stream = open("logs/profiling/" + date_and_time.strftime("%y%m%d@%H%M") + ".profile", "w")
    ps = pstats.Stats("logs/profiling/profile.dump", stream=out_stream)
    ps.strip_dirs().sort_stats("cumulative").print_stats()


if __name__ == "__main__":  # prevents being run from other modules
    main()
