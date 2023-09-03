import tkinter as tk
import sqlite3
import random

def create_table():
    # Connect to the database
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS candidate_attendance
                      (attendance_id INTEGER , candidate_id INTEGER, 
                      candidate_name TEXT, batch_id INTEGER, center_id INTEGER, center_name TEXT,
                      address TEXT, date TEXT, in_time TEXT, out_time TEXT, attendance_status TEXT)''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def generate_dummy_data():
    # Connect to the database
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    for _ in range(100):
        # Generate random data
        candidate_id = random.randint(1, 10000)
        candidate_name = random.choice(candidate_names)
        batch_id = random.randint(1, 100)
        center_id = random.randint(1, 5)
        center_name = random.choice(center_names)
        address = random.choice(addresses)
        date = f"{random.randint(1, 28):02d}-{random.randint(1, 12):02d}-2023"
        in_time = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
        out_time = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
        attendance_status = random.choice(["Present", "Absent"])

        # Insert the data into the table
        cursor.execute('''INSERT INTO candidate_attendance (candidate_id, candidate_name, batch_id,
                          center_id, center_name, address, date, in_time, out_time, attendance_status)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (candidate_id, candidate_name, batch_id, center_id, center_name,
                        address, date, in_time, out_time, attendance_status))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def display_table():
    # Connect to the database
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # Retrieve data from the table
    cursor.execute("SELECT * FROM candidate_attendance")
    data = cursor.fetchall()

    # Update the table display
    for widget in table.winfo_children():
        widget.destroy()

    # Create the table headings
    headings = ["Candidate ID", "Candidate Name", "Batch ID", "Center ID", "Center Name",
                "Address", "Date", "In Time", "Out Time", "Attendance Status"]

    for i, heading in enumerate(headings):
        tk.Label(table, text=heading, relief=tk.RIDGE, width=15,bg="lightgreen").grid(row=0, column=i)

    # Insert data into the table
    for row_num, row_data in enumerate(data, start=1):
        for col_num, cell_data in enumerate(row_data):
            tk.Label(table, text=cell_data, relief=tk.RIDGE, width=15,bg="lightblue").grid(row=row_num, column=col_num)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Define the dummy data lists
candidate_names = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Brown", "David Davis"]
center_names = ["Center 1", "Center 2", "Center 3", "Center 4", "Center 5"]
addresses = ["123 Main St", "456 Elm St", "789 Oak St", "321 Pine St", "654 Maple St"]

# Create the table if it doesn't exist
create_table()

# Generate dummy data for candidate attendances
generate_dummy_data()

# Create a tkinter window
window = tk.Tk()
window.title("Candidate Attendance")

# Create a table using tkinter
table = tk.Frame(window)
table.pack()

# Display the table
display_table()

# Run the tkinter event loop
window.mainloop()
