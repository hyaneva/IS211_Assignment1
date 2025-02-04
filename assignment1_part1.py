
#2

def list_divide(numbers, divide = 2):
    some_list = []
    for x in numbers:
        if x % divide == 0:
            some_list.append(x)
    return len(some_list)





#3

class ListDivideException(Exception):
    pass





#4

def test_list_divide():
    if list_divide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException()

    if list_divide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException()

    if list_divide([30, 54, 63, 98, 100], divide=10) != 2:
        raise ListDivideException()
    
    if list_divide([]) != 0:
        raise ListDivideException()

    if list_divide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException()





test_list_divide()







