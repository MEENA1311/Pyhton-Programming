n = int(input("Enter a number: "))
original = n
reversed_num = 0
if n < 0:
    print("Not a Palindrome")
else:
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    if original == reversed_num:
        print("Palindrome")
    else:
        print("Not a Palindrome")
