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
nnnnt
pvvvx
puyuz
yyyyz

pnttt
pvxxx
puuuz
iiiii

llllt
fvwlx
ffwwz
ffwwz
```

You can also get the output as an array with `to_grid(sol)`:

```
[[['n', 'n', 'n', 'n', 't'],
  ['p', 'v', 'v', 'v', 'x'],
  ['p', 'u', 'y', 'u', 'z'],
  ['y', 'y', 'y', 'y', 'z']],
 [['p', 'n', 't', 't', 't'],
  ['p', 'v', 'x', 'x', 'x'],
  ['p', 'u', 'u', 'u', 'z'],
  ['i', 'i', 'i', 'i', 'i']],
 [['l', 'l', 'l', 'l', 't'],
  ['f', 'v', 'w', 'l', 'x'],
  ['f', 'f', 'w', 'w', 'z'],
  ['f', 'f', 'w', 'w', 'z']]]
```

## Hackability

`shape` must be set can be changed to any set of 3D coordinates. `PENTAMINOS` can be changed to any list of 2D tiles.

For instance, the `f` tile is represented with `('f', ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0)))`.




