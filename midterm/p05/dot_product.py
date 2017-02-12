def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    dotProduct = []

    for index, value in enumerate(listA):
        dotProduct.append(value * listB[index])

    return sum(dotProduct)
