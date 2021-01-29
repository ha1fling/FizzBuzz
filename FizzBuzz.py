def check_divisibility(dividend, divisor):
    return dividend % divisor == 0


def fizz_buzz(n, lower_range, upper_range):
    for n in range(lower_range, upper_range):
        if check_divisibility(n, 15):
            print("FizzBuzz")
        elif check_divisibility(n, 3):
            print("Fizz")
        elif check_divisibility(n, 5):
            print("Buzz")
        else:
            print(n)


fizz_buzz(1, 1, 101)









