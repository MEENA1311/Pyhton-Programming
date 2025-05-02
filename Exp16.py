def fun1(*numbers):
    last = numbers[-1]
    divisors = [i for i in range(1, last + 1) if last % i == 0]
    print("Divisors of", last, "are:", divisors)

fun1(3, 6, 12, 15, 20)
