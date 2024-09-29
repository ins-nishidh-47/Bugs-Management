import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox

class BugManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bug Management System with Date Picker")
        self.geometry("500x300")
        
        self.label = tk.Label(self, text="Select Date for Bug Entry", font=("Helvetica", 14))
        self.label.pack(pady=10)

        # Adding DateEntry widget for date selection
        self.date_label = tk.Label(self, text="Bug Date:")
        self.date_label.pack(pady=5)
        self.date_entry = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.pack(pady=5)

        # A button to submit the selected date and handle further logic
        self.submit_button = tk.Button(self, text="Submit Date", command=self.submit_date)
        self.submit_button.pack(pady=10)

    def submit_date(self):
        selected_date = self.date_entry.get_date()  # Get the selected date
        messagebox.showinfo("Selected Date", f"Bug Date: {selected_date}")

# Running the Application
if __name__ == "__main__":
    app = BugManagementApp()
    app.mainloop()
