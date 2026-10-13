
import tkinter as tk
from tkinter import messagebox
import text_analyzer

root = tk.Tk()
root.title("Text Analyser")
root.geometry("800x850")
root.config(bg="#1B1F3B")

tk.Label(
    root,
    text="TEXT ANALYSER",
    font=("Arial", 22, "bold"),
    bg="#1B1F3B",
    fg="#FFF3CD"
).pack(pady=10)

tk.Label(
    root,
    text="Enter your paragraph:",
    bg="#1B1F3B",
    fg="white",
    font=("Arial", 12)
).pack()

input_box = tk.Text(root, height=12, width=75, font=("Arial", 11))
input_box.pack(padx=10, pady=10)


def run_analyser1():
    text = input_box.get("1.0", "end-1c")

    if not text.strip():
        messagebox.showwarning("Warning", "Please enter a paragraph!")
        return

    try:
        text_analyzer.main(text)
        messagebox.showinfo(
            "Success",
            "Analysis complete! Check analyser.txt"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))




tk.Label(
    root,
    text="Analysis Results:",
    bg="#1B1F3B",
    fg="#FFF3CD",
    font=("Arial", 12, "bold")
).pack()

output_box = tk.Text(root, height=12, width=75, font=("Consolas", 10))
output_box.pack(padx=10, pady=10)
output_box.config(state="disabled")


def run_analyser():
    text = input_box.get("1.0", "end-1c")

    if not text.strip():
        messagebox.showwarning("Warning", "Please enter a paragraph!")
        return

    try:
        result = text_analyzer.main(text)

        output_box.config(state="normal")
        output_box.delete("1.0", "end")
        output_box.insert("1.0", result)
        output_box.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))
tk.Button(
    root,
    text="Analyse",
    command=run_analyser,
    font=("Arial", 12, "bold"),
    bg="#FFF3CD",
    fg="#1B1F3B"
).pack(pady=10)



root.mainloop()
