def mro(the_cls):
    """
    my mro takes in a class as an argument
    """
    if the_cls is object:

        # if class is object
        return [object]
    else:
        # be recursive

        return [the_cls] + merge([mro(base) for base in the_cls.__bases__])


def merge(mros):

    if not any(mros):
        # if mro is an empty list
        return []
    for current, *_ in mros:
        # *_ takes other values after first as a variable
        if all(current not in tail for _, *tail in mros):
            return [current] + merge(
                [tail if head is current else [head, *tail] for head, *tail in mros]
            )

        # if i've gone through every item in list
    else:
        raise TypeError("class heiracy not legal")



