import math
import random

HOUSE_WIDTH = 4.0    # along the edge it sits on
HOUSE_DEPTH = 4.0    # from road side toward block centre
CURB_GAP = 0.5       # empty space between road edge and house
MIN_SPACING = 5.0    # roof is 4.5 wide, so never closer than this


def along_edge(start, end, spacing):
    """1D helper: centres of evenly spread houses between start and end."""
    span = end - start
    if span < HOUSE_WIDTH:
        return []
    n = int((span - HOUSE_WIDTH) // spacing) + 1
    used = (n - 1) * spacing + HOUSE_WIDTH
    first = start + (span - used) / 2 + HOUSE_WIDTH / 2
    return [first + k * spacing for k in range(n)]


def block_houses(x0, y0, x1, y1, spacing, rng, min_floors, max_floors):
    """Houses around the 4 edges of one block, all facing outward to the road."""
    houses = []
    inset = CURB_GAP + HOUSE_DEPTH / 2

    def _rand_floors():
        return rng.randint(min(min_floors, max_floors), max(min_floors, max_floors))

    # South and north rows run the full block width
    for x in along_edge(x0, x1, spacing):
        houses.append(((x, y0 + inset, 0.0), math.pi, _rand_floors()))
        houses.append(((x, y1 - inset, 0.0), 0.0, _rand_floors()))

    # West and east rows fit between the south and north rows
    y_start = y0 + CURB_GAP + HOUSE_DEPTH + 0.5
    y_end = y1 - CURB_GAP - HOUSE_DEPTH - 0.5
    for y in along_edge(y_start, y_end, spacing):
        houses.append(((x0 + inset, y, 0.0), math.pi / 2, _rand_floors()))
        houses.append(((x1 - inset, y, 0.0), -math.pi / 2, _rand_floors()))
    return houses

