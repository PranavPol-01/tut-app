
# copilot codefrom tkinter import *
from tkinter import *
from PIL import Image, ImageTk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button, Entry, Frame
from ttkbootstrap.dialogs import Messagebox
import subprocess
import sqlite3
import hashlib

# current_user = None



# Toggle password visibility
def toggle_password_visibility():
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
    if event.widget.get() == 'Username' or event.widget.get() == 'Password':
        event.widget.delete(0, 'end')
        event.widget.config(fg='black')

# Open the signup page using subprocess
def sign_up():
    print("Navigating to signup page...")  # Debug message    
    print("Signup page opened")  # Debug message    
    create_database()
    root.destroy()
    subprocess.run(["python", "signup.py"])
    
    
def create_database():
    conn = sqlite3.connect('Form.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        email TEXT NOT NULL,                   
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        token TEXT
    )""")
    conn.commit()
    conn.close()
    print("Database created successfully!")


def sign_in():
    global current_user
    username = user.get()
    password = code.get()
    
    
    # Hash the password entered by the user
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect('Form.db')
    cursor = conn.cursor()

    # Fetch the hashed password from the database
    cursor.execute("SELECT username FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    result = cursor.fetchone()

    if result is not None:
        current_user = username  # Set current_user after successful login
        print("Debug: Current user set to", current_user)
        Messagebox.show_info("Welcome, " + username + "!", "Login Successful")
        root.destroy()
        navigate_to_recommendation(username)  # Pass only username here
        
    else:
        Messagebox.show_error("Invalid username or password", "Login Failed")
        print("Debug: Login failed for username", username)
    conn.close()

def navigate_to_recommendation(username):
    global current_user
    if current_user is not None:
        print(f"Debug: Received username in recommendation: {current_user}")
        subprocess.run(["python", "recommendation.py", current_user])  # Pass current_user here
    else:
        print("Error: Current user is not set.")    

def reset_password():
    root.destroy()
    subprocess.run(["python", "reset_password.py"])
   

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.resizable(False, False)

style = Style(theme='lumen')

# Create a frame for the image
image_frame = Frame(root, width=400, height=500)
image_frame.place(x=40, y=0)

# Add an image to the image frame
image_path = "./assets/authentication.png"  # Adjust the path to your image
login_image = Image.open(image_path)
login_image = login_image.resize((400, 500))  # Resize the image to fit the frame
login_image = ImageTk.PhotoImage(login_image)

image_label = Label(image_frame, image=login_image)
image_label.place(x=0, y=0)

# Create the login frame
login_frame = Frame(root, width=350, height=350)
login_frame.place(x=480, y=70)

heading = Label(login_frame, text='Sign in', font=('Microsoft YaHei UI Light', 23, 'bold'),fg='black')
heading.place(x=120, y=5)

user = Entry(login_frame, width=25, font=('Microsoft yaHei UI Light', 11),foreground='black')
user.place(x=65, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", clear_entry)

code = Entry(login_frame, width=25, font=('Microsoft yaHei UI Light', 11), show='*',foreground='black')
code.place(x=65, y=130)
code.insert(0, 'Password')
code.bind("<FocusIn>", clear_entry)

# Show/hide password icon
# Load the eye icons using PIL
show_password_icon_image = Image.open("./assets/view_709612.png")
hide_password_icon_image = Image.open("./assets/hidden_2355322.png")

# Resize the images if needed
show_password_icon_image = show_password_icon_image.resize((24, 24))
hide_password_icon_image = hide_password_icon_image.resize((24, 24))

# Convert images to Tkinter PhotoImage objects
show_password_icon_image = ImageTk.PhotoImage(show_password_icon_image)
hide_password_icon_image = ImageTk.PhotoImage(hide_password_icon_image)

# Create a label to display the eye icon
show_password_icon = Label(login_frame, image=show_password_icon_image)
show_password_icon.place(x=305, y=135)  # Adjusted position slightly
show_password_icon.bind("<Button-1>", lambda event: toggle_password_visibility())

# Flag to track whether password is visible or not
show_password = False

signin = Button(login_frame, width=20, text='Sign in', command=sign_in, padding='7')
signin.place(x=100, y=184)

label = Label(login_frame, text="Don't have an account ?", font=('Microsoft yaHei UI Light', 9))
label.place(x=60, y=250)

# Use a button to open the signup page
sign_up_button = Button(login_frame, width=7, text='Sign up', command=sign_up)
sign_up_button.place(x=210, y=250)

reset_password_button = Button(login_frame, width=20, text='Reset Password', padding='7',command=reset_password)
reset_password_button.place(x=100, y=300)
# Map foreground color for Entry widget
style.map('TEntry', foreground=[
    ('disabled', 'gray'),
    ('focus !disabled', 'white'),
    ('hover !disabled', 'yellow')
])

root.mainloop()
