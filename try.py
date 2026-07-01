import tkinter as tk

# --- Functions ---
def button_click(item):
    """Handles button clicks and updates the display."""
    global expression
    expression += str(item)
    input_text.set(expression)

def button_clear():
    """Clears the calculator display."""
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    """Evaluates the mathematical expression."""
    global expression
    try:
        # eval() computes the math expression in the string
        result = str(eval(expression))
        input_text.set(result)
        expression = result  # Allow continuing calculations with the result
    except ZeroDivisionError:
        input_text.set("Error: Div by 0")
        expression = ""
    except Exception:
        input_text.set("Error")
        expression = ""

# --- Main Window Setup ---
window = tk.Tk()
window.title("Python Calculator")
window.geometry("312x324")
window.resizable(0, 0)  # Prevents resizing of the window

expression = ""
input_text = tk.StringVar()

# --- Display Frame ---
input_frame = tk.Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)

# Input Field
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) # Increases height of the input field

# --- Button Frame ---
btns_frame = tk.Frame(window, width=312, height=272.5, bg="grey")
btns_frame.pack()

# --- Button Layout ---
# Row 1
clear_btn = tk.Button(btns_frame, text="Clear", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=button_clear).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide_btn = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("/")).grid(row=0, column=3, padx=1, pady=1)

# Row 2
btn_7 = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)
btn_8 = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)
btn_9 = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply_btn = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("*")).grid(row=1, column=3, padx=1, pady=1)

# Row 3
btn_4 = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)
btn_5 = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)
btn_6 = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus_btn = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("-")).grid(row=2, column=3, padx=1, pady=1)

# Row 4
btn_1 = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)
btn_2 = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)
btn_3 = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus_btn = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("+")).grid(row=3, column=3, padx=1, pady=1)

# Row 5
btn_0 = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point_btn = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click(".")).grid(row=4, column=2, padx=1, pady=1)
equal_btn = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=button_equal).grid(row=4, column=3, padx=1, pady=1)

# Run the application
window.mainloop()