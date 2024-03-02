from StudentClass import Student

def main():
    # Creating a student object
    student1 = Student(student_id="892657017", name="Aiden Murphy", dob="2003-02-16", classification="Jr")

    # Displaying student information
    print(f"Student ID: {student1.student_id}")
    print(f"Name: {student1.name}")
    print(f"{student1.get_age()}")
    print(f"{student1.get_registration_dates()}")

if __name__ == "__main__":
    main()