import tkinter as tk
import sqlite3
import random

def create_table():
    # Connect to the database
    conn = sqlite3.connect("candidate.db")
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS candidate_batch
                      (candidate_id INTEGER , aadhar_no INTEGER, name TEXT,
                      email TEXT, center_id INTEGER, center_name TEXT, center_address TEXT,
                      contact_no TEXT, state TEXT, city TEXT, batch_id INTEGER, course_name TEXT,
                      start_date TEXT, end_date TEXT)''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def generate_dummy_data():
    # Connect to the database
    conn = sqlite3.connect("candidate.db")
    cursor = conn.cursor()

    for _ in range(100):
        # Generate random data
        candidate_id = random.randint(2000, 3000)
        aadhar_no = random.randint(600000000000, 899999999999)
        name = random.choice(candidate_names)
        email = f"{name.lower().replace(' ', '')}@example.com"
        center_id = random.randint(1, 5)
        center_name = random.choice(center_names)
        center_address = random.choice(addresses)
        contact_no = f"91{random.randint(6000000000, 8999999999)}"
        state = random.choice(states)
        city = random.choice(cities)
        batch_id = random.randint(1, 100)
        course_name = random.choice(course_names)
        start_date = f"{random.randint(1, 28):02d}-{random.randint(1, 12):02d}-2023"
        end_date = f"{random.randint(1, 28):02d}-{random.randint(1, 12):02d}-2024"

        # Insert the data into the table
        cursor.execute('''INSERT INTO candidate_batch (candidate_id, aadhar_no, name, email,
                          center_id, center_name, center_address, contact_no, state, city,
                          batch_id, course_name, start_date, end_date)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (candidate_id, aadhar_no, name, email, center_id, center_name,
                        center_address, contact_no, state, city, batch_id, course_name,
                        start_date, end_date))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def display_table():
    # Connect to the database
    conn = sqlite3.connect("candidate.db")
    cursor = conn.cursor()

    # Retrieve data from the table
    cursor.execute("SELECT * FROM candidate_batch")
    data = cursor.fetchall()

    # Update the table display
    for widget in table.winfo_children():
        widget.destroy()

    # Create the table headings
    headings = ["Candidate ID", "Aadhar No.", "Name", "Email", "Center ID", "Center Name",
                "Center Address", "Contact No.", "State", "City", "Batch ID", "Course Name",
                "Start Date", "End Date"]
    for i, heading in enumerate(headings):
        tk.Label(table, text=heading, relief=tk.RIDGE, width=12,bg="lightgreen").grid(row=0, column=i)

    # Insert data into the table
    for row_num, row_data in enumerate(data, start=1):
        for col_num, cell_data in enumerate(row_data):
            tk.Label(table, text=cell_data, relief=tk.RIDGE, width=12,bg="lightblue").grid(row=row_num, column=col_num)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Define the dummy data lists
candidate_names = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Brown", "David Davis"]
center_names = ["Center 1", "Center 2", "Center 3", "Center 4", "Center 5"]
addresses = ["123 Elm St", "456 Main St", "789 Oak St", "321 Pine St", "654 Maple St"]
states = ["State A", "State B", "State C", "State D", "State E"]
cities = ["City A", "City B", "City C", "City D", "City E"]
course_names = ["Math", "Science", "English", "Hindi", "French"]

# Create the table if it doesn't exist
create_table()

# Generate dummy data for candidates
generate_dummy_data()

# Create a tkinter window
window = tk.Tk()
window.title("Candidate Batch")

# Create a table using tkinter
table = tk.Frame(window)
table.pack()

# Display the table
display_table()

# Run the tkinter event loop
window.mainloop()
