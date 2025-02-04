import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Database Configuration
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mansoon111",
    database="student_management_db"
)
mycursor = mydb.cursor()

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.state('zoomed')
        
        # Main Heading
        heading_frame = tk.Frame(root, bg="yellow")
        heading_frame.pack(fill=tk.X)
        tk.Label(heading_frame, text="Synergy Institute of Technology", font=("Arial", 24, "bold"),
                bg="yellow", fg="black").pack(pady=10, fill=tk.X)

        # Sub Heading
        subheading_frame = tk.Frame(root, bg="black")
        subheading_frame.pack(fill=tk.X)
        tk.Label(subheading_frame, text="Student Management System", font=("Arial", 18),
                bg="black", fg="yellow").pack(pady=5, fill=tk.X)

        # Personal Information Section
        personal_frame = tk.Frame(root)
        personal_frame.pack(pady=10, fill=tk.X)

        tk.Label(personal_frame, text="Student Personal Information", font=("Arial", 14, "bold"),
                fg="red").grid(row=0, column=0, columnspan=10, sticky='ew')

        self.personal_fields = [
            "Student ID", "Name", "Branch", "Year", "BPUT Reg No",
            "Phone Number", "Address", "Guardian Name", "Guardian Number", "Complaint"
        ]
        self.personal_entries = {}
        
        for i, field in enumerate(self.personal_fields):
            tk.Label(personal_frame, text=field).grid(row=1, column=i, padx=5)
            entry = tk.Entry(personal_frame, width=15)
            entry.grid(row=2, column=i, padx=5)
            self.personal_entries[field] = entry

        # Personal Info Buttons
        btn_frame_personal = tk.Frame(personal_frame)
        btn_frame_personal.grid(row=3, column=0, columnspan=10, pady=10)
        
        tk.Button(btn_frame_personal, text="Add", bg="green", fg="white", command=self.add_personal).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame_personal, text="Delete", bg="red", fg="white", command=self.delete_personal).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame_personal, text="Update", bg="grey", fg="white", command=self.update_personal).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame_personal, text="Search", bg="black", fg="white", command=self.search_personal).pack(side=tk.LEFT, padx=5)

        # Personal Info Table
        personal_columns = ("ID", "Name", "Branch", "Year", "BPUT Reg", "Phone", 
                          "Address", "Guardian", "G-Phone", "Complaint")
        self.personal_tree = ttk.Treeview(root, columns=personal_columns, show="headings", height=5)
        
        for col in personal_columns:
            self.personal_tree.heading(col, text=col)
            self.personal_tree.column(col, width=100)
        
        self.personal_tree.pack(fill=tk.X, padx=10)
        self.personal_tree.bind("<<TreeviewSelect>>", self.load_personal_data)

        # Fees Information Section
        fees_frame = tk.Frame(root)
        fees_frame.pack(pady=10, fill=tk.X)

        tk.Label(fees_frame, text="Student Fees Information", font=("Arial", 14, "bold"),
                 fg="red").grid(row=0, column=0, columnspan=10, sticky='ew')

        self.fees_fields = [
            "Student ID", "Name", "Branch", "Year", "Fees",
            "Fees Paid", "Hostel Staying", "Fine", "Fine Paid"
        ]
        self.fees_entries = {}
        
        for i, field in enumerate(self.fees_fields):
            tk.Label(fees_frame, text=field).grid(row=1, column=i, padx=5)
            entry = tk.Entry(fees_frame, width=15)
            entry.grid(row=2, column=i, padx=5)
            self.fees_entries[field] = entry

        # Fees Info Buttons
        btn_frame_fees = tk.Frame(fees_frame)
        btn_frame_fees.grid(row=3, column=0, columnspan=10, pady=10)
        
        tk.Button(btn_frame_fees, text="Add", bg="green", fg="white", command=self.add_fees).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame_fees, text="Delete", bg="red", fg="white", command=self.delete_fees).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame_fees, text="Update", bg="grey", fg="white", command=self.update_fees).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame_fees, text="Search", bg="black", fg="white", command=self.search_fees).pack(side=tk.LEFT, padx=5)

        # Fees Info Table
        fees_columns = ("ID", "Name", "Branch", "Year", "Fees", 
                       "Fees Paid", "Hostel", "Fine", "Fine Paid")
        self.fees_tree = ttk.Treeview(root, columns=fees_columns, show="headings", height=5)
        
        for col in fees_columns:
            self.fees_tree.heading(col, text=col)
            self.fees_tree.column(col, width=100)
        
        self.fees_tree.pack(fill=tk.X, padx=10)
        self.fees_tree.bind("<<TreeviewSelect>>", self.load_fees_data)

        self.refresh_tables()

    # CRUD Operations for Personal Information
    def add_personal(self):
        values = [self.personal_entries[field].get() for field in self.personal_fields]
        query = """INSERT INTO student_personal VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        try:
            mycursor.execute(query, values)
            mydb.commit()
            self.refresh_tables()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_personal(self):
        selected = self.personal_tree.selection()
        if selected:
            student_id = self.personal_tree.item(selected[0])['values'][0]
            try:
                mycursor.execute("DELETE FROM student_personal WHERE student_id=%s", (student_id,))
                mydb.commit()
                self.refresh_tables()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def update_personal(self):
        selected = self.personal_tree.selection()
        if selected:
            values = [self.personal_entries[field].get() for field in self.personal_fields]
            query = """UPDATE student_personal SET 
                    student_name=%s, student_branch=%s, student_year=%s, 
                    bput_reg_no=%s, phone_number=%s, address=%s, 
                    guardian_name=%s, guardian_number=%s, complaint=%s 
                    WHERE student_id=%s"""
            try:
                mycursor.execute(query, (values[1], values[2], values[3], values[4], 
                                       values[5], values[6], values[7], values[8], 
                                       values[9], values[0]))
                mydb.commit()
                self.refresh_tables()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def search_personal(self):
        pass  # Implement similar to previous example

    # CRUD Operations for Fees Information
    def add_fees(self):
        values = [self.fees_entries[field].get() for field in self.fees_fields]
        query = """INSERT INTO student_fees VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        try:
            mycursor.execute(query, values)
            mydb.commit()
            self.refresh_tables()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_fees(self):
        selected = self.fees_tree.selection()
        if selected:
            student_id = self.fees_tree.item(selected[0])['values'][0]
            try:
                mycursor.execute("DELETE FROM student_fees WHERE student_id=%s", (student_id,))
                mydb.commit()
                self.refresh_tables()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def update_fees(self):
        selected = self.fees_tree.selection()
        if selected:
            values = [self.fees_entries[field].get() for field in self.fees_fields]
            query = """UPDATE student_fees SET 
                    student_name=%s, student_branch=%s, student_year=%s, 
                    fees=%s, fees_paid=%s, hostel_staying=%s, 
                    any_fine=%s, fine_paid=%s 
                    WHERE student_id=%s"""
            try:
                mycursor.execute(query, (values[1], values[2], values[3], values[4], 
                                       values[5], values[6], values[7], values[8], 
                                       values[0]))
                mydb.commit()
                self.refresh_tables()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def search_fees(self):
        pass  # Implement similar to previous example

    # Helper Methods
    def refresh_tables(self):
        # Clear tables
        for item in self.personal_tree.get_children():
            self.personal_tree.delete(item)
        for item in self.fees_tree.get_children():
            self.fees_tree.delete(item)

        # Load Personal Data
        mycursor.execute("SELECT * FROM student_personal")
        for row in mycursor.fetchall():
            self.personal_tree.insert("", tk.END, values=row)

        # Load Fees Data
        mycursor.execute("SELECT * FROM student_fees")
        for row in mycursor.fetchall():
            self.fees_tree.insert("", tk.END, values=row)

    def load_personal_data(self, event):
        selected = self.personal_tree.selection()
        if selected:
            values = self.personal_tree.item(selected[0])['values']
            for field, value in zip(self.personal_fields, values):
                self.personal_entries[field].delete(0, tk.END)
                self.personal_entries[field].insert(0, value)

    def load_fees_data(self, event):
        selected = self.fees_tree.selection()
        if selected:
            values = self.fees_tree.item(selected[0])['values']
            for field, value in zip(self.fees_fields, values):
                self.fees_entries[field].delete(0, tk.END)
                self.fees_entries[field].insert(0, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()