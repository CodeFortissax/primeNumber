# Import the functions from the other files
from oddnum import count_odd_numbers
from prime_number import count_primes


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    try:
        # Calculate and display the total number of odd numbers
        total_odd_numbers = count_odd_numbers()
        print("Total odd numbers between 1 and 1,000,000:", total_odd_numbers)

        # Calculate and display the total count of prime numbers
        total_primes = count_primes()
        print("Total prime numbers between 1 and 1,000,000:", total_primes)

        # Ask the user for input and check if it's prime
        user_input = int(input("Enter a number between 1 and 1,000,000: "))

        if 1 <= user_input <= 1000000:
            if is_prime(user_input):
                print(f"{user_input} is a prime number.")
            else:
                print(f"{user_input} is not a prime number.")
        else:
            print("Input is out of range (1 to 1,000,000).")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
