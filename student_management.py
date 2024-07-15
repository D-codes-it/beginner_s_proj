import time
#Classes available for selection stored in a dictionary
classes ={
    "Arts":  [] ,
    "Science": [],
    "Business": [],
}

#Taking student's information
def add_student():
    name = input("\nEnter student's name: ")
    age = input("Enter student's age: ")
    number = input("Enter student's number: ")

#Displaying the classes available to users
    print("\nSelect a class")
    print("1. Arts")
    print("2. Science")
    print("3. Business")

#User should enter number assigned to class
    class_choice = input("Enter class number: ")

#Depending on user choice of class number, display a class assigned that number
    if class_choice=='1':
        class_name = "Arts"
    elif class_choice=='2':
        class_name = "Science"
    elif class_choice=='3':
        class_name = "Business"
    else:
        print("Invalid input")

    #Creating student dictionary to store student information (a)
    student = {
        "Name": name,
        "Age": age,
        "Number": number
    }

#Assign student to class. and display the output. Stores individual student with assigned class in (a) and displays it
    classes[class_name].append(student)
    print(f"\nstudent {student['Name']} added to {class_name.capitalize()} class.")

#Displays total student information stored
def display_student():
    #for each class, print the students
    for class_name, students in classes.items():
        print(f"\n{class_name.capitalize()}")
        #print all students in student dictionary by the categories
        for student in students:
            print(f"Name: {student['Name']}, Age: {student['Age']}")

#main function that runs the program
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add student")
        print("2. Display all students")
        print("3. Exit")

        choice = input("\nWhat would you like to do?  ")
        if choice == '1':
         start_time = time.time()
         add_student()
         end_time = time.time()
         execution_time = end_time - start_time
         print(f"\nExecution time: {execution_time:.4f} seconds")
        elif choice == '2':
         display_student()
        elif choice == '3':
         break
        else:
            print("Invalid input. Try again")
if __name__ == "__main__":
    main()