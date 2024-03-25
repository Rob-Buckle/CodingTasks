# Program asking user to enter a number
# When user enters -1 the program stops asking for a new number
# The program then calculates the average of all the numbers entered excluding -1
# Makes use of While loop

# Created a count to use later to work out the average of all the numbers entered by user
total = 0
count = 0

# Request user to enter a number and display
# While not -1 continue to request a new number
while True:
    number_entered = input("Please enter a number or -1 to exit:")

    # Break in code to stop while look once it returns value of false or -1
# Using strip function to remove any blank spaces
    if number_entered.strip() == "-1":
        break

# Converting all other numbers entered by user to an int
    total += int(number_entered)
    count += 1 

# Displays the average of all numbers entered, excluding -1
print(f"The average of all the numbers entered is: {total/count}")

