print("\nYou may enter any number including negatives.")

# define list for numbers to be added to for avg. calculation
number_list = []

# Create program that prompts user to input any numbers repeatedly
# Once -1 is entered, stop running and calculate avg. of all numbers excluding -1
# print average to user and end program run
while True:
    try:
        user_number = float(input("\nPlease enter a number: "))
        if user_number == -1:
            break
        number_list.append(user_number)
    except ValueError:
            print("Error: Please enter a valid number with no special characters.")
if number_list:
    average = sum(number_list) / len(number_list)
    print(f"\nThe average of the your entered numbers is: {average:.2f}")
else:
    print("\nNo valid numbers entered.")