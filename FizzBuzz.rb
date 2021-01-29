#!/usr/bin/ruby
def check_divisibility(dividend, divisor)
    return dividend % divisor == 0
end
def fizz_buzz(n, max)
  until n == max
    n += 1
    if check_divisibility(n,15)
      puts "FizzBuzz"
    elsif check_divisibility(n,3)
      puts "Fizz"
    elsif check_divisibility(n, 5)
      puts "Buzz"
    else
      puts n
    end
  end
end
fizz_buzz 0, 100


