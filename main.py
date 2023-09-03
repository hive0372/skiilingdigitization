import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect("center_details.db")
cursor = conn.cursor()

# Create the center details table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS center_details (
        center_name TEXT,
        center_address TEXT,
        contact_number TEXT,
        center_id TEXT,
        incharge_name TEXT,
        city TEXT,
        state TEXT,
        pin TEXT
    )
""")

# Sample center values
centers = [
    ("Center 1", "123 Main St", "1234567890", "C001", "Incharge 1", "City A", "State A", "12345"),
    ("Center 2", "456 Elm St", "2345678901", "C002", "Incharge 2", "City B", "State B", "23456"),
    ("Center 3", "789 Oak St", "3456789012", "C003", "Incharge 3", "City C", "State C", "34567"),
    ("Center 4", "321 Pine St", "4567890123", "C004", "Incharge 4", "City D", "State D", "45678"),
    ("Center 5", "654 Maple St", "5678901234", "C005", "Incharge 5", "City E", "State E", "56789")
]

# Insert the sample center values into the table
cursor.executemany("INSERT INTO center_details VALUES (?, ?, ?, ?, ?, ?, ?, ?)", centers)

# Commit the changes
conn.commit()

# Create the main window
window = tk.Tk()
window.title("Center Details")

# Create the table
table = ttk.Treeview(window)
table["columns"] = ("center_name", "center_address", "contact_number", "center_id",
                    "incharge_name", "city", "state", "pin")
table.heading("#0", text="ID")
table.column("#0", width=50)
table.heading("center_name", text="Center Name")
table.column("center_name", width=100)
table.heading("center_address", text="Center Address")
table.column("center_address", width=200)
table.heading("contact_number", text="Contact Number")
table.column("contact_number", width=100)
table.heading("center_id", text="Center ID")
table.column("center_id", width=100)
table.heading("incharge_name", text="Incharge Name")
table.column("incharge_name", width=100)
table.heading("city", text="City")
table.column("city", width=100)
table.heading("state", text="State")
table.column("state", width=100)
table.heading("pin", text="Pin")
table.column("pin", width=100)

# Retrieve center details from the database
cursor.execute("SELECT rowid, * FROM center_details")
center_details = cursor.fetchall()

# Insert center details into the table
for center in center_details:
    table.insert("", "end", text=center[0], values=center[1:])

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
