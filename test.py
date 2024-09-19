import mysql.connector as mysql
import modules as easy  
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox, scrolledtext

# Connect to MySQL
db = mysql.connect(host="localhost", user="root", passwd="nishidh@123", database="bug_tracking")
cur = db.cursor()  # Creating cursor
class BugManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bug Management System")
        self.geometry("500x500")
        
        self.main_screen()

    def main_screen(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Bug Tracking System", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.login_button = tk.Button(self, text="Login", command=self.login_screen)
        self.login_button.pack(pady=5)

        self.signup_button = tk.Button(self, text="Sign Up", command=self.signup_screen)
        self.signup_button.pack(pady=5)

        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
    
    def login_screen(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Login", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.verify_login)
        self.login_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.main_screen)
        self.back_button.pack(pady=10)

    def signup_screen(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Sign Up", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.username_label = tk.Label(self, text="Name:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.signup_button = tk.Button(self, text="Sign Up", command=self.verify_signup)
        self.signup_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.main_screen)
        self.back_button.pack(pady=10)

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
            cur.execute(f"insert into userinfo (username,password,email,hash) values ('{username}', '{password}', '{email}', '{easy.hashID()}')")
            db.commit()
            messagebox.showinfo("Success", "Signed up successfully!")
            self.login_screen()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def work_screen(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Bug Management", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.add_bug_button = tk.Button(self, text="Add Bug", command=self.add_bug)
        self.add_bug_button.pack(pady=5)

        self.switch_assignees_button = tk.Button(self, text="Switch Assignees", command=self.switch_assignees)
        self.switch_assignees_button.pack(pady=5)

        self.bug_report_button = tk.Button(self, text="Bug Report", command=self.bug_report)
        self.bug_report_button.pack(pady=5)

        self.view_all_bugs_button = tk.Button(self, text="View All Bugs", command=self.view_all_bugs)
        self.view_all_bugs_button.pack(pady=5)

        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack(pady=5)

    def add_bug(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Add Bug", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.bug_id_label = tk.Label(self, text="Enter BugID :")
        self.bug_id_label.pack()
        self.bug_id_entry_label = tk.Entry(self)
        self.bug_id_entry_label.pack()

        self.bug_description_label = tk.Label(self, text="Bug Description:")
        self.bug_description_label.pack()
        self.bug_description_entry = tk.Entry(self)
        self.bug_description_entry.pack()

        self.severity_label = tk.Label(self, text="Enter Severity :")
        self.severity_label.pack()
        self.severity_entry_label = tk.Entry(self)
        self.severity_entry_label.pack()

        self.req_days_label = tk.Label(self, text="Enter no. of expected days :")
        self.req_days_label.pack()
        self.req_days_entry_label = tk.Entry(self)
        self.req_days_entry_label.pack()

        self.priority_label = tk.Label(self, text="Enter Priority :")
        self.priority_label.pack()
        self.priority_entry_label = tk.Entry(self)
        self.priority_entry_label.pack()

        self.assignee_label = tk.Label(self, text="Assignee:")
        self.assignee_label.pack()
        self.assignee_entry = tk.Entry(self)
        self.assignee_entry.pack()

        self.status_label = tk.Label(self, text="Bug Status (1-5):")
        self.status_label.pack()
        self.status_entry = tk.Entry(self)
        self.status_entry.pack()
        
        self.label = tk.Label(self, text="Select Date for Bug Entry")
        self.label.pack()

        # Adding DateEntry widget for date selection
        self.date_label = tk.Label(self, text="Bug Date:")
        self.date_label.pack(pady=5)
        self.date_entry = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.pack(pady=5)


        self.submit_button = tk.Button(self, text="Submit", command=self.submit_bug)
        self.submit_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.work_screen)
        self.back_button.pack(pady=10)

    def submit_bug(self):
        bugID = self.bug_id_entry_label.get()
        severity = self.severity_entry_label.get()
        days = self.req_days_entry_label.get()
        priority = self.priority_entry_label.get()
        description = self.bug_description_entry.get()
        assignee = self.assignee_entry.get()
        status = self.status_entry.get()
        selected_date = self.date_entry.get_date()
        print("Data:", bugID, severity, days, priority, description, assignee, status, selected_date)

        try:
            cur.execute(f"INSERT INTO buginfo (bugID,bugstatus,bugdesc,severity,reqdays,opendt,priority) VALUES ('{bugID}',{status},'{description}', '{severity}', {days},'{selected_date}',{priority})")
            db.commit()
            messagebox.showinfo("Success", "Bug added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def switch_assignees(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Switch Assignees", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.bug_id_label = tk.Label(self, text="Bug ID:")
        self.bug_id_label.pack()
        self.bug_id_entry = tk.Entry(self)
        self.bug_id_entry.pack()

        self.new_assignee_label = tk.Label(self, text="New Assignee:")
        self.new_assignee_label.pack()
        self.new_assignee_entry = tk.Entry(self)
        self.new_assignee_entry.pack()

        self.switch_button = tk.Button(self, text="Switch", command=self.submit_switch_assignee)
        self.switch_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.work_screen)
        self.back_button.pack(pady=10)

    def submit_switch_assignee(self):
        bug_id = self.bug_id_entry.get()
        new_assignee = self.new_assignee_entry.get()

        try:
            cur.execute(f"UPDATE buginfo SET assignee='{new_assignee}' WHERE bugID='{bug_id}'")
            db.commit()
            messagebox.showinfo("Success", "Assignee switched successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def bug_report(self):
        self.clear_screen()
        self.label = tk.Label(self, text="Bug Report", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.bug_id_label = tk.Label(self, text="Enter Bug ID:")
        self.bug_id_label.pack()
        self.bug_id_entry = tk.Entry(self)
        self.bug_id_entry.pack()

        self.report_button = tk.Button(self, text="Generate Report", command=self.generate_bug_report)
        self.report_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back", command=self.work_screen)
        self.back_button.pack(pady=10)

    def generate_bug_report(self):
        bug_id = self.bug_id_entry.get()

        try:
            cur.execute(f"SELECT * FROM buginfo WHERE bugID='{bug_id}'")
            result = cur.fetchone()

            if result:
                report = f"Bug ID: {result[0]}\nDescription: {result[1]}\nAssignee: {result[2]}\nStatus: {result[3]}"
                messagebox.showinfo("Bug Report", report)
            else:
                messagebox.showerror("Error", "No bug found with the given ID")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def view_all_bugs(self):
        self.clear_screen()
        self.label = tk.Label(self, text="All Bugs", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.bug_text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=15)
        self.bug_text_area.pack(pady=10)

        try:
            cur.execute(f"SELECT * FROM buginfo")
            results = cur.fetchall()

            if results:
                for row in results:
                    self.bug_text_area.insert(tk.END, f"Bug ID: {row[0]}, Description: {row[1]}, Assignee: {row[2]}, Status: {row[3]}\n\n")
            else:
                self.bug_text_area.insert(tk.END, "No bugs found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

        self.back_button = tk.Button(self, text="Back", command=self.work_screen)
        self.back_button.pack(pady=10)

    def logout(self):
        self.main_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

# Running the Application
if __name__ == "__main__":
    app = BugManagementApp()
    app.mainloop()
