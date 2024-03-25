while True:
    number_of_students = input("Please enter the number of students to be registed: ")
# Added in error handling, to confirm user has entered a number
    try:
        number_of_students = int(number_of_students)
    except ValueError:
        print("Please enter a valid number.")
        continue

# Display back to user number of students to be registered, asking for confirmation
    print("You entered:", number_of_students)
    answer_confirm = input("Is this correct? Please type 'Yes' or 'No': ")

    if answer_confirm.lower().strip() == "yes":
        count = 0
        while count < number_of_students:
            student_name = input("Please enter the name of student to be registered: ")
            student_id = input("Now enter their id number: ")
            count += 1
            with open("reg_form.txt", "a") as file:
# Txt file created and information generated storing the student's names and id
                file.write(f"Name: {student_name}\nID: {student_id}\n\n{'-' * 40}\n")
        break  
    elif answer_confirm.lower().strip() == "no":
        continue
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

# Now that the number of students is confirmed, register the students
    count = 0

    while count <= number_of_students:
            student_name = input("Please enter the name of the student you would like to register: ")
            student_id = input("Now enter their id number: ")


   