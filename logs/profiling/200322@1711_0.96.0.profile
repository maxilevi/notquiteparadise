Sun Mar 22 17:11:53 2020    logs/profiling/profile.dump

         2191593 function calls (2059776 primitive calls) in 13.114 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.130    0.130   13.072   13.072 main.py:103(game_loop)
      744    8.442    0.011    8.442    0.011 {method 'tick' of 'Clock' objects}
      372    0.001    0.000    4.238    0.011 state.py:63(update_clock)
      372    0.002    0.000    4.207    0.011 state.py:38(get_delta_time)
      372    0.005    0.000    1.755    0.005 manager.py:73(draw)
      372    0.001    0.000    1.737    0.005 manager.py:54(update)
      372    0.105    0.000    1.735    0.005 ui_manager.py:122(update)
   122559    1.266    0.000    1.266    0.000 {method 'blit' of 'pygame.Surface' objects}
      372    0.059    0.000    1.054    0.003 sprite.py:453(update)
      372    0.001    0.000    0.871    0.002 event_core.py:24(update)
       31    0.000    0.000    0.845    0.027 ui_handler.py:31(process_event)
        5    0.000    0.000    0.820    0.164 ui_handler.py:201(_update_camera)
        5    0.000    0.000    0.808    0.162 manager.py:295(update_camera_grid)
        5    0.005    0.001    0.808    0.162 camera.py:105(update_grid)
      758    0.010    0.000    0.795    0.001 ui_button.py:30(__init__)
      758    0.041    0.000    0.748    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
      376    0.337    0.001    0.735    0.002 camera.py:79(update_game_map)
      371    0.002    0.000    0.730    0.002 camera.py:72(update)
      372    0.003    0.000    0.672    0.002 ui_manager.py:173(draw_ui)
      372    0.105    0.000    0.669    0.002 sprite.py:753(draw)
        6    0.000    0.000    0.659    0.110 ui_handler.py:44(process_entity_event)
    22111    0.056    0.000    0.604    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
