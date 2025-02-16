import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import bcrypt

# Database connection
def connect_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="mansoon111",  # Replace with your MySQL password
            database="voting_system"
        )
    except Error as e:
        print(f"Error: {e}")
        return None


    

class VotingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Virtual Voting System")
        self.current_user = None
       
        self.login_frame = tk.Frame(master)
        self.register_frame = tk.Frame(master)
        self.vote_frame = tk.Frame(master)
        self.results_frame = tk.Frame(master)

        self.create_login_frame()
        self.create_register_frame()
        self.create_vote_frame()
        self.create_results_frame()

        self.show_frame(self.login_frame)

    def create_login_frame(self):
        tk.Label(self.login_frame, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack(pady=5)
        # Set the title of the window
        root.title("My Tkinter Window")
    
    # Set the size of the window (width x height)
        root.geometry("500x300")  # Width: 400 pixels, Height: 300 pixels
    
   


        tk.Label(self.login_frame, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.login_frame, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.login_frame, text="Register", command=lambda: self.show_frame(self.register_frame)).pack(pady=10)

    def create_register_frame(self):
        tk.Label(self.register_frame, text="Username").pack(pady=5)
        self.reg_username_entry = tk.Entry(self.register_frame)
        self.reg_username_entry.pack(pady=5)

        tk.Label(self.register_frame, text="Password").pack(pady=5)
        self.reg_password_entry = tk.Entry(self.register_frame, show="*")
        self.reg_password_entry.pack(pady=5)

        tk.Button(self.register_frame, text="Register", command=self.register).pack(pady=10)
        tk.Button(self.register_frame, text="Back to Login", command=lambda: self.show_frame(self.login_frame)).pack(pady=10)

    def create_vote_frame(self):
        tk.Label(self.vote_frame, text="Select a candidate to vote for:").pack(pady=10)
        self.candidate_var = tk.StringVar(value="")

        self.candidates = self.fetch_candidates()
        self.candidate_buttons = []
        for candidate in self.candidates:
            rb = tk.Radiobutton(self.vote_frame, text=candidate[1], variable=self.candidate_var, value=candidate[0])
            rb.pack(anchor=tk.W)
            self.candidate_buttons.append(rb)

        tk.Button(self.vote_frame, text="Vote", command=self.cast_vote).pack(pady=10)
        tk.Button(self.vote_frame, text="View Results", command=self.view_results).pack(pady=10)

    def create_results_frame(self):
        tk.Label(self.results_frame, text="Voting Results:").pack(pady=10)
        self.results_text = tk.Text(self.results_frame, height=10, width=50)
        self.results_text.pack(pady=10)

        tk.Button(self.results_frame, text="Back to Voting", command=lambda: self.show_frame(self.vote_frame)).pack(pady=10)

    def show_frame(self, frame):
        frame.pack(fill="both", expand=True)
        for f in (self.login_frame, self.register_frame, self.vote_frame, self.results_frame):
            if f != frame:
                f.pack_forget()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[2].encode('utf-8')):
            self.current_user = user[0]  # Store user ID
            self.show_frame(self.vote_frame)
        else:
            messagebox.showwarning("Login Failed", "Invalid username or password.")

    def register(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password.decode('utf-8')))
            conn.commit()
            messagebox.showinfo("Registration Successful", "You can now log in.")
            self.show_frame(self.login_frame)
        except Error as e:
            messagebox.showerror("Registration Failed", str(e))
        finally:
            cursor.close()
            conn.close()

    def fetch_candidates(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM candidates WHERE election_id = 1")
        candidates = cursor.fetchall()
        cursor.close()
        conn.close()
        return candidates

    def cast_vote(self):
        candidate_id = self.candidate_var.get()
        if not candidate_id:
            messagebox.showwarning("No Selection", "Please select a candidate to vote for.")
            return

        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO votes (user_id, candidate_id, election_id) VALUES (%s, %s, %s)", 
                           (self.current_user, candidate_id, 1))
            cursor.execute("UPDATE candidates SET votes = votes + 1 WHERE id = %s", (candidate_id,))
            conn.commit()
            messagebox.showinfo("Vote Cast", "Your vote has been successfully cast.")
        except Error as e:
            messagebox.showerror("Vote Failed", str(e))
        finally:
            cursor.close()
            conn.close()

    def view_results(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT name , votes FROM candidates WHERE election_id = 1")
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        self.results_text.delete(1.0, tk.END)  # Clear previous results
        for candidate in results:
            self.results_text.insert(tk.END, f"{candidate[0]}: {candidate[1]} votes\n")
        self.show_frame(self.results_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingSystem(root)
    root.mainloop()