N = 1
for N in range(1, 101):
    print(N)

DivBy3 = False
DivBy6 = False
DivByBoth = False

#smaller number is divisor and larger number is dividend


def check_divisibility(dividend, divisor):
    divisible = False
    if dividend % divisor == 0:
        divisible = True
    print("Divisible by " + str(divisor) + " " + str(divisible))
    return divisible


check_divisibility(9, 3)
check_divisibility(10, 3)
check_divisibility(15, 5)
check_divisibility(16, 5)

