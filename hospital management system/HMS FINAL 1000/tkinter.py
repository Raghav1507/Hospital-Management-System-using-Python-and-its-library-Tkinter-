import tkinter as tk

def add_numbers():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

root = tk.Tk()
root.title("Addition Calculator")

entry1 = tk.Entry(root, width=15)
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(root, width=15)
entry2.grid(row=0, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()