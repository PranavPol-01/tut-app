# import tkinter as tk
# from tkinter import ttk
# from ttkbootstrap import Style
# import subprocess
# from PIL import Image, ImageTk



# class CongratulationsPage(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.title("Congratulations")

#         # Create a Style object to use with ttkbootstrap
#         self.style = Style(theme="superhero")

#         # Set background color to white
#         self.configure(bg="#ffffff")  # White background color

#         # Message Label with customized text color and background color
#         self.message_label = ttk.Label(self, text="Congrats! You completed the assessment.", font=("Helvetica", 20), foreground="#000000", background="#ffffff")
#         self.message_label.pack(pady=50)

#         # # Green Tick Image
#         # self.blue_tick_image = tk.PhotoImage(file="greentick.png")  # Replace with the path to your blue tick image
#         # self.resized_image = self.blue_tick_image.subsample(4,4)
#         # self.blue_tick_label = ttk.Label(self, image=self.resized_image, background="#ffffff")
#         # self.blue_tick_label.pack()

#         # Green Tick Image
#         # self.blue_tick_image = tk.PhotoImage(file=".\greentick.png")  # Replace with the path to your blue tick image
#         # self.resized_image = self.blue_tick_image.subsample(4,4)
#         # self.blue_tick_label = ttk.Label(self, image=self.resized_image, background="#ffffff")
#         # self.blue_tick_label.image = self.resized_image  # Keep a reference to the image
#         # self.blue_tick_label.pack()

#         image= Image.open(".\greentick.png")
#         image = image.resize((100, 100), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         self.blue_tick_label = ttk.Label(self, image=photo, background="#ffffff")
#         self.blue_tick_label.image = photo  # Keep a reference to the image
#         self.blue_tick_label.pack()
        # Green Tick Image
        # self.blue_tick_image = tk.PhotoImage(file="./greentick.png")  # Replace with the path to your blue tick image
        # self.resized_image = self.blue_tick_image.subsample(4,4)
        # self.blue_tick_label = ttk.Label(self, image=self.resized_image, background="#ffffff")
        # self.blue_tick_label.image = self.resized_image  # Keep a reference to the image
        # self.blue_tick_label.pack()







#         # Frame to contain the buttons
#         self.button_frame = ttk.Frame(self)
#         self.button_frame.pack(pady=30)

#         # Deny Button with customized background and text color
#         self.take_test_button = ttk.Button(self.button_frame, text="No! Thanks", command=self.additional_action, style="success.Outline")
#         self.take_test_button.pack(side=tk.LEFT, padx=10)

#         def on_take_test_button_clicked():
#             self.additional_action()
#             subprocess.run(["python", "quiz.py"])
#             #quiz.QuizApp()

#         # Take Test Button
#         self.additional_button = ttk.Button(self.button_frame, text="Take Test", command=on_take_test_button_clicked, style="success.Outline")
#         self.additional_button.pack(side=tk.LEFT, padx=30)

#         # def on_take_test_button_clicked():
#         #     self.additional_action()        
            
            

#         # self.additional_button = ttk.Button(self.button_frame, text="Take Test", style="success.Outline")
#         # self.additional_button.pack(side=tk.LEFT, padx=30)

#     def take_test(self):
#         print("Redirecting to the test page...")
#           # Placeholder for redirection functionality
#         subprocess.call(["python", "quiz.py"])
#     def additional_action(self):
#         print("Additional button clicked.")  # Placeholder for additional button functionality
#         subprocess.call(["python", "recommendation.py"])

# app = CongratulationsPage()
# app.mainloop()


# import tkinter as tk
# import ttkbootstrap as ttk
# from ttkbootstrap.widgets import *
# from ttkbootstrap import Style
# import subprocess
# import quiz
# from PIL import Image, ImageTk
# from ttkbootstrap.constants import *

# def take_test():
#     print("Redirecting to the test page...")
#     root.destroy()
#     # subprocess.run(["python", "quiz.py"])
#     quiz.QuizApp()

# def additional_action():
#     print("Additional button clicked.")
    

# root = tk.Tk()
# root.title("Congratulations")
# root.geometry("600x400")

# # Create a Style object to use with ttkbootstrap
# style = Style(theme="lumen")

# # Set background color to white
# root.configure(bg="#ffffff")  # White background color

# success_frame = Frame(root, width=350, height=350)
# success_frame.place(relx=0.5, rely=0.5, anchor= tk.CENTER)

