from enum import Enum, auto

TILE_SIZE = 64
ICON_IN_TEXT_SIZE = 16


class VisualInfo:
    """
    Constant info about visual aspects such as resolution and frame rate
    """
    # TODO -  should this be in game manager?
    BASE_WINDOW_WIDTH = 1280
    BASE_WINDOW_HEIGHT = 720
    GAME_FPS = 60
    ENTITY_SPRITE_FRAME_DURATION = 0.05  # seconds


class FOVInfo:
    """
    Constant info about the FOV settings
    """
    LIGHT_WALLS = True
    FOV_ALGORITHM = 0


class RenderOrder(Enum):
    """
    Render order for sprites
    """
    BACKGROUND = 0
    TERRAIN = 1
    ENTITY = 2
    ASPECT = 3
    TEXT = 99


class GameStates(Enum):
    """
    States the Game can be in.
    """
    PLAYER_TURN = auto()
    ENEMY_TURN = auto()
    PLAYER_DEAD = auto()
    TARGETING_MODE = auto()
    EXIT_GAME = auto()
    GAME_INITIALISING = auto()
    NEW_TURN = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class EventTopics(Enum):
    """
    Topics that Events can be associated with.
    """
    GAME = auto()
    MESSAGE = auto()
    ENTITY = auto()
    UI = auto()
    MAP = auto()


class GameEventTypes(Enum):
    """Types of Game Events"""
    EXIT = auto()  # go back a step / exit current focus
    END_TURN = auto()  # end of turn
    CHANGE_GAME_STATE = auto()  # move from one game state to another
    END_ROUND = auto()  # end of round

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class MessageEventTypes(Enum):
    """Types of Message Events"""
    BASIC = auto()
    SYSTEM = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class EntityEventTypes(Enum):
    """Types of Entity Events"""
    DIE = auto()
    SKILL = auto()
    MOVE = auto()
    LEARN = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class UIEventTypes(Enum):
    """
    Types of UI events
    """
    CLICK_UI = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class MapEventTypes(Enum):
    """
    Types of Map events
    """
    TILE_INTERACTION = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class TargetTags(Enum):
    """
    Types of target
    """
    SELF = auto()
    OTHER_ENTITY = auto()
    NO_ENTITY = auto()
    OUT_OF_BOUNDS = auto()
    ANY = auto()

    # TODO - externalise terrain types
    FLOOR = auto()
    WALL = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class DamageTypes(Enum):
    """
    Damage types
    """
    BURN = auto()
    CHEMICAL = auto()
    ASTRAL = auto()
    COLD = auto()
    MUNDANE = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class StatTypes(Enum):
    """
    Primary stats
    """
    PRIMARY = auto()
    SECONDARY = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class PrimaryStatTypes(Enum):
    """
    Primary stats
    """
    VIGOUR = auto()
    CLOUT = auto()
    SKULLDUGGERY = auto()
    BUSTLE = auto()
    EXACTITUDE = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class SecondaryStatTypes(Enum):
    """
    Secondary stats
    """
    MAX_HP = auto()
    MAX_STAMINA = auto()
    HP = auto()
    STAMINA = auto()
    ACCURACY = auto()
    RESIST_BURN = auto()
    RESIST_CHEMICAL = auto()
    RESIST_ASTRAL = auto()
    RESIST_COLD = auto()
    RESIST_MUNDANE = auto()
    SIGHT_RANGE = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class HitTypes(Enum):
    """
    The value of each hit type. The value is the starting amount.
    """
    GRAZE = auto()
    HIT = auto()
    CRIT = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class HitValues(Enum):
    """
    The value of each hit type. The value is the starting amount.
    """
    # TODO - externalise the values
    GRAZE = 0
    HIT = 5
    CRIT = 20


class HitModifiers(Enum):
    """
    The modifier for each hit type
    """
    GRAZE = 0.6
    HIT = 1
    CRIT = 1.4


class EffectTypes(Enum):
    """
    Types of effects
    """
    APPLY_AFFLICTION = auto()
    DAMAGE = auto()
    MOVE = auto()
    CHANGE_TERRAIN = auto()
    AFFECT_STAT = auto()
    ADD_ASPECT = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class AfflictionCategory(Enum):
    """
    Boon or Bane
    """
    BANE = auto()
    BOON = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class AfflictionTriggers(Enum):
    """
    When to trigger the afflictions
    """
    PASSIVE = auto()  # always applying effects, overrides duration
    END_TURN = auto()  # apply at end of round turn
    MOVE = auto()  # apply if afflicted entity moves
    ACTION = auto()  # apply when an action is taken

    # Other triggers to consider
    # DEAL_DAMAGE = auto()  # apply if afflicted entity deals damage
    # TAKE_DAMAGE = auto()  # apply if afflicted entity receives damage
    # USE_BURN = auto()  # apply if afflicted entity uses a burn type - etc.
    # DEATH = auto()  # apply if afflicted entity dies

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class AfflictionLifespan(Enum):
    """
    Identify if the affliction duration should be reduced or not
    """
    PERMANENT = 999

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class SkillShapes(Enum):
    """
    When to trigger the afflictions
    """
    TARGET = auto()  # single target
    SQUARE = auto()
    CIRCLE = auto()
    CROSS = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class InputModes(Enum):
    MOUSE_AND_KB = auto()
    GAMEPAD = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class MouseButtons(Enum):
    LEFT_BUTTON = auto()
    RIGHT_BUTTON = auto()
    MIDDLE_BUTTON = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None


class UIElementTypes(Enum):
    """
    The different UI elements
    """
    MESSAGE_LOG = auto()
    ENTITY_INFO = auto()
    TARGETING_OVERLAY = auto()
    SKILL_BAR = auto()
    ENTITY_QUEUE = auto()
    CAMERA = auto()

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.value == other.value
        return NotImplemented

    __hash__ = None
