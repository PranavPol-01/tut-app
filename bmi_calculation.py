# import tkinter as tk
# import sqlite3
# from tkinter import messagebox

# # Create a SQLite database (or connect to an existing one)
# conn = sqlite3.connect("bmi_tracker.db")
# cursor = conn.cursor()

# # Create a table to store user BMI entries
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS bmi_entries (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         weight_kg REAL,
#         height_cm REAL
#     )
# """)
# conn.commit()

# def calculate_bmi():
#     name = name_entry.get()
#     weight_kg = float(weight_entry.get())
#     height_cm = float(height_entry.get())

#     # Calculate BMI
#     height_m = height_cm / 100
#     bmi = weight_kg / (height_m ** 2)
#     bmi = round(bmi, 1)

#     # Store the entry in the database
#     cursor.execute("INSERT INTO bmi_entries (name, weight_kg, height_cm) VALUES (?, ?, ?)",
#                    (name, weight_kg, height_cm))
#     conn.commit()

#     # Display BMI category
#     bmi_index(bmi)

# def bmi_index(bmi):
#     if bmi < 18.5:
#         category = "Underweight"
#     elif 18.5 <= bmi < 24.9:
#         category = "Normal"
#     elif 25 <= bmi < 29.9:
#         category = "Overweight"
#     else:
#         category = "Obesity"

#     result_label.config(text=f"BMI: {bmi} ({category})")

# # Create the main application window
# window = tk.Tk()
# window.title("BMI Calculator")

# # Entry fields
# name_label = tk.Label(window, text="Name:")
# name_entry = tk.Entry(window)
# weight_label = tk.Label(window, text="Weight (kg):")
# weight_entry = tk.Entry(window)
# height_label = tk.Label(window, text="Height (cm):")
# height_entry = tk.Entry(window)

# # Buttons
# calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)

# # Result display
# result_label = tk.Label(window, text="")

# # Layout
# name_label.grid(row=0, column=0)
# name_entry.grid(row=0, column=1)
# weight_label.grid(row=1, column=0)
# weight_entry.grid(row=1, column=1)
# height_label.grid(row=2, column=0)
# height_entry.grid(row=2, column=1)
# calculate_button.grid(row=3, column=0, columnspan=2)
# result_label.grid(row=4, column=0, columnspan=2)

# # Start the GUI event loop
# window.mainloop()

# # Close the database connection when the application exits
# conn.close()



























import tkinter as tk
import sqlite3
from tkinter import messagebox

# Create a SQLite database (or connect to an existing one)
conn = sqlite3.connect("bmi_tracker.db")
cursor = conn.cursor()

# Create a table to store user BMI entries
cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi_entries (
        id INTEGER PRIMARY KEY,
        name TEXT,
        weight_kg REAL,
        height_cm REAL
    )
""")
conn.commit()

def calculate_bmi():
    name = name_entry.get()
    weight_kg = float(weight_entry.get())
    height_cm = float(height_entry.get())

    # Calculate BMI
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 1)

    # Store the entry in the database
    cursor.execute("INSERT INTO bmi_entries (name, weight_kg, height_cm) VALUES (?, ?, ?)",
                   (name, weight_kg, height_cm))
    conn.commit()

    # Display BMI category and exercise recommendations
    bmi_index(bmi)

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

    result_label.config(text=f"BMI: {bmi} ({category})\n\nExercise Recommendations:\n" + "\n".join(recommendations))

# Create the main application window
window = tk.Tk()
window.title("BMI Calculator")

# Entry fields
name_label = tk.Label(window, text="Name:")
name_entry = tk.Entry(window)
weight_label = tk.Label(window, text="Weight (kg):")
weight_entry = tk.Entry(window)
height_label = tk.Label(window, text="Height (cm):")
height_entry = tk.Entry(window)

# Buttons
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)

# Result display
result_label = tk.Label(window, text="")

# Layout
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
weight_label.grid(row=1, column=0)
weight_entry.grid(row=1, column=1)
height_label.grid(row=2, column=0)
height_entry.grid(row=2, column=1)
calculate_button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)

# Start the GUI event loop
window.mainloop()

# Close the database connection when the application exits
conn.close()

































# import tkinter as tk
# import sqlite3
# from tkinter import messagebox

# # Create a SQLite database (or connect to an existing one)
# conn = sqlite3.connect("bmi_tracker.db")
# cursor = conn.cursor()

# # Create a table to store user BMI entries
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS bmi_entries (
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         weight_kg REAL,
#         height_cm REAL,
#         age INTEGER
#     )
# """)
# conn.commit()

