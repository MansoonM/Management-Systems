import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Database Setup
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mansoon111",
    database="library_db"
)
mycursor = mydb.cursor()

# # Create Staff Table
# mycursor.execute("""
# CREATE TABLE IF NOT EXISTS staff (
#     staff_id INT PRIMARY KEY,
#     staff_name VARCHAR(255),
#     staff_branch VARCHAR(255),
#     staff_job_position VARCHAR(255),
#     BookName VARCHAR(255),
#     BookType VARCHAR(255),
#     DateOfIssue DATE,
#     DateOfReturn DATE,
#     AnyFine INT
# )
# """)

# # Create Student Table
# mycursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     student_id INT PRIMARY KEY,
#     student_name VARCHAR(255),
#     student_branch VARCHAR(255),
#     student_year INT,
#     BookName VARCHAR(255),
#     BookType VARCHAR(255),
#     DateOfIssue DATE,
#     DateOfReturn DATE,
#     AnyFine INT
# )
# """)

# Main Application
class LibraryManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.state('zoomed')
        
        # Main Heading
        heading_frame = tk.Frame(root, bg="yellow")
        heading_frame.pack(fill=tk.X)
        tk.Label(heading_frame, text="Synergy Institute of Technology, BBSR", font=("Arial", 20),
                 bg="black", fg="yellow").pack(pady=8, fill=tk.X)
        # Sub Heading
        subheading_frame = tk.Frame(root, bg="black")
        subheading_frame.pack(fill=tk.X)
        tk.Label(subheading_frame, text="Library Management System", font=("Arial", 18),
                 bg="black", fg="yellow").pack(pady=5, fill=tk.X)

        # Staff Section
        staff_frame = tk.Frame(root)
        staff_frame.pack(pady=10, fill=tk.X)

        tk.Label(staff_frame, text="Book Issue to Staff", font=("Arial", 14, "bold"),
                 fg="red").grid(row=0, column=0, columnspan=6, pady=5)

        # Staff Form
        self.staff_fields = ["Staff ID", "Name", "Branch", "Job Position", "Book Name", 
                           "Book Type", "Date of Issue", "Date of Return", "Fine"]
        self.staff_entries = {}
        
        for i, field in enumerate(self.staff_fields):
            tk.Label(staff_frame, text=field).grid(row=1, column=i, padx=5)
            entry = tk.Entry(staff_frame)
            entry.grid(row=2, column=i, padx=5)
            self.staff_entries[field] = entry

        # Staff Buttons
        btn_frame = tk.Frame(staff_frame)
        btn_frame.grid(row=3, column=0, columnspan=9, pady=10)
        
        tk.Button(btn_frame, text="Add", bg="green", fg="white", command=self.add_staff).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete", bg="red", fg="white", command=self.delete_staff).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Update", bg="grey", fg="white", command=self.update_staff).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Search", bg="black", fg="white", command=self.search_staff).pack(side=tk.LEFT, padx=5)

        # Staff Table
        columns = ("ID", "Name", "Branch", "Position", "Book", "Type", "Issue", "Return", "Fine")
        self.staff_tree = ttk.Treeview(root, columns=columns, show="headings", height=5)
        
        for col in columns:
            self.staff_tree.heading(col, text=col)
            self.staff_tree.column(col, width=100)
        
        self.staff_tree.pack(fill=tk.X, padx=10)
        self.staff_tree.bind("<<TreeviewSelect>>", self.load_staff_data)

        # Student Section
        student_frame = tk.Frame(root)
        student_frame.pack(pady=10, fill=tk.X)

        tk.Label(student_frame, text="Book Issue to Student", font=("Arial", 14, "bold"),
                 fg="red").grid(row=0, column=0, columnspan=6, pady=5)

        # Student Form
        self.student_fields = ["Student ID", "Name", "Branch", "Year", "Book Name", 
                             "Book Type", "Date of Issue", "Date of Return", "Fine"]
        self.student_entries = {}
        
        for i, field in enumerate(self.student_fields):
            tk.Label(student_frame, text=field).grid(row=1, column=i, padx=5)
            entry = tk.Entry(student_frame)
            entry.grid(row=2, column=i, padx=5)
            self.student_entries[field] = entry

        # Student Buttons
        btn_frame = tk.Frame(student_frame)
        btn_frame.grid(row=3, column=0, columnspan=9, pady=10)
        
        tk.Button(btn_frame, text="Add", bg="green", fg="white", command=self.add_student).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete", bg="red", fg="white", command=self.delete_student).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Update", bg="grey", fg="white", command=self.update_student).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Search", bg="black", fg="white", command=self.search_student).pack(side=tk.LEFT, padx=5)

        # Student Table
        self.student_tree = ttk.Treeview(root, columns=columns, show="headings", height=5)
        
        for col in columns:
            self.student_tree.heading(col, text=col)
            self.student_tree.column(col, width=100)
        
        self.student_tree.pack(fill=tk.X, padx=10)
        self.student_tree.bind("<<TreeviewSelect>>", self.load_student_data)

        self.refresh_tables()

    # CRUD Operations for Staff
    def add_staff(self):
        values = [self.staff_entries[field].get() for field in self.staff_fields]
        query = """INSERT INTO staff VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        mycursor.execute(query, values)
        mydb.commit()
        self.refresh_tables()

    def delete_staff(self):
        selected = self.staff_tree.selection()
        if selected:
            staff_id = self.staff_tree.item(selected[0])['values'][0]
            mycursor.execute("DELETE FROM staff WHERE staff_id=%s", (staff_id,))
            mydb.commit()
            self.refresh_tables()

    def update_staff(self):
        selected = self.staff_tree.selection()
        if selected:
            values = [self.staff_entries[field].get() for field in self.staff_fields]
            query = """UPDATE staff SET staff_name=%s, staff_branch=%s, staff_job_position=%s,
                      BookName=%s, BookType=%s, DateOfIssue=%s, DateOfReturn=%s, AnyFine=%s
                      WHERE staff_id=%s"""
            mycursor.execute(query, (values[1], values[2], values[3], values[4], 
                                   values[5], values[6], values[7], values[8], values[0]))
            mydb.commit()
            self.refresh_tables()

    # Search Functionality for Staff
    def search_staff(self):
        conditions = []
        params = []
        for field in self.staff_fields:
            entry = self.staff_entries[field].get().strip()
            if entry:
                db_field = self.get_staff_db_field(field)
                conditions.append(f"{db_field} LIKE %s")
                params.append(f"%{entry}%")
        
        query = "SELECT * FROM staff"
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        
        try:
            mycursor.execute(query, tuple(params))
            rows = mycursor.fetchall()
            
            self.staff_tree.delete(*self.staff_tree.get_children())
            for row in rows:
                self.staff_tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", str(e))


    # CRUD Operations for Students
    def add_student(self):
        values = [self.student_entries[field].get() for field in self.student_fields]
        query = """INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        mycursor.execute(query, values)
        mydb.commit()
        self.refresh_tables()

    def delete_student(self):
        selected = self.student_tree.selection()
        if selected:
            student_id = self.student_tree.item(selected[0])['values'][0]
            mycursor.execute("DELETE FROM students WHERE student_id=%s", (student_id,))
            mydb.commit()
            self.refresh_tables()

    def update_student(self):
        selected = self.student_tree.selection()
        if selected:
            values = [self.student_entries[field].get() for field in self.student_fields]
            query = """UPDATE students SET student_name=%s, student_branch=%s, student_year=%s,
                      BookName=%s, BookType=%s, DateOfIssue=%s, DateOfReturn=%s, AnyFine=%s
                      WHERE student_id=%s"""
            mycursor.execute(query, (values[1], values[2], values[3], values[4], 
                                   values[5], values[6], values[7], values[8], values[0]))
            mydb.commit()
            self.refresh_tables()

    
    # Search Functionality for Students
    def search_student(self):
        conditions = []
        params = []
        for field in self.student_fields:
            entry = self.student_entries[field].get().strip()
            if entry:
                db_field = self.get_student_db_field(field)
                conditions.append(f"{db_field} LIKE %s")
                params.append(f"%{entry}%")
        
        query = "SELECT * FROM students"
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        
        try:
            mycursor.execute(query, tuple(params))
            rows = mycursor.fetchall()
            
            self.student_tree.delete(*self.student_tree.get_children())
            for row in rows:
                self.student_tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", str(e))




     # Helper methods for field mapping
    def get_staff_db_field(self, field):
        field_mapping = {
            "Staff ID": "staff_id",
            "Name": "staff_name",
            "Branch": "staff_branch",
            "Job Position": "staff_job_position",
            "Book Name": "BookName",
            "Book Type": "BookType",
            "Date of Issue": "DateOfIssue",
            "Date of Return": "DateOfReturn",
            "Fine": "AnyFine"
        }
        return field_mapping.get(field, field)

    def get_student_db_field(self, field):
        field_mapping = {
            "Student ID": "student_id",
            "Name": "student_name",
            "Branch": "student_branch",
            "Year": "student_year",
            "Book Name": "BookName",
            "Book Type": "BookType",
            "Date of Issue": "DateOfIssue",
            "Date of Return": "DateOfReturn",
            "Fine": "AnyFine"
        }
        return field_mapping.get(field, field)
    # Helper Functions
    def refresh_tables(self):
        # Clear existing data
        for item in self.staff_tree.get_children():
            self.staff_tree.delete(item)
        for item in self.student_tree.get_children():
            self.student_tree.delete(item)

        # Load Staff Data
        mycursor.execute("SELECT * FROM staff")
        for row in mycursor.fetchall():
            self.staff_tree.insert("", tk.END, values=row)

        # Load Student Data
        mycursor.execute("SELECT * FROM students")
        for row in mycursor.fetchall():
            self.student_tree.insert("", tk.END, values=row)

    def load_staff_data(self, event):
        selected = self.staff_tree.selection()
        if selected:
            values = self.staff_tree.item(selected[0])['values']
            for field, value in zip(self.staff_fields, values):
                self.staff_entries[field].delete(0, tk.END)
                self.staff_entries[field].insert(0, value)

    def load_student_data(self, event):
        selected = self.student_tree.selection()
        if selected:
            values = self.student_tree.item(selected[0])['values']
            for field, value in zip(self.student_fields, values):
                self.student_entries[field].delete(0, tk.END)
                self.student_entries[field].insert(0, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagement(root)
    root.mainloop()