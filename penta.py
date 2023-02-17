# all pieces

from itertools import product
from malib import exact_cover


def norm2(tile):
    """normalized orientation of tile"""
    minx = min(x for x, _ in tile)
    miny = min(y for _, y in tile)
    return tuple(sorted((x - minx, y - miny) for x, y in tile))


def coordinates(tile):
    """return letter and coordinates of tile"""
    ans = []
    for i, l in enumerate(tile.split("\n")):
        for j, c in enumerate(l):
            if c != " ":
                ans.append((i, j))
                letter = c
    return letter, norm2(ans)


def rotations2(tile):
    """return all 2d rotations of tile"""
    l = [tuple(tile)]
    l += [norm2([(x, -y) for x, y in tile]) for tile in l]
    l += [norm2([(-x, y) for x, y in tile]) for tile in l]
    l += [norm2([(y, x) for x, y in tile]) for tile in l]
    return list(set(l))


def all_rotations(tile):
    """return all 3d rotations of tile"""
    rots = rotations2(tile)
    return list(
        set(
            [tuple((x, y, 0) for x, y in rot) for rot in rots]
            + [tuple((x, 0, y) for x, y in rot) for rot in rots]
            + [tuple((0, x, y) for x, y in rot) for rot in rots]
        )
    )


def gen_shape(name):
    if name == "rectangle":
        return set(product(range(1), range(6), range(10)))
    if name == "cube":
        return set(product(range(3), range(4), range(5)))
    if name == "pyramid":
        pyramid = set()
        for z in range(5):
            for x in range(5 - z):
                for y in range(5 - z):
                    pyramid.add((x, y, z))
        return pyramid


def bounds(shape):
    return (
        max(x for x, _, _ in shape) + 1,
        max(y for _, y, _ in shape) + 1,
        max(z for _, _, z in shape) + 1,
    )


def all_shifts(shape, tile):
    """return all shifts of tile that fit in shape"""
    ans = []
    dims = bounds(shape)
    for dx in range(dims[0]):
        for dy in range(dims[1]):
            for dz in range(dims[2]):
                t = [(x + dx, y + dy, z + dz) for x, y, z in tile]
                if shape.issuperset(t):
                    ans.append(t)
    return ans


def prepare(shape, tiles):

    piece_to_constraints = {}

    for letter, tile in tiles:
        for rot in all_rotations(tile):
            for shift in all_shifts(shape, rot):
                piece = tuple(shift + [letter])
                piece_to_constraints[piece] = piece
    return piece_to_constraints


def to_grid(sol):
    dims = [0, 0, 0]
    for *coords, letter in sol:
        for c in coords:
            for i in range(3):
                dims[i] = max(dims[i], c[i] + 1)

    pic = [
        [[" " for _ in range(dims[2])] for _ in range(dims[1])] for _ in range(dims[0])
    ]
    for *coords, letter in sol:
        for x, y, z in coords:
            pic[x][y][z] = letter
    return pic


def display(sol):
    grid = to_grid(sol)
    for a in grid:
        for b in a:
            print("".join(b))
        print()


PENTAMINOS = list(
    map(
        coordinates,
        """
    ff
    ff
    f

    w
    ww
    ww

    iiiii

    y
    yy
    y
    y

    vvv
    v
    v

    ll
    l
    l
    l

    pp
    pp
    p

    n
    nn
    n
    n

    uu
    u
    uu

    zz
    z
    zz

    t
    ttt
    t

    x
    xxx
    x
    """.split(
            "\n\n"
        ),
    )
)


if __name__ == "__main__":
    piece_to_constraints = prepare(gen_shape("cube"), PENTAMINOS)
    sol = next(exact_cover(piece_to_constraints))
    display(sol)
