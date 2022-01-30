# contributed by @maracoo
def flatten(lst):
     for elem in lst:
         if isinstance(elem, list):
             yield from flatten(elem)
         else:
             yield elem

def ubc(out, head, *tail):
    return list(flatten([(*out, x) for x in head]) if len(tail) == 0 else flatten([ubc((*out, x), *tail) for x in head]))