
# import tkinter as tk
# import math
# from ttkbootstrap.widgets import Button, Entry, Label, Frame
# from ttkbootstrap.widgets import Meter
# from PIL import Image, ImageTk
# import math
# from tkinter import ttk
# from ttkbootstrap import Style
# import subprocess
# from ttkbootstrap.scrolled import ScrolledFrame

# # Define the features and properties of the sports
# sports = [
#     {"name": "Soccer", "type": "team", "difficulty": "easy", "intensity": "high", "equipment": "ball, goal, field"},
#     {"name": "Basketball", "type": "team", "difficulty": "medium", "intensity": "high", "equipment": "ball, hoop, court"},
#     {"name": "Tennis", "type": "individual", "difficulty": "medium", "intensity": "medium", "equipment": "racket, ball, net, court"},
#     {"name": "Swimming", "type": "individual", "difficulty": "easy", "intensity": "medium", "equipment": "swimsuit, goggles, pool"},
#     {"name": "Golf", "type": "individual", "difficulty": "hard", "intensity": "low", "equipment": "club, ball, hole, course"},
#     {"name": "Chess", "type": "individual", "difficulty": "hard", "intensity": "low", "equipment": "board, pieces"}
# ]

# # Create a profile for each sport, using a vector of numbers
# profiles = []
# for sport in sports:
#     profile = []
#     # Type
#     if sport["type"] == "team":
#         profile.append(0.5)
#     else:
#         profile.append(0.0)
#     # Difficulty
#     if sport["difficulty"] == "easy":
#         profile.append(0.2)
#     elif sport["difficulty"] == "medium":
#         profile.append(0.5)
#     else:
#         profile.append(0.8)
#     # Intensity
#     if sport["intensity"] == "low":
#         profile.append(0.2)
#     elif sport["intensity"] == "medium":
#         profile.append(0.5)
#     else:
#         profile.append(1.0)
#     # Equipment
#     equipment = ["ball", "goal", "field", "hoop", "court", "racket", "net", "swimsuit", "goggles", "pool", "club", "hole", "course", "board", "pieces"]
#     for item in equipment:
#         if item in sport["equipment"]:
#             profile.append(0.05)
#         else:
#             profile.append(0.0)
#     profiles.append(profile)

# # Define a function to calculate the cosine similarity between two vectors
# def calculate_cosine_similarity(v1, v2):
#     dot_product = sum(x * y for x, y in zip(v1, v2))
#     magnitude_v1 = math.sqrt(sum(x ** 2 for x in v1))
#     magnitude_v2 = math.sqrt(sum(x ** 2 for x in v2))
#     if magnitude_v1 == 0 or magnitude_v2 == 0:
#         return 0  # Avoid division by zero
#     return dot_product / (magnitude_v1 * magnitude_v2)

# # Define a function to recommend sports based on an age group
# def recommend_sports(selected_age_group):
#     preference_weights = {
#         "Children (5-12 years)": [0.8, 0.2, 1.0, 0.1],      # high preference for team sports, easy difficulty, high intensity, moderate equipment
#         "Teenagers (13-18 years)": [0.7, 0.5, 0.8, 0.2],    # moderate preference for team sports, medium difficulty, high intensity, more equipment
#         "Adults (19-64 years)": [0.5, 0.5, 0.5, 0.5],       # equal preference for team and individual sports, medium difficulty, medium intensity, diverse equipment
#         "Older Adults (65 years and older)": [0.3, 0.7, 0.3, 0.8]  # high preference for individual sports, high difficulty, low intensity, less equipment
#     }
#     preference = preference_weights.get(selected_age_group)
#     preference += [0] * (len(profiles[0]) - len(preference))  # Adjust the length of preference vector
#     similarity_scores = [calculate_cosine_similarity(preference, profile) for profile in profiles]
#     top_3_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:3]
#     return [sports[i] for i in top_3_indices]

# user_course_details = {
#     "course_name": "Badminton",
#     "instructor": "student 1",
#     "duration": "6 weeks"
# }

# # Create a user interface with tkinter
# root = tk.Tk()
# root.title("Sports Recommendation System")
# root.geometry('925x500+300+200')

# # Create a ttkbootstrap style
# style = Style(theme="superhero")

# # Create a frame to contain all widgets
# main_frame = ScrolledFrame(root)
# main_frame.pack(fill=tk.BOTH, expand=tk.YES)

# course_name_label = ttk.Label(main_frame, text="Course Name: " + user_course_details["course_name"], font=("Arial", 14))
# course_name_label.pack(pady=5)

# instructor_label = ttk.Label(main_frame, text="Instructor: " + user_course_details["instructor"], font=("Arial", 14))
# instructor_label.pack(pady=5)

