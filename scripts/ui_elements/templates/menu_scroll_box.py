import glooey
import pyglet


class MenuScrollBox(glooey.ScrollBox):
    custom_alignment = 'center'

    class Frame(glooey.Frame):
        class Decoration(glooey.Background):
            custom_color = '#eeeeec'
            custom_top = pyglet.resource.texture("ui/horizontal.png")
            custom_bottom = pyglet.resource.texture("ui/horizontal.png")
            custom_left = pyglet.resource.texture("ui/vertical.png")

        class Box(glooey.Bin):
            custom_horz_padding = 2

    class VBar(glooey.VScrollBar):
        custom_scale_grip = True

        class Decoration(glooey.Background):
            custom_vert_padding = 25
            custom_color = 'green'

        class Forward(glooey.Button):
            custom_size_hint = 20, 20
            custom_base_color = 'purple'

        class Backward(glooey.Button):
            custom_size_hint = 20, 20
            custom_base_color = 'purple'

        class Grip(glooey.Button):
            custom_size_hint = 20, 20
            custom_alignment = 'fill'
            custom_base_color = 'orange'
#
# class MenuScrollBox(glooey.ScrollBox):
#
#     custom_alignment = 'center'
#
#     class Frame(glooey.Frame):
#
#         class Decoration(glooey.Background):
#             custom_color = '#eeeeec'
#
#             # custom_center = pyglet.resource.texture("ui/bg.png")
#             # custom_top = pyglet.resource.texture("ui/horizontal.png")
#             # custom_bottom = pyglet.resource.texture("ui/horizontal.png")
#             # custom_left = pyglet.resource.texture("ui/vertical.png")
#             # custom_right = pyglet.resource.texture("ui/vertical.png")
#             # custom_top_left = pyglet.resource.image("ui/top_left.png")
#             # custom_top_right = pyglet.resource.image("ui/top_right.png")
#             # custom_bottom_left = pyglet.resource.image("ui/bottom_left.png")
#             # custom_bottom_right = pyglet.resource.image("ui/bottom_right.png")
#
#         class Box(glooey.Bin):
#             custom_horz_padding = 2
#
#     class VBar(glooey.VScrollBar):
#         custom_scale_grip = True
#
#         class Decoration(glooey.Background):
#             custom_vert_padding = 25
#
#         class Forward(glooey.Button):
#             custom_color = '#babdb6'
#
#         class Backward(glooey.Button):
#             custom_color = '#babdb6'
#
#         class Grip(glooey.Button):
#             custom_height_hint = 20
#             custom_alignment = 'fill'