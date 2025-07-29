import tkinter as tk

# App initialization
root = tk.Tk()
root.title("Ordinary Calculator")
root.geometry("320x420")
root.configure(bg="#1e1e1e")
root.resizable(False, False)
root.attributes('-topmost', True)

# display screen
display = tk.Entry(
    root,
    font=('Segoe UI', 24),
    bg="white",          
    fg="black",          
    bd=0,
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew", ipady=15)

# logic to add text in display
def insert_to_display(char):
    display.insert(tk.END, char)

# Logic to evaluate expression
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Clear display (saaf)
def clear_display():
    display.delete(0, tk.END)

# Percentage function
def percentage():
    try:
        val = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(val / 100))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Square function
def square_value():
    try:
        val = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(val ** 2))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Brackets toggle ()
bracket_open = True
def toggle_bracket():
    global bracket_open
    if bracket_open:
        display.insert(tk.END, "(")
    else:
        display.insert(tk.END, ")")
    bracket_open = not bracket_open

# Button layout
button_labels = [
    ['AC', '/', '*', '-'],
    ['7', '8', '9', '+'],
    ['4', '5', '6', '()'],
    ['1', '2', '3', 'x²'],
    ['0', '.', '%', '=']
]

# Color names (humanized)
color_map = {
    # Group 1: Soft Purple
    '0': "medium orchid",'.': "medium orchid",'%': "medium orchid",'x²': "medium orchid",

    # Group 2: Lavender Pink
    '1': "orchid",'2': "orchid",'3': "orchid",'()': "orchid",

    # Group 3: Plum
    '4': "plum",'5': "plum",'6': "plum",'+': "plum",

    # Group 4: Light Violet
    '7': "thistle",'8': "thistle",'9': "thistle",'-': "thistle",

    # Group 5: Pale Pink
    'AC': "lavender blush",      '/': "lavender blush",
    '*': "lavender blush",

    '=': "medium orchid"
}

# Creating and placing buttons
for row_index, row in enumerate(button_labels, start=1):
    for col_index, label in enumerate(row):
        if label == 'AC':
            action = clear_display
        elif label == '=':
            action = calculate
        elif label == '%':
            action = percentage
        elif label == 'x²':
            action = square_value
        elif label == '()':
            action = toggle_bracket
        else:
            action = lambda val=label: insert_to_display(val)

        # Get background color
        bg = color_map.get(label, "#333")
        fg = "black" if bg == "lavender blush" else "white"

        button = tk.Button(
            root,
            text=label,
            font=('Segoe UI', 16),
            width=5,
            height=2,
            bg=bg,
            fg=fg,
            bd=0,
            command=action
        )
        button.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")

# Make layout responsive
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

# Run app
root.mainloop()