# duration_label = ttk.Label(main_frame, text="Duration: " + user_course_details["duration"], font=("Arial", 14))
# duration_label.pack(pady=5)

# # Define a separator to visually separate the course details from the recommendation section
# separator = ttk.Separator(main_frame, orient='horizontal')
# separator.pack(fill='x', padx=20, pady=20)

# # Create another frame to contain the recommendation widgets
# recommendation_frame = Frame(main_frame)
# recommendation_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)

# # add a large number of checkbuttons into the scrolled frame
# # sf = ScrolledFrame(recommendation_frame, autohide=True)
# # sf.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)

# # for x in range(20):
# #     ttk.Checkbutton(sf, text=f"Checkbutton {x}").pack(anchor=tk.W)

# # Create the meter widget
# meter = Meter(
#     recommendation_frame,
#     metersize=180,
#     padding=5,
#     amountused=25,
#     metertype="semi",
#     subtext="miles per hour",
#     interactive=True,
# )
# meter.pack()

# # Update the subtext
# meter.configure(subtext="Loading...")

# # Update the amount used directly
# meter.configure(amountused=50)

# # Create an entry widget to update the amount used
# entry = ttk.Entry(recommendation_frame, textvariable=meter.amountusedvar)
# entry.pack(fill='x', pady=10)

# # Increment the amount by 10 steps
# meter.step(10)

# # Decrement the amount by 15 steps
# meter.step(-15)

# title_label = ttk.Label(recommendation_frame, text="Sports Recommendation System", font=("Arial", 24))
# title_label.pack(pady=20)

# instruction_label = ttk.Label(recommendation_frame, text="Select an age group to see suitable sports recommended to you.", font=("Arial", 16))
# instruction_label.pack(pady=10)

# age_group_combobox = ttk.Combobox(recommendation_frame, values=["Children (5-12 years)", "Teenagers (13-18 years)", "Adults (19-64 years)", "Older Adults (65 years and older)"], font=("Arial", 14), state="readonly")
# age_group_combobox.pack(pady=10)

# recommendation_label = ttk.Label(recommendation_frame, text="", font=("Arial", 14))
# recommendation_label.pack(pady=10)

# def show_recommendations():
#     selected_age_group = age_group_combobox.get()
#     if selected_age_group in ["Children (5-12 years)", "Teenagers (13-18 years)", "Adults (19-64 years)", "Older Adults (65 years and older)"]:
#         recommended_sports = recommend_sports(selected_age_group)
#         recommendation_text = "If you belong to the age group of {}, you may enjoy these sports:\n".format(selected_age_group)
#         for sport in recommended_sports:
#             recommendation_text += "- {}\n".format(sport["name"])
#         recommendation_label.config(text=recommendation_text)
#     else:
#         recommendation_label.config(text="Please select a valid age group.")

# recommend_button = ttk.Button(recommendation_frame, text="Recommend", style="primary.TButton", command=show_recommendations)
# recommend_button.pack(pady=10)

# # Start the main loop
# root.mainloop()


#--------------------------------------------------------------------------------------------------------------------------------------------
# import tkinter as tk
# import math
# from ttkbootstrap.widgets import Button, Entry, Label, Frame
# from ttkbootstrap.widgets import Meter
# from PIL import Image, ImageTk
# import math
# from tkinter import ttk
# from ttkbootstrap import Style
# import subprocess
# from ttkbootstrap.scrolled import ScrolledFrame
# import pandas as pd  # Import pandas module
# import sqlite3
# from openpyxl.workbook import Workbook

# # Load data from Excel file
# df = pd.read_excel('sports.xlsx')

# # Store data in SQLite database
# conn = sqlite3.connect('sports.db')
# df.to_sql('sports', conn, if_exists='replace', index=False)

# # Global variable to store the username
# current_user = None


# def get_recommendations(preferences):
#     conn = sqlite3.connect('sports.db')
#     cursor = conn.cursor()
#     cursor.execute(f"SELECT [{preferences}] FROM sports")
#     recommendations = cursor.fetchall()
#     conn.close()
#     return recommendations

# def show_recommendation_cards(recommendations):
#     for i, recommendation in enumerate(recommendations):
#         # Create a frame for the recommendation card
#         card_frame = ttk.Frame(cards_frame)
#         card_frame.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")

#         # Add a label to display the recommendation
#         recommendation_label = ttk.Label(card_frame, text=recommendation[0], font=("Arial", 12))
#         recommendation_label.pack()

# # Create a user interface with tkinter
# root = tk.Tk()
# root.title("Sports Recommendation System")
# root.geometry('925x500+300+200')

# # Create a ttkbootstrap style
# style = Style(theme="superhero")

# # Create a frame to contain all widgets
# main_frame = ScrolledFrame(root)
# main_frame.pack(fill=tk.BOTH, expand=tk.YES)

