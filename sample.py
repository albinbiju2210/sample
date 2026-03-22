import os

# ---------- Function to input student details ----------
def get_student_details():
    student = {}
    print("\n===== Enter Student Details =====")
    student['name']     = input("Enter Name       : ")
    student['roll_no']  = input("Enter Roll No    : ")
    student['age']      = input("Enter Age        : ")
    student['course']   = input("Enter Course     : ")
    student['marks']    = input("Enter Marks      : ")
    return student

# ---------- Function to save to file ----------
def save_to_file(student, filename="students.txt"):
    with open(filename, 'a') as f:
        f.write("=" * 35 + "\n")
        f.write(f"Name    : {student['name']}\n")
        f.write(f"Roll No : {student['roll_no']}\n")
        f.write(f"Age     : {student['age']}\n")
        f.write(f"Course  : {student['course']}\n")
        f.write(f"Marks   : {student['marks']}\n")
    print(f"\n✅ Student details saved to '{filename}' successfully!")

# ---------- Function to display all records from file ----------
def read_from_file(filename="students.txt"):
    print("\n===== All Student Records =====")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            if content.strip() == "":
                print("No records found.")
            else:
                print(content)
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist yet. Add a student first.")

# ---------- Function to display from dictionary ----------
def display_student(student):
    print("\n===== Student Details (from Dictionary) =====")
    for key, value in student.items():
        print(f"  {key.capitalize():10} : {value}")

# ---------- Function to delete the file ----------
def delete_file(filename="students.txt"):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\n🗑️  File '{filename}' deleted successfully.")
    else:
        print(f"\nFile '{filename}' not found.")

# ---------- Main Menu ----------
def main():
    students = {}   # dictionary to store multiple students

    while True:
        print("\n========== MENU ==========")
        print("1. Add Student")
        print("2. View All Records (from file)")
        print("3. Display Last Entered Student (from dictionary)")
        print("4. Delete File")
        print("5. Exit")
        print("==========================")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            student = get_student_details()
            roll = student['roll_no']
            students[roll] = student          # store in dictionary with roll no as key
            save_to_file(student)             # save to file

        elif choice == '2':
            read_from_file()

        elif choice == '3':
            if students:
                last_roll = list(students.keys())[-1]
                display_student(students[last_roll])
            else:
                print("\nNo student added yet.")

        elif choice == '4':
            delete_file()

        elif choice == '5':
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter 1-5.")

# ---------- Run ----------
main()
