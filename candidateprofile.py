import tkinter as tk
import sqlite3
import random

def create_table():
    # Connect to the database
    conn = sqlite3.connect("candidate_data.db")
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS candidates
                      (candidate_id INTEGER , aadhar_no INTEGER, name TEXT,
                      age INTEGER, dob TEXT, gender TEXT, father_name TEXT,
                      mother_name TEXT, education TEXT, contact_no TEXT, email TEXT,
                      center_id INTEGER, center_name TEXT, address TEXT, state TEXT,
                      city TEXT, pin TEXT, social_category TEXT, religion TEXT)''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def generate_random_data():
    # Connect to the database
    conn = sqlite3.connect("candidate_data.db")
    cursor = conn.cursor()

    for _ in range(100):
        # Generate random data
        candidate_id = random.randint(1, 10000)
        aadhar_no = random.randint(100000000000, 599999999999)
        name = random.choice(candidate_names)
        age = random.randint(18, 25)
        dob = f"{random.randint(1, 28):02d}-{random.randint(1, 12):02d}-{random.randint(1995, 2003)}"
        gender = random.choice(["Male", "Female", "Other"])
        father_name = random.choice(father_names)
        mother_name = random.choice(mother_names)
        education = random.choice(["High School", "Bachelor's Degree", "Master's Degree"])
        contact_no = f"+91{random.randint(1000000000, 4999999999)}"
        email = f"{name.lower().replace(' ', '')}@example.com"
        center_id = random.randint(1, 5)
        center_name = random.choice(center_names)
        address = random.choice(addresses)
        state = random.choice(states)
        city = random.choice(cities)
        pin = f"{random.randint(100000, 599999)}"
        social_category = random.choice(["General", "SC", "ST", "OBC"])
        religion = random.choice(["Hindu", "Muslim", "Christian", "Sikh", "Other"])

        # Insert the data into the table
        cursor.execute('''INSERT INTO candidates (candidate_id, aadhar_no, name, age, dob, gender,
                          father_name, mother_name, education, contact_no, email, center_id,
                          center_name, address, state, city, pin, social_category, religion)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (candidate_id, aadhar_no, name, age, dob, gender, father_name,
                        mother_name, education, contact_no, email, center_id, center_name,
                        address, state, city, pin, social_category, religion))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def display_table():
    # Connect to the database
    conn = sqlite3.connect("candidate_data.db")
    cursor = conn.cursor()

    # Retrieve data from the table
    cursor.execute("SELECT * FROM candidates")
    data = cursor.fetchall()

    # Update the table display
    for widget in table.winfo_children():
        widget.destroy()

    # Create the table headings
    headings = ["Candidate ID", "Aadhar No.", "Name", "Age", "DOB", "Gender", "Father's Name",
                "Mother's Name", "Education", "Contact No.", "Email", "Center ID", "Center Name",
                "Address", "State", "City", "PIN", "Social Category", "Religion"]
    for i, heading in enumerate(headings):
        tk.Label(table, text=heading, relief=tk.RIDGE, width=10,bg="lightgreen").grid(row=0, column=i)

    # Insert data into the table
    for row_num, row_data in enumerate(data, start=1):
        for col_num, cell_data in enumerate(row_data):
            tk.Label(table, text=cell_data, relief=tk.RIDGE, width=10,bg="lightblue").grid(row=row_num, column=col_num)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Define the dummy data lists
candidate_names = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Brown", "David Davis"]
mother_names=["Julia Doe", "Jasmine Smith", "Maria Johnson", "Ashley Brown","Daisy Davis"]
father_names=["Joe Doe", "James Smith", "Morty Johnson", "Arnold Brown","Dave Davis"]
center_names = ["Center 1", "Center 2", "Center 3", "Center 4", "Center 5"]
addresses = ["123 Main St", "456 Elm St", "789 Oak St", "321 Pine St", "654 Maple St"]
states = ["State A", "State B", "State C", "State D", "State E"]
cities = ["City A", "City B", "City C", "City D", "City E"]

# Create the table if it doesn't exist
create_table()

# Generate random data for candidates
generate_random_data()

# Create a tkinter window
window = tk.Tk()
window.title("Candidate Profiles")

# Create a table using tkinter
table = tk.Frame(window)
table.pack()

# Display the table
display_table()

# Run the tkinter event loop
window.mainloop()
