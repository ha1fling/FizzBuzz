using System.IO;
using System;
class FizzBuzz {
    static void Main(string[] args) {
        for (int n =1; n< 101; n++){
            if (CheckDivisibility(n, 15)) {
                Console.WriteLine("FizzBuzz");
            } else if (CheckDivisibility(n, 3)) {
                Console.WriteLine("Fizz");
            } else if (CheckDivisibility(n, 5)) {
                Console.WriteLine("Buzz");
            } else{
                Console.WriteLine(n);
            }
        }
    }
    static bool CheckDivisibility(int dividend, int divisor) {
        return dividend % divisor == 0;
    }
}


