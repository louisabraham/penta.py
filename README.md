# Penta.py


Simple pentomino and polycubes solver in python. It uses the exact cover algorithm from [malib](https://github.com/louisabraham/malib/) to find all solutions.

## Usage

```py
from penta import gen_shape, prepare, PENTAMINOS, exact_cover, display

shape = gen_shape("cube")
piece_to_constraints = prepare(shape, PENTAMINOS)
sol = next(exact_cover(piece_to_constraints))
display(sol)
```

```
YYYYT
FYZZW
IIIII
VLLLL

FPTTT
FPXZW
FXXXW
VLXNN

FPUUT
VPUZZ
VPUUW
VNNNW
```

You can also get the output as an array with `to_grid(sol)`:

```
[[['Y', 'Y', 'Y', 'Y', 'T'],
  ['F', 'Y', 'Z', 'Z', 'W'],
  ['I', 'I', 'I', 'I', 'I'],
  ['V', 'L', 'L', 'L', 'L']],
 [['F', 'P', 'T', 'T', 'T'],
  ['F', 'P', 'X', 'Z', 'W'],
  ['F', 'X', 'X', 'X', 'W'],
  ['V', 'L', 'X', 'N', 'N']],
 [['F', 'P', 'U', 'U', 'T'],
  ['V', 'P', 'U', 'Z', 'Z'],
  ['V', 'P', 'U', 'U', 'W'],
  ['V', 'N', 'N', 'N', 'W']]]
```

## Hackability

`shape` must be set can be changed to any set of 3D coordinates. `PENTAMINOS` can be changed to any list of 2D tiles.

For instance, the `F` tile is represented with `('F', ((0, 1), (0, 2), (1, 0), (1, 1), (2, 1)))`.
