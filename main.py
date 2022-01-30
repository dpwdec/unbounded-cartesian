def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])

def ubc(out, arr):
    head, *tail = arr
    if len(tail) == 0:
        return flatten([(*out, x) for x in head])
    else:
        return flatten([ubc((*out, x), tail) for x in head])