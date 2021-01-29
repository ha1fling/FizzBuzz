N = 1

for N in range(1, 101):

    def check_divisibility(dividend, divisor):
        divisible = False
        if dividend % divisor == 0:
            divisible = True
        return divisible


    if (check_divisibility(N, 3)) & (check_divisibility(N, 5)):
        print("FizzBuzz")
    elif check_divisibility(N, 3):
        print("Fizz")
    elif check_divisibility(N, 5):
        print("Buzz")
    else:
        print(N)



