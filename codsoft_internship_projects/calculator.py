import tkinter as tk

# Function to update the display when a button is pressed
def button_click(value):
    current = display.get()
    display.set(current + value)

# Function to clear the display
def button_clear():
    display.set("")

# Function to evaluate the expression and update the display
def button_equals():
    try:
        result = eval(display.get())
        display.set(result)
    except Exception as e:
        display.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a StringVar for the display
display = tk.StringVar()

# Create the display widget
display_entry = tk.Entry(root, textvariable=display, font=("Arial", 24), bd=10, relief="ridge", justify="right")
display_entry.grid(row=0, column=0, columnspan=4)

# Define button text and layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create and place buttons
row_val = 1
col_val = 0
for button_text in buttons:
    if button_text == 'C':
        button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 18), command=button_clear)
    elif button_text == '=':
        button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 18), command=button_equals)
    else:
        button = tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 18), command=lambda text=button_text: button_click(text))
    
    button.grid(row=row_val, column=col_val, sticky="nsew")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid weights
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i + 1, weight=1)

# Start the main event loop
root.mainloop()
