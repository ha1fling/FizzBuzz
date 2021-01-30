public class Main {
    public static void main(String[] args) {
        for (int n =1; n< 101; n++){
            if (CheckDivisibility(n, 15)) {
                System.out.println("FizzBuzz");
            } else if (CheckDivisibility(n, 3)) {
                System.out.println("Fizz");
            } else if (CheckDivisibility(n, 5)) {
                System.out.println("Buzz");
            } else{
                System.out.println(n);
            }
        }
    }
    static Boolean CheckDivisibility(int dividend, int divisor) {
        return dividend % divisor == 0;
    }
}