# style.configure("Inverted.TLabel", background=style.colors.dark, foreground=style.colors.light)

# # Create a frame for the header with a specified height and inverted colors
# header_frame = ttk.Frame(main_frame, height=100)
# header_frame.pack(fill='x')


# # Create the main label with inverted colors
# welcome_label = Label(header_frame, text="SPORTS TUTORIAL APP", font=('Courier New', 35, 'bold'), style="Inverted.TLabel", borderwidth=12, relief="groove")
# welcome_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# # Adjust position of the main label to create the shadow effect
# welcome_label.lift() 

# separator = ttk.Separator(main_frame, orient='horizontal')
# separator.pack(fill='x', padx=20, pady=20)


# # Create a frame for the course details
# course_d_frame = ttk.Frame(main_frame, padding=10, borderwidth=2, relief="solid", height=400, width=400)
# course_d_frame.pack(pady=10, anchor=tk.CENTER, expand=True)

# # Add a meter showing the course completion progress
# course_completion_meter = Meter(course_d_frame, metersize=100, padding=5, amountused=25, metertype="semi", subtext="current course")
# course_completion_meter.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# # Create a frame for course details
# course_details_frame = ttk.Frame(course_d_frame, padding=10, borderwidth=2, relief="solid", height=200, width=200)
# course_details_frame.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# # Add labels for course details
# course_name_label = ttk.Label(course_details_frame, text="Course Name: Badminton", font=("Arial", 14))
# course_name_label.grid(row=0, column=0, pady=5, sticky='w')

# instructor_label = ttk.Label(course_details_frame, text="Instructor: sapp", font=("Arial", 14))
# instructor_label.grid(row=1, column=0, pady=5, sticky='w')

# duration_label = ttk.Label(course_details_frame, text="Duration: 6 weeks", font=("Arial", 14))
# duration_label.grid(row=2, column=0, pady=5, sticky='w')




# # Separator between course details and recommendations
# separator = ttk.Separator(main_frame, orient='horizontal')
# separator.pack(fill='x', padx=20, pady=20)


# recommendation_frame = Frame(main_frame)
# recommendation_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)

# meter = Meter(
#     recommendation_frame,
#     metersize=180,
#     padding=5,
#     amountused=25,
#     metertype="semi",
#     subtext="miles per hour",
#     interactive=True,
# )





# title_label = ttk.Label(recommendation_frame, text="Sports Recommendation System", font=("Arial", 24))
# title_label.pack(pady=20)

# instruction_label = ttk.Label(recommendation_frame, text="Select an age group to see suitable sports recommended to you.", font=("Arial", 16))
# instruction_label.pack(pady=10)

# age_group_combobox = ttk.Combobox(recommendation_frame, values=["Children (Ages 0-12):", "Teenagers (Ages 13-19):", "Young Adults (Ages 20-39):", "Middle-Aged Adults (Ages 40-59):", "Older Adults (Ages 60+):"], font=("Arial", 14), state="readonly")
# age_group_combobox.pack(pady=10)

# cards_frame = ttk.Frame(main_frame)
# cards_frame.pack(padx=10, pady=10)

# recommendation_label = ttk.Label(recommendation_frame, text="", font=("Arial", 14))
# recommendation_label.pack(pady=10)

# def show_recommendations():
#     selected_age_group = age_group_combobox.get()
#     if selected_age_group:
#         recommendations = get_recommendations(selected_age_group)
#         recommendation_text = f"Recommendations for {selected_age_group}:\n"
#         if recommendations:
#             show_recommendation_cards(recommendations)
#             # for recommendation in recommendations:
#             #     recommendation_text += f"- {recommendation}\n"  # Fetch the first element of the tuple
#         else:
#             recommendation_text += "No recommendations found for the selected age group."
#         recommendation_label.config(text=recommendation_text)
#     else:
#         recommendation_label.config(text="Please select an age group.")


# recommend_button = ttk.Button(recommendation_frame, text="Recommend", style="primary.TButton", command=show_recommendations)
# recommend_button.pack(pady=10)

# root.mainloop()


#-------------------------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------
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


def create_rounded_rectangle(width, height, radius, color):
    image = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), fill=color)
    draw.pieslice((0, 0, 2 * radius, 2 * radius), 180, 270, fill=color)
    draw.pieslice((width - 2 * radius, 0, width, 2 * radius), 270, 360, fill=color)
    draw.pieslice((0, height - 2 * radius, 2 * radius, height), 90, 180, fill=color)
    draw.pieslice((width - 2 * radius, height - 2 * radius, width, height), 0, 90, fill=color)
    draw.rectangle((radius, 0, width - radius, height), fill=color)
    draw.rectangle((0, radius, width, height - radius), fill=color)
    return image


