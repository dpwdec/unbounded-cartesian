# contributed by @maracoo
def flatten(lst):
     for elem in lst:
         if isinstance(elem, list):
             yield from flatten(elem)
         else:
             yield elem

def ubc(head, *tail, out = ()):
    return list(flatten([(*out, x) for x in head]) if len(tail) == 0 else flatten([ubc(*tail, out = (*out, x)) for x in head]))