# def calculate_bmi():
#     name = name_entry.get()
#     weight_kg = float(weight_entry.get())
#     height_cm = float(height_entry.get())
#     age = int(age_var.get())

#     # Calculate BMI
#     height_m = height_cm / 100
#     bmi = weight_kg / (height_m ** 2)
#     bmi = round(bmi, 1)

#     # Store the entry in the database
#     cursor.execute("INSERT INTO bmi_entries (name, weight_kg, height_cm, age) VALUES (?, ?, ?, ?)",
#                    (name, weight_kg, height_cm, age))
#     conn.commit()

#     # Display BMI category and exercise recommendations
#     bmi_index(bmi, age)

# def bmi_index(bmi, age):
#     if bmi < 18.5:
#         category = "Underweight"
#     elif 18.5 <= bmi < 24.9:
#         category = "Normal"
#     elif 25 <= bmi < 29.9:
#         category = "Overweight"
#     else:
#         category = "Obesity"

#     # Adjust recommendations based on age
#     if age <= 12:
#         recommendations = [
#             "1. Swimming: Freestyle, breaststroke, or backstroke are good options to build muscle mass.",
#             "2. Running: Short bursts of running or jogging can be beneficial for children.",
#             "3. Gymnastics: Improves flexibility, strength, and coordination."
#         ]
#     elif 13 <= age <= 21:
#         recommendations = [
#             "1. Weightlifting: Focus on compound exercises like squats, deadlifts, and bench presses.",
#             "2. Cycling: Ride a bicycle to improve cardiovascular health and leg strength.",
#             "3. Yoga: Helps in improving flexibility, strength, and overall well-being."
#         ]
#     elif 22 <= age <= 35:
#         recommendations = [
#             "1. Running: Start with a mix of walking and running to build endurance and burn calories.",
#             "2. Aerobics: High-energy workouts like Zumba or aerobics classes can help with weight loss.",
#             "3. Interval Training: Incorporate intervals of high-intensity exercise with periods of rest."
#         ]
#     elif 36 <= age <= 55:
#         recommendations = [
#             "1. Yoga: Promotes flexibility, balance, and stress reduction.",
#             "2. Swimming: Low-impact exercise that's gentle on the joints.",
#             "3. Hiking: Enjoy nature while improving cardiovascular health and muscle strength."
#         ]
#     else:
#         recommendations = [
#             "1. Walking: A brisk walk is an excellent low-impact exercise for older adults.",
#             "2. Tai Chi: Improves balance, flexibility, and mental well-being.",
#             "3. Resistance Training: Helps maintain muscle mass and bone density as you age."
#         ]

#     result_label.config(text=f"BMI: {bmi} ({category})\n\nExercise Recommendations:\n" + "\n".join(recommendations))

# # Create the main application window
# window = tk.Tk()
# window.title("BMI Calculator")

# # Entry fields
# name_label = tk.Label(window, text="Name:")
# name_entry = tk.Entry(window)
# weight_label = tk.Label(window, text="Weight (kg):")
# weight_entry = tk.Entry(window)
# height_label = tk.Label(window, text="Height (cm):")
# height_entry = tk.Entry(window)
# age_label = tk.Label(window, text="Age:")
# age_var = tk.IntVar()
# age_dropdown = tk.OptionMenu(window, age_var, 8, 13, 22, 36, 56)
# age_var.set(8)  # Default age selection

# # Buttons
# calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)

# # Result display
# result_label = tk.Label(window, text="")

# # Layout
# name_label.grid(row=0, column=0)
# name_entry.grid(row=0, column=1)
# weight_label.grid(row=1, column=0)
# weight_entry.grid(row=1, column=1)
# height_label.grid(row=2, column=0)
# height_entry.grid(row=2, column=1)
# age_label.grid(row=3, column=0)
# age_dropdown.grid(row=3, column=1)
# calculate_button.grid(row=4, column=0, columnspan=2)
# result_label.grid(row=5, column=0, columnspan=2)

# # Start the GUI event loop
# window.mainloop()

# # Close the database connection when the application exits
# conn.close()
