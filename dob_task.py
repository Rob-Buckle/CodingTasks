# Using file open to create DOB.txt file in same directory as dob_task
def process_dob_file(file_path):
    try:
       with open(file_path, 'r') as file:
            names = []
            dobs = []

# Splitting the line into components - to separate Names and Dates of birth
            for line in file:
                components = line.strip().split(' ')
           
                name_components = components[:2]
                dob_components = components[2:]

                name = ' '.join(name_components)
                dob = ' '.join(dob_components)

                names.append(name)
                dobs.append(dob)
# Print names
            print("\nName:")
            for name in names:
                print(name)

# Print date of birth
            print("\nDate of Birth:")
            for dob in dobs:
                print(dob)

# File error handling
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

# Full file pathway
file_path = r'C:\Users\robfr\Desktop\hyperion\Task 8 - File IO\DOB'
process_dob_file(file_path)
