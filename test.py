import tkinter as tk
import math
from ttkbootstrap.widgets import  *
from ttkbootstrap.widgets import Meter
from PIL import Image, ImageTk
import math
from tkinter import ttk
from ttkbootstrap import Style
import subprocess
from ttkbootstrap.scrolled import ScrolledFrame
import sqlite3
from openpyxl.workbook import Workbook
from PIL import Image, ImageDraw
from tkinter.scrolledtext import ScrolledText
import sys
from PIL import ImageTk, Image
# Get the current user from command-line arguments
current_user = sys.argv[1]
# sprt= sys.argv[2]


root = tk.Tk()
root.title("Sports Recommendation System")

# root.geometry('925x500+300+200')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Set the geometry of the root window to fill the screen
root.geometry("%dx%d" % (width, height))


# Store data in SQLite database
conn = sqlite3.connect('sport.db')


conn1 = sqlite3.connect('rules.db')
cursor = conn1.cursor()
cursor.execute("SELECT sport_name FROM Badminton")
sports = cursor.fetchone()
sports = ', '.join(sports[0].split(", "))
conn1.close()
print(sports)
# Global variable to store the username
# current_user = None




def get_recommendations(preferences):
    conn = sqlite3.connect('sport.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT [{preferences}] FROM sport")
    recommendations = cursor.fetchall()
    conn.close()
    return recommendations





# Define a rounded frame style
style = ttk.Style()


def navigate_to_next_page(sport):
    # You can pass the username to the next page here
    print(f"Navigating to the next page for {sport} with username: {current_user}")

# Create a function to display recommendation cards
def show_recommendation_cards(recommendations):
    # Clear existing recommendation frames
    for widget in cards_frame.winfo_children():
        widget.destroy()

    # Define background color for recommendation frames
    bg_color = style.lookup("Inverted.TLabel", "background")

    # Calculate number of rows and columns based on number of recommendations
    num_rows = math.ceil(len(recommendations) / 3)
    num_cols = 3

    # Define padding and spacing for the grid
    padx = 20  # Padding for width
    pady = 40  # Padding for height
    row_weight = 1  # Weight for row resizing
    col_weight = 1  # Weight for column resizing

    # Define fixed width for recommendation cards
    card_width = 250  # Adjust as needed

    # Configure row and column weights for resizing
    for i in range(num_rows):
        cards_frame.rowconfigure(i, weight=row_weight)
    for j in range(num_cols):
        cards_frame.columnconfigure(j, weight=col_weight)

    # Iterate through recommendations and place them in the grid
    for i, recommendation in enumerate(recommendations):
        row = i // num_cols
        col = i % num_cols

        # Create a frame for the recommendation card with fixed width
        card_frame = ttk.Frame(cards_frame, width=card_width, padding=(padx, pady), style="Inverted.TLabel", borderwidth=2, relief="solid")
        card_frame.grid(row=row, column=col, padx=padx, pady=pady, sticky="nsew")

        # Add a colored label behind the frame
        background_label = ttk.Label(card_frame, background=bg_color)
        background_label.place(relwidth=1, relheight=1)

        # Modify recommendation text to wrap if length exceeds 15 characters
        recommendation_text = recommendation[0]
        if len(recommendation_text) > 15:
            recommendation_text = "\n".join([recommendation_text[i:i+15] for i in range(0, len(recommendation_text), 15)])

        # Add a label to display the wrapped recommendation text
        recommendation_label = ttk.Label(card_frame, text=recommendation_text, font=("helvetica", 16), anchor="center", wraplength=200,background=style.colors.dark,foreground=style.colors.light)  # Center text and wrap
        recommendation_label.pack(fill="both", expand=True)

        # Add a button to navigate to the next page
        navigate_button = ttk.Button(card_frame, text="Test", command=lambda sport=recommendation[0]: navigate_to_next_page(sport))
        navigate_button.pack(side="bottom", pady=10, padx=20)  # Increase padding for button

    # Add empty frames to fill in the empty grid spaces, ensuring proper alignment
    for i in range(num_rows * num_cols - len(recommendations)):
        row = (len(recommendations) + i) // num_cols
        col = (len(recommendations) + i) % num_cols

        # Create an empty frame
        empty_frame = ttk.Frame(cards_frame, width=card_width, padding=(padx, pady))
        empty_frame.grid(row=row, column=col, padx=padx, pady=pady, sticky="nsew")



def navigate_to_next_page(sport):
    global current_user
    if current_user is not None:
        # Run sports.py script with current user and selected sport as arguments
        #subprocess.Popen(["python", "sport.py", current_user, sport])
        if sport =='Badminton':
            root.destroy()
            subprocess.run(['python','quiz.py', current_user])
    
        else:
            root.destroy()
            subprocess.run(['python','footballquiz.py', current_user])    
    else:
        print("Error: Current user is not set.")

# Establish a connection to the database sport.db
conn = sqlite3.connect('sport.db')
cursor = conn.cursor()
cursor.execute("SELECT value FROM progress WHERE ROWID = (SELECT MAX(ROWID) FROM progress)")
row = cursor.fetchone()
number = int(row[0])
print(number)
conn.close()


def navigate_to_recommendation():
    print("Navigating to recommendation page...")
    root.destroy()
    subprocess.run(["python", "recommendation.py",current_user])

def navigate_to_test():
    print("Navigating to test page...") 
     # Placeholder for navigation logic
    root.destroy()
    subprocess.run(["python", "test.py",current_user])

def navigate_to_explore():
    print("Navigating to explore page...")
    subprocess.run(["python", "calorie_entry.py",current_user])

# Create a user interface with tkinter


# Create a ttkbootstrap style
style = Style(theme="lumen")

# Create a frame to contain all widgets
main_frame = ScrolledFrame(root)

main_frame.pack(fill=tk.BOTH, expand=tk.YES)


# Set the geometry of the root window to fill the screen


# Create a frame to contain all widgets


# Pack the main_frame or do any other layout management as needed
# main_frame.pack(fill=BOTH, expand=YES)


style.configure("Inverted.TLabel", background=style.colors.dark, foreground=style.colors.light)
style.configure("Sidebar.TButton", font=("Arial", 15), width=15)

# Create a frame for the sidebar
sidebar_frame = ttk.Frame(main_frame,padding=20,style="Inverted.TLabel", borderwidth=12, )
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

# Add components to the sidebar
sidebar_label = ttk.Label(sidebar_frame, text="Navbar", font=("Arial", 16,'bold'),background=style.colors.dark,foreground=style.colors.light)
sidebar_label.pack(pady=10)
button_width = 20

sidebar_button1 = ttk.Button(sidebar_frame, text="Recommendation", style="Sidebar.TButton",command=navigate_to_recommendation)
sidebar_button1.pack(pady=5)

sidebar_button2 = ttk.Button(sidebar_frame, text="Test", style="Sidebar.TButton",command=navigate_to_test)
sidebar_button2.pack(pady=5)

sidebar_button3 = ttk.Button(sidebar_frame, text="Fitness", style="Sidebar.TButton",command=navigate_to_explore)
sidebar_button3.pack(pady=5)

# Create a frame for the content
content_frame = ttk.Frame(main_frame, height=height, width=width)
content_frame.pack(fill=tk.BOTH, expand=tk.YES)
# Function to load the background image
canvas = tk.Canvas(content_frame, width=400, height=300)
canvas.pack(fill="both", expand=True)
# =========================================================================img bg
# # Load the background image
# bg_image = tk.PhotoImage(file="./assets/greentick.png")  # Path to your background image
# canvas.create_image(0, 0, image=bg_image, anchor="nw")

style.configure('My.TFrame', background='#AFD3E2')

# Create a frame for the header with a specified height and inverted colors
header_frame = ttk.Frame(canvas, height=100,style='My.TFrame')
header_frame.pack(pady=10, anchor=tk.CENTER, expand=True)

# Create the main label with inverted colors
welcome_label = Label(header_frame, text="SPORTS TUTORIAL APP", font=('Times New Roman', 35, 'bold'),foreground='#146C94',background='#AFD3E2', borderwidth=4, relief="solid")
welcome_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
welcome_label.pack(pady=10,padx=10)
# Create the main label with inverted colors

welcome_label.lift() 



# Use the style when creating the Frame
recommendation_frame = ttk.Frame(canvas, style='My.TFrame')
recommendation_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)

