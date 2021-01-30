#!/usr/bin/env python3
# Module: FizzBuzz.py
#
# Write a program that prints the numbers from 1 to 100. But for multiples of 
# three print “Fizz” instead of the number and for the multiples of five print 
# “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz"

def check_divisibility(dividend, divisor):
    """ Checks whether a dividend is divsible by the divsor passed

    Args:
        dividend (int)
        divisor (int)

    Returns:
        bool
    """
    return dividend % divisor == 0

def fizz_buzz(lower_range, upper_range):
    """ FizzBuzz implementation

    Args:
        lower_range (int)
        upper_range (int)
    """
    for n in range(lower_range, upper_range):
        divisable_by_three = check_divisibility(n, 3)
        divisable_by_five = check_divisibility(n, 5)

        if divisable_by_three and divisable_by_five:
            yield "FizzBuzz"
        elif divisable_by_three:
            yield "Fizz"
        elif divisable_by_five:
            yield "Buzz"
        else:
            yield n

if __name__ == "__main__":
    for item in fizz_buzz(1, 101):
        print (item)