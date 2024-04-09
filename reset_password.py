# from tkinter import *
# from ttkbootstrap import *
# from ttkbootstrap.dialogs import Messagebox
# import sqlite3
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import random
# import string
# import hashlib

# def send_email(email, token):
#     msg = MIMEMultipart()
#     msg['From'] = '2022.your.account@ves.ac.in' # Your email address use only ves account
#     msg['To'] = email
#     msg['Subject'] = 'Password Reset Request'
#     body = 'Your token is {}'.format(token)
#     msg.attach(MIMEText(body, 'plain'))

#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(msg['From'], 'YourPassword123') # Your password. But pls enable less secure app to use this feature
#     server.sendmail(msg['From'], msg['To'], msg.as_string())
#     server.quit()

# def reset_password_request():
#     email = email_entry.get()
#     conn = sqlite3.connect('Form.db')
#     c = conn.cursor()
#     c.execute('SELECT * FROM users WHERE email = ?', (email,))
#     if c.fetchone() is not None:
#         token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
#         c.execute('UPDATE users SET token = ? WHERE email = ?', (token, email))
#         conn.commit()
#         send_email(email, token)
#         Messagebox.show_info('Info', 'Email sent!')
#     else:
#         Messagebox.show_error('Info', 'Email not found!')

# def reset_password():
#     email = email_entry.get()
#     token = token_entry.get()
#     new_password = password_entry.get()
#     hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
#     conn = sqlite3.connect('Form.db')
#     c = conn.cursor()
#     c.execute('SELECT * FROM users WHERE email = ? AND token = ?', (email, token))
#     if c.fetchone() is not None:
#         c.execute('UPDATE users SET password = ? WHERE email = ?', (hashed_password, email))
#         conn.commit()
#         Messagebox.show_info('Info', 'Password reset successful!')
#     else:
#         Messagebox.show_error('Info', 'Invalid token!')

# root = Tk()
# style = Style(theme='superhero')
# email_label = ttk.Label(root, text='Email')
# email_label.pack()
# email_entry = ttk.Entry(root)
# email_entry.pack()

# token_label = ttk.Label(root, text='Token')
# token_label.pack()
# token_entry = ttk.Entry(root)
# token_entry.pack()

# password_label = ttk.Label(root, text='New Password')
# password_label.pack()
# password_entry = ttk.Entry(root, show='*')
# password_entry.pack()

# reset_password_request_button = ttk.Button(root, text='Reset Password Request', command=reset_password_request)
# reset_password_request_button.pack()

# reset_password_button = ttk.Button(root, text='Reset Password', command=reset_password)
# reset_password_button.pack()

# style.map('TEntry', foreground=[
#     ('disabled', 'gray'),
#     ('focus !disabled', 'white'),
#     ('hover !disabled', 'yellow')
# ])

# root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button, Entry, Label, Frame
from ttkbootstrap.dialogs import Messagebox
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string
import hashlib

def send_email(email, token):
    msg = MIMEMultipart()
    msg['From'] = '2022.pranav.account@ves.ac.in' # Your email address use only ves account
    msg['To'] = email
    msg['Subject'] = 'Password Reset Request'
    body = 'Your token is {}'.format(token)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], 'YourPassword123') # Your password. But pls enable less secure app to use this feature
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

def reset_password_request():
    email = email_entry.get()
    conn = sqlite3.connect('Form.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ?', (email,))
    if c.fetchone() is not None:
        token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        c.execute('UPDATE users SET token = ? WHERE email = ?', (token, email))
        conn.commit()
        send_email(email, token)
        Messagebox.show_info('Info', 'Email sent!')
    else:
        Messagebox.show_error('Info', 'Email not found!')

def reset_password():
    email = email_entry.get()
    token = token_entry.get()
    new_password = password_entry.get()
    hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
    conn = sqlite3.connect('Form.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ? AND token = ?', (email, token))
    if c.fetchone() is not None:
        c.execute('UPDATE users SET password = ? WHERE email = ?', (hashed_password, email))
        conn.commit()
        Messagebox.show_info('Info', 'Password reset successful!')
    else:
        Messagebox.show_error('Info', 'Invalid token!')

root = Tk()
root.title('Reset Password')
root.geometry('925x500+300+200')
root.resizable(False, False)

style = Style(theme='lumen')

# Create the image frame
image_frame = Frame(root, width=400, height=500, bootstyle="dark")
image_frame.place(x=40, y=0)

# Add an image to the image frame
image_path = "./assets/authentication.png"  # Adjust the path to your image
reset_image = Image.open(image_path)
reset_image = reset_image.resize((400, 500))  # Resize the image to fit the frame
reset_image = ImageTk.PhotoImage(reset_image)

image_label = Label(image_frame, image=reset_image)
image_label.place(x=0, y=0)

# Create the reset password frame
reset_frame = Frame(root)
reset_frame.place(x=480, y=70, width=550, height=700)

heading = Label(reset_frame, text='Reset Password', font=('Microsoft YaHei UI Light', 23, 'bold'),padding=1)
heading.place(x=90, y=-11)

email_label = Label(reset_frame, text='Email', font=('Microsoft YaHei UI Light', 11))
email_label.place(x=70, y=40)
email_entry = Entry(reset_frame, width=30, font=('Microsoft yaHei UI Light', 11),foreground='black')
email_entry.place(x=70, y=70)

token_label = Label(reset_frame, text='Token', font=('Microsoft YaHei UI Light', 11))
token_label.place(x=70, y=110)
token_entry = Entry(reset_frame, width=30, font=('Microsoft yaHei UI Light', 11),foreground='black')
token_entry.place(x=70, y=140)

password_label = Label(reset_frame, text='New Password', font=('Microsoft YaHei UI Light', 11))
password_label.place(x=70, y=180)
password_entry = Entry(reset_frame, width=30, font=('Microsoft yaHei UI Light', 11), show='*',foreground='black')
password_entry.place(x=70, y=210)

reset_password_request_button = Button(reset_frame, width=25, text='Reset Password Request', command=reset_password_request)
reset_password_request_button.place(x=105, y=280)

reset_password_button = Button(reset_frame, width=25, text='Reset Password', command=reset_password)
reset_password_button.place(x=105, y=350)

style.map('TEntry', foreground=[
    ('disabled', 'gray'),
    ('focus !disabled', 'white'),
    ('hover !disabled', 'yellow')
])

root.mainloop()
