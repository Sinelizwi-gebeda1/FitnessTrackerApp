import customtkinter as ctk
from tkinter import messagebox
import subprocess
import sys

class ScheduleApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Exercise Schedule")
        self.geometry("800x600")
        self.selected_days = []

        self.create_widgets()

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text="Exercise Schedule", font=("Helvetica", 24))
        title_label.pack(pady=20)

        # List of days
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.check_vars = [ctk.BooleanVar(value=False) for _ in self.days]  # Create a list to hold BooleanVars for each checkbox

        # Create checkboxes for each day
        for day, var in zip(self.days, self.check_vars):
            checkbox = ctk.CTkCheckBox(self, text=day, variable=var)
            checkbox.pack(pady=5)

        # Submit Button
        submit_button = ctk.CTkButton(self, text="Submit Schedule", command=self.submit_schedule, corner_radius=10)
        submit_button.pack(pady=20)

    def submit_schedule(self):
        self.selected_days = [day for day, var in zip(self.days, self.check_vars) if var.get()]
        if self.selected_days:
            # Save the selected days to the same line in the text file
            with open("FitnessData.txt", "a") as file:
                file.write("Selected days for exercise: " + ", ".join(self.selected_days) + " |\n "  )

            print("Selected days for exercise:", self.selected_days)
            messagebox.showinfo("Schedule Submitted", f"You have scheduled exercises on: {', '.join(self.selected_days)}")
            self.open_summary()  # Go to summary screen
        else:
            messagebox.showinfo("Schedule Submitted", "No days selected for exercise.")

    def open_summary(self):
        # Use subprocess to run summary.py
        subprocess.Popen(['python', 'summary.py', ', '.join(self.selected_days)])  # Pass the selected days
        self.quit()  # Close the current app

if __name__ == "__main__":
    app = ScheduleApp()
    app.mainloop()