def set_bg_image():
    global photo  # Declare photo as a global variable
    desktop_width = root.winfo_screenwidth()
    desktop_height = root.winfo_screenheight()

    # Load the image and resize it to the desktop size
    image = Image.open(r".\assets/greentick.png")  # Use raw string and backslashes
    image = image.resize((desktop_width, desktop_height))

    # Create an image with an alpha channel for opacity
    alpha = Image.new('L', image.size, 99)  # 99 is the alpha value (30% opacity)
    image.putalpha(alpha)

    photo = ImageTk.PhotoImage(image)
    main_frame.config(image=photo)
    main_frame.image = photo
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

def load_background_image(frame):
    # Load the background image
    background_image = Image.open("./assets/sport_tut.jpg")
    # Resize the image to fit the frame
    background_image = background_image.resize((frame.winfo_width(), frame.winfo_height()))
    # Convert the image to Tkinter-compatible format
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label to hold the background image
    background_label = ttk.Label(frame, image=background_photo)
    background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Make sure other widgets are stacked above the background label
    background_label.lower()

# Call the load_background_image function with the background frame as parameter
# load_background_image(background_frame)



def get_recommendations(preferences):
    conn = sqlite3.connect('sport.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT [{preferences}] FROM sport")
    recommendations = cursor.fetchall()
    conn.close()
    return recommendations


rounded_rectangle_image = create_rounded_rectangle(200, 100, 10, "lightblue")

# Convert the PIL image to Tkinter-compatible image
rounded_rectangle_photo = ImageTk.PhotoImage(rounded_rectangle_image)

# Define a rounded frame style
style = ttk.Style()
style.element_create("Rounded.Frame", "image", rounded_rectangle_photo, border=0, sticky="nsew")
style.layout("Rounded.TFrame", [("Rounded.Frame", {"sticky": "nsew"})])

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
        navigate_button = ttk.Button(card_frame, text="Explore", command=lambda sport=recommendation[0]: navigate_to_next_page(sport))
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
        if sport == "Badminton":
         
         subprocess.Popen(["python", "sport.py", current_user,'badminton'])
        else:
        #  root.destroy()
         subprocess.Popen(["python", "football.py", current_user,'football'])

        
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

# Define the progress status based on the number
progress = ""
if number == 100:
    progress = "Completed"
elif number == 80:
    progress = "Almost Completed"
elif number == 40:
    progress = "Halfway Completed"
elif number == 20:
    progress = "Just Started"
else:
    progress= "Not Started"


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

separator = ttk.Separator(canvas, orient='horizontal')
separator.pack(fill='x', padx=20, pady=20)

# Create a frame for the course details
course_d_frame = ttk.Frame(canvas, padding=10, borderwidth=2, relief="solid", height=400, width=400)
course_d_frame.pack(pady=10, anchor=tk.CENTER, expand=True)

# Add a meter showing the course completion progress
course_completion_meter = Meter(course_d_frame, metersize=100, padding=5, amountused=f"{number}", metertype="semi", subtext=f"{progress}", interactive=True)
course_completion_meter.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Create a frame for course details
course_details_frame = ttk.Frame(course_d_frame, padding=10, borderwidth=2, relief="solid", height=200, width=200)
course_details_frame.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Add labels for course details
course_name_label = ttk.Label(course_details_frame, text=f"Course Name: {sports}", font=("Arial", 14))
course_name_label.grid(row=0, column=0, pady=5, sticky='w')

instructor_label = ttk.Label(course_details_frame, text="Instructor: sapp", font=("Arial", 14))
instructor_label.grid(row=1, column=0, pady=5, sticky='w')

duration_label = ttk.Label(course_details_frame, text="Duration: 6 weeks", font=("Arial", 14))
duration_label.grid(row=2, column=0, pady=5, sticky='w')

# Separator between course details and recommendations
separator = ttk.Separator(canvas, orient='horizontal')
separator.pack(fill='x', padx=20, )



# Use the style when creating the Frame
recommendation_frame = ttk.Frame(canvas, style='My.TFrame')
recommendation_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=10)

meter = Meter(
    recommendation_frame,
    metersize=200,
    padding=5,
    amountused=f"{number}",
    metertype="semi",
    subtext="miles per hour",
    interactive=True,
)

title_label = ttk.Label(recommendation_frame, text="Sports Recommendation System", font=("Helvetica", 24),foreground='#146C94',background='#AFD3E2')
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

# Now, let's make sure other frames stack above the background frame
sidebar_frame.lift()  # Lift the sidebar frame above the background frame
# header_frame.lift()   # Lift the header frame above the background frame
course_d_frame.lift() # Lift the course details frame above the background frame
recommendation_frame.lift() # Lift the recommendation frame above the background frame

root.mainloop()

