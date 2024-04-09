# import tkinter as tk
# import sqlite3

# # Create a SQLite database (or connect to an existing one)
# conn = sqlite3.connect("calorie_tracker.db")
# cursor = conn.cursor()

# # Create a table to store user entries
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS calorie_entries (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         calories INT
#     )
# """)
# conn.commit()

# def add_entry():
#     name = name_entry.get()
#     calories = int(calories_entry.get())

#     # Insert the entry into the database
#     cursor.execute("INSERT INTO calorie_entries (name, calories) VALUES (?, ?)", (name, calories))
#     conn.commit()

# def show_result():
#     name = name_entry.get()

#     # Retrieve total calorie intake for the specified user
#     cursor.execute("SELECT SUM(calories) FROM calorie_entries WHERE name=?", (name,))
#     total_calories = cursor.fetchone()[0]

#     result_label.config(text=f"Total calories for {name}: {total_calories} kcal")

# # Create the main application window
# window = tk.Tk()
# window.title("Calorie Tracker")

# # Entry fields
# name_label = tk.Label(window, text="Name:")
# name_entry = tk.Entry(window)
# calories_label = tk.Label(window, text="Calories:")
# calories_entry = tk.Entry(window)

# # Buttons
# add_button = tk.Button(window, text="Add Entry", command=add_entry)
# show_button = tk.Button(window, text="Show Result", command=show_result)

# # Result display
# result_label = tk.Label(window, text="")

# # Layout
# name_label.grid(row=0, column=0)
# name_entry.grid(row=0, column=1)
# calories_label.grid(row=1, column=0)
# calories_entry.grid(row=1, column=1)
# add_button.grid(row=2, column=0, columnspan=2)
# show_button.grid(row=3, column=0, columnspan=2)
# result_label.grid(row=4, column=0, columnspan=2)

# # Start the GUI event loop
# window.mainloop()

# # Close the database connection when the application exits
# conn.close()




# //////////////////////////////////// NEWLY CODE //////////////////////////////
import tkinter as tk
import sqlite3
from PIL import Image, ImageTk
import datetime
import subprocess
import sys
from tkcalendar import  DateEntry
import tkinter.messagebox
current_user=sys.argv[1]
print(current_user)


# Create a SQLite database (or connect to an existing one)
conn = sqlite3.connect("tracker.db")
cursor = conn.cursor()

# Create a table to store user entries
cursor.execute("""
    CREATE TABLE IF NOT EXISTS calorie_entries (
        id INTEGER PRIMARY KEY,
        name TEXT,
        calories INT,
        date TEXT
    )
""")
conn.commit()



def set_bg_image():
    global photo  
    desktop_width = window.winfo_screenwidth()
    desktop_height = window.winfo_screenheight()

    image = Image.open("assets/bg.jpg")
    image = image.resize((desktop_width, desktop_height))

    blue_tint = Image.new('RGB', image.size, (173, 216, 230))  # Create a new image with a light blue color
    image = Image.blend(image, blue_tint, 0.5)  # Blend the original image and the blue tint image

    photo = ImageTk.PhotoImage(image)
    bg_label.config(image=photo)
    bg_label.image = photo

    # welcome_label = tk.Label(bg_label, text="WELCOME TO TRAVEL-BUDDY", font=('Courier New', 35, 'bold'), fg='white', bg='#016A70', bd=10, relief=tk.GROOVE)
    # welcome_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

# def add_entry():
#     name = name_entry.get()
#     calories = int(calories_entry.get())

#     # Insert the entry into the database
#     cursor.execute("INSERT INTO calorie_entries (name, calories) VALUES (?, ?)", (name, calories))
#     conn.commit()

def show_result():
    name = current_user

    # Retrieve total calorie intake for the specified user
    cursor.execute("SELECT SUM(calories) FROM calorie_entries WHERE name=? and date=?", (name, datetime.datetime.now().date().isoformat()))
    total_calories = cursor.fetchone()[0]
    print(total_calories)
    # result_label.config(text=f"Total calories of a day for {name}: {total_calories} kcal")
    result_text = f"Total calories of a day for {name}: {total_calories} kcal"

    # Show the text in a popup
    tkinter.messagebox.showinfo("Calorie Intake Result", result_text)

def enter_raw_data():
    conn = sqlite3.connect("calorie_counter.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calorie_counter (
        id INTEGER PRIMARY KEY,
        meal TEXT,
        calories INT,
        image BLOB
        )
    """)
    cursor.execute("""
        INSERT INTO calorie_counter (meal, calories, image) 
        VALUES 
        ('chapati', 104, 'assets/chapati.png'),
        ('bread', 82, 'assets/bread.png'),
        ('lady finger', 35, 'assets/lady finger.png'),
        ('cheese', 350, 'assets/cheese.png'),
        ('rice', 242, 'assets/rice.png'),
        ('idli', 58, 'assets/idli.png')
    """)

    conn.commit()
    print("Added entry to database")
    conn.close()


# def calorie_counter1():
#     con = sqlite3.connect("calorie_counter.db")
#     c1 = con.cursor()  
#     meal_calories = 0
#     meal_entries = [item1_entry.get(), item2_entry.get(), item3_entry.get(), item4_entry.get()]

#     for meal in meal_entries:
#         if meal:  # Check if the meal entry is not empty
#             c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (meal,))
#             result = c1.fetchone()
#             if result:  # Check if the query result is not None
#                 calorie_entry = int(result[0])
#                 meal_calories += calorie_entry
#             else:
#                 print(f"No calorie information found for {meal}")
#         else:
#             print("Empty meal entry")

#     print("Total meal calories:", meal_calories)
#     calorie_label.config(text=f"Total calories from the meal: {meal_calories} kcal")
#     con.close()
#     # Starting the new cursor to point to the calorie_tracker.db
#     conn = sqlite3.connect("tracker.db")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO calorie_entries (name, calories, date) VALUES (?, ?,?)", (current_user, meal_calories,datetime.datetime.now().date().isoformat()))
#     conn.commit()
#     conn.close()
def calorie_counter1():
    con = sqlite3.connect("calorie_counter.db")
    c1 = con.cursor()
    meal_calories = 0
    meal_entries = [(item1_entry.get(), quantity1_entry.get()),
                    (item2_entry.get(), quantity2_entry.get()),
                    (item3_entry.get(), quantity3_entry.get()),
                    (item4_entry.get(), quantity4_entry.get())]

    for item, quantity in meal_entries:
        if item and quantity:  # Check if both item and quantity are not empty
            c1.execute("SELECT calories FROM calorie_counter WHERE meal=?", (item,))
            result = c1.fetchone()
            if result:  # Check if the query result is not None
                calorie_entry = int(result[0])
                meal_calories += calorie_entry * int(quantity)  # Multiply by quantity
            else:
                print(f"No calorie information found for {item}")
        else:
            print("Empty item or quantity")

    print("Total meal calories:", meal_calories)
    # calorie_label.config(text=f"Total calories from the meal: {meal_calories} kcal")
    tkinter.messagebox.showinfo("Meal Calories", f"Total calories from the meal: {meal_calories} kcal")
    con.close()

    # Starting the new cursor to point to the tracker.db
    conn = sqlite3.connect("tracker.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO calorie_entries (name, calories, date) VALUES (?, ?,?)", (current_user, meal_calories, datetime.datetime.now().date().isoformat()))
    conn.commit()
    conn.close()

# Code to calculate BMR
# def calorie_counter():
#     weight = float(weight_entry.get())
#     height = float(height_entry.get())
#     age = int(age_entry.get())
#     gender = gender_var.get()

#     if gender == "Male":
#         bmr = 10 * weight + 6.25 * height - 5 * age + 5
#     else:
#         bmr = 10 * weight + 6.25 * height - 5 * age - 161

#     result_label.config(text=f"Your BMR: {bmr} kcal/day")
# Create the main application window

def navigate_to_recommendation():
    print("Navigating to recommendation page...")
    window.destroy()
    subprocess.run(["python", "recommendation.py", current_user])


def navigate_to_test():
    print("Navigating to test page...") 
     # Placeholder for navigation logic
    window.destroy()
    subprocess.run(["python", "test.py",current_user])


def navigate_to_explore():
    print("Navigating to explore page...")
    subprocess.run(["python", "explore.py", current_user])    

def show_calorie_table_info():
    # Display the table with appropriate images
    con=sqlite3.connect('calorie_counter.db')
    c = con.cursor()    
    
    # Create labels for table headers
    header_labels = ["Name", "Calories", "Image"]
    for i, header in enumerate(header_labels):
        label = tk.Label(frame2, text=header, font=("Arial", 12, "bold"),background="lightblue")
        label.grid(row=0, column=i, padx=10, pady=20)

    # Retrieve all entries from the database
    c.execute("SELECT * FROM calorie_counter")
    entries = c.fetchall()

    # Display the entries in the table
    for i, entry in enumerate(entries):
        name = entry[1]
        calories = entry[2]
        image = entry[3]

        # Create labels for name and calories
        name_label = tk.Label(frame2, text=name,background="lightblue",font=("Arial", 12))
        name_label.grid(row=i+1, column=0, padx=10, pady=5)

        calories_label = tk.Label(frame2, text=calories,background="lightblue",font=("Arial", 12))
        calories_label.grid(row=i+1, column=1, padx=10, pady=5)

        # Create an image label
        image_path = image  # Assuming the images are stored in a folder named "images"
        try:
            image_pil = Image.open(image_path)
            image_pil = image_pil.resize((50, 50))  # Resize the image as needed
            image_tk = ImageTk.PhotoImage(image_pil)
            image_label = tk.Label(frame2, image=image_tk)
            image_label.image = image_tk  # Keep a reference to the image to prevent it from being garbage collected
            image_label.grid(row=i + 1, column=2, padx=10, pady=5)
        except FileNotFoundError:
            print(f"Image not found for {name}: {image_path}")
    con.close()

def show_history():
    con = sqlite3.connect("tracker.db")
    c = con.cursor()
    # date = history_entry.get()
    date = cal.get_date()
    name = current_user
    c.execute("SELECT name, calories FROM calorie_entries WHERE date=? AND name=?", (date, name))
    entries = c.fetchall()
    print(entries)
    

    # Create labels for table headers
    header_labels = ["Name", "Calories"]
    for i, header in enumerate(header_labels):
        label = tk.Label(frame3, text=header, font=("Arial", 12, "bold"),background="lightblue")
        label.grid(row=3, column=i, padx=10, pady=20)

    # Display the entries in the table
   
    for j, entry in enumerate(entries):
        name, calories = entry

        # Create labels for name and calories
        name_label = tk.Label(frame3, text=name,background="lightblue",font=("Arial", 12),foreground='blue')
        name_label.grid(row=j + 4, column=0, padx=5, pady=2)  # Adjust padding values

        calories_label = tk.Label(frame3, text=calories,background="lightblue",font=("Arial", 12),foreground='blue')
        calories_label.grid(row=j + 4, column=1, padx=5, pady=2)  # Adjust padding values

    con.close()

     

def calculate_bmi():
    con = sqlite3.connect("bmi_tracker.db")
    cursor = con.cursor()
    # bmi_name = bmi_name_entry.get()
    bmi_name = current_user
    weight_kg = float(weight_entry.get())
    height_cm = float(height_entry.get())

    # Calculate BMI
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 1)

    # Store the entry in the database
    cursor.execute("INSERT INTO bmi_entries (name, weight_kg, height_cm) VALUES (?, ?, ?)",
                   (bmi_name, weight_kg, height_cm))
    con.commit()

    # Display BMI category and exercise recommendations
    bmi_index(bmi)
    con.close()

def bmi_index(bmi):
    if bmi < 18.5:
        category = "Underweight"
        recommendations = [
            "1. Swimming: Freestyle, breaststroke, or backstroke are good options to build muscle mass.",
            "2. Weightlifting: Focus on compound exercises like squats, deadlifts, and bench presses.",
            "3. Yoga: Helps in improving flexibility, strength, and overall well-being."
        ]
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
        recommendations = [
            "1. Walking: Brisk walking is a great way to maintain overall health and fitness.",
            "2. Cycling: Ride a bicycle to improve cardiovascular health and leg strength.",
            "3. Dancing: Fun and effective for cardiovascular fitness and overall well-being."
        ]
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        recommendations = [
            "1. Running: Start with a mix of walking and running to build endurance and burn calories.",
            "2. Aerobics: High-energy workouts like Zumba or aerobics classes can help with weight loss.",
            "3. Interval Training: Incorporate intervals of high-intensity exercise with periods of rest."
        ]
    else:
        category = "Obesity"
        recommendations = [
            "1. High-Intensity Interval Training (HIIT): Effective for burning calories and improving cardiovascular health.",
            "2. CrossFit: Combines strength training and high-intensity cardio for a full-body workout.",
            "3. Rowing: Low-impact exercise that engages multiple muscle groups and helps with weight loss."
        ]

    bmi_result_label.config(text=f"BMI: {bmi} ({category})\n\nExercise Recommendations:\n" + "\n".join(recommendations))
    
    # Create a scrollable frame


# Create the main application window
window = tk.Tk()
window.title("Calorie Tracker")
# window.geometry("800x600")
# window.configure(background="lightblue")
bg_label = tk.Label(window, bg="lightblue")
bg_label.pack(fill="both", expand=True)
set_bg_image()


width = window.winfo_screenwidth()
height = window.winfo_screenheight()


# Set the geometry of the window window to fill the screen
window.geometry("%dx%d" % (width, height))

content_frame = tk.Frame(window)

content_frame.pack(fill=tk.BOTH, expand=tk.YES)



# Create a frame
frame = tk.Frame(window, bg="lightblue")
frame1 = tk.Frame(window, bg="lightblue")
frame2 = tk.Frame(window, bg="lightblue")
frame3 = tk.Frame(window, bg="lightblue")
frame4 = tk.Frame(window, bg="lightblue")
frame5 = tk.Frame(window, bg="lightblue")

# Frame
name_label = tk.Label(frame, text="Total calories",background="lightblue",font=("Arial", 12,'bold'))
# name_entry = tk.Entry(frame)
show_button = tk.Button(frame, text="Show Result", command=show_result,background="#0097B2",foreground="white",font=("Arial", 12))
result_label = tk.Label(frame, text="",background="lightblue",font=("Arial", 14),foreground='blue')

# # Frame1
# title = tk.Label(frame1, text="Calorie Counter",background="lightblue",font=("Arial", 12,'bold'))
# # user_name = tk.Label(frame1, text="Your Name:",background="lightblue",font=("Arial", 12))
# # user_name_entry = tk.Entry(frame1)
# item1 = tk.Label(frame1, text="Food item 1:",background="lightblue",font=("Arial", 12))
# item1_entry = tk.Entry(frame1)
# item2 = tk.Label(frame1, text="Food item 2:",background="lightblue",font=("Arial", 12))
# item2_entry = tk.Entry(frame1)
# item3 = tk.Label(frame1, text="Food item 3:",background="lightblue",font=("Arial", 12))
# item3_entry = tk.Entry(frame1)
# item4 = tk.Label(frame1, text ="Food item 4:",background="lightblue",font=("Arial", 12))
# item4_entry = tk.Entry(frame1)
# calorie_counter_button = tk.Button(frame1, text="Calculate Calories", command=calorie_counter1,background="#0097B2",foreground="white",font=("Arial", 12))
# calorie_label = tk.Label(frame1, text="",background="lightblue",font=("Arial", 12),foreground='blue')
title = tk.Label(frame1, text="Calorie Counter", background="lightblue", font=("Arial", 12, 'bold'))
title.pack(pady=20)
item1 = tk.Label(frame1, text="Food item 1:", background="lightblue", font=("Arial", 12))
item1_entry = tk.Entry(frame1)
quantity1 = tk.Label(frame1, text="Quantity:", background="lightblue", font=("Arial", 12))
quantity1_entry = tk.Entry(frame1)

item2 = tk.Label(frame1, text="Food item 2:", background="lightblue", font=("Arial", 12))
item2_entry = tk.Entry(frame1)
quantity2 = tk.Label(frame1, text="Quantity:", background="lightblue", font=("Arial", 12))
quantity2_entry = tk.Entry(frame1)

item3 = tk.Label(frame1, text="Food item 3:", background="lightblue", font=("Arial", 12))
item3_entry = tk.Entry(frame1)
quantity3 = tk.Label(frame1, text="Quantity:", background="lightblue", font=("Arial", 12))
quantity3_entry = tk.Entry(frame1)

item4 = tk.Label(frame1, text="Food item 4:", background="lightblue", font=("Arial", 12))
item4_entry = tk.Entry(frame1)
quantity4 = tk.Label(frame1, text="Quantity:", background="lightblue", font=("Arial", 12))
quantity4_entry = tk.Entry(frame1)

# Button and calorie label
calorie_counter_button = tk.Button(frame1, text="Calculate Calories", command=calorie_counter1, background="#0097B2", foreground="white", font=("Arial", 12))
calorie_label = tk.Label(frame1, text="", background="lightblue", font=("Arial", 12), foreground='blue')


# Frame3
# title_history = tk.Label(frame3, text="Know your calorie intake history",background="lightblue",font=("Arial", 12))
# history_label = tk.Label(frame3, text="Enter the date :",background="lightblue",font=("Arial", 12))
# history_entry = tk.Entry(frame3)
# show_history_btn = tk.Button(frame3, text="Show History", command=show_history,background="#0097B2",foreground="white",font=("Arial", 12))
title_history = tk.Label(frame3, text="Know your calorie intake history", background="lightblue", font=("Arial", 12,'bold'))
title_history.grid(row=0, column=0, padx=10, pady=10)

# Define the label for choosing a date
history_label = tk.Label(frame3, text="Choose a Date", background='gray61', foreground="white")
history_label.grid(row=1, column=0, padx=10, pady=10)

# Create a Calendar using DateEntry
cal = DateEntry(frame3, width=16, background="magenta3", foreground="white", bd=2)
cal.grid(row=2, column=0, padx=10, pady=10)

# Define the button to show history
show_history_btn = tk.Button(frame3, text="Show History", command=show_history, background="#0097B2",
                             foreground="white", font=("Arial", 12))
show_history_btn.grid(row=3, column=0, padx=10, pady=10)
# Frame4
bmi_title = tk.Label(frame4, text="BMI Calculator",background="lightblue",font=("Arial", 12,'bold'))
# bmi_name_label = tk.Label(frame4, text="Name:",background="lightblue",font=("Arial", 12))
# bmi_name_entry = tk.Entry(frame4)
weight_label = tk.Label(frame4, text="Weight (kg):",background="lightblue",font=("Arial", 12))
weight_entry = tk.Entry(frame4)
height_label = tk.Label(frame4, text="Height (cm):",background="lightblue",font=("Arial", 12))
height_entry = tk.Entry(frame4)
calculate_button = tk.Button(frame4, text="Calculate BMI", command=calculate_bmi,background="#0097B2",foreground="white",font=("Arial", 12))
bmi_result_label = tk.Label(frame5, text="",background="lightblue",font=("Helvetica", 12,),foreground='darkblue')


# raw_data=tk.Button(frame1,text='Enter raw data',command=enter_raw_data)
# show_calorie_chart=tk.Button(frame2,text='Show Calorie Chart',command=show_calorie_table_info)
# Result display



# Layouts

# frame layout
name_label.grid(row=0, column=0)
# name_entry.grid(row=0, column=1,pady=20)
show_button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2,pady=15)


# # frame1 layout
# title.grid(row=0, column=0)
# # user_name.grid(row=1, column=0)
# # user_name_entry.grid(row=1, column=1,pady=10)
# item1.grid(row=2, column=0)
# item1_entry.grid(row=2, column=1,pady=10)
# item2.grid(row=3, column=0)
# item2_entry.grid(row=3, column=1,pady=10)
# item3.grid(row=4, column=0)
# item3_entry.grid(row=4, column=1,pady=10)
# item4.grid(row=5, column=0)
# item4_entry.grid(row=5, column=1,pady=10)
# calorie_counter_button.grid(row=6, column=0, columnspan=2)
# calorie_label.grid(row=7, column=0, columnspan=2,pady=15)
title.grid(row=0, column=0, columnspan=2, pady=10)
item1.grid(row=1, column=0, pady=10)
item1_entry.grid(row=1, column=1, pady=10)
quantity1.grid(row=1, column=2, pady=10)
quantity1_entry.grid(row=1, column=3, pady=10)

item2.grid(row=2, column=0, pady=10)
item2_entry.grid(row=2, column=1, pady=10)
quantity2.grid(row=2, column=2, pady=10)
quantity2_entry.grid(row=2, column=3, pady=10)

item3.grid(row=3, column=0, pady=10)
item3_entry.grid(row=3, column=1, pady=10)
quantity3.grid(row=3, column=2, pady=10)
quantity3_entry.grid(row=3, column=3, pady=10)

item4.grid(row=4, column=0, pady=10)
item4_entry.grid(row=4, column=1, pady=10)
quantity4.grid(row=4, column=2, pady=10)
quantity4_entry.grid(row=4, column=3, pady=10)

calorie_counter_button.grid(row=5, column=0, columnspan=4, pady=5)
calorie_label.grid(row=6, column=0, columnspan=4, pady=5)



# # Frame3 layout
# title_history.grid(row=0,column=0)
# history_label.grid(row=1,column=0)
# history_entry.grid(row=1,column=1,pady=20)
# show_history_btn.grid(row=2,column=0,columnspan=2)  
title_history.grid(row=0, column=0, padx=0, pady=10)
history_label.grid(row=1, column=0, padx=10, pady=10)
cal.grid(row=2, column=0, padx=10, pady=10)
show_history_btn.grid(row=2, column=1, padx=10, pady=10)


# Frame4 layout
bmi_title.grid(row=0, column=0)
# bmi_name_label.grid(row=1, column=0)
# bmi_name_entry.grid(row=1, column=1,pady=20)
weight_label.grid(row=2, column=0)
weight_entry.grid(row=2, column=1,pady=10)
height_label.grid(row=3, column=0)
height_entry.grid(row=3, column=1,pady=10)
calculate_button.grid(row=4, column=0, columnspan=2)
# bmi_result_label.grid(row=1, column=10, columnspan=2,pady=15)

bmi_result_label.grid(row=0, column=0, columnspan=2, pady=10)
# enter_raw_data()--> Frame2
show_calorie_table_info()

# Pack the frame
frame.place(x=180,y=80)
frame1.place(x=180,y=200)
frame3.place(x=930,y=50)
frame2.place(x=610,y=50)
frame4.place(x=210,y=510)
frame5.place(x=610,y=510)

# Start the GUI event loop
window.mainloop()


# Close the database connection when the application exits
conn.close()



