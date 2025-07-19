# task1_report_card.py

def get_student_data():
    """
    Asks the user to input student name and marks in 5 subjects.
    Returns the student name and a list of marks.
    """
    student_name = input("Enter student name: ")
    marks = []
    subjects = ["Math", "Science", "English", "History", "Computer Science"]
    print("Enter marks for the following 5 subjects (out of 100):")
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"{subject}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return student_name, marks

def calculate_report(marks):
    """
    Calculates total marks, percentage, and assigns a grade.
    Args:
        marks (list): A list of marks obtained in subjects.
    Returns:
        tuple: (total_marks, percentage, grade)
    """
    total_marks = sum(marks)
    percentage = (total_marks / (len(marks) * 100)) * 100

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    return total_marks, percentage, grade

def display_report_card(student_name, marks, total_marks, percentage, grade):
    """
    Displays the student's report card in a formatted way.
    """
    print("\n" + "="*40)
    print(f"{'Student Report Card':^40}")
    print("="*40)
    print(f"Student Name: {student_name}")
    print("-" * 40)
    
    subjects = ["Math", "Science", "English", "History", "Computer Science"]
    for i, mark in enumerate(marks):
        print(f"{subjects[i]:<20}: {mark:>5.2f}")
    
    print("-" * 40)
    print(f"Total Marks   : {total_marks:>5.2f} / {len(marks) * 100}")
    print(f"Percentage    : {percentage:>5.2f}%")
    print(f"Grade         : {grade}")
    print("="*40)

if __name__ == "__main__":
    name, student_marks = get_student_data()
    total, percent, final_grade = calculate_report(student_marks)
    display_report_card(name, student_marks, total, percent, final_grade)