title_label = ttk.Label(recommendation_frame, text="Test Recommendation System", font=("Helvetica", 24),foreground='#146C94',background='#AFD3E2')
title_label.pack(pady=20)

instruction_label = ttk.Label(recommendation_frame, text="Select an age group to see suitable sports recommended to you.", font=("Arial", 16),foreground='blue',background='#AFD3E2')
instruction_label.pack(pady=10)

age_group_combobox = ttk.Combobox(recommendation_frame, values=["Children (Ages 8-12)", "Teenagers (Ages 13-19)", "Young Adults (Ages 20-39)", "Middle-Aged Adults (Ages 40-59)", "Older Adults (Ages 60+)"], font=("Arial", 14), state="readonly",background='#AFD3E2')
age_group_combobox.pack(pady=10)

cards_frame = ttk.Frame(content_frame,style='My.TFrame')
cards_frame.pack(padx=10, pady=10 ,fill=tk.BOTH, expand=tk.YES)

recommendation_label = ttk.Label(recommendation_frame,wraplength=300, text="", font=("Arial", 14),foreground='#146C94',background='#AFD3E2')
recommendation_label.pack(pady=20)

def show_recommendations():
    selected_age_group = age_group_combobox.get()
    if selected_age_group:
        recommendations = get_recommendations(selected_age_group)
        recommendation_text = f"Recommendations for {selected_age_group}:\n"
        if recommendations:
            show_recommendation_cards(recommendations)
        else:
            recommendation_text += "No recommendations found for the selected age group."
        recommendation_label.config(text=recommendation_text)
    else:
        recommendation_label.config(text="Please select an age group.")

recommend_button = ttk.Button(recommendation_frame, text="Recommend", style="Sidebar.TButton", command=show_recommendations)
recommend_button.pack(pady=10)
# Create a frame to act as the background image frame


# Load the background image onto the background frame


# Create other frames and widgets as needed (including the sidebar, header, course details, recommendations, etc.)

# # Now, let's make sure other frames stack above the background frame
# sidebar_frame.lift()  # Lift the sidebar frame above the background frame
# header_frame.lift()   # Lift the header frame above the background frame
# # Lift the course details frame above the background frame
# recommendation_frame.lift() # Lift the recommendation frame above the background frame

root.mainloop()

