# Unbounded Cartesian

Creates an unbounded cartesian product of N lists of lists recursively.

Equivalent to
```python
for x in xs:
    for y in ys:
        for z in zs:
            ...
            for n in ns:
                (x, y, z, ..., n)
```