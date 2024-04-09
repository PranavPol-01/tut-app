import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess
import sys
from ttkbootstrap import Style
from ttkbootstrap.scrolled import ScrolledFrame

current_user = sys.argv[1]

# Define the quiz questions and answers
quiz_questions = [
    {
        "question": "How many players are there in a standard football (soccer) team?",
        "choices": ["9", "10", "11", "12"],
        "answer": "11"
    },
    {
        "question": "What is the maximum duration of a football match in regular time?",
        "choices": ["80 minutes", "90 minutes", "100 minutes", "120 minutes"],
        "answer": "90 minutes"
    },
    {
        "question": "What is the name of the trophy awarded to the winners of the FIFA World Cup?",
        "choices": ["Golden Globe", "Silver Cup", "Golden Boot", "FIFA World Cup Trophy"],
        "answer": "FIFA World Cup Trophy"
    },
    {
        "question": "Which country has won the most FIFA World Cup titles?",
        "choices": ["Brazil", "Germany", "Italy", "Argentina"],
        "answer": "Brazil"
    },
    {
        "question": "Who is the all-time leading goalscorer in FIFA World Cup history?",
        "choices": ["Pelé", "Diego Maradona", "Miroslav Klose", "Lionel Messi"],
        "answer": "Miroslav Klose"
    },
    {
        "question": "What is the circumference of a standard football (soccer) ball?",
        "choices": ["68–70 cm", "71–73 cm", "74–76 cm", "77–79 cm"],
        "answer": "68–70 cm"
    },
    {
        "question": "Which player has won the most FIFA Ballon d'Or awards?",
        "choices": ["Lionel Messi", "Cristiano Ronaldo", "Michel Platini", "Johan Cruyff"],
        "answer": "Lionel Messi"
    },
    {
        "question": "Who is the only player to have won FIFA World Cup Golden Boot, Golden Ball, and Golden Glove in the same tournament?",
        "choices": ["Pelé", "Diego Maradona", "Ronaldo", "Zinedine Zidane"],
        "answer": "Diego Maradona"
    },
    {
        "question": "Which country hosted the first ever FIFA World Cup in 1930?",
        "choices": ["Brazil", "Argentina", "Uruguay", "Italy"],
        "answer": "Uruguay"
    },
    {
        "question": "What is the maximum number of substitutions allowed in a football match?",
        "choices": ["3", "4", "5", "6"],
        "answer": "3"
    }
]

choice_variables = []  # Define choice_variables outside of the loop


def navigate_to_recommendation():
    print("Navigating to recommendation page...")
    root.destroy()
    subprocess.run(["python", "recommendation.py", current_user])


def navigate_to_test():
    print("Navigating to test page...") 
     # Placeholder for navigation logic
    root.destroy()
    subprocess.run(["python", "test.py",current_user])

def navigate_to_explore():
    print("Navigating to explore page...")
    subprocess.run(["python", "calorie_entry.py", current_user])


def check_answer():
    user_answers = [variable.get() for variable in choice_variables]
    correct_answers = [question["answer"] for question in quiz_questions]
    score = sum(user_answer == correct_answer for user_answer, correct_answer in zip(user_answers, correct_answers))
    messagebox.showinfo("Quiz Finished",
                        f"Congratulations! You have completed the quiz. You scored {score} out of {len(quiz_questions)} questions correctly.")
    for variable in choice_variables:
        variable.set("")  # Reset the radio button selections
    root.destroy()
    subprocess.run(["python", "recommendation.py", current_user])


root = tk.Tk()
root.title("Sports Quiz for Football")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

style = Style(theme="lumen")
style.configure("Inverted.TLabel", background=style.colors.dark, foreground=style.colors.light)
# Set the geometry of the root window to fill the screen
root.geometry("%dx%d" % (width, height))

style.configure("Sidebar.TButton", font=("Helvetica", 16), width=15)

sidebar_frame = ttk.Frame(root, padding=20, style="Inverted.TLabel", borderwidth=12, )
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

# Add components to the sidebar
sidebar_label = ttk.Label(sidebar_frame, text="Navbar", font=("Arial", 16,'bold'),background=style.colors.dark,foreground=style.colors.light)
sidebar_label.pack(pady=10)
button_width = 20

sidebar_button1 = ttk.Button(sidebar_frame, text="Recommendation", style="Sidebar.TButton",
                              command=navigate_to_recommendation)
sidebar_button1.pack(pady=5)

sidebar_button2 = ttk.Button(sidebar_frame, text="Test", style="Sidebar.TButton", command=navigate_to_test)
sidebar_button2.pack(pady=5)

sidebar_button3 = ttk.Button(sidebar_frame, text="Fitness", style="Sidebar.TButton", command=navigate_to_explore)
sidebar_button3.pack(pady=5)


# Scrolled Frame
scrolled_frame = ScrolledFrame(root)
scrolled_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Quiz label
quiz_label = tk.Label(scrolled_frame, text="Football Quiz", font=("Helvetica", 22, "bold"),fg='#146C94')
quiz_label.pack(pady=10)

# Display all questions and options
y_offset = 0
y_increment = 10  # Increase this value to increase spacing between questions
for question_data in quiz_questions:
    question_label = tk.Label(scrolled_frame, text=question_data["question"], font=("Helvetica", 14))
    question_label.pack(anchor='w', padx=20, pady=20)

    choice_frame = ttk.Frame(scrolled_frame)
    choice_frame.pack(anchor='w', padx=40, pady=10)

    for choice in question_data["choices"]:
        choice_var = tk.StringVar(value="")
        choice_variables.append(choice_var)
        choice_button = ttk.Radiobutton(choice_frame, text=choice, variable=choice_var, value=choice)
        choice_button.pack(side="left", padx=10)

    y_offset += y_increment

# Submit button
submit_button = ttk.Button(scrolled_frame, text="Submit", command=check_answer)
submit_button.pack()

root.mainloop()
