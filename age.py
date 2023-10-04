import datetime

def calculate_age(year_of_birth):
    current_year = datetime.datetime.now().year
    age_in_2023 = 2023 - year_of_birth
    return age_in_2023

def main():
    try:
        year_of_birth = int(input("Enter the year you were born: "))
        age_in_2023 = calculate_age(year_of_birth)

        if age_in_2023 >= 0:
            print(f"In 2023, you will be {age_in_2023} years old.")
        else:
            print("Please enter a valid year of birth.")

    except ValueError:
        print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    main()
#This program defines a calculate_age function to calculate the age in 2023 based on the provided year of birth. The main function takes user input for the year of birth, calls calculate_age to determine the age, and then prints the calculated age in 2023. If the user enters an invalid year (not a number), it will display an error message.





