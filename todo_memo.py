import os
import tkinter as tk
from tkinter import scrolledtext, messagebox

# File Path Setting
file_path = os.path.join(os.path.expanduser("~"), "memo.txt") # Saved Yout Home Directory

def save_file():
    try:
        with open('memo.txt','w') as file:
            file.write(text_area.get("1.0",tk.END))
        messagebox.showinfo("Successfully Saved!","Saved File")
    except Exception as e:
        messagebox.showerror("Error",f"Error occurred while saving the file : {e}")

def load_file():
    try:
        with open('memo.txt','r') as file:
            text_area.delete("1.0",tk.END)
            text_area.insert(tk.END, file.read())
    except FileNotFoundError:
        messagebox.showwarning("No Such File","No Saved file")
    except Exception as e:
        messagebox.showerror("Error",f"Error occured while loading the file : {e}")

# Main Window Creative
root = tk.Tk()
root.title("ToDo-List")
root.geometry("400x300")
root.resizable(False, False)

# Create a scrollable text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15)
text_area.pack(padx=10,pady=10)

# Add Button
save_button = tk.Button(root, text="Save!", command=save_file)
save_button.pack(side=tk.LEFT, padx=10)

# load_button = tk.Button(root,text="Load Content!", command=load_file)
# load_button.pack(side=tk.LEFT, padx=10)

# Automatically laod file when program starts
load_file()

# Main Loop start
root.mainloop()