#!/usr/bin/env python3
"""Calculator GUI using Tkinter"""

import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x550")
        self.expression = ""
        self.result = tk.StringVar()
        self.create_ui()

    def create_ui(self):
        # Display
        display = tk.Entry(
            self.root,
            textvariable=self.result,
            font=('Arial', 20),
            justify='right'
        )
        display.pack(fill='both', padx=10, pady=10, ipady=10)
        self.result.set("0")

        # Buttons
        buttons = [
            ['C', '←', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '−'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']
        ]

        for row in buttons:
            frame = tk.Frame(self.root)
            frame.pack(fill='both', expand=True)

            for btn_text in row:
                if btn_text:
                    btn = tk.Button(
                        frame,
                        text=btn_text,
                        font=('Arial', 18),
                        command=lambda x=btn_text: self.on_click(x)
                    )
                    btn.pack(side='left', fill='both', expand=True, padx=2, pady=2)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.result.set("0")
        elif char == '←':
            self.expression = self.expression[:-1]
            self.result.set(self.expression or "0")
        elif char == '=':
            try:
                calc_expr = self.expression.replace('×', '*').replace('÷', '/').replace('−', '-')
                result = eval(calc_expr)
                self.expression = str(result)
                self.result.set(self.expression)
            except:
                self.result.set("Error")
        else:
            self.expression += char
            self.result.set(self.expression)

def main():
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
