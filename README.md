# Your own Memo Application 
---
## 📌How to use this application?
- Open your terminal, go to the path of the downloaded file and run python3 todo_memo.py.
- `python3 todo_memo.py`
---
↑ _This is a hassle to do every time!_

## 📌 How to Automatically Run a Program at Startup (by OS)
- ### Windows
Convert a Python Script to a .bat File: 

- Open Notepad or any text editor.

- Enter the following content:
```
@echo off
start pythonw "C:\path\to\your_script.py"
```
- Replace C:\path\to\your_script.py with the actual path to your Python script.

- Save the file as start_script.bat

Add a Batch File to Startup:

- Press Win + R to open the Run dialog
- Type `shell:startup` and press Enter to open the Startup folder
- Copy yout .bat file into this folder

- ### Linux(Debian/Ubuntu)

- Enter Startup Application : GUI Program run automatically at boot time
- Add a new itme : enter a Python script in the command
- `python3 /home/username/tkinter_memo/todo_memo.py`

---
Version2 Released!! 
- Auto Save!
- Tk program Icon added!
