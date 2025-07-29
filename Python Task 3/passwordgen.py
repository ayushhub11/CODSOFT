import tkinter as tk
import random
import string

def make_password():
    try:
        size = int(length_entry.get())
        if size <= 0:
            output_label.config(text="Please enter number above 0")
            return
    except:
        output_label.config(text="Please type a number only")
        return

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(size):
        password += random.choice(all_chars)

    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)
    output_label.config(text="")

def copy_password():
    text = result_entry.get()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        output_label.config(text="Password copied")

root = tk.Tk()
root.title("Password Maker")
root.geometry("350x250")
root.config(bg="white")
root.resizable(False, False)

tk.Label(root, text="Enter password length:", bg="white").pack(pady=10)
length_entry = tk.Entry(root, width=30)
length_entry.pack()
tk.Button(root, text="Make Password", command=make_password).pack(pady=10)

result_entry = tk.Entry(root, width=35)
result_entry.pack(pady=5)

tk.Button(root, text="Copy", command=copy_password).pack(pady=5)
output_label = tk.Label(root, text="", fg="green", bg="white")
output_label.pack(pady=5)


#Run app 
root.mainloop()
