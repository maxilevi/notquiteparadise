Search.setIndex({docnames:["core","event_handlers","events","index","managers","skills","ui_elements","world"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.cpp":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.intersphinx":1,"sphinx.ext.todo":1,"sphinx.ext.viewcode":1,sphinx:56},filenames:["core.rst","event_handlers.rst","events.rst","index.rst","managers.rst","skills.rst","ui_elements.rst","world.rst"],objects:{"scripts.core":{constants:[0,0,0,"-"],library_of_alexandria:[0,0,0,"-"]},"scripts.core.constants":{AfflictionCategory:[0,1,1,""],AfflictionLifespan:[0,1,1,""],AfflictionTriggers:[0,1,1,""],DamageTypes:[0,1,1,""],EffectTypes:[0,1,1,""],EntityEventTypes:[0,1,1,""],EventTopics:[0,1,1,""],FOVInfo:[0,1,1,""],GameEventTypes:[0,1,1,""],GameStates:[0,1,1,""],HitModifiers:[0,1,1,""],HitTypes:[0,1,1,""],HitValues:[0,1,1,""],InputModes:[0,1,1,""],MapEventTypes:[0,1,1,""],MessageEventTypes:[0,1,1,""],MouseButtons:[0,1,1,""],PrimaryStatTypes:[0,1,1,""],SecondaryStatTypes:[0,1,1,""],SkillShapes:[0,1,1,""],StatTypes:[0,1,1,""],TargetTags:[0,1,1,""],UIEventTypes:[0,1,1,""],VisualInfo:[0,1,1,""]},"scripts.core.library_of_alexandria":{LibraryOfAlexandria:[0,1,1,""]},"scripts.core.library_of_alexandria.LibraryOfAlexandria":{convert_afflictions_to_data_classes:[0,2,1,""],convert_aspects_to_data_classes:[0,2,1,""],convert_external_strings_to_internal_enums:[0,2,1,""],convert_gods_to_data_classes:[0,2,1,""],convert_homelands_to_data_classes:[0,2,1,""],convert_races_to_data_classes:[0,2,1,""],convert_savvys_to_data_classes:[0,2,1,""],convert_stats_to_data_classes:[0,2,1,""],get_actor_template_data:[0,2,1,""],get_affliction_data:[0,2,1,""],get_affliction_effect_data:[0,2,1,""],get_aspect_data:[0,2,1,""],get_aspect_effect_data:[0,2,1,""],get_god_attitudes_data:[0,2,1,""],get_god_data:[0,2,1,""],get_god_intervention_data:[0,2,1,""],get_god_intervention_effect_data:[0,2,1,""],get_god_intervention_effects_data:[0,2,1,""],get_god_interventions_data:[0,2,1,""],get_homeland_data:[0,2,1,""],get_primary_stat_data:[0,2,1,""],get_race_data:[0,2,1,""],get_savvy_data:[0,2,1,""],get_secondary_stat_data:[0,2,1,""],get_skill_data:[0,2,1,""],get_skill_effect_data:[0,2,1,""],get_terrain_data:[0,2,1,""],load_data_into_library:[0,2,1,""],load_values_from_actor_json:[0,3,1,""],load_values_from_affliction_json:[0,3,1,""],load_values_from_aspect_json:[0,3,1,""],load_values_from_gods_json:[0,3,1,""],load_values_from_homeland_json:[0,3,1,""],load_values_from_race_json:[0,3,1,""],load_values_from_savvy_json:[0,3,1,""],load_values_from_stat_json:[0,3,1,""],load_values_from_terrain_json:[0,3,1,""],recursive_replace:[0,2,1,""],refresh_library_data:[0,2,1,""]},"scripts.event_handlers":{pub_sub_hub:[1,0,0,"-"]},"scripts.events":{entity_events:[2,0,0,"-"],game_events:[2,0,0,"-"],message_events:[2,0,0,"-"],ui_events:[2,0,0,"-"]},"scripts.events.entity_events":{LearnEvent:[2,1,1,""],MoveEvent:[2,1,1,""],UseSkillEvent:[2,1,1,""]},"scripts.events.entity_events.MoveEvent":{__init__:[2,2,1,""]},"scripts.events.game_events":{ChangeGameStateEvent:[2,1,1,""],EndRoundEvent:[2,1,1,""],EndTurnEvent:[2,1,1,""],ExitGameEvent:[2,1,1,""]},"scripts.events.ui_events":{ClickUIEvent:[2,1,1,""]},"scripts.managers.world_methods":{affliction_methods:[4,0,0,"-"],entity_methods:[4,0,0,"-"],fov_methods:[4,0,0,"-"],map_methods:[4,0,0,"-"],skill_methods:[4,0,0,"-"]},"scripts.managers.world_methods.affliction_methods":{AfflictionMethods:[4,1,1,""]},"scripts.managers.world_methods.affliction_methods.AfflictionMethods":{active_afflictions:[4,4,1,""],cleanse_expired_afflictions:[4,2,1,""],create_affliction:[4,3,1,""],create_effect:[4,2,1,""],expired_afflictions:[4,4,1,""],get_affliction_effects_for_entity:[4,2,1,""],get_affliction_for_entity:[4,2,1,""],get_afflictions_for_entity:[4,2,1,""],get_stat_change_from_afflictions_on_entity:[4,2,1,""],manager:[4,4,1,""],reduce_affliction_durations_on_entity:[4,2,1,""],register_active_affliction:[4,2,1,""],trigger_afflictions_on_entity:[4,2,1,""]},"scripts.managers.world_methods.entity_methods":{EntityMethods:[4,1,1,""]},"scripts.managers.world_methods.entity_methods.EntityMethods":{add_entity_to_central_list:[4,2,1,""],add_player_to_central_list:[4,2,1,""],create_actor_entity:[4,2,1,""],get_a_star_direction_between_entities:[4,3,1,""],get_all_entities:[4,2,1,""],get_blocking_entity_at_location:[4,2,1,""],get_chebyshev_distance_between_tiles:[4,3,1,""],get_direct_direction_between_entities:[4,2,1,""],get_entity_in_fov_at_tile:[4,2,1,""],get_euclidean_distance_between_entities:[4,3,1,""],get_player:[4,2,1,""],manager:[4,4,1,""],remove_entity:[4,2,1,""]},"scripts.managers.world_methods.fov_methods":{FOVMethods:[4,1,1,""]},"scripts.managers.world_methods.fov_methods.FOVMethods":{create_player_fov_map:[4,2,1,""],get_player_fov:[4,2,1,""],is_tile_in_fov:[4,2,1,""],recompute_player_fov:[4,2,1,""],set_player_fov_state:[4,2,1,""],update_tile_visibility:[4,2,1,""]},"scripts.managers.world_methods.map_methods":{MapMethods:[4,1,1,""]},"scripts.managers.world_methods.map_methods.MapMethods":{add_aspect_to_tile:[4,3,1,""],cleanse_expired_aspects:[4,3,1,""],convert_xy_to_tile:[4,3,1,""],create_game_map:[4,2,1,""],get_entity_on_tile:[4,3,1,""],get_game_map:[4,2,1,""],get_target_type_from_tile:[4,2,1,""],get_terrain_on_tile:[4,3,1,""],get_tile:[4,2,1,""],get_tiles:[4,2,1,""],is_tile_blocking_movement:[4,2,1,""],is_tile_blocking_sight:[4,2,1,""],is_tile_in_bounds:[4,2,1,""],is_tile_visible_to_player:[4,2,1,""],manager:[4,4,1,""],reduce_aspect_durations_on_tile:[4,3,1,""],remove_aspect_from_tile:[4,3,1,""],set_entity_on_tile:[4,3,1,""],set_terrain_on_tile:[4,3,1,""],tile_has_tag:[4,3,1,""],trigger_aspects_on_tile:[4,3,1,""]},"scripts.managers.world_methods.skill_methods":{SkillMethods:[4,1,1,""]},"scripts.managers.world_methods.skill_methods.SkillMethods":{calculate_to_hit_score:[4,3,1,""],can_afford_cost:[4,3,1,""],can_use_skill:[4,2,1,""],create_effect:[4,3,1,""],create_shape:[4,3,1,""],create_skill:[4,3,1,""],get_hit_type:[4,3,1,""],has_required_tags:[4,2,1,""],manager:[4,4,1,""],pay_resource_cost:[4,3,1,""]},"scripts.skills":{affliction:[5,0,0,"-"],skill:[5,0,0,"-"]},"scripts.skills.affliction":{Affliction:[5,1,1,""]},"scripts.skills.affliction.Affliction":{affected_entity:[5,4,1,""],affliction_category:[5,4,1,""],affliction_effects:[5,4,1,""],description:[5,4,1,""],duration:[5,4,1,""],icon:[5,4,1,""],name:[5,4,1,""],trigger:[5,2,1,""],trigger_event:[5,4,1,""]},"scripts.skills.skill":{Skill:[5,1,1,""]},"scripts.skills.skill.Skill":{name:[5,4,1,""],owner:[5,4,1,""],skill_tree_name:[5,4,1,""],use:[5,2,1,""]},"scripts.ui_elements":{colours:[6,0,0,"-"],entity_info:[6,0,0,"-"],message_log:[6,0,0,"-"],palette:[6,0,0,"-"],skill_bar:[6,0,0,"-"],targeting_overlay:[6,0,0,"-"]},"scripts.ui_elements.colours":{Colour:[6,1,1,""]},"scripts.ui_elements.colours.Colour":{ComplementColour:[6,1,1,""],PrimaryColour:[6,1,1,""],SecondaryColour:[6,1,1,""],TertiaryColour:[6,1,1,""],complement:[6,4,1,""],primary:[6,4,1,""],secondary:[6,4,1,""],tertiary:[6,4,1,""]},"scripts.ui_elements.colours.Colour.ComplementColour":{darker:[6,4,1,""],darkest:[6,4,1,""],lighter:[6,4,1,""],lightest:[6,4,1,""],neutral:[6,4,1,""]},"scripts.ui_elements.colours.Colour.PrimaryColour":{darker:[6,4,1,""],darkest:[6,4,1,""],lighter:[6,4,1,""],lightest:[6,4,1,""],neutral:[6,4,1,""]},"scripts.ui_elements.colours.Colour.SecondaryColour":{darker:[6,4,1,""],darkest:[6,4,1,""],lighter:[6,4,1,""],lightest:[6,4,1,""],neutral:[6,4,1,""]},"scripts.ui_elements.colours.Colour.TertiaryColour":{darker:[6,4,1,""],darkest:[6,4,1,""],lighter:[6,4,1,""],lightest:[6,4,1,""],neutral:[6,4,1,""]},"scripts.ui_elements.entity_info":{SelectedEntityInfo:[6,1,1,""]},"scripts.ui_elements.entity_info.SelectedEntityInfo":{draw:[6,2,1,""],set_selected_entity:[6,2,1,""],set_visibility:[6,2,1,""]},"scripts.ui_elements.message_log":{MessageLog:[6,1,1,""]},"scripts.ui_elements.message_log.MessageLog":{add_message:[6,2,1,""],displayed_hyperlinks:[6,4,1,""],draw:[6,2,1,""],expressions:[6,4,1,""],hyperlinks:[6,4,1,""],icons:[6,4,1,""],index_of_active_hyperlink:[6,4,1,""],initialise_icons:[6,2,1,""],initialise_keywords:[6,2,1,""],is_dirty:[6,4,1,""],message_list:[6,4,1,""],message_type_to_show:[6,4,1,""],palette:[6,4,1,""],parse_message_and_convert_to_surface:[6,2,1,""],process_message_command:[6,2,1,""],text_wrap_message:[6,2,1,""],update:[6,2,1,""]},"scripts.ui_elements.palette":{Palette:[6,1,1,""]},"scripts.ui_elements.palette.Palette":{EntityInfoPalette:[6,1,1,""],EntityQueuePalette:[6,1,1,""],GameMapPalette:[6,1,1,""],MessageLogPalette:[6,1,1,""],SkillBarPalette:[6,1,1,""],TargetingOverlayPalette:[6,1,1,""],debug_font_colour:[6,4,1,""],menu_background:[6,4,1,""]},"scripts.ui_elements.palette.Palette.GameMapPalette":{border:[6,4,1,""]},"scripts.ui_elements.palette.Palette.MessageLogPalette":{background:[6,4,1,""],expressions_player:[6,4,1,""],hyperlink:[6,4,1,""],text_default:[6,4,1,""],tooltip_background:[6,4,1,""],tooltip_text:[6,4,1,""]},"scripts.ui_elements.skill_bar":{SkillBar:[6,1,1,""]},"scripts.ui_elements.skill_bar.SkillBar":{draw:[6,2,1,""],get_skill_index_from_skill_clicked:[6,2,1,""],update_skill_icons_to_show:[6,2,1,""]},"scripts.ui_elements.targeting_overlay":{TargetingOverlay:[6,1,1,""]},"scripts.ui_elements.targeting_overlay.TargetingOverlay":{draw:[6,2,1,""],draw_effect_highlight:[6,2,1,""],draw_range_highlight:[6,2,1,""],draw_selected_tile:[6,2,1,""],set_selected_tile:[6,2,1,""],set_skill_being_targeted:[6,2,1,""],set_visibility:[6,2,1,""],skill_being_targeted:[6,4,1,""],update_tiles_in_range_and_fov:[6,2,1,""],update_tiles_in_skill_effect_range:[6,2,1,""]},"scripts.ui_elements.templates":{panel:[6,0,0,"-"],skill_container:[6,0,0,"-"]},"scripts.ui_elements.templates.panel":{Panel:[6,1,1,""]},"scripts.ui_elements.templates.panel.Panel":{border_colour:[6,4,1,""],border_size:[6,4,1,""],colour:[6,4,1,""],draw_background:[6,2,1,""],draw_border:[6,2,1,""],height:[6,4,1,""],width:[6,4,1,""],x:[6,4,1,""],y:[6,4,1,""]},"scripts.ui_elements.templates.skill_container":{SkillContainer:[6,1,1,""]},"scripts.ui_elements.templates.skill_container.SkillContainer":{draw_self_on_other_surface:[6,2,1,""],draw_skill_icon:[6,2,1,""],draw_skill_key:[6,2,1,""]},"scripts.world":{entity:[7,0,0,"-"],game_map:[7,0,0,"-"],tile:[7,0,0,"-"]},"scripts.world.entity":{Entity:[7,1,1,""]},"scripts.world.entity.Entity":{__init__:[7,2,1,""],animation_timer:[7,4,1,""],current_sprite:[7,4,1,""],current_sprite_frame:[7,4,1,""],delay_until_idle_animation:[7,4,1,""],sight_range:[7,4,1,""],x:[7,4,1,""],y:[7,4,1,""]},"scripts.world.game_map":{GameMap:[7,1,1,""]},"scripts.world.game_map.GameMap":{draw:[7,2,1,""]},"scripts.world.terrain":{floor:[7,0,0,"-"],terrain:[7,0,0,"-"],wall:[7,0,0,"-"]},"scripts.world.terrain.floor":{Floor:[7,1,1,""]},"scripts.world.terrain.terrain":{Terrain:[7,1,1,""]},"scripts.world.terrain.terrain.Terrain":{blocks_movement:[7,4,1,""],blocks_sight:[7,4,1,""],name:[7,4,1,""],owner:[7,4,1,""],sprite:[7,4,1,""],x:[7,4,1,""],y:[7,4,1,""]},"scripts.world.terrain.wall":{Wall:[7,1,1,""]},"scripts.world.tile":{Tile:[7,1,1,""]},"scripts.world.tile.Tile":{aspect:[7,4,1,""],blocks_movement:[7,4,1,""],blocks_sight:[7,4,1,""],draw:[7,2,1,""],entity:[7,4,1,""],has_entity:[7,4,1,""],is_floor:[7,4,1,""],is_visible:[7,4,1,""],is_wall:[7,4,1,""],terrain:[7,4,1,""],x:[7,4,1,""],y:[7,4,1,""]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","staticmethod","Python static method"],"4":["py","attribute","Python attribute"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:staticmethod","4":"py:attribute"},terms:{"break":6,"class":[0,2,4,5,6,7],"default":6,"enum":0,"float":[4,7],"function":6,"int":[2,4,5,6,7],"new":[2,4],"return":[0,4,6,7],"static":[0,4],"true":[4,7],The:[0,4,6,7],Use:[4,5],__init__:[2,7],abil:[2,7],about:0,accuraci:[],act:2,action:[2,4],activ:[4,5],active_afflict:4,active_ent:4,actor:[4,5,7],actor_nam:4,actor_templ:0,actor_template_nam:[0,4],add:[4,6],add_aspect_to_til:4,add_ent:[],add_entity_to_central_list:4,add_messag:6,add_play:[],add_player_to_central_list:4,addit:[],affect:4,affect_stat:[],affected_ent:[4,5],affectstatafflictioneffect:[],afflict:0,affliction_categori:5,affliction_dur:[],affliction_effect:5,affliction_effect_nam:[],affliction_exist:[],affliction_method:4,affliction_nam:[0,4,5],affliction_trigg:4,affliction_typ:[],afflictioncategori:[0,5],afflictiondata:0,afflictioneffect:5,afflictioneffecttyp:[],afflictionlifespan:0,afflictionmethod:4,afflictiontrigg:[0,4,5],afflictiontyp:[],afford:4,against:0,alexandria:[],all:[0,4,5,6],alreadi:4,amount:[0,4,5],ani:0,anim:7,animation_tim:7,anoth:[4,6],anyth:[0,7],appli:[4,6],applic:[5,7],apply_afflict:[],apply_damag:[],applyafflictionskilleffect:[],appropri:[],aspect:[0,4],aspect_nam:[0,4],aspect_str:[],aspectdata:0,aspecttyp:[],assign:4,associ:[0,6],attack:4,attacking_ent:[],attitud:0,attitudedata:0,attribut:[],aug:[],background:6,background_colour:6,bane:[0,5],bar:[],base:[4,6,7],basi:[],basic:2,been:[],befor:[4,5],being:5,block:[4,7],blocks_mov:7,blocks_sight:7,bog:[],bool:[4,6,7],boon:[0,5],border:6,border_colour:6,border_s:6,borders:6,both:4,build:[],build_new_turn_queu:[],button:[],button_press:2,calculate_damag:[],calculate_to_hit_scor:4,call:[],can:[0,4,7],can_afford_cost:4,can_use_skil:4,cancel:[],categori:[],caus:4,centr:0,central:[0,4],chang:[2,4,6],change_terrain:[],changegamestateev:2,changeterrainskilleffect:[],characteristicdata:0,check:[0,4,6,7],check_kb_directional_input:[],check_kb_general_input:[],check_kb_interaction_input:[],check_mouse_input:[],cleans:[],cleanse_expired_afflict:4,cleanse_expired_aspect:4,click:[2,6],clickuiev:2,collect:6,colour:[],combat:7,command:6,complement:6,complementcolour:6,compon:7,confirm:4,constant:[],contain:[4,7],control:7,convert:[0,4],convert_afflictions_to_data_class:0,convert_aspects_to_data_class:0,convert_external_strings_to_internal_enum:0,convert_gods_to_data_class:0,convert_homelands_to_data_class:0,convert_races_to_data_class:0,convert_savvys_to_data_class:0,convert_skills_to_data_class:[],convert_stats_to_data_class:0,convert_xy_to_til:4,coord:4,coordin:4,core:3,correct:6,cost:4,creat:4,create_actor_ent:4,create_affect_stat_effect:[],create_afflict:4,create_apply_affliction_effect:[],create_change_terrain_effect:[],create_damage_effect:[],create_effect:4,create_game_map:4,create_new_map:[],create_player_fov_map:4,create_shap:4,create_skil:4,current:[2,4,6,7],current_sprit:7,current_sprite_fram:7,damag:0,damage_typ:[],damageafflictioneffect:[],damageskilleffect:[],damagetyp:0,darker:6,darkest:6,data:0,dealt:[],debug:6,debug_act:[],debug_font_colour:6,debugmanag:[],decrement:5,defend:4,defending_ent:[],defin:6,delay_until_idle_anim:7,delayed_init:[],delet:4,depend:[],descript:5,detail:[],determin:[],dict:[0,6,7],dictat:[5,6],dictionari:[6,7],dir_i:[],dir_x:[],direct:4,dirti:4,displai:7,displayed_hyperlink:6,distanc:4,doe:7,doesnt:7,draw:[6,7],draw_background:6,draw_bord:6,draw_effect_highlight:6,draw_gam:[],draw_range_highlight:6,draw_selected_til:6,draw_self_on_other_surfac:6,draw_skill_icon:6,draw_skill_kei:6,due:[],durat:[0,4,5,7],each:[0,6],effect:[0,4,6,7],effect_nam:[],effect_typ:[0,4],effectdata:0,effecttyp:[0,4],either:5,element:3,els:[0,4,6],empti:4,end:[2,4,5],end_til:4,end_turn:[],endroundev:2,endturnev:2,ensur:6,entir:[],entiti:[0,5],entity_ev:2,entity_info:6,entity_method:4,entity_to_learn_skil:2,entity_to_mov:2,entity_using_skil:2,entityeventtyp:0,entityinfopalett:6,entitymethod:4,entityqueuepalett:6,enumer:0,etc:[],ether:4,event:[0,3,5],event_handl:[],eventtop:0,everi:7,except:5,exist:4,exit:2,exitgameev:2,expir:4,expired_afflict:4,expiri:[4,5],express:6,expressions_play:6,extend:7,extern:0,fals:4,far:7,fire:7,floor:[],focu:[],focused_window:[],font:6,format:6,found:4,fov:[0,7],fov_map:4,fov_method:4,fovinfo:0,fovmethod:4,frame:[0,7],from:[0,4,6],game:[0,6],game_ev:2,game_map:[4,7],gameeventtyp:0,gameloop:4,gamemanag:[],gamemap:[4,7],gamemappalett:6,gamest:0,gener:[],get:[0,4,6,7],get_a_star_direction_between_ent:4,get_actor_template_data:0,get_affliction_category_from_str:[],get_affliction_data:0,get_affliction_effect_data:0,get_affliction_effect_type_from_str:[],get_affliction_effects_for_ent:4,get_affliction_for_ent:4,get_affliction_nam:[],get_affliction_string_from_typ:[],get_affliction_type_for_ent:[],get_affliction_type_from_str:[],get_afflictions_for_ent:4,get_all_ent:4,get_aspect:[],get_aspect_data:0,get_aspect_effect_data:0,get_blocking_entity_at_loc:4,get_chebyshev_distance_between_ent:[],get_chebyshev_distance_between_til:4,get_clicked_panels_rect:[],get_damage_type_from_str:[],get_direct_direction_between_ent:4,get_entity_in_fov_at_til:4,get_entity_on_til:4,get_euclidean_distance_between_ent:4,get_game_map:4,get_god_attitudes_data:0,get_god_data:0,get_god_intervention_data:0,get_god_intervention_effect_data:0,get_god_intervention_effects_data:0,get_god_interventions_data:0,get_hit_typ:4,get_homeland_data:0,get_play:4,get_player_fov:4,get_pressed_direct:[],get_pressed_mouse_button:[],get_pressed_skill_numb:[],get_primary_stat_data:0,get_primary_stat_from_str:[],get_race_data:0,get_relative_scaled_mouse_po:[],get_savvy_data:0,get_scaled_mouse_po:[],get_secondary_stat_data:0,get_secondary_stat_from_str:[],get_skill_data:0,get_skill_effect_data:0,get_skill_effect_type_from_str:[],get_skill_index_from_skill_click:6,get_stat_change_from_afflictions_on_ent:4,get_stat_from_str:[],get_stat_modifier_from_afflictions_on_ent:[],get_target:[],get_target_tags_from_str:[],get_target_typ:[],get_target_type_from_str:[],get_target_type_from_til:4,get_terrain_data:0,get_terrain_on_til:4,get_til:4,get_trigger_event_from_str:[],get_values_from_actor_json:[],get_values_from_affliction_json:[],get_values_from_aspect_json:[],get_values_from_general_json:[],get_values_from_homeland_json:[],get_values_from_race_json:[],get_values_from_savvy_json:[],get_values_from_skill_json:[],get_values_from_terrain_json:[],give:[],given:4,god:0,god_nam:0,goddata:0,gradient:6,handl:6,handler:3,has:[4,7],has_ent:7,has_required_tag:4,height:[4,6,7],highlight:6,hit:[0,4],hit_typ:[],hitmodifi:0,hittyp:[0,4],hitvalu:0,hold:[4,6,7],holder:[],homeland:[0,7],homeland_nam:0,how:7,hub:[],hyperlink:6,icon:[5,6,7],identifi:0,idl:7,imag:[5,7],impact:5,includ:6,inclus:7,index:[3,6],index_of_active_hyperlink:6,info:[0,4],inform:6,init:[],init_entity_info:[],init_entity_queu:[],init_message_log:[],init_skill_bar:[],init_targeting_overlai:[],initialis:6,initialise_icon:6,initialise_keyword:6,input:[],input_valu:[],inputmanag:[],inputmod:0,intend:[],interact:[],intern:0,internal_clock:[],interpret:[],intervent:0,intervention_nam:0,interventiondata:0,is_dirti:6,is_floor:7,is_required_target_typ:[],is_tile_blocking_mov:4,is_tile_blocking_sight:4,is_tile_in_bound:4,is_tile_in_fov:4,is_tile_visible_to_play:4,is_vis:7,is_wal:7,its:5,json:0,jul:[],kei:[0,6],keyboard:[],keyword:6,knowledg:0,known:6,last:3,late:[],learn:2,learnev:2,librari:[],library_of_alexandria:0,libraryofalexandria:0,lighter:6,lightest:6,line:[4,6],link:6,list:[0,4,5,6,7],load:[0,6],load_data_into_librari:0,load_values_from_actor_json:0,load_values_from_affliction_json:0,load_values_from_aspect_json:0,load_values_from_gods_json:0,load_values_from_homeland_json:0,load_values_from_race_json:0,load_values_from_savvy_json:0,load_values_from_skill_json:[],load_values_from_stat_json:0,load_values_from_terrain_json:0,locat:4,log:[],loggingeventtyp:[],look:[0,6],main:6,main_surfac:[],make:6,manag:3,map:[0,6],map_method:4,mapeventtyp:0,mapmethod:4,menu:6,menu_background:6,messag:0,message_list:6,message_log:6,message_typ:6,message_type_to_show:6,messageeventtyp:[0,6],messagelog:6,messagelogpalett:6,method:[],mode:[],modifi:0,modified_dur:[],modul:3,mous:[],mouse_i:[],mouse_po:2,mouse_x:[],mousebutton:[0,2],move:[2,7],moveev:2,movement:[4,7],multipl:4,must:6,name:[0,5,7],nest:0,neutral:6,new_game_st:2,new_terrain:[],new_valu:0,newmessagelog:[],next:7,next_turn:[],non:4,none:[2,4,7],note:6,noth:[4,6],number:[0,7],obj:0,object:[0,4,7],one:[4,6],option:[],order:6,otherwis:4,out:[],overlai:[],owner:[4,5,7],page:3,pair:0,palett:[],panel:[],param:[4,6],paramet:[0,2,4,5,6,7],parse_message_and_convert_to_surfac:6,pathfind:4,pay_resource_cost:4,per:6,period:5,perman:[4,5],plai:7,player:[4,6,7],popul:[],posit:[4,6],possibl:6,prefix:6,press:[],primari:[0,4,6],primary_stat:[],primary_stat_typ:0,primarycolour:6,primarystatdata:0,primarystattyp:[0,4],proce:[],process:[2,6],process_generic_input:[],process_input:[],process_message_command:6,process_player_turn_input:[],process_targeting_mode_input:[],provid:[],pull:6,purpos:6,pygam:[5,6,7],queri:4,queue:6,race:[0,7],race_nam:0,racedata:[],radiu:4,rang:6,rate:0,recent:[],recompute_player_fov:4,rect:6,recursive_replac:0,reduc:[0,4,5],reduce_affliction_durations_on_ent:4,reduce_aspect_durations_on_til:4,ref:4,refresh_library_data:0,regist:4,register_active_afflict:4,rel:[],relat:[4,6],relative_i:6,relative_x:6,remov:4,remove_aspect_from_til:4,remove_aspect_on_til:[],remove_ent:4,remove_entity_on_til:[],remove_terrain_on_til:[],render:[],replac:0,request:4,requir:[4,6],required_tag:4,required_target_typ:[],reset:4,resolut:0,resourc:4,rgb:6,round:2,run:[],savvi:[0,7],savvy_nam:0,scale:[],score:4,screen:[],script:[0,2,4,5,6,7],search:3,second:7,secondari:[0,4,6],secondary_stat:[],secondary_stat_typ:0,secondarycolour:6,secondarystatdata:0,secondarystattyp:[0,4],section:6,see:7,select:6,selected_til:6,selectedentityinfo:6,self:[],sep:3,set:[0,4,6],set_aspect_on_til:[],set_entity_on_til:4,set_player_fov_st:4,set_selected_ent:6,set_selected_til:6,set_skill_being_target:6,set_terrain_on_til:4,set_vis:6,shape:4,should:0,show:6,shown:6,sight:[4,7],sight_rang:7,simplifi:[],size:4,skill:[0,2,3],skill_accuraci:4,skill_bar:6,skill_being_target:6,skill_contain:6,skill_effect:[],skill_effect_nam:[],skill_icon:6,skill_method:4,skill_nam:[0,2,4,5],skill_numb:6,skill_to_be_us:2,skill_tre:0,skill_tree_nam:[2,4,5],skillbar:6,skillbarpalett:6,skillcontain:6,skilldata:0,skilleffect:[],skilleffecttyp:[],skillmethod:4,skillshap:[0,4],smoke:7,sourc:[0,2,4,5,6,7],specif:6,specifi:[0,4,7],spent:[],spent_tim:[],sprite:7,spritesheet:7,stamina:4,start:[0,4],start_ent:4,start_til:4,start_tile_i:4,start_tile_x:4,stat:[0,4],stat_to_affect:[],stat_to_target:4,state:[0,2],stattyp:0,store:[0,6],str:[0,4,5,6,7],straight:4,string:[0,5,6],sub:[],success:4,suffix:6,surfac:[6,7],symbolis:5,tag:[4,7],take:[0,4],target:[0,4,5],target_ent:4,target_po:[2,4,5],target_tag:4,target_til:4,target_typ:[],targeting_overlai:6,targetingoverlai:6,targetingoverlaypalett:6,targettag:[0,4],targettyp:[],tcod:4,templat:4,terrain:[0,4],terrain_nam:0,terrain_to_chang:[],tertiari:6,tertiarycolour:6,text:6,text_default:6,text_wrap_messag:6,thei:4,them:0,thi:[0,4],those:6,through:0,tick:[],tile:[4,6],tile_has_tag:4,tile_i:[4,7],tile_x:[4,7],tiles_in_range_and_fov:6,tiles_in_skill_effect_rang:6,tiles_to_highlight:[],time:[],time_sp:2,to_hit_scor:4,tooltip:6,tooltip_background:6,tooltip_text:6,top:6,topic:0,toward:4,trade:[],trigger:[0,4,5],trigger_afflictions_on_ent:4,trigger_aspect_effect_on_til:[],trigger_aspects_on_til:4,trigger_ev:5,tupl:[0,2,4,5,6],turn:5,turnmanag:[],type:[0,4,5,6,7],ui_el:6,ui_ev:2,ui_object:[],uieventtyp:0,uimanag:[],under:4,until:7,updat:[3,4,6],update_debug_messag:[],update_game_st:[],update_input_valu:[],update_panel_vis:[],update_skill_icons_to_show:6,update_tile_vis:4,update_tiles_in_range_and_fov:6,update_tiles_in_skill_effect_rang:6,update_tiles_to_highlight:[],use:[4,5,6],used:[4,5],useskillev:2,using:4,utilis:0,valid:6,valu:[0,4,6],value_to_replac:0,variou:[],version:3,visibl:[4,6,7],visible_panel_nam:[],visual:0,visualinfo:0,wall:[],when:0,where:0,whether:[],which:[],width:[4,6,7],window:6,within:6,without:4,word:6,word_to_affect:6,work:[],world:[0,3],world_manag:4,world_method:4,worldmanag:4,wrap:6,wrapper:4},titles:["Core","Event Handlers","Events","Welcome to Not Quite Paradise\u2019s documentation!","Managers","Skills","UI Elements","World"],titleterms:{Not:3,affect:5,afflict:[4,5],alexandria:0,appli:5,aspect:7,bar:6,bog:7,chang:5,colour:6,constant:0,contain:6,content:[],core:0,damag:5,debug:4,document:3,effect:5,element:6,entiti:[1,2,4,6,7],event:[1,2],event_handl:[],floor:7,fov:4,game:[1,2,4,7],handler:1,hub:1,indic:3,info:6,input:4,librari:0,log:[1,2,6],manag:4,map:[4,7],messag:[1,2,6],method:4,overlai:6,palett:6,panel:6,paradis:3,quit:3,skill:[4,5,6],stat:5,tabl:3,target:6,templat:6,terrain:[5,7],tile:7,turn:4,ui_el:[],wall:7,welcom:3,world:[4,7]}})