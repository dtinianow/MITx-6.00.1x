def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """

    valuesToRemove = []

    for value in L:
        if not g(f(value)):
            valuesToRemove.append(value)

    for value in valuesToRemove:
        L.remove(value)

    if L:
        largestElement = max(L)
    else:
        largestElement = -1

    return largestElement
