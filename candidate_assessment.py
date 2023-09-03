import tkinter as tk
import sqlite3
import random

def create_table():
    # Connect to the database
    conn = sqlite3.connect("candidate_assessment.db")
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS candidate_assessment_details
                      (candidate_id INTEGER , candidate_name TEXT, batch_id INTEGER,
                      course_code TEXT, course_name TEXT, exam_type TEXT, exam_date TEXT,
                      mode_of_exam TEXT, marks_scored_theory INTEGER, marks_scored_practical INTEGER,
                      result TEXT)''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def generate_dummy_data():
    # Connect to the database
    conn = sqlite3.connect("candidate_assessment.db")
    cursor = conn.cursor()

    for _ in range(100):
        # Generate random data
        candidate_id = random.randint(1, 1000)
        candidate_name = random.choice(candidate_names)
        batch_id = random.randint(1, 100)
        course_code = random.choice(course_codes)
        course_name = random.choice(course_names)
        exam_type = random.choice(exam_types)
        exam_date = generate_random_date()
        mode_of_exam = random.choice(modes_of_exam)
        marks_scored_theory = random.randint(0, 100)
        marks_scored_practical = random.randint(0, 100)
        result = random.choice(results)

        # Insert the data into the table
        cursor.execute('''INSERT INTO candidate_assessment_details (candidate_id, candidate_name, batch_id,
                          course_code, course_name, exam_type, exam_date, mode_of_exam,
                          marks_scored_theory, marks_scored_practical, result)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (candidate_id, candidate_name, batch_id, course_code, course_name,
                        exam_type, exam_date, mode_of_exam, marks_scored_theory,
                        marks_scored_practical, result))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def generate_random_date():
    # Generate a random date in the format "YYYY-MM-DD"
    year = random.randint(2000, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year:04d}-{month:02d}-{day:02d}"

def display_table():
    # Connect to the database
    conn = sqlite3.connect("candidate_assessment.db")
    cursor = conn.cursor()

    # Retrieve data from the table
    cursor.execute("SELECT * FROM candidate_assessment_details")
    data = cursor.fetchall()

    # Update the table display
    for widget in table.winfo_children():
        widget.destroy()

    # Create the table headings
    headings = ["Candidate ID", "Candidate Name", "Batch ID", "Course Code", "Course Name",
                "Exam Type", "Exam Date", "Mode of Exam", "Marks Scored (Theory)",
                "Marks Scored (Practical)", "Result"]
    for i, heading in enumerate(headings):
        tk.Label(table, text=heading, relief=tk.RIDGE, width=16,bg="lightgreen").grid(row=0, column=i)

    # Insert data into the table
    for row_num, row_data in enumerate(data, start=1):
        for col_num, cell_data in enumerate(row_data):
            tk.Label(table, text=cell_data, relief=tk.RIDGE, width=16,bg="lightblue").grid(row=row_num, column=col_num)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Create the table if it doesn't exist
create_table()

# Generate dummy data for candidate assessment details
candidate_names = ["John Doe", "Jane Smith", "David Johnson", "Emily Davis"]
course_codes =["18CS201J","18CS202J","18CS203J","18CS204J","18CS205J"]
course_names =["Math", "Science", "English", "Hindi", "French"]
exam_types = ["Written", "Oral", "Practical"]
modes_of_exam = ["Online", "Offline"]
results = ["Pass", "Fail"]

generate_dummy_data()

# Create a tkinter window
window = tk.Tk()
window.title("Candidate Assessment Details")

# Create a table using tkinter
table = tk.Frame(window)
table.pack()

# Display the table
display_table()

# Run the tkinter event loop
window.mainloop()