153867/22111    0.515    0.000    0.544    0.000 ui_appearance_theme.py:322(get_next_id_node)
      376    0.503    0.001    0.503    0.001 {built-in method pygame.transform.scale}
    59919    0.251    0.000    0.445    0.000 ui_element.py:121(check_hover)
    11430    0.029    0.000    0.341    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
    58483    0.113    0.000    0.212    0.000 ui_button.py:197(update)
     6882    0.013    0.000    0.199    0.000 ui_appearance_theme.py:428(get_misc_data)
       21    0.000    0.000    0.175    0.008 ui_handler.py:68(process_game_event)
        1    0.000    0.000    0.169    0.169 ui_handler.py:107(init_game_ui)
      372    0.134    0.000    0.134    0.000 {built-in method pygame.display.flip}
    58483    0.070    0.000    0.132    0.000 ui_button.py:138(hover_point)
     3756    0.113    0.000    0.119    0.000 sprite.py:913(get_sprites_from_layer)
      758    0.005    0.000    0.093    0.000 ui_button.py:97(set_any_images_from_theme)
     3032    0.006    0.000    0.088    0.000 ui_appearance_theme.py:366(get_image)
      372    0.085    0.000    0.085    0.000 {built-in method pygame.event.get}
    56403    0.081    0.000    0.081    0.000 camera.py:233(world_to_screen_position)
    58483    0.033    0.000    0.076    0.000 drawable_shape.py:36(update)
    58483    0.055    0.000    0.063    0.000 rect_drawable_shape.py:84(collide_point)
     2899    0.019    0.000    0.056    0.000 rect_drawable_shape.py:118(redraw_state)
      903    0.055    0.000    0.055    0.000 {method 'fill' of 'pygame.Surface' objects}
   121694    0.042    0.000    0.050    0.000 sprite.py:208(alive)
      758    0.006    0.000    0.045    0.000 ui_button.py:537(rebuild_shape)
        1    0.000    0.000    0.043    0.043 main.py:211(initialise_game)
      368    0.002    0.000    0.040    0.000 screen_message.py:34(update)
      767    0.003    0.000    0.040    0.000 rect_drawable_shape.py:22(__init__)
        2    0.000    0.000    0.038    0.019 entity.py:232(create_actor)
      777    0.008    0.000    0.036    0.000 ui_element.py:23(__init__)
      767    0.011    0.000    0.035    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
      246    0.001    0.000    0.035    0.000 ui_text_box.py:347(redraw_from_chunks)
        2    0.008    0.004    0.031    0.016 world.py:26(create_fov_map)
      739    0.007    0.000    0.031    0.000 ui_text_box.py:205(update)
   406199    0.030    0.000    0.030    0.000 {method 'append' of 'list' objects}
      758    0.003    0.000    0.029    0.000 ui_appearance_theme.py:405(get_font)
      246    0.003    0.000    0.025    0.000 ui_text_box.py:327(redraw_from_text_block)
    58483    0.023    0.000    0.023    0.000 ui_button.py:154(can_hover)
      767    0.004    0.000    0.021    0.000 drawable_shape.py:45(redraw_all_states)
      372    0.001    0.000    0.021    0.000 processors.py:18(process_all)
      372    0.011    0.000    0.020    0.000 processors.py:25(_process_aesthetic_update)
       35    0.000    0.000    0.020    0.001 manager.py:60(process_ui_events)
        8    0.000    0.000    0.020    0.002 ui_text_box.py:50(__init__)
       35    0.007    0.000    0.020    0.001 ui_manager.py:86(process_events)
        8    0.000    0.000    0.019    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
     4503    0.006    0.000    0.018    0.000 _internal.py:24(wrapper)
        8    0.000    0.000    0.018    0.002 ui_text_box.py:110(rebuild)
      777    0.002    0.000    0.017    0.000 ui_container.py:42(add_element)
   310923    0.016    0.000    0.016    0.000 {built-in method builtins.len}
     2935    0.016    0.000    0.016    0.000 {method 'copy' of 'pygame.Surface' objects}
     2899    0.015    0.000    0.015    0.000 surface_cache.py:119(build_cache_id)
        5    0.003    0.001    0.014    0.003 ui_container.py:116(clear)
     3762    0.008    0.000    0.013    0.000 world.py:55(get_tile)
        5    0.000    0.000    0.013    0.003 message_log.py:50(add_message)
     1384    0.013    0.000    0.013    0.000 ui_container.py:62(recalculate_container_layer_thickness)
      124    0.001    0.000    0.013    0.000 ui_text_box.py:462(set_active_effect)
       27    0.000    0.000    0.012    0.000 entity_handler.py:26(process_event)
      600    0.001    0.000    0.012    0.000 ui_button.py:130(kill)
     2743    0.009    0.000    0.011    0.000 query.py:212(__iter__)
        4    0.000    0.000    0.011    0.003 ui_handler.py:151(process_ui_event)
        4    0.000    0.000    0.011    0.003 ui_handler.py:232(_process_message)
        4    0.000    0.000    0.011    0.003 manager.py:444(add_to_message_log)
      607    0.001    0.000    0.011    0.000 ui_element.py:114(kill)
        9    0.000    0.000    0.011    0.001 ui_text_box.py:310(parse_html_into_style_data)
      777    0.001    0.000    0.011    0.000 sprite.py:121(__init__)
    63211    0.010    0.000    0.010    0.000 ui_manager.py:167(get_mouse_position)
       76    0.001    0.000    0.010    0.000 __init__.py:1496(_log)
     4504    0.009    0.000    0.010    0.000 {built-in method _warnings.warn}
      246    0.003    0.000    0.009    0.000 text_block.py:265(redraw_from_chunks)
      777    0.003    0.000    0.009    0.000 sprite.py:126(add)
        9    0.000    0.000    0.009    0.001 text_block.py:16(__init__)
   121694    0.009    0.000    0.009    0.000 {built-in method _operator.truth}
        9    0.001    0.000    0.008    0.001 text_block.py:40(redraw)
        3    0.000    0.000    0.008    0.003 entity_handler.py:45(_process_move)
     2227    0.006    0.000    0.008    0.000 ui_container.py:124(check_hover)
    62146    0.008    0.000    0.008    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
        5    0.000    0.000    0.008    0.002 manager.py:286(update_camera_game_map)
        1    0.002    0.002    0.008    0.008 world.py:433(update_tile_visibility)
    59313    0.008    0.000    0.008    0.000 {method 'union' of 'pygame.Rect' objects}
       51    0.000    0.000    0.007    0.000 __init__.py:1996(debug)
      777    0.002    0.000    0.007    0.000 ui_element.py:104(change_layer)
       51    0.000    0.000    0.007    0.000 __init__.py:1361(debug)
       21    0.000    0.000    0.007    0.000 game_handler.py:26(process_event)
      607    0.001    0.000    0.007    0.000 ui_container.py:52(remove_element)
    63550    0.006    0.000    0.006    0.000 {method 'colliderect' of 'pygame.Rect' objects}
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
        2    0.000    0.000    0.006    0.003 entity.py:339(build_characteristic_sprites)
      844    0.002    0.000    0.006    0.000 ui_font_dictionary.py:89(find_font)
        2    0.000    0.000    0.006    0.003 interaction_handler.py:27(process_event)
        2    0.000    0.000    0.006    0.003 interaction_handler.py:85(_process_entity_collision)
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
      785    0.005    0.000    0.006    0.000 sprite.py:822(change_layer)
    87896    0.006    0.000    0.006    0.000 {method 'reverse' of 'list' objects}
      777    0.005    0.000    0.006    0.000 sprite.py:646(add_internal)
        2    0.000    0.000    0.005    0.003 skill.py:138(_call_skill_func)
       76    0.000    0.000    0.005    0.000 __init__.py:1521(handle)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
        2    0.000    0.000    0.005    0.003 interaction_handler.py:135(_apply_effects_to_tiles)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
       76    0.000    0.000    0.005    0.000 __init__.py:1575(callHandlers)
      372    0.001    0.000    0.005    0.000 ui_appearance_theme.py:158(update_shape_cache)
     2899    0.004    0.000    0.005    0.000 drawable_shape.py:122(rebuild_images_and_text)
       76    0.000    0.000    0.005    0.000 __init__.py:892(handle)
     3774    0.004    0.000    0.004    0.000 world.py:347(_is_tile_in_bounds)
        1    0.000    0.000    0.004    0.004 ui_vertical_scroll_bar.py:22(__init__)
        6    0.000    0.000    0.004    0.001 game_handler.py:81(_process_end_turn)
      3/2    0.000    0.000    0.004    0.002 skill.py:218(process_effect)
       76    0.000    0.000    0.004    0.000 __init__.py:1123(emit)
        6    0.000    0.000    0.004    0.001 chrono.py:47(next_turn)
       76    0.000    0.000    0.004    0.000 __init__.py:1022(emit)
     1177    0.004    0.000    0.004    0.000 typing.py:806(__new__)
      372    0.002    0.000    0.004    0.000 ecs.py:265(process_pending_deletions)
        5    0.000    0.000    0.004    0.001 manager.py:275(update_cameras_tiles)
      372    0.001    0.000    0.004    0.000 surface_cache.py:24(update)
        5    0.001    0.000    0.004    0.001 camera.py:167(update_camera_tiles)
     1177    0.003    0.000    0.004    0.000 query.py:170(__init__)
        1    0.000    0.000    0.004    0.004 world.py:19(create_game_map)
        1    0.002    0.002    0.004    0.004 game_map.py:12(__init__)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
     1856    0.003    0.000    0.004    0.000 ui_window.py:97(update)
        1    0.000    0.000    0.004    0.004 skill.py:259(_process_activate_skill)
      407    0.002    0.000    0.004    0.000 sprite.py:814(layers)
       76    0.000    0.000    0.003    0.000 __init__.py:1481(makeRecord)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
       24    0.000    0.000    0.003    0.000 __init__.py:1986(info)
        1    0.000    0.000    0.003    0.003 message_log.py:19(__init__)
      607    0.001    0.000    0.003    0.000 sprite.py:183(kill)
       24    0.000    0.000    0.003    0.000 __init__.py:1373(info)
       76    0.001    0.000    0.003    0.000 __init__.py:293(__init__)
       18    0.002    0.000    0.003    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
        1    0.000    0.000    0.003    0.003 entity_handler.py:119(_process_use_skill)
     3464    0.003    0.000    0.003    0.000 ui_button.py:257(process_event)
        1    0.000    0.000    0.003    0.003 skill.py:113(use)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
       22    0.001    0.000    0.003    0.000 styled_chunk.py:8(__init__)
      372    0.002    0.000    0.002    0.000 ui_manager.py:158(update_mouse_position)
       14    0.000    0.000    0.002    0.000 game_handler.py:39(_process_change_game_state)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
      744    0.002    0.000    0.002    0.000 sprite.py:745(sprites)
      607    0.001    0.000    0.002    0.000 sprite.py:728(remove_internal)
        7    0.000    0.000    0.002    0.000 chrono.py:24(rebuild_turn_queue)
       76    0.000    0.000    0.002    0.000 __init__.py:869(format)
        4    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:722(exec_module)
      767    0.002    0.000    0.002    0.000 drawable_shape.py:11(__init__)
        1    0.000    0.000    0.002    0.002 basic_attack.py:18(activate)
       13    0.000    0.000    0.002    0.000 state.py:71(set_new)
       76    0.000    0.000    0.002    0.000 __init__.py:606(format)
      371    0.001    0.000    0.002    0.000 skill_bar.py:45(update)
       57    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
      232    0.002    0.000    0.002    0.000 ui_manager.py:104(<listcomp>)
      773    0.001    0.000    0.002    0.000 ui_element.py:68(create_valid_ids)
        2    0.000    0.000    0.002    0.001 __init__.py:109(import_module)
      3/2    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:994(_gcd_import)
      326    0.002    0.000    0.002    0.000 ui_vertical_scroll_bar.py:228(update)
      3/2    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:978(_find_and_load)
      9/7    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
        2    0.000    0.000    0.002    0.001 __init__.py:133(reload)
        9    0.000    0.000    0.002    0.000 parser.py:104(feed)
        9    0.000    0.000    0.002    0.000 parser.py:134(goahead)
     2899    0.002    0.000    0.002    0.000 surface_cache.py:109(find_surface_in_cache)
      2/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
        4    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:793(get_code)
      327    0.001    0.000    0.002    0.000 ecs.py:247(delete_entity_immediately)
       44    0.002    0.000    0.002    0.000 {method 'metrics' of 'pygame.font.Font' objects}
     1436    0.001    0.000    0.002    0.000 ui_element.py:186(hover_point)
        1    0.000    0.000    0.001    0.001 skill.py:413(_process_damage_effect)
     1942    0.001    0.000    0.001    0.000 query.py:243(<listcomp>)
       35    0.000    0.000    0.001    0.000 processors.py:59(process_intent)
      815    0.001    0.000    0.001    0.000 {built-in method builtins.sorted}
       76    0.000    0.000    0.001    0.000 __init__.py:1011(flush)
      371    0.001    0.000    0.001    0.000 message_log.py:37(update)
        5    0.000    0.000    0.001    0.000 entity.py:482(take_turn)
        2    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:610(_exec)
       21    0.000    0.000    0.001    0.000 processors.py:140(_process_player_turn_intents)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
       81    0.000    0.000    0.001    0.000 ntpath.py:212(basename)
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3300(map_is_in_fov)
      371    0.001    0.000    0.001    0.000 entity_info.py:47(update)
       34    0.001    0.000    0.001    0.000 entity.py:43(get_player)
     1177    0.001    0.000    0.001    0.000 query.py:50(__init__)
      845    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
     7542    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
       22    0.001    0.000    0.001    0.000 {built-in method nt.stat}
      767    0.001    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
     1429    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
       81    0.001    0.000    0.001    0.000 ntpath.py:178(split)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:882(_find_spec)
       76    0.001    0.000    0.001    0.000 __init__.py:1451(findCaller)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:663(_load_unlocked)
     3068    0.001    0.000    0.001    0.000 {built-in method math.floor}
       77    0.001    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
       76    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
       76    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
        6    0.001    0.000    0.001    0.000 {built-in method builtins.compile}
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
      762    0.001    0.000    0.001    0.000 state.py:45(get_current)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
      372    0.001    0.000    0.001    0.000 {built-in method pygame.mouse.get_pos}
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
      384    0.001    0.000    0.001    0.000 query.py:225(<listcomp>)
       22    0.000    0.000    0.001    0.000 parser.py:301(parse_starttag)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
  190/189    0.000    0.000    0.001    0.000 entity.py:93(get_entitys_component)
       36    0.000    0.000    0.001    0.000 entity.py:131(get_primary_stat)
        9    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
     2645    0.001    0.000    0.001    0.000 ui_window.py:107(get_container)
        9    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
        1    0.000    0.000    0.001    0.001 skill.py:536(_calculate_to_hit_score)
     4637    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
       15    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
     1439    0.001    0.000    0.001    0.000 {method 'pop' of 'dict' objects}
     1496    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
      804    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
        1    0.000    0.000    0.001    0.001 entity_handler.py:142(_process_die)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
       42    0.000    0.000    0.001    0.000 html_parser.py:118(add_text)
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:233(_insert_code)
      767    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
     2563    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
       76    0.000    0.000    0.001    0.000 ntpath.py:201(splitext)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
        1    0.000    0.000    0.001    0.001 skill.py:484(_calculate_damage)
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
     1178    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF8298D9BA0}
       76    0.000    0.000    0.000    0.000 {built-in method time.strftime}
     1552    0.000    0.000    0.000    0.000 {built-in method builtins.min}
      371    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
     1562    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
        6    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
       42    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
     2598    0.000    0.000    0.000    0.000 sprite.py:168(update)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:914(get_data)
      786    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
     2899    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
     1503    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       22    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
       73    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
        1    0.000    0.000    0.000    0.000 entity.py:201(create_god)
      162    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
      124    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
       35    0.000    0.000    0.000    0.000 action.py:12(convert_to_intent)
     1856    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
       91    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
        5    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       22    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
       49    0.000    0.000    0.000    0.000 entity.py:104(get_name)
       45    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
     1563    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
      374    0.000    0.000    0.000    0.000 {built-in method builtins.any}
       32    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
       76    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
       30    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
      122    0.000    0.000    0.000    0.000 text_effects.py:88(update)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
     1436    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
  348/330    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
      777    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
       35    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
        1    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
       49    0.000    0.000    0.000    0.000 entity.py:117(get_identity)
     2034    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
       76    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        8    0.000    0.000    0.000    0.000 world.py:268(tile_has_tag)
       10    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
     1520    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
        1    0.000    0.000    0.000    0.000 entity_handler.py:162(_process_want_to_use_skill)
       76    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
        8    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
       76    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
        1    0.000    0.000    0.000    0.000 entity.py:300(create_projectile)
      159    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
        1    0.000    0.000    0.000    0.000 combat_stats.py:118(accuracy)
       10    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
        1    0.000    0.000    0.000    0.000 combat_stats.py:270(sight_range)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
      133    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
       18    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
       76    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
        1    0.000    0.000    0.000    0.000 combat_stats.py:245(resist_mundane)
      152    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        7    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
       76    0.000    0.000    0.000    0.000 __init__.py:432(format)
      777    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
      251    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        6    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
      773    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        1    0.000    0.000    0.000    0.000 debug.py:28(log_component_not_found)
        7    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
      649    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        7    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        9    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
      326    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
        7    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        7    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
        1    0.000    0.000    0.000    0.000 __init__.py:1971(warning)
      777    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        1    0.000    0.000    0.000    0.000 skill.py:76(can_afford_cost)
        7    0.000    0.000    0.000    0.000 chrono.py:153(_get_pretty_queue)
        1    0.000    0.000    0.000    0.000 __init__.py:1385(warning)
        1    0.000    0.000    0.000    0.000 skill.py:95(pay_resource_cost)
      451    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 entity.py:189(delete)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
        6    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
      100    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
      152    0.000    0.000    0.000    0.000 __init__.py:856(release)
      765    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
       64    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
       33    0.000    0.000    0.000    0.000 event_core.py:41(publish)
        3    0.000    0.000    0.000    0.000 entity.py:73(get_entities_and_components_in_area)
        4    0.000    0.000    0.000    0.000 entity.py:174(create)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
        4    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
       40    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
      152    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        1    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
       76    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
        4    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
      195    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
        3    0.000    0.000    0.000    0.000 ai.py:68(act)
       35    0.000    0.000    0.000    0.000 processors.py:120(_process_stateless_intents)
       18    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
       76    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
        6    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
       51    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
        3    0.000    0.000    0.000    0.000 world.py:397(_tile_has_entity_blocking_movement)
       76    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
       21    0.000    0.000    0.000    0.000 processors.py:73(_get_pressed_direction)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
      124    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        2    0.000    0.000    0.000    0.000 world.py:315(tile_has_tags)
       22    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
       76    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
      228    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
       76    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
       35    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
      123    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
      432    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        1    0.000    0.000    0.000    0.000 main.py:238(initialise_event_handlers)
        1    0.000    0.000    0.000    0.000 god_handler.py:70(process_interventions)
       48    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
      607    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
        3    0.000    0.000    0.000    0.000 world.py:83(get_tiles)
       76    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
       18    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
        6    0.000    0.000    0.000    0.000 entity_handler.py:221(_process_end_turn)
       51    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
      264    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
      189    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
       18    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
        1    0.000    0.000    0.000    0.000 entity.py:425(consider_intervening)
       76    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
       33    0.000    0.000    0.000    0.000 event_core.py:15(notify)
      458    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
      120    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
        9    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      295    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
      155    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
       14    0.000    0.000    0.000    0.000 event.py:90(__init__)
       81    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        3    0.000    0.000    0.000    0.000 world.py:366(_tile_has_any_entity)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
      246    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        6    0.000    0.000    0.000    0.000 entity.py:377(spend_time)
        1    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
       76    0.000    0.000    0.000    0.000 threading.py:1052(name)
       12    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
      167    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        2    0.000    0.000    0.000    0.000 ai.py:42(act)
        2    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
      122    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
       23    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
      164    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000    0.000    0.000 world.py:426(recompute_fov)
       42    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        1    0.000    0.000    0.000    0.000 world.py:381(_tile_has_specific_entity)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
        9    0.000    0.000    0.000    0.000 parser.py:96(reset)
       51    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        1    0.000    0.000    0.000    0.000 skill.py:246(_process_trigger_skill_effect)
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       21    0.000    0.000    0.000    0.000 processors.py:100(_get_pressed_skills_number)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
      433    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
       35    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
      131    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
       77    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
       12    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       18    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
       33    0.000    0.000    0.000    0.000 event_core.py:73(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
        7    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
       76    0.000    0.000    0.000    0.000 {built-in method time.time}
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
       33    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        8    0.000    0.000    0.000    0.000 event_core.py:53(subscribe)
        4    0.000    0.000    0.000    0.000 event.py:168(__init__)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
       76    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
      122    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
       12    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        7    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
        1    0.000    0.000    0.000    0.000 random.py:218(randint)
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
       12    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        5    0.000    0.000    0.000    0.000 entity.py:332(add_component)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
       18    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
      155    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
       32    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        6    0.000    0.000    0.000    0.000 event.py:72(__init__)
       22    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
       46    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
        5    0.000    0.000    0.000    0.000 entity.py:124(get_combat_stats)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       84    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 random.py:174(randrange)
        3    0.000    0.000    0.000    0.000 event.py:55(__init__)
       38    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        4    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
       58    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       22    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
        1    0.000    0.000    0.000    0.000 random.py:344(choices)
       30    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
       38    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
       40    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
       38    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       10    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        1    0.000    0.000    0.000    0.000 world.py:103(get_direction)
        5    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       37    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        8    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        8    0.000    0.000    0.000    0.000 event_core.py:18(subscribe)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
        8    0.000    0.000    0.000    0.000 {built-in method math.sin}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
       19    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        9    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
       28    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        9    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
       20    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
        7    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       64    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        2    0.000    0.000    0.000    0.000 event.py:120(__init__)
       48    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
       15    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        4    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        1    0.000    0.000    0.000    0.000 ui_button.py:226(set_position)
       30    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
       18    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.format}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        2    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
       18    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.all}
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
       22    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        7    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        3    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
        8    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
       22    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
       52    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        3    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        3    0.000    0.000    0.000    0.000 component.py:40(__init__)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        3    0.000    0.000    0.000    0.000 <string>:1(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
        1    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
       15    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
        1    0.000    0.000    0.000    0.000 event.py:82(__init__)
       20    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        5    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
        1    0.000    0.000    0.000    0.000 main.py:188(disable_profiling)
       15    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        9    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        1    0.000    0.000    0.000    0.000 event.py:19(__init__)
       45    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        8    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
       23    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
        1    0.000    0.000    0.000    0.000 event.py:46(__init__)
        8    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
        1    0.000    0.000    0.000    0.000 entity_handler.py:23(__init__)
        5    0.000    0.000    0.000    0.000 event_core.py:49(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
       24    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        1    0.000    0.000    0.000    0.000 event.py:33(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
       18    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
        5    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
       22    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
       24    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        4    0.000    0.000    0.000    0.000 component.py:82(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
       25    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        2    0.000    0.000    0.000    0.000 component.py:184(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
       10    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 skill.py:204(_get_hit_type)
        3    0.000    0.000    0.000    0.000 entity.py:84(<listcomp>)
        3    0.000    0.000    0.000    0.000 component.py:31(__init__)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:45(process_judgements)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        6    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
        6    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
        3    0.000    0.000    0.000    0.000 component.py:133(__init__)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        8    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        1    0.000    0.000    0.000    0.000 ui_handler.py:28(__init__)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        3    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        3    0.000    0.000    0.000    0.000 component.py:64(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:34(__init__)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:24(__init__)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        3    0.000    0.000    0.000    0.000 component.py:56(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        4    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        4    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        6    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        4    0.000    0.000    0.000    0.000 world.py:326(<genexpr>)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        2    0.000    0.000    0.000    0.000 component.py:73(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        1    0.000    0.000    0.000    0.000 ecs.py:233(delete_entity)
        6    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        1    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        1    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        2    0.000    0.000    0.000    0.000 component.py:118(__init__)
        1    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
        2    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        1    0.000    0.000    0.000    0.000 component.py:176(__init__)
        1    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        6    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
        1    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
        2    0.000    0.000    0.000    0.000 component.py:92(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        2    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        1    0.000    0.000    0.000    0.000 component.py:199(__init__)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:65(__init__)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        2    0.000    0.000    0.000    0.000 component.py:101(__init__)
        2    0.000    0.000    0.000    0.000 component.py:110(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        2    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 basic_attack.py:14(use)


