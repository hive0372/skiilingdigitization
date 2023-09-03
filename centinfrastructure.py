import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect("center_infrastructure.db")
cursor = conn.cursor()

# Create the center infrastructure details table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS center_infrastructure (
        center_name TEXT,
        classrooms INTEGER,
        libraries INTEGER,
        laboratories INTEGER,
        computers INTEGER,
        canteens INTEGER,
        auditorium_available TEXT,
        male_washrooms INTEGER,
        female_washrooms INTEGER,
        biometric_equipment_available TEXT,
        biometric_equipment_count INTEGER,
        fire_extinguisher_available TEXT,
        fire_extinguisher_count INTEGER
    )
""")

# Sample center infrastructure values
infrastructures = [
    ("Center 1", 5, 2, 3, 30, 2, "Yes", 4, 4, "Yes", 2, "Yes", 5),
    ("Center 2", 4, 1, 2, 20, 1, "No", 2, 2, "No", 0, "Yes", 3),
    ("Center 3", 6, 3, 4, 40, 3, "Yes", 6, 6, "No", 0, "No", 0),
    ("Center 4", 3, 1, 1, 10, 1, "No", 1, 1, "Yes", 1, "Yes", 2),
    ("Center 5", 4, 2, 2, 15, 1, "Yes", 3, 3, "Yes", 3, "Yes", 4)
]

# Insert the sample center infrastructure values into the table
cursor.executemany("INSERT INTO center_infrastructure VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", infrastructures)

# Commit the changes
conn.commit()

# Create the main window
window = tk.Tk()
window.title("Center Infrastructure Details")

# Create the table
table = ttk.Treeview(window)
table["columns"] = ("classrooms", "libraries", "laboratories", "computers", "canteens",
                    "auditorium_available", "male_washrooms", "female_washrooms",
                    "biometric_equipment_available", "biometric_equipment_count",
                    "fire_extinguisher_available", "fire_extinguisher_count")
table.heading("#0", text="Center Name")
table.column("#0", width=70)
table.heading("classrooms", text="No. of Classrooms")
table.column("classrooms", width=65)
table.heading("libraries", text="No. of Libraries")
table.column("libraries", width=65)
table.heading("laboratories", text="No. of Laboratories")
table.column("laboratories", width=65)
table.heading("computers", text="No. of Computers")
table.column("computers", width=75)
table.heading("canteens", text="No. of Canteens")
table.column("canteens", width=75)
table.heading("auditorium_available", text="Auditorium Available")
table.column("auditorium_available", width=70)
table.heading("male_washrooms", text="No. of Male Washrooms")
table.column("male_washrooms", width=70)
table.heading("female_washrooms", text="No. of Female Washrooms")
table.column("female_washrooms", width=90)
table.heading("biometric_equipment_available", text="Biometric Equipment Available")
table.column("biometric_equipment_available", width=90)
table.heading("biometric_equipment_count", text="No. of Biometric Equipment")
table.column("biometric_equipment_count", width=100)
table.heading("fire_extinguisher_available", text="Fire Extinguisher Available")
table.column("fire_extinguisher_available", width=100)
table.heading("fire_extinguisher_count", text="No. of Fire Extinguishers")
table.column("fire_extinguisher_count", width=100)

# Retrieve center infrastructure details from the database
cursor.execute("SELECT rowid, * FROM center_infrastructure")
center_infrastructures = cursor.fetchall()

# Insert center infrastructure details into the table
for center in center_infrastructures:
    table.insert("", "end", text=center[1], values=center[2:])

# Configure the table's style
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", font=("Arial", 10))
style.configure("Treeview.Heading", font=("Arial", 10, "bold"), foreground="white", background="#3F51B5")
style.map("Treeview", background=[("alternate", "#F5F5F5"), ("", "white")])

# Add the table to a scrollable frame
scrollbar = ttk.Scrollbar(window, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
table.pack(expand=True, fill="both")

# Start the main event loop
window.mainloop()

# Close the database connection
conn.close()
