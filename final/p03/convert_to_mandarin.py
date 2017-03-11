def convert_to_mandarin(number):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
             '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    mandarin = []

    if len(number) is 1:
        mandarin.append(trans[number])
    elif number[0] is '1':
        mandarin.append(trans['10'])
    else:
        mandarin.append(trans[number[0]])
        mandarin.append(trans['10'])

    for digit in number[1:]:
        if digit is not '0':
            mandarin.append(trans[digit])

    return " ".join(mandarin)
