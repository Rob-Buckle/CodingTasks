class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        if self.age >= 18:
            print(f"{self.name} is old enough to drive.")
        else:
            print(f"{self.name} is not old enough to drive.")


class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive.")


if __name__ == "__main__":
    # Taking user input for person's details
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    hair_colour = input("Enter hair colour: ")
    eye_colour = input("Enter eye colour: ")

# Logic to determine whether to instantiate Adult or Child object
    if age >= 18:
        person = Adult(name, age, hair_colour, eye_colour)
    else:
        person = Child(name, age, hair_colour, eye_colour)

# Calling can_drive method to print whether person is old enough to drive
    person.can_drive()