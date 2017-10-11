import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# Create a variable
var = tk.StringVar()

# Create a Label
l = tk.Label(window, bg='yellow', width=20, text=None)
l.pack()

# Function for 1st Radiobutton
def print_selection():
    # config() means to 改变相应参数
    l.config(text='you have selected ' + var.get())

# Create 1st Radiobutton
r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A',
                    command=print_selection)
r1.pack()

# Create 2st Radiobutton
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B',
                    command=print_selection)
r2.pack()

# Create 3st Radiobutton
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C',
                    command=print_selection)
r3.pack()

window.mainloop()
