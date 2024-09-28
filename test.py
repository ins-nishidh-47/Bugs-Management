import mysql.connector as mysql
import modules as easy  # Assuming this is your custom module for hashID and select
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox, scrolledtext

# Connect to MySQL
db = mysql.connect(host="localhost", user="root", passwd="Nishidh@123", database="bug_tracking")
cur = db.cursor()  # Creating cursor

class BugManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bug Management System")
        self.geometry("500x500")
        self.main_screen()

    def main_screen(self):
        self.clear_screen()
        label = tk.Label(self, text="Bug Tracking System", font=("Helvetica", 18))
        label.pack(pady=10)

        login_button = tk.Button(self, text="Login", command=self.login_screen)
        login_button.pack(pady=5)

        signup_button = tk.Button(self, text="Sign Up", command=self.signup_screen)
        signup_button.pack(pady=5)

    def login_screen(self):
        self.clear_screen()
        label = tk.Label(self, text="Login", font=("Helvetica", 18))
        label.pack(pady=10)

        email_label = tk.Label(self, text="Email:")
        email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        password_label = tk.Label(self, text="Password:")
        password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        login_button = tk.Button(self, text="Login", command=self.verify_login)
        login_button.pack(pady=10)

        back_button = tk.Button(self, text="Back", command=self.main_screen)
        back_button.pack(pady=10)

    def signup_screen(self):
        self.clear_screen()
        label = tk.Label(self, text="Sign Up", font=("Helvetica", 18))
        label.pack(pady=10)

        username_label = tk.Label(self, text="Name:")
        username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        email_label = tk.Label(self, text="Email:")
        email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        password_label = tk.Label(self, text="Password:")
        password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        signup_button = tk.Button(self, text="Sign Up", command=self.verify_signup)
        signup_button.pack(pady=10)

        back_button = tk.Button(self, text="Back", command=self.main_screen)
        back_button.pack(pady=10)

    def verify_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        try:
            record = easy.select('userinfo', '*', 1, f"password = '{password}' and email = '{email}'")
            if record:
                messagebox.showinfo("Success", "Logged in successfully!")
                self.work_screen()
            else:
                messagebox.showerror("Error", "Wrong Credentials")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def verify_signup(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        try:
            cur.execute(f"INSERT INTO userinfo (username,password,email,hash) VALUES ('{username}', '{password}', '{email}', '{easy.hashID()}')")
            db.commit()
            messagebox.showinfo("Success", "Signed up successfully!")
            self.login_screen()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def work_screen(self):
        self.clear_screen()
        label = tk.Label(self, text="Bug Management", font=("Helvetica", 18))
        label.pack(pady=10)

        add_bug_button = tk.Button(self, text="Add Bug", command=self.add_bug)
        add_bug_button.pack(pady=5)

        switch_assignees_button = tk.Button(self, text="Switch Assignees", command=self.switch_assignees)
        switch_assignees_button.pack(pady=5)

        bug_report_button = tk.Button(self, text="Bug Report", command=self.bug_report)
        bug_report_button.pack(pady=5)

        view_all_bugs_button = tk.Button(self, text="View All Bugs", command=self.view_all_bugs)
        view_all_bugs_button.pack(pady=5)

        logout_button = tk.Button(self, text="Logout", command=self.logout)
        logout_button.pack(pady=5)

    def add_bug(self):
        self.clear_screen()
        label = tk.Label(self, text="Add Bug", font=("Helvetica", 20, "bold"))
        label.pack(pady=20)

        # Bug Details Section
        self.add_bug_entry("Enter BugID:", self.bug_id_entry_label)
        self.add_bug_entry("Bug Description:", self.bug_description_entry)
        self.add_bug_entry("Enter Severity:", self.severity_entry_label)
        self.add_bug_entry("Enter no. of expected days:", self.req_days_entry_label)
        self.add_bug_entry("Enter Priority:", self.priority_entry_label)
        self.add_bug_entry("Assignee:", self.assignee_entry)
        self.add_bug_entry("Bug Status (1-5):", self.status_entry)

        # Date Entry
        date_label = tk.Label(self, text="Select Date for Bug Entry", font=("Helvetica", 12))
        date_label.pack(anchor='w', padx=20, pady=5)
        self.date_entry = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2, font=("Helvetica", 12))
        self.date_entry.pack(fill='x', padx=20, pady=5)

        # Submit Button
        submit_button = tk.Button(self, text="Submit", command=self.submit_bug, font=("Helvetica", 12, "bold"), bg="green", fg="white")
        submit_button.pack(pady=20)

        # Back Button
        back_button = tk.Button(self, text="Back", command=self.work_screen, font=("Helvetica", 12, "bold"), bg="red", fg="white")
        back_button.pack(pady=10)

    def add_bug_entry(self, label_text, entry_variable):
        label = tk.Label(self, text=label_text, font=("Helvetica", 12))
        label.pack(anchor='w', padx=20, pady=5)
        entry_variable = tk.Entry(self, font=("Helvetica", 12))
        entry_variable.pack(fill='x', padx=20)

    def submit_bug(self):
        bugID = self.bug_id_entry_label.get()
        severity = self.severity_entry_label.get()
        days = self.req_days_entry_label.get()
        priority = self.priority_entry_label.get()
        description = self.bug_description_entry.get()
        assignee = self.assignee_entry.get()
        status = self.status_entry.get()
        selected_date = self.date_entry.get_date()

        try:
            cur.execute(f"INSERT INTO buginfo (bugID, bugstatus, bugdesc, severity, reqdays, opendt, priority) VALUES ('{bugID}', {status}, '{description}', '{severity}', {days}, '{selected_date}', {priority})")
            db.commit()
            messagebox.showinfo("Success", "Bug added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def view_all_bugs(self):
        self.clear_screen()
        label = tk.Label(self, text="All Bugs", font=("Helvetica", 18))
        label.pack(pady=10)

        # Adding scrolled text area for displaying all bugs
        bug_text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=15)
        bug_text_area.pack(pady=10)

        try:
            cur.execute(f"SELECT * FROM buginfo")
            results = cur.fetchall()

            if results:
                for row in results:
                    bug_text_area.insert(tk.END, f"Bug ID: {row[0]}, Description: {row[1]}, Assignee: {row[2]}, Status: {row[3]}\n\n")
            else:
                bug_text_area.insert(tk.END, "No bugs found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

        back_button = tk.Button(self, text="Back", command=self.work_screen)
        back_button.pack(pady=10)

    def bug_report(self):
        self.clear_screen()
        label = tk.Label(self, text="Bug Report", font=("Helvetica", 18))
        label.pack(pady=10)

        bug_id_label = tk.Label(self, text="Enter Bug ID:")
        bug_id_label.pack()
        self.bug_id_entry = tk.Entry(self)
        self.bug_id_entry.pack()

        report_button = tk.Button(self, text="Generate Report", command=self.generate_bug_report)
        report_button.pack(pady=10)

        back_button = tk.Button(self, text="Back", command=self.work_screen)
        back_button
