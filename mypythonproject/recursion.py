def sum_array(array):
    '''Return sum of all items in array'''
    sum = 0
    for item in array:
        sum+= item
    return sum



def fibonacci(number):
    """
    Return nth term in fibonacci sequence
    The Fibonacci sequence is characterized by the fact that every number
    after the first two is the sum of the two preceding ones
    """
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)


def factorial(n):
    '''Return n!'''
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def reverse(word):
    '''Return word in reverse'''
    return word[::-1]