# # Message Label with customized text color and background color
# message_label = ttk.Label(root, text="Congrats! You completed the assessment.", font=("Helvetica", 20), foreground="#000000", background="#ffffff")
# message_label.pack(pady=50)

# # Green Tick Image
# image = Image.open("greentick.png")
# image = image.resize((100, 100), Image.LANCZOS)
# photo = ImageTk.PhotoImage(image)
# blue_tick_label = ttk.Label(root, image=photo, background="#ffffff")
# blue_tick_label.image = photo
# blue_tick_label.pack()

# # Frame to contain the buttons
# button_frame = ttk.Frame(root)
# button_frame.pack(pady=30)

# # Deny Button with customized background and text color
# take_test_button = ttk.Button(button_frame, text="No! Thanks", command=additional_action, style="success.Outline")
# take_test_button.pack(side=tk.LEFT, padx=10)

# # Take Test Button
# additional_button = ttk.Button(button_frame, text="Take Test", command=take_test, style="success.Outline")
# additional_button.pack(side=tk.LEFT, padx=30)

# root.mainloop()



# import tkinter as tk
# from ttkbootstrap import widgets as ttk  # Corrected import statement
# from ttkbootstrap import Style
# from PIL import Image, ImageTk
# from ttkbootstrap.constants import *
# import quiz

# def take_test():
#     print("Redirecting to the test page...")
#     root.destroy()
#     # subprocess.run(["python", "quiz.py"])
#     quiz.QuizApp()

# def additional_action():
#     print("Additional button clicked.")

# root = tk.Tk()
# root.title("Congratulations")
# root.geometry("600x400")

# # Create a Style object to use with ttkbootstrap
# style = Style(theme="lumen")

# # Set background color to white
# root.configure(bg="#ffffff")  # White background color

# success_frame = ttk.Frame(root, width=350, height=350)  # Modified import statement
# success_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# # Message Label with customized text color and background color
# message_label = ttk.Label(root, text="Congrats! You completed the assessment.", font=("Helvetica", 20), foreground="#000000", background="#ffffff")
# message_label.pack(pady=50)

# # Green Tick Image
# image = Image.open(".\\assets\greentick.png")
# image = image.resize((100, 100), Image.LANCZOS)
# photo = ImageTk.PhotoImage(image)
# blue_tick_label = ttk.Label(root, image=photo, background="#ffffff")
# blue_tick_label.image = photo
# blue_tick_label.pack()

# # Frame to contain the buttons
# button_frame = ttk.Frame(root)
# button_frame.pack(pady=30)

# # Deny Button with customized background and text color
# take_test_button = ttk.Button(button_frame, text="No! Thanks", command=additional_action, style="success.Outline")
# take_test_button.pack(side=tk.LEFT, padx=10)

# # Take Test Button
# additional_button = ttk.Button(button_frame, text="Take Test", command=take_test, style="success.Outline")
# additional_button.pack(side=tk.LEFT, padx=30)

# root.mainloop()



import tkinter as tk
from ttkbootstrap import widgets as ttk
from PIL import Image, ImageTk
from ttkbootstrap import style
import quiz


def take_test():
    print("Redirecting to the test page...")
    root.destroy()
    # subprocess.run(["python", "quiz.py"])
    quiz.QuizApp()

def additional_action():
    print("Additional button clicked.")

root = tk.Tk()
root.title("Congratulations")
root.geometry("600x400")

# Create a Style object to use with ttkbootstrap
style = ttk.Style(theme="lumen")

# Set background color to white
root.configure(bg="#ffffff")  # White background color

success_frame = ttk.Frame(root, width=350, height=350)
success_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Message Label with customized text color and background color
message_label = ttk.Label(root, text="Congrats! You completed the assessment.", font=("Helvetica", 20), foreground="#000000", background="#ffffff")
message_label.pack(pady=50)

# Green Tick Image
image = Image.open("greentick.png")
image = image.resize((100, 100), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
blue_tick_label = ttk.Label(root, image=photo, background="#ffffff")
blue_tick_label.image = photo  # Keep a reference to the image object
blue_tick_label.pack()

# Frame to contain the buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=30)

# Deny Button with customized background and text color
take_test_button = ttk.Button(button_frame, text="No! Thanks", command=additional_action, style="success.Outline")
take_test_button.pack(side=tk.LEFT, padx=10)

# Take Test Button
additional_button = ttk.Button(button_frame, text="Take Test", command=take_test, style="success.Outline")
additional_button.pack(side=tk.LEFT, padx=30)

root.mainloop()
