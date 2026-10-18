import math
import random
from .buildings import MIN_SPACING, block_houses, CURB_GAP, HOUSE_DEPTH


def rotate_point(x, y, angle_rad, cx=0.0, cy=0.0):
    """Rotate (x, y) around center (cx, cy) by angle_rad."""
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    dx = x - cx
    dy = y - cy
    rx = dx * cos_a - dy * sin_a + cx
    ry = dx * sin_a + dy * cos_a + cy
    return rx, ry


def generate_city_grid(blocks_x, blocks_y, block_size, road_width, spacing, seed=42, min_floors=1, max_floors=4, angle_deg=0.0):
    """Generates orthogonal or angled grid city layouts."""
    rng = random.Random(seed)
    spacing = max(spacing, MIN_SPACING)
    pitch = block_size + road_width
    total_x = blocks_x * pitch
    total_y = blocks_y * pitch
    center_x = total_x / 2.0
    center_y = total_y / 2.0
    angle_rad = math.radians(angle_deg)

    raw_roads = []
    for i in range(blocks_x + 1):
        raw_roads.append(((i * pitch, total_y / 2.0, 0.0), (road_width, total_y + road_width), 0.0))

    for j in range(blocks_y + 1):
        for i in range(blocks_x):
            raw_roads.append(((i * pitch + pitch / 2.0, j * pitch, 0.0), (block_size, road_width), 0.0))

    raw_houses = []
    for i in range(blocks_x):
        for j in range(blocks_y):
            x0 = i * pitch + road_width / 2.0
            y0 = j * pitch + road_width / 2.0
            raw_houses += block_houses(x0, y0, x0 + block_size, y0 + block_size, spacing, rng, min_floors, max_floors)

    if abs(angle_deg) < 1e-4:
        return {"roads": raw_roads, "houses": raw_houses}

    rotated_roads = []
    for (rx, ry, rz), size, rot in raw_roads:
        nx, ny = rotate_point(rx, ry, angle_rad, center_x, center_y)
        rotated_roads.append(((nx, ny, rz), size, rot + angle_rad))

    rotated_houses = []
    for (hx, hy, hz), hrot, floors in raw_houses:
        nx, ny = rotate_point(hx, hy, angle_rad, center_x, center_y)
        rotated_houses.append(((nx, ny, hz), hrot + angle_rad, floors))

    return {"roads": rotated_roads, "houses": rotated_houses}


def generate_city_radial(ring_count, ring_radius, avenues_count, road_width, spacing, seed=42, min_floors=1, max_floors=4):
    """Generates curved concentric ring roads and radial avenues."""
    rng = random.Random(seed)
    spacing = max(spacing, MIN_SPACING)
    roads = []
    houses = []

    def _rand_floors():
        return rng.randint(min(min_floors, max_floors), max(min_floors, max_floors))

    max_radius = (ring_count + 1) * ring_radius
    avenue_step = (2 * math.pi) / avenues_count

    for a_idx in range(avenues_count):
        theta = a_idx * avenue_step
        cx = (max_radius / 2.0) * math.cos(theta)
        cy = (max_radius / 2.0) * math.sin(theta)
        roads.append(((cx, cy, 0.0), (max_radius, road_width), theta))

    inset = CURB_GAP + HOUSE_DEPTH / 2.0

    for r_idx in range(1, ring_count + 1):
        radius = r_idx * ring_radius
        circumference = 2 * math.pi * radius
        num_segments = max(16, int(circumference / 10.0))
        seg_angle = (2 * math.pi) / num_segments
        chord_len = 2.0 * radius * math.sin(seg_angle / 2.0) * 1.05

        for s in range(num_segments):
            mid_theta = (s + 0.5) * seg_angle
            cx = radius * math.cos(mid_theta)
            cy = radius * math.sin(mid_theta)
            tangent_rot = mid_theta + math.pi / 2.0
            roads.append(((cx, cy, 0.0), (chord_len, road_width), tangent_rot))

        r_outer = radius + road_width / 2.0 + inset
        num_outer = max(4, int((2 * math.pi * r_outer) / spacing))
        for h in range(num_outer):
            ang = h * (2 * math.pi / num_outer)
            hx = r_outer * math.cos(ang)
            hy = r_outer * math.sin(ang)
            houses.append(((hx, hy, 0.0), ang + math.pi, _rand_floors()))

        r_inner = radius - road_width / 2.0 - inset
        if r_inner > 8.0:
            num_inner = max(3, int((2 * math.pi * r_inner) / spacing))
            for h in range(num_inner):
                ang = h * (2 * math.pi / num_inner)
                hx = r_inner * math.cos(ang)
                hy = r_inner * math.sin(ang)
                houses.append(((hx, hy, 0.0), ang, _rand_floors()))

    return {"roads": roads, "houses": houses}

