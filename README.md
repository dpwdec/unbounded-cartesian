# Unbounded Cartesian

Creates an unbounded cartesian product of a list of N lists recursively.

Equivalent to
```python
for x in xs:
    for y in ys:
        for z in zs:
            ...
            for n in ns:
                (x, y, z, ..., n)
```