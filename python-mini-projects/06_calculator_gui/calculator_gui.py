#!/usr/bin/env python3
"""Beautiful Colorful Calculator - Beginner Friendly"""

import tkinter as tk

class Calc:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("330x450")
        self.root.configure(bg="#ffffff")
        self.root.resizable(False, False)

        self.expr = ""
        self.val = tk.StringVar(value="0")

        self.build_ui()

    def build_ui(self):
        # Display
        disp = tk.Entry(
            self.root,
            textvariable=self.val,
            font=("Arial", 32, "bold"),
            justify="right",
            bg="#f0f7ff",
            fg="#1a1a1a",
            border=0,
            relief="flat"
        )
        disp.pack(fill="both", padx=12, pady=15, ipady=18)

        # Color themes
        colors = {
            "num": "#e3f2fd",     # light blue
            "op":  "#ffcccb",     # soft red
            "act": "#c8e6c9",     # green
            "dot": "#fff3cd",     # soft yellow
            "eq":  "#90caf9"      # blue
        }

        # Buttons layout
        btns = [
            ["C", "←", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", "00", ".", "="]
        ]

        frame = tk.Frame(self.root, bg="white")
        frame.pack(fill="both", expand=True, padx=5, pady=5)

        for r in range(5):
            for c in range(4):
                txt = btns[r][c]

                # Color mapping
                if txt in "0123456789" or txt == "00":
                    bg = colors["num"]
                elif txt == ".":
                    bg = colors["dot"]
                elif txt == "=":
                    bg = colors["eq"]
                elif txt in ["C", "←"]:
                    bg = colors["act"]
                else:
                    bg = colors["op"]

                b = tk.Button(
                    frame,
                    text=txt,
                    font=("Arial", 20, "bold"),
                    bg=bg,
                    fg="black",
                    activebackground="#d9d9d9",
                    border=0,
                    command=lambda x=txt: self.press(x)
                )
                b.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)

        # Equal button sizes
        for i in range(5):
            frame.rowconfigure(i, weight=1)
        for i in range(4):
            frame.columnconfigure(i, weight=1)

    def press(self, ch):
        if ch == "C":
            self.expr = ""
            self.val.set("0")

        elif ch == "←":
            self.expr = self.expr[:-1]
            self.val.set(self.expr if self.expr else "0")

        elif ch == "=":
            try:
                self.expr = str(eval(self.expr))
                self.val.set(self.expr)
            except:
                self.val.set("Error")
                self.expr = ""

        else:
            self.expr += ch
            self.val.set(self.expr)

def main():
    root = tk.Tk()
    Calc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
