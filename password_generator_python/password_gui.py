import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# --- Password Generation Logic (from previous enhancement) ---
def generate_strong_password(length: int) -> str:
    if length < 4:
        raise ValueError("Password length must be at least 4.")
    password_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password_chars.extend(random.choices(all_chars, k=length - 4))
    random.shuffle(password_chars)
    return ''.join(password_chars)

# --- GUI Application ---
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        # Style configuration
        style = ttk.Style(self.root)
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 10, "bold"))
        style.configure("TEntry", font=("Courier", 12))

        # --- Widgets ---
        # Length selection
        ttk.Label(self.root, text="Password Length:").pack(pady=(10, 0))
        self.length_var = tk.IntVar(value=12)
        ttk.Spinbox(self.root, from_=4, to=50, textvariable=self.length_var, width=5).pack()

        # Generate button
        ttk.Button(self.root, text="Generate Password", command=self.generate_and_display).pack(pady=10)

        # Password display
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(self.root, textvariable=self.password_var, state="readonly", width=35, justify="center")
        password_entry.pack(pady=5)

        # Copy button
        ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack()

    def generate_and_display(self):
        try:
            length = self.length_var.get()
            password = generate_strong_password(length)
            self.password_var.set(password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy.")

if __name__ == "__main__":
    main_window = tk.Tk()
    app = PasswordGeneratorApp(main_window)
    main_window.mainloop()