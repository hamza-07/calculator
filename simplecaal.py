import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        self.memory = 0

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, font=("Times New Roman", 18), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        buttons = [
            ['%', 'CE', 'C', '⌫'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row_index, row in enumerate(buttons):
            for col_index, button in enumerate(row):
                self.create_button(button, row_index + 1, col_index)

        self.root.bind('<Return>', self.equal)
        self.root.bind('<BackSpace>', self.backspace)


    def create_button(self, text, row, col):
        if text == '=':
            button = tk.Button(self.root, text=text, font=("Times New Roman", 16), bg='skyblue', command=lambda: self.on_button_click(text))
        else:
            button = tk.Button(self.root, text=text, font=("Arial", 14), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        self.root.grid_rowconfigure(row, weight=1)
        self.root.grid_columnconfigure(col, weight=1)

    def on_button_click(self, char):
        if char in '0123456789':
            if self.entry.get() == "Invalid input":
                self.clear()
            self.expression += char
            self.entry.insert(tk.END, char)
        elif char == 'C':
            self.clear()
        elif char == 'CE':
            self.clear_entry()
        elif char == '⌫':
            self.backspace()
        elif char in '+-*/%':
            if self.entry.get() == "Invalid input":
                self.clear()
            self.expression += char
            self.entry.insert(tk.END, char)
        elif char == '=':
            self.equal()
        elif char == '.':
            if self.entry.get() == "Invalid input":
                self.clear()
            self.expression += char
            self.entry.insert(tk.END, char)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def backspace(self, event=None):
        current_text = self.entry.get()
        if current_text == "Invalid input":
            self.clear()
        else:
            self.expression = self.expression[:-1]
            self.entry.delete(len(self.entry.get()) - 1, tk.END)

    def equal(self, event=None):
        try:
            result = str(eval(self.expression))
            self.clear()
            self.entry.insert(tk.END, result)
            self.expression = result
        except Exception:
            self.clear()
            self.entry.insert(tk.END, "Invalid input")

    def toggle_sign(self):
        if self.entry.get() == "Invalid input":
            self.clear()
        if self.expression and self.expression[0] == '-':
            self.expression = self.expression[1:]
        else:
            self.expression = '-' + self.expression
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def reciprocal(self):
        try:
            result = str(1 / float(self.expression))
            self.clear()
            self.entry.insert(tk.END, result)
            self.expression = result
        except Exception:
            self.clear()
            self.entry.insert(tk.END, "Invalid input")

    def square(self):
        try:
            result = str(float(self.expression) ** 2)
            self.clear()
            self.entry.insert(tk.END, result)
            self.expression = result
        except Exception:
            self.clear()
            self.entry.insert(tk.END, "Invalid input")

    def square_root(self):
        try:
            result = str(float(self.expression) ** 0.5)
            self.clear()
            self.entry.insert(tk.END, result)
            self.expression = result
        except Exception:
            self.clear()
            self.entry.insert(tk.END, "Invalid input")

    def memory_clear(self):
        self.memory = 0

    def memory_recall(self):
        self.clear()
        self.entry.insert(tk.END, str(self.memory))
        self.expression = str(self.memory)

    def memory_add(self):
        try:
            self.memory += float(self.expression)
            self.clear()
        except Exception:
            self.clear()
            self.entry.insert(tk.END, "Invalid input")

    def memory_subtract(self):
        try:
            self.memory -= float(self.expression)
            self.clear()
        except Exception:
            self.clear()
            self.entry.insert(tk.END, "Invalid input")

    def memory_store(self):
        try:
            self.memory = float(self.expression)
            self.clear()
        except Exception:
            self.clear()
            self.entry.insert(tk.END, "Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
