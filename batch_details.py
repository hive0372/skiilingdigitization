import tkinter as tk
import sqlite3
import random

def create_table():
    # Connect to the database
    conn = sqlite3.connect("batches.db")
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS batch_details
                      (batch_id INTEGER , start_date TEXT, end_date TEXT,
                      address TEXT, start_time TEXT, end_time TEXT, total_duration INTEGER,
                      mentor_id INTEGER, mentor_name TEXT, course_code TEXT, course_name TEXT,
                      num_candidates INTEGER, center_id INTEGER, center_name TEXT)''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def generate_dummy_data():
    # Connect to the database
    conn = sqlite3.connect("batches.db")
    cursor = conn.cursor()

    for _ in range(100):
        # Generate random data
        batch_id = random.randint(1, 100)
        start_date = f"{random.randint(1, 28):02d}-{random.randint(1, 12):02d}-2023"
        end_date = f"{random.randint(1, 28):02d}-{random.randint(1, 12):02d}-2024"
        address = random.choice(addresses)
        start_time = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
        end_time = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
        total_duration = random.randint(1, 10)
        mentor_id = random.randint(1, 1000)
        mentor_name = random.choice(mentor_names)
        course_code = random.choice(course_codes)
        course_name = random.choice(course_names)
        num_candidates = random.randint(10, 30)
        center_id = random.randint(1, 5)
        center_name = random.choice(center_names)

        # Insert the data into the table
        cursor.execute('''INSERT INTO batch_details (batch_id, start_date, end_date, address, start_time,
                          end_time, total_duration, mentor_id, mentor_name, course_code, course_name,
                          num_candidates, center_id, center_name)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (batch_id, start_date, end_date, address, start_time, end_time, total_duration,
                        mentor_id, mentor_name, course_code, course_name, num_candidates, center_id, center_name))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def display_table():
    # Connect to the database
    conn = sqlite3.connect("batches.db")
    cursor = conn.cursor()

    # Retrieve data from the table
    cursor.execute("SELECT * FROM batch_details")
    data = cursor.fetchall()

    # Update the table display
    for widget in table.winfo_children():
        widget.destroy()

    # Create the table headings
    headings = ["Batch ID", "Start Date", "End Date", "Address", "Start Time", "End Time",
                "Total Duration", "Mentor ID", "Mentor Name", "Course Code", "Course Name",
                "Num Candidates", "Center ID", "Center Name"]
    for i, heading in enumerate(headings):
        tk.Label(table, text=heading, relief=tk.RIDGE, width=12,bg="lightgreen").grid(row=0, column=i)

    # Insert data into the table
    for row_num, row_data in enumerate(data, start=1):
        for col_num, cell_data in enumerate(row_data):
            tk.Label(table, text=cell_data, relief=tk.RIDGE, width=12,bg="lightblue").grid(row=row_num, column=col_num)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

mentor_names = ["Johny Walker", "Damian Smith", "Mike Johnson", "Emma Brown", "Croma Davis"]
center_names = ["Center 1", "Center 2", "Center 3", "Center 4", "Center 5"]
addresses=["123 Main St", "456 Elm St", "789 Oak St", "321 Pine St", "654 Maple St"]
course_codes=["18CS201J","18CS202J","18CS203J","18CS204J","18CS205J"]
course_names=["Math", "Science", "English", "Hindi", "French"]

# Create the table if it doesn't exist
create_table()

# Generate dummy data for batch details
generate_dummy_data()

# Create a tkinter window
window = tk.Tk()
window.title("Batch Details")

# Create a table using tkinter
table = tk.Frame(window)
table.pack()

# Display the table
display_table()

# Run the tkinter event loop
window.mainloop()
