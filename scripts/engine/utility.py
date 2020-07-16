from __future__ import annotations

import math
from typing import Any, List, TYPE_CHECKING, Tuple, Type

import pygame
import scipy
import logging

from scripts.engine.core.constants import IMAGE_NOT_FOUND_PATH, Shape, ShapeType, TILE_SIZE

if TYPE_CHECKING:
    from typing import Tuple


def get_image(img_path: str, desired_dimensions: Tuple[int, int] = None) -> pygame.Surface:
    """
    Get the specified image and resize if dimensions provided. Dimensions are in (width, height) format. If img
    path is "none" then a blank surface is created to the size of the desired dimensions, or TILE_SIZE if no
    dimensions provided.
    """
    # check if image path provided
    if img_path.lower() != "none":
        try:
            # try and get the image provided
            image = pygame.image.load(img_path).convert_alpha()

        except:
            image = pygame.image.load(IMAGE_NOT_FOUND_PATH).convert_alpha()
    else:
        image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        image.set_alpha(0)

    # resize if needed
    if desired_dimensions:
        width, height = desired_dimensions
        image = pygame.transform.smoothscale(image, (width, height))

    return image


def get_images(img_paths: List[str], desired_dimensions: Tuple[int, int] = None) -> List[pygame.Surface]:
    """
    Get a collection of images.
    """
    images = []

    for path in img_paths:
        images.append(get_image(path, desired_dimensions))

    return images


def flatten_images(images: List[pygame.Surface]) -> pygame.Surface:
    """
    Flatten a list of images into a single image. All images must be the same size. Images are blitted in order.
    """
    base = images.pop(0)

    for image in images:
        base.blit(image, (0, 0))

    return base


def recursive_replace(obj, key, value_to_replace, new_value):
    """
    Check through any number of nested dicts or lists for the specified key->value pair and replace the value.

    Args:
        obj (object): dict, list, string, or anything else to be checked.
        key (str): The key to look for in the object
        value_to_replace (): The value to look for, stored against the key.
        new_value (): The value to set.
    """
    if isinstance(obj, dict):
        # Break the dict out and run recursively against the elements
        for k, v in obj.items():
            if k == key:
                # The value may be a list so handle it if so
                if isinstance(v, list):
                    # Loop the list and replace the required value
                    for index, item in enumerate(v):
                        if item == value_to_replace:
                            v[index] = new_value
                elif v == value_to_replace:
                    obj[key] = new_value
            else:
                recursive_replace(v, key, value_to_replace, new_value)

    elif isinstance(obj, list):
        # Break the list out and run recursively against the elements
        for element in obj:
            recursive_replace(element, key, value_to_replace, new_value)


def get_class_members(cls: Type[Any]) -> List[str]:
    """
    Get a class' members, excluding special methods e.g. anything prefixed with '__'. Useful for use with dataclasses.
    """
    members = []

    for member in cls.__dict__.keys():
        if member[:2] != "__":
            members.append(member)

    return members


def lerp(initial_value: float, target_value: float, lerp_fraction: float) -> float:
    """
    Linear interpolation between initial and target by amount. Fraction clamped between 0 and 1.
    """
    clamped_lerp_fraction = clamp(lerp_fraction, 0, 1)

    if clamped_lerp_fraction >= 0.99:
        return target_value
    else:
        return initial_value * (1 - clamped_lerp_fraction) + target_value * clamped_lerp_fraction


def clamp(value, min_value, max_value):
    """
    Return the value, clamped between min and max.
    """
    return max(min_value, min(value, max_value))


def get_euclidean_distance(start_pos: Tuple[int, int], target_pos: Tuple[int, int]) -> float:
    """
    Get distance from an xy position towards another location. Expected tuple in the form of (x, y).
    This returns a float indicating the straight line distance between the two points.
    """
    dx = target_pos[0] - start_pos[0]
    dy = target_pos[1] - start_pos[1]
    return math.sqrt(dx ** 2 + dy ** 2)


def get_chebyshev_distance(start_pos: Tuple[int, int], target_pos: Tuple[int, int]):
    """
    Get distance from an xy position towards another location. Expected tuple in the form of (x, y).
    This returns an int indicating the number of tile moves between the two points.
    """
    # TODO - take chebyshev code from scipy and remove scipy
    return scipy.spatial.distance.chebyshev(start_pos, target_pos)


def _calculate_square_shape(size: int) -> List[Tuple[int, int]]:
    """
    Calculate all the tiles in the range of a square
    """
    coord_list = []
    width = size
    height = size

    for x in range(-width, width + 1):
        for y in range(-height, height + 1):
            coord_list.append((x, y))
    return coord_list


def _calculate_circle_shape(size: int) -> List[Tuple[int, int]]:
    """
    Calculate all the tiles in the range of a circle
    """
    coord_list = []
    radius = (size + size + 1) / 2

    for x in range(-size, size + 1):
        for y in range(-size, size + 1):
            if x * x + y * y < radius * radius:
                coord_list.append((x, y))

    return coord_list


def _calculate_cross_shape(size: int) -> List[Tuple[int, int]]:
    """
    Calculate all the tiles in the range of a cross
    """
    coord_list = [(0, 0)]
    x_coords = [-1, 1]

    for x in x_coords:
        for y in range(-size, size + 1):

            # ignore 0's to ensure no duplication when running through the range
            # the multiplication of x by y means they are always both 0 if y is
            if y != 0:
                coord_list.append((x * y, y))

    return coord_list


def get_coords_from_shape(shape: ShapeType, size: int, direction: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Get a list of coordinates from a shape, size and direction.
    """
    if shape == Shape.TARGET:
        return [(0, 0)]  # single target, centred on selection

    elif shape == Shape.SQUARE:
        return _calculate_square_shape(size)

    elif shape == Shape.CIRCLE:
        return _calculate_circle_shape(size)

    elif shape == Shape.CROSS:
        return _calculate_cross_shape(size)

    elif shape == Shape.CONE:
        return _calculate_cone_shape(size, direction)

    logging.error(f'Unknown shape "{shape}" passed to get_coords_from_shape')
    raise KeyError(f'Unknown shape "{shape}"')


def value_to_member(value: Any, cls: Type[Any]) -> str:
    """
    Get a member of a class that matches the value given
    """
    members = get_class_members(cls)

    for member in members:
        if getattr(cls, member) == value:
            return member

    return "No member with value found."


def convert_tile_string(tile_pos_string: str) -> Tuple[int, int]:
    """
    Convert a tile position string to (x, y)
    """
    _x, _y = tile_pos_string.split(",")
    x = int(_x)  # str to int
    y = int(_y)
    return x, y


def is_close(current_pos: Tuple[float, float], target_pos: Tuple[float, float], delta=0.05) -> bool:
    """
    returns true if the absolute distance between both coordinates is less than delta
    """
    return abs(current_pos[0] - target_pos[0]) <= delta and abs(current_pos[1] - target_pos[1]) <= delta


def is_coordinate_in_bounds(coordinate: float, bounds: Tuple[float, float], edge=0) -> bool:
    """
    check if a coordinate is inside a bound for a given edge
    """
    start_coordinate = bounds[0] + edge
    end_coordinate = bounds[1] - edge - 1
    within_bounds = start_coordinate <= coordinate < end_coordinate
    return within_bounds
