
from tkinter import *
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button, Entry, Label, Frame
from PIL import Image, ImageTk
import subprocess
import sqlite3
import hashlib
import re

# Toggle password visibility
def toggle_password_visibility(event=None):
    global show_password
    show_password = not show_password
    if show_password:
        code.config(show="")
        show_password_icon.config(image=hide_password_icon_image)
    else:
        code.config(show="*")
        show_password_icon.config(image=show_password_icon_image)

# Clear entry text when clicked
def clear_entry(event):
    if event.widget.get() == 'Email' or event.widget.get() == 'Username' or event.widget.get() == 'Password':
        event.widget.delete(0, 'end')
        event.widget.config(fg='black')

# Open the login page using subprocess
def navigate_to_login():
    print("Navigating to login page...")
    subprocess.run(["python", "login.py"]) 
    print("Login page opened")  
    root.destroy()


def is_valid_email(email):
    # Regular expression for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # If the string is empty, it's not a valid email
    if email == "":
        return False

    # If the string matches the regular expression, it's a valid email
    if re.fullmatch(regex, email):
        return True
    else:
        return False



def sign_up():
    global current_user
    email = emailid.get()  # Assuming emailid is the Entry widget for email
    username = user.get()
    password = code.get()
    try:
        conn = sqlite3.connect('Form.db')
        if not is_valid_email(email):
            Messagebox.show_error("Invalid email address. Please enter a valid email.","Invalid Email")
            print("Invalid email address. Please enter a valid email.")
            return
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users(email, username, password) VALUES(?, ?, ?)
        """, (email, username, hashed_password))
        conn.commit()
        conn.close()
        Messagebox.show_info("Sign Up Successful!", "Sign Up")
        current_user = username  # Set current_user after successful sign up
        print("Debug: Current user set to", current_user)
        root.destroy()  
        navigate_to_recommendation(username)
    except Exception as e:
        print(e)
        Messagebox.show_error("Sign Up Failed", "An error occurred while signing up")

def navigate_to_recommendation(username):
    global current_user
    if current_user is not None:
        print(f"Debug: Received username in recommendation: {current_user}")
        subprocess.run(["python", "recommendation.py", current_user])  # Pass current_user here
    else:
        print("Error: Current user is not set.")

root = Tk()
root.title('Sign Up')
root.geometry('925x500+300+200')
root.resizable(False, False)

style = Style(theme='lumen')

# Create a frame for the image
image_frame = Frame(root, width=400, height=500, bootstyle="dark")
image_frame.place(x=40, y=0)

# Add an image to the image frame
image_path = "./assets/authentication.png"  # Adjust the path to your image
login_image = Image.open(image_path)
login_image = login_image.resize((400, 500))  # Resize the image to fit the frame
login_image = ImageTk.PhotoImage(login_image)

image_label = Label(image_frame, image=login_image)
image_label.place(x=0, y=0)

# Create the sign-up frame
signup_frame = Frame(root, width=350, height=350)
signup_frame.place(x=480, y=70)

heading = Label(signup_frame, text='Sign Up', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=120, y=5)

# Email Entry
emailid = Entry(signup_frame, width=25, font=('Microsoft yaHei UI Light', 11),foreground='black')
emailid.place(x=65, y=80)
emailid.insert(0, 'Email')
emailid.bind("<FocusIn>", clear_entry)

# Username Entry
user = Entry(signup_frame, width=25, font=('Microsoft yaHei UI Light', 11),foreground='black')
user.place(x=65, y=130)
user.insert(0, 'Username')
user.bind("<FocusIn>", clear_entry)

# Password Entry
code = Entry(signup_frame, width=25, font=('Microsoft yaHei UI Light', 11), show='*',foreground='black')
code.place(x=65, y=180)
code.insert(0, 'Password')
code.bind("<FocusIn>", clear_entry)


show_password_icon_image = Image.open("./assets/view_709612.png")
hide_password_icon_image = Image.open("./assets/hidden_2355322.png")

show_password_icon_image = show_password_icon_image.resize((24, 24))
hide_password_icon_image = hide_password_icon_image.resize((24, 24))


show_password_icon_image = ImageTk.PhotoImage(show_password_icon_image)
hide_password_icon_image = ImageTk.PhotoImage(hide_password_icon_image)

show_password_icon = Label(signup_frame, image=show_password_icon_image)
show_password_icon.place(x=305, y=185)
show_password_icon.bind("<Button-1>", toggle_password_visibility)

show_password = False


signup_button = Button(signup_frame, width=20, text='Sign up', command=sign_up, padding='7')
signup_button.place(x=100, y=234)

label = Label(signup_frame, text="Already have an account ?", font=('Microsoft yaHei UI Light', 9))
label.place(x=60, y=300)

# Use a button to navigate to the login page
login_button = Button(signup_frame, width=7, text='Login',  command=navigate_to_login)
login_button.place(x=220, y=300)

style.map('TEntry', foreground=[
    ('disabled', 'gray'),
    ('focus !disabled', 'white'),
    ('hover !disabled', 'yellow')
])

root.mainloop()
