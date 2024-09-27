import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Retrieve form data
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    password = entry_password.get()
    
    # Display submitted data
    messagebox.showinfo("Registration Info", f"Name: {first_name} {last_name}\nEmail: {email}\nPhone: {phone}")
    
    # Store the data, e.g., in a file or database
    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'password': password
    }

# Create the main application window
root = tk.Tk()
root.title("Registration Form")

# First Name
label_first_name = tk.Label(root, text="First Name:")
label_first_name.grid(row=0, column=0)
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1)

# Last Name
label_last_name = tk.Label(root, text="Last Name:")
label_last_name.grid(row=1, column=0)
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1)

# Email
label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

# Phone
label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=3, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=3, column=1)

# Password
label_password = tk.Label(root, text="Password:")
label_password.grid(row=4, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=4, column=1)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, column=1)

# Start the Tkinter main loop
root.mainloop()
