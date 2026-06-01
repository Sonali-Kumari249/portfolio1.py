from tkinter import *
from tkinter import messagebox
import webbrowser

def open_github():
    webbrowser.open("https://github.com/Sonali-Kumari249")

def open_linkedin():
    webbrowser.open("https://www.linkedin.com/in/sonali-kumari-68b712310")

def open_resume():
    messagebox.showinfo(
        "Resume",
        r"C:\Users\Sonali Kumari\Desktop\sonaliresume..pdf"
    )
root = Tk()
root.title("Student Portfolio")
root.geometry("1000x700")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

canvas = Canvas(main_frame, bg="#f0f8ff")
canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

content_frame = Frame(canvas, bg="#f0f8ff")

canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Mouse Wheel Scroll

def mouse_scroll(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", mouse_scroll)

title = Label(
    content_frame,
    text="SONALI KUMARI",
    font=("Arial", 28, "bold"),
    bg="#f0f8ff",
    fg="#003366"
)
title.pack(pady=10)

subtitle = Label(
    content_frame,
    text="B.Tech CSE Student | Python Developer | AI/ML Enthusiast",
    font=("Arial", 14),
    bg="#f0f8ff"
)
subtitle.pack()

about_frame = LabelFrame(
    content_frame,
    text="About Me",
    font=("Arial", 12, "bold"),
    bg="blue",
    padx=10,
    pady=10
)
about_frame.pack(fill="x", padx=20, pady=10)

Label(
    about_frame,
    text="""
I am a B.Tech Computer Science Engineering student.

Interested in:
• Python Development
• AI/ML
• Data Science
• Web Development

Currently building projects to strengthen my placement profile.
""",
    bg="white",
    justify=LEFT,
    font=("Arial", 11)
).pack()

edu_frame = LabelFrame(
    content_frame,
    text="Education",
    font=("Arial", 12, "bold"),
    bg="blue",
    padx=10,
    pady=10
)
edu_frame.pack(fill="x", padx=20, pady=10)

Label(
    edu_frame,
    text="""
B.Tech Computer Science Engineering

University: Your University Name

Expected Graduation: 2028

Current CGPA: 8.4
""",
    bg="white",
    justify=LEFT,
    font=("Arial", 11)
).pack()

skill_frame = LabelFrame(
    content_frame,
    text="Skills",
    font=("Arial", 12, "bold"),
    bg="blue",
    padx=10,
    pady=10
)
skill_frame.pack(fill="x", padx=20, pady=10)

Label(
    skill_frame,
    text="""
• Python
• C Programming
• Java
• Data Structures & Algorithms
• HTML
• CSS
• JavaScript
• Git & GitHub
• AI/ML Fundamentals
""",
    bg="white",
    justify=LEFT,
    font=("Arial", 11)
).pack()

project_frame = LabelFrame(
    content_frame,
    text="Projects",
    font=("Arial", 12, "bold"),
    bg="blue",
    padx=10,
    pady=10
)
project_frame.pack(fill="x", padx=20, pady=10)

Label(
    project_frame,
    text="""
1. GUI Calculator using Python Tkinter

2. Personal Portfolio Application

3. Student Management System

4. AI Chatbot (Future Project)

5. Expense Tracker (Future Project)
""",
    bg="white",
    justify=LEFT,
    font=("Arial", 11)
).pack()

cert_frame = LabelFrame(
    content_frame,
    text="Certifications",
    font=("Arial", 12, "bold"),
    bg="blue",
    padx=10,
    pady=10
)
cert_frame.pack(fill="x", padx=20, pady=10)

Label(
    cert_frame,
    text="""
• Python Programming Certificate

• AI/ML Summer Training

• Generative AI Fundamentals

• Data Science Basics

• Git & GitHub Workshop
""",
    bg="white",
    justify=LEFT,
    font=("Arial", 11)
).pack()

contact_frame = LabelFrame(
    content_frame,
    text="Contact",
    font=("Arial", 12, "bold"),
    bg="blue",
    padx=10,
    pady=10
)
contact_frame.pack(fill="x", padx=20, pady=10)

Label(
    contact_frame,
    text="""
Email : sonalikumari71069@gmail.com

Phone : +91 9905428105

Location : Lucknow, Uttar Pradesh, India
""",
    bg="white",
    justify=LEFT,
    font=("Arial", 11)
).pack()
button_frame = Frame(content_frame, bg="#f0f8ff")
button_frame.pack(pady=20)

Button(
    button_frame,
    text="GitHub",
    width=15,
    command=open_github,
    font=("Arial", 11, "bold")
).grid(row=0, column=0, padx=10)

Button(
    button_frame,
    text="LinkedIn",
    width=15,
    command=open_linkedin,
    font=("Arial", 11, "bold")
).grid(row=0, column=1, padx=10)

Button(
    button_frame,
    text="Resume",
    width=15,
    command=open_resume,
    font=("Arial", 11, "bold")
).grid(row=0, column=2, padx=10)
footer = Label(
    content_frame,
    text="© 2026 Sonali Kumari | Portfolio Project ",
    bg="#f0f8ff",
    fg="gray",
    font=("Arial", 10)
)
footer.pack(pady=20)
root.mainloop()
#portfolio updated