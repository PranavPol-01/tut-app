from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
import subprocess
import os
from PIL import Image
import sys
username = sys.argv[1]
sprt=sys.argv[2]

# # Get the directory of the current file
# dir_path = os.path.dirname(os.path.realpath(__file__))

# # Create the full path to the image
# tick_image_path = os.path.join(dir_path, 'greentick.png')

# # Open the image
# tick_image = Image.open(tick_image_path)

def navigate_to_test():
    print("Navigating to test page...") 
     # Placeholder for navigation logic
    if sprt =='badminton':
        root.destroy()
        subprocess.run(['python','quiz.py', username,sprt])
    
    else:
        root.destroy()
        subprocess.run(['python','footballquiz.py', username,sprt])

def navigate_back():
    print("Navigating back...")  # Placeholder for navigation logic
    root.destroy()
    subprocess.run(["python", "recommendation.py", username,sprt])

root = Tk()
root.title('Congratulations!')
root.geometry('925x600+300+200')

style = Style(theme='lumen')
style.configure("Inverted.TLabel", background=style.colors.dark, foreground=style.colors.light)
style.configure("Sidebar.TButton", font=("Arial", 15), width=15)

# Congratulatory message
congrats_label = Label(root, text="Congratulations, you have completed the course!", font=('Helvetica', 20))
congrats_label.pack(pady=20)

# Green tick image frame
tick_frame = Frame(root, width=400, height=400)
tick_frame.pack(pady=10)

# Load and display the green tick image
tick_image_path = "./assets/greentick.png"
tick_image = Image.open(tick_image_path)
tick_image = tick_image.resize((400, 400))
tick_image = ImageTk.PhotoImage(tick_image)

tick_label = Label(tick_frame, image=tick_image)
tick_label.image = tick_image
tick_label.pack()

# Frame for buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

# "No Thanks" button
no_thanks_button = ttk.Button(button_frame, text="No Thanks", style="Sidebar.TButton", command=navigate_back)
no_thanks_button.pack(side=LEFT,pady=10)

# "Take Test" button
take_test_button = ttk.Button(button_frame, text="Take Test",style="Sidebar.TButton", command=navigate_to_test)
take_test_button.pack(side=LEFT, padx=10)

style.map('TButton', foreground=[
    ('pressed', 'black'),
    ('active', 'blue')
])

root.mainloop()
