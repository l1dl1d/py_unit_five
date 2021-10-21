def fibonacci(a):
    """
    Ex. fibonacci(5) returns "1 1 2 3 5 "
    :param number: The number of Fibonacci terms to return
    :return: A string consisting of a number of terms of the Fibonacci sequence.
    """
    a = 0
    b = 1
    test = "0 1 "
    for x in range(0, 4):
        c = a + b
        a = b
        b = c
        test += str(c) + " "
    return test
print(fibonacci(9))