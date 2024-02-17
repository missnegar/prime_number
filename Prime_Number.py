def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True 

input_number = int(input("Enter a number: "))
if is_prime(input_number):
    print(input_number, "prime")
else:
    print(input_number, "not prime")