import random
import time
import turtle
import tkinter as tk

# Create turtle and set up screen
t = turtle.Turtle()
turtle.bgcolor("#f2f2f2")
turtle.colormode(255)
t.speed(0)

# Create GUI window
root = tk.Tk()
root.title("Turtle Drawing Application")
root.geometry("400x190")
root.resizable(False, False)

# Add label to GUI window
label = tk.Label(root, text="Click the 'Start Drawing' button to start drawing!", font=("Arial", 12), bg="#f2f2f2")
label.pack(pady=10)

# Add canvas to turtle window
canvas = turtle.getcanvas()
canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# Define functions for drawing and stopping
def start_drawing():
    global drawing
    drawing = True
    while drawing:
        x = random.randint(-600, 600)
        y = random.randint(-600, 600)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pencolor(red, green, blue)
        shape = random.choice(['polygon', 'circle', 'square', 'rectangle', 'triangle'])
        if shape == 'polygon':
            sides = random.randint(3, 10)
            length = random.randint(10, 100)
            angle = 360 / sides
            for i in range(sides):
                t.forward(length)
                t.right(angle)
        elif shape == 'circle':
            radius = random.randint(10, 100)
            t.circle(radius)
        elif shape == 'square':
            length = random.randint(10, 100)
            for i in range(4):
                t.forward(length)
                t.right(90)
        elif shape == 'rectangle':
            length = random.randint(10, 100)
            width = random.randint(10, 100)
            for i in range(2):
                t.forward(length)
                t.right(90)
                t.forward(width)
                t.right(90)
        elif shape == 'triangle':
            length = random.randint(10, 100)
            for i in range(3):
                t.forward(length)
                t.right(120)
        root.update()
        time.sleep(0.1)


def stop_drawing():
    global drawing
    drawing = False


def clear_canvas():
    t.clear()


def on_closing():
    stop_drawing()
    root.destroy()


button_style = {"bg": "#4CAF50", "fg": "#FFFFFF", "font": ("Arial", 12), "bd": 0, "highlightthickness": 0,
                "activebackground": "#3E8E41", "activeforeground": "#FFFFFF"}

start_button = tk.Button(root, text="Start Drawing", command=start_drawing, relief=tk.RAISED, **button_style)
start_button.pack(pady=10, padx=20, fill=tk.X)

stop_button = tk.Button(root, text="Stop Drawing", command=stop_drawing, relief=tk.RAISED, **button_style)
stop_button.pack(pady=10, padx=20, fill=tk.X)

clear_button = tk.Button(root, text="Clear Canvas", command=clear_canvas, relief=tk.RAISED, **button_style)
clear_button.pack(pady=10, padx=20, fill=tk.X)

t.pen(fillcolor="#d9d9d9", pencolor="#333", pensize=3)

root.protocol("WM_DELETE_WINDOW", on_closing)

# Move turtle window to center of screen and add title
turtle.Screen().title("Turtle Drawing Application")
turtle.Screen().setup(width=800, height=600, startx=200, starty=50)

# Start GUI loop
turtle.mainloop()
