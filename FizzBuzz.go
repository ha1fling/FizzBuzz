package main
import "fmt"
func main() {
	for n := 1; n < 101; n++ {
		if CheckDivisibility(n, 15) {
			fmt.Println("FizzBuzz")
		} else if CheckDivisibility(n, 3) {
			fmt.Println("Fizz")
		} else if CheckDivisibility(n, 5) {
			fmt.Println("Buzz")
		} else {
			fmt.Println(n)
		}
	}
}

func CheckDivisibility(dividend int, divisor int) bool {
	return dividend % divisor == 0
}
