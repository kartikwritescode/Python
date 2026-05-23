import tkinter as tk

def show_quad():
    root = tk.Tk()
    root.title("quadratic eqn")
    root.geometry("300x200")

    label = tk.Label(root, text="🖕", font=("Arial", 100))
    label.pack(expand=True)

    root.mainloop()

show_quad()
