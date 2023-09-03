import tkinter as tk
import sqlite3

def create_table():
    # Connect to the database
    conn = sqlite3.connect("trainers.db")
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS trainer_details
                      (mentor_id INTEGER PRIMARY KEY AUTOINCREMENT, mentor_name TEXT,
                      course_handled TEXT, course_id INTEGER, teaching_experience INTEGER,
                      contact_no TEXT)''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def add_trainer_details():
    # Connect to the database
    conn = sqlite3.connect("trainers.db")
    cursor = conn.cursor()

    # Retrieve the input values from the form
    mentor_name = mentor_name_entry.get()
    course_handled = course_handled_entry.get()
    course_id = int(course_id_entry.get())
    teaching_experience = int(teaching_experience_entry.get())
    contact_no = contact_no_entry.get()

    # Insert the input values into the table
    cursor.execute('''INSERT INTO trainer_details (mentor_name, course_handled, course_id,
                      teaching_experience, contact_no) VALUES (?, ?, ?, ?, ?)''',
                   (mentor_name, course_handled, course_id, teaching_experience, contact_no))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    # Clear the input fields after adding the trainer details
    clear_form()

    # Refresh the table display
    display_table()

def clear_form():
    # Clear the input fields
    mentor_name_entry.delete(0, tk.END)
    course_handled_entry.delete(0, tk.END)
    course_id_entry.delete(0, tk.END)
    teaching_experience_entry.delete(0, tk.END)
    contact_no_entry.delete(0, tk.END)

def display_table():
    # Connect to the database
    conn = sqlite3.connect("trainers.db")
    cursor = conn.cursor()

    # Retrieve data from the table
    cursor.execute("SELECT * FROM trainer_details")
    data = cursor.fetchall()

    # Update the table display
    for widget in table.winfo_children():
        widget.destroy()

    # Create the table headings
    headings = ["Mentor ID", "Mentor Name", "Course Handled", "Course ID",
                "Teaching Experience", "Contact No"]
    for i, heading in enumerate(headings):
        tk.Label(table, text=heading, relief=tk.RIDGE, width=20, bg="lightgreen").grid(row=0, column=i)

    # Insert data into the table
    for row_num, row_data in enumerate(data, start=1):
        for col_num, cell_data in enumerate(row_data):
            tk.Label(table, text=cell_data, relief=tk.RIDGE, width=20, bg="lightblue").grid(row=row_num, column=col_num)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Create the table if it doesn't exist
create_table()

# Create a tkinter window
window = tk.Tk()
window.title("Trainer Details")

# Create a form to add trainer details
form = tk.Frame(window)
form.pack()

# Mentor Name
mentor_name_label = tk.Label(form, text="Mentor Name:")
mentor_name_label.grid(row=0, column=0, sticky=tk.E)
mentor_name_entry = tk.Entry(form)
mentor_name_entry.grid(row=0, column=1)

# Course Handled
course_handled_label = tk.Label(form, text="Course Handled:")
course_handled_label.grid(row=1, column=0, sticky=tk.E)
course_handled_entry = tk.Entry(form)
course_handled_entry.grid(row=1, column=1)

# Course ID
course_id_label = tk.Label(form, text="Course ID:")
course_id_label.grid(row=2, column=0, sticky=tk.E)
course_id_entry = tk.Entry(form)
course_id_entry.grid(row=2, column=1)

# Teaching Experience
teaching_experience_label = tk.Label(form, text="Teaching Experience:")
teaching_experience_label.grid(row=3, column=0, sticky=tk.E)
teaching_experience_entry = tk.Entry(form)
teaching_experience_entry.grid(row=3, column=1)

# Contact No.
contact_no_label = tk.Label(form, text="Contact No:")
contact_no_label.grid(row=4, column=0, sticky=tk.E)
contact_no_entry = tk.Entry(form)
contact_no_entry.grid(row=4, column=1)

# Submit button
submit_button = tk.Button(form, text="Submit", command=add_trainer_details)
submit_button.grid(row=5, column=0, sticky=tk.E)

# Clear button
clear_button = tk.Button(form, text="Clear", command=clear_form)
clear_button.grid(row=5, column=1, sticky=tk.W)

# Create a table using tkinter
table = tk.Frame(window)
table.pack()

# Display the table
display_table()

# Run the tkinter event loop
window.mainloop()
