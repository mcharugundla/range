def range_num(mini,maxi,num):
    '''(number,number,number) -> bool
    Returns the bool value by checking whether the given number
    is between the given range of min and max values.

    >>>range_num(6,9,8)
    True
    >>>range_num(-23,-45,-24)
    True

    '''
    return num > mini and num < maxi
print (range_num(6,9,8))
print (range_num(-23,-45,-24))    
