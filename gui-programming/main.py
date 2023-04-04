import tkinter as tk


def show_login():
    signup_form_frame.pack_forget()
    login_form_frame.pack()


def show_signup():
    signup_form_frame.pack()
    login_form_frame.pack_forget()


def signup():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    city = city_entry.get()
    address = address_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    verify_password = verify_password_entry.get()

    if not all([first_name, last_name, age, gender, city, address, username, password, verify_password]):
        error_var.set("Fill all the details!")
    elif not verify_password == password:
        error_var.set("Password does not match")
    else:
        error_var.set("")
        print(f"""
        Name: {first_name} {last_name}
        Age: {age}
        Gender: {gender}
        City: {city}
        Address: {address}
        username: {username}
        """)
        clear()


def clear():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("")
    city_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    verify_password_entry.delete(0, tk.END)
    error_var.set("")


def login():
    user = login_username_entry.get()
    print(f"Welcome {user}")


window = tk.Tk()
window.title("Doctor Appointment App")
window.geometry("400x425")

signup_form_frame = tk.Frame(window, padx=30, pady=10)

login_button = tk.Button(signup_form_frame, text="Switch to Login", command=show_login)
login_button.grid(row=0, column=0, columnspan=2, pady=5, sticky="E")

signup_label = tk.Label(signup_form_frame, text="Signup", font=("Arial Bold", 20))
signup_label.grid(row=1, column=0, columnspan=2, pady=5, sticky="W")

first_name_label = tk.Label(signup_form_frame, text="First Name:")
last_name_label = tk.Label(signup_form_frame, text="Last Name:")
age_label = tk.Label(signup_form_frame, text="Age:")
gender_label = tk.Label(signup_form_frame, text="Gender:")
city_label = tk.Label(signup_form_frame, text="City:")
address_label = tk.Label(signup_form_frame, text="Address:")
username_label = tk.Label(signup_form_frame, text="Username:")
password_label = tk.Label(signup_form_frame, text="Password:")
verify_password_label = tk.Label(signup_form_frame, text="Verify Password:")

first_name_entry = tk.Entry(signup_form_frame)
last_name_entry = tk.Entry(signup_form_frame)
age_entry = tk.Entry(signup_form_frame)
city_entry = tk.Entry(signup_form_frame)
address_entry = tk.Entry(signup_form_frame)
username_entry = tk.Entry(signup_form_frame)
password_entry = tk.Entry(signup_form_frame, show="*")
verify_password_entry = tk.Entry(signup_form_frame, show="*")

gender_var = tk.StringVar()
male_radio = tk.Radiobutton(signup_form_frame, text="Male", variable=gender_var, value="Male")
female_radio = tk.Radiobutton(signup_form_frame, text="Female", variable=gender_var, value="Female")
other_radio = tk.Radiobutton(signup_form_frame, text="Other", variable=gender_var, value="Other")

first_name_label.grid(row=2, column=0, sticky="W")
first_name_entry.grid(row=2, column=1)
last_name_label.grid(row=3, column=0, sticky="W")
last_name_entry.grid(row=3, column=1)
age_label.grid(row=4, column=0, sticky="W")
age_entry.grid(row=4, column=1)
gender_label.grid(row=5, column=0, sticky="W")
male_radio.grid(row=5, column=1, sticky="W")
female_radio.grid(row=6, column=1, sticky="W")
other_radio.grid(row=7, column=1, sticky="W")
city_label.grid(row=8, column=0, sticky="W")
city_entry.grid(row=8, column=1)
address_label.grid(row=9, column=0, sticky="W")
address_entry.grid(row=9, column=1)
username_label.grid(row=10, column=0, sticky="W")
username_entry.grid(row=10, column=1)
password_label.grid(row=11, column=0, sticky="W")
password_entry.grid(row=11, column=1)
verify_password_label.grid(row=12, column=0, sticky="W")
verify_password_entry.grid(row=12, column=1)

signup_button = tk.Button(signup_form_frame, text="Signup", command=signup)
signup_button.grid(row=13, column=0, pady=10)
clear_button = tk.Button(signup_form_frame, text="Clear", command=clear)
clear_button.grid(row=13, column=1, pady=10)

error_var = tk.StringVar()
error_label = tk.Label(signup_form_frame, textvariable=error_var, fg="red")
error_label.grid(row=14, columnspan=2)

signup_form_frame.pack()

login_form_frame = tk.Frame(window, padx=30, pady=10)

signup_button = tk.Button(login_form_frame, text="Switch to Signup", command=show_signup)
signup_button.grid(row=0, column=0, columnspan=2, pady=5, sticky="E")

login_label = tk.Label(login_form_frame, text="Signup", font=("Arial Bold", 20))
login_label.grid(row=1, column=0, columnspan=2, pady=5, sticky="W")

login_username_label = tk.Label(login_form_frame, text="Username:")
login_password_label = tk.Label(login_form_frame, text="Password:")

login_username_entry = tk.Entry(login_form_frame)
login_password_entry = tk.Entry(login_form_frame, show="*")

login_username_label.grid(row=2, column=0, sticky="W")
login_username_entry.grid(row=2, column=1)
login_password_label.grid(row=3, column=0, sticky="W")
login_password_entry.grid(row=3, column=1)

login_button = tk.Button(login_form_frame, text="Login", command=login)
login_button.grid(row=4, column=0, columnspan=2, sticky="ew", pady=10)

window.mainloop()
