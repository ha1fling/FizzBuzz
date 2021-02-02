<?php
class FizzBuzz {
    public function printFizzBuzz()
    {
        for ($n = 1; $n <= 100; $n++) {
            if ($this->checkDivisibility($n, 15)) {
                echo("FizzBuzz");
            } elseif ($this->checkDivisibility($n, 3)) {
                echo("Fizz");
            } elseif ($this->checkDivisibility($n, 5)) {
                echo("Buzz");
            } else {
                echo $n;
            }
        }
    }
    public function checkDivisibility($dividend, $divisor)
    {
        return $dividend % $divisor == 0;
    }
}
$fizzBuzz = new FizzBuzz();
$fizzBuzz -> printFizzBuzz();

















