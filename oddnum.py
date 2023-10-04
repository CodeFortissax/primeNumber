# Function to count the number of odd numbers between 1 and 1,000,000
def count_odd_numbers():
    count = 0
    for number in range(1, 1000001):
        if number % 2 != 0:  # Check if the number is odd
            count += 1
    return count


# Main program
if __name__ == "__main__":
    try:
        # Calculate and display the total number of odd numbers
        total_odd_numbers = count_odd_numbers()
        print("Total odd numbers between 1 and 1,000,000:", total_odd_numbers)

        # Ask the user for input and check if it's odd
        user_input = int(input("Enter a number between 1 and 1,000,000: "))

        if 1 <= user_input <= 1000000:
            if user_input % 2 != 0:
                print(f"{user_input} is an odd number.")
            else:
                print(f"{user_input} is not an odd number.")
        else:
            print("Input is out of range (1 to 1,000,000).")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
