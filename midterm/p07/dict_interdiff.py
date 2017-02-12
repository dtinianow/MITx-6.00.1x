def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}
    diff = {}
    keys = []

    for key in d1.keys():
        keys.append(key)

    for key in d2.keys():
        keys.append(key)

    all_keys = list(set(keys))

    for key in all_keys:
        if key in d1 and key in d2:
            # f(a,b) function was built into exam grader
            # It calculates an operation on a and b, such '+' or '>'
            intersect[key] = f(d1[key], d2[key])
        else:
            if key in d1:
                diff[key] = d1[key]
            else:
                diff[key] = d2[key]

    return (intersect, diff)
