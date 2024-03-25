class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

# Defining a method of displaying contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

# Defining a method of displaying the location
    def head_office_location(self):
        print("Head office location: Cape Town")

class OOPCourse(Course):
    def __init__(self, name, duration):
        super().__init__()
        self.name = name
        self.duration = duration
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

# Method to display the trainers details
    def trainer_details(self):
        print(f"Course: {self.description}")
        print(f"Trainer: {self.trainer}")

# Defining the student ID
    def show_course_id(self):
        print("Course ID: #12345")

if __name__ == "__main__":
    course_1 = OOPCourse("Python OOP", 6) #Creating an instance of OOPCourse
    course_1.contact_details()
    course_1.trainer_details()
    course_1.show_course_id()
# Call method from superclass
    course_1.head_office_location()