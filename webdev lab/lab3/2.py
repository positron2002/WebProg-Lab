class Student:
    def __init__(self, name, roll_no, department, address, gender, marks):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.address = address
        self.gender = gender
        self.marks = marks
        self.total_marks = sum(marks)
        self.percentage = self.total_marks / len(marks)

def get_student_details():
    name = input("Enter Name: ")
    roll_no = input("Enter Roll No: ")
    department = input("Enter Department: ")
    address = input("Enter Address: ")
    gender = input("Enter Gender: ")
    marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]
    return Student(name, roll_no, department, address, gender, marks)

def display_student_details(student):
    print(f"\nStudent Details:\nName: {student.name}\nRoll No: {student.roll_no}\nDepartment: {student.department}\nAddress: {student.address}\nGender: {student.gender}\nTotal Marks: {student.total_marks}\nPercentage: {student.percentage:.2f}%")

def main():
    students = []
    n = int(input("Enter the number of students: "))
    for _ in range(n):
        students.append(get_student_details())

    for student in students:
        display_student_details(student)

    max_marks_student = max(students, key=lambda s: s.total_marks)
    min_marks_student = min(students, key=lambda s: s.total_marks)
    fail_students = [student.name for student in students if any(mark < 10 for mark in student.marks)]

    print(f"\nStudent with Maximum Marks: {max_marks_student.name}")
    print(f"Student with Minimum Marks: {min_marks_student.name}")
    if fail_students:
        print(f"Students who failed (marks < 10): {', '.join(fail_students)}")
    else:
        print("No students failed.")

if __name__ == "__main__":
    main()
