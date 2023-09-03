import tkinter as tk
import sqlite3
import random

def create_table():
    # Connect to the database
    conn = sqlite3.connect("batch_assessment.db")
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS batch_assessment_details
                      (batch_id INTEGER , batch_name TEXT, course_code TEXT,
                      course_name TEXT, eligible_candidates INTEGER, exam_date_theory TEXT,
                      exam_date_practical TEXT, theory_examiner TEXT, practical_examiner TEXT,
                      candidates_present INTEGER, candidates_absent INTEGER, mode_of_assessment TEXT,
                      exam_type TEXT)''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def generate_dummy_data():
    # Connect to the database
    conn = sqlite3.connect("batch_assessment.db")
    cursor = conn.cursor()

    for _ in range(100):
        # Generate random data
        batch_id = random.randint(1, 1000)
        batch_name = random.choice(batch_names)
        course_code = random.choice(course_codes)
        course_name = random.choice(course_names)
        eligible_candidates = random.randint(1, 50)
        exam_date_theory = generate_random_date()
        exam_date_practical = generate_random_date()
        theory_examiner = random.choice(examiner_names)
        practical_examiner = random.choice(examiner_names)
        candidates_present = random.randint(1, eligible_candidates)
        candidates_absent = eligible_candidates - candidates_present
        mode_of_assessment = random.choice(modes_of_assessment)
        exam_type = random.choice(exam_types)

        # Insert the data into the table
        cursor.execute('''INSERT INTO batch_assessment_details (batch_id, batch_name, course_code,
                          course_name, eligible_candidates, exam_date_theory, exam_date_practical,
                          theory_examiner, practical_examiner, candidates_present, candidates_absent,
                          mode_of_assessment, exam_type)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (batch_id, batch_name, course_code, course_name, eligible_candidates,
                        exam_date_theory, exam_date_practical, theory_examiner, practical_examiner,
                        candidates_present, candidates_absent, mode_of_assessment, exam_type))

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
    conn = sqlite3.connect("batch_assessment.db")
    cursor = conn.cursor()

    # Retrieve data from the table
    cursor.execute("SELECT * FROM batch_assessment_details")
    data = cursor.fetchall()

    # Update the table display
    for widget in table.winfo_children():
        widget.destroy()

    # Create the table headings
    headings = ["Batch ID", "Batch Name", "Course Code", "Course Name", "Eligible Candidates",
                "Exam Date (Theory)", "Exam Date (Practical)", "Theory Examiner", "Practical Examiner",
                "Candidates Present", "Candidates Absent", "Mode of Assessment", "Exam Type"]
    for i, heading in enumerate(headings):
        tk.Label(table, text=heading, relief=tk.RIDGE, width=13,bg="lightgreen").grid(row=0, column=i)

    # Insert data into the table
    for row_num, row_data in enumerate(data, start=1):
        for col_num, cell_data in enumerate(row_data):
            tk.Label(table, text=cell_data, relief=tk.RIDGE, width=13,bg="lightblue").grid(row=row_num, column=col_num)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

batch_names=["batch 1","batch 2","batch 3","batch 4","batch 5"]
course_codes=["18CS201J","18CS202J","18CS203J","18CS204J","18CS205J"]
course_names=["Math", "Science", "English", "Hindi", "French"]
examiner_names=["Matt Davis","Michael Johnson","Jason P","Percy Jackson","Tania Gulati"]
modes_of_assessment=["Online","Offline"]
exam_types=["Written","Oral","Practical"]

# Create the table if it doesn't exist
create_table()

# Generate dummy data for batch assessment details
generate_dummy_data()

# Create a tkinter window
window = tk.Tk()
window.title("Batch Assessment Details")

# Create a table using tkinter
table = tk.Frame(window)
table.pack()

# Display the table
display_table()

# Run the tkinter event loop
window.mainloop()
