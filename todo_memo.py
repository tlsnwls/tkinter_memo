import os
import tkinter as tk
from tkinter import scrolledtext, messagebox

# File Path Setting
file_path = os.path.join(os.path.expanduser("~"), "memo.txt")  # Saved to your home directory

def save_file():
    try:
        with open(file_path, 'w') as file:
            file.write(text_area.get("1.0", tk.END))
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred while saving the file: {e}")

def load_file():
    try:
        with open(file_path, 'r') as file:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, file.read())
    except FileNotFoundError:
        messagebox.showwarning("No Such File", "No saved file")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred while loading the file: {e}")

def auto_save():
    save_file()  # Call the save_file function
    root.after(30000, auto_save)  # 30초 후에 다시 호출 (30000ms)

# Main Window Creation
root = tk.Tk()
root.title("ToDo-List")
root.geometry("400x300")

# Icon Setting
icon_path = os.path.join(os.path.expanduser("~"),"tkinter_memo","pngegg.png")  
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(True, icon) 

root.resizable(True,True)

# Create a scrollable text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Add Buttons
save_button = tk.Button(button_frame, text="Save!", command=save_file)
save_button.pack(side=tk.LEFT, padx=10)

# Automatically load file when program starts
load_file()

# Start auto-saving every 30 seconds
auto_save()

# Main Loop start
root.mainloop()