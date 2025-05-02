import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_var.get()
    email = email_var.get()
    gender = gender_var.get()
    country = country_var.get()
    langs = []
    if python_var.get(): langs.append("Python")
    if java_var.get(): langs.append("Java")
    if not name or not email:
        messagebox.showwarning("Validation Error", "Please fill all fields")
    else:
        info = f"Name: {name}\nEmail: {email}\nGender: {gender}\nCountry: {country}\nLanguages: {', '.join(langs)}"
        messagebox.showinfo("Registration Info", info)

root = tk.Tk()
root.title("Registration Form")

name_var = tk.StringVar()
email_var = tk.StringVar()
gender_var = tk.StringVar(value="Male")
country_var = tk.StringVar()
python_var = tk.BooleanVar()
java_var = tk.BooleanVar()

tk.Entry(root, textvariable=name_var).pack()
tk.Entry(root, textvariable=email_var).pack()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.OptionMenu(root, country_var, "India", "USA", "UK").pack()
tk.Checkbutton(root, text="Python", variable=python_var).pack()
tk.Checkbutton(root, text="Java", variable=java_var).pack()
tk.Button(root, text="Submit", command=submit).pack()

root.mainloop()
