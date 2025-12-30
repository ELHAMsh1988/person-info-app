import tkinter as tk
from tkinter import colorchooser, messagebox


class PersonInfoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Person Info App")
        self.root.geometry("400x450")

        self.selected_color = "#ffffff"

        self.build_ui()
        self.root.mainloop()

    def build_ui(self):
        frame = tk.LabelFrame(
            self.root,
            text="Person Information",
            font=("Arial", 14, "bold"),
            padx=10,
            pady=10
        )
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Name
        tk.Label(frame, text="First Name").pack(anchor="w")
        self.name_entry = tk.Entry(frame)
        self.name_entry.pack(fill="x")

        # Family
        tk.Label(frame, text="Family Name").pack(anchor="w")
        self.family_entry = tk.Entry(frame)
        self.family_entry.pack(fill="x")

        # Age
        tk.Label(frame, text="Age").pack(anchor="w")
        self.age_spin = tk.Spinbox(frame, from_=0, to=100)
        self.age_spin.pack(fill="x")

        # Gender
        tk.Label(frame, text="Gender").pack(anchor="w")
        self.gender_var = tk.IntVar(value=1)
        tk.Radiobutton(frame, text="Female", variable=self.gender_var, value=1).pack(anchor="w")
        tk.Radiobutton(frame, text="Male", variable=self.gender_var, value=2).pack(anchor="w")

        # Color picker
        self.color_btn = tk.Button(
            frame,
            text="Choose Favorite Color",
            command=self.choose_color
        )
        self.color_btn.pack(pady=10)

        # Submit
        submit_btn = tk.Button(
            frame,
            text="Submit",
            command=self.submit_data,
            bg="#4CAF50",
            fg="white"
        )
        submit_btn.pack(pady=10)

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Color")
        if color[1]:
            self.selected_color = color[1]
            self.color_btn.config(bg=self.selected_color)

    def submit_data(self):
        data = {
            "name": self.name_entry.get(),
            "family": self.family_entry.get(),
            "age": self.age_spin.get(),
            "gender": "Female" if self.gender_var.get() == 1 else "Male",
            "color": self.selected_color
        }

        print("Person Info:")
        for key, value in data.items():
            print(f"{key}: {value}")

        messagebox.showinfo("Saved", "Information saved successfully!")


if __name__ == "__main__":
    PersonInfoApp()
