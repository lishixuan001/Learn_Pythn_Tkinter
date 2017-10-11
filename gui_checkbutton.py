import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# Create a Label
l = tk.Label(window, bg='yellow', width=20, text=None)
l.pack()

# Function for Checkbutton
def print_selection():
    if (var1.get() == 1) and (var2.get() == 0):
        l.config(text='I love only Python')
    elif (var1.get() == 0) and (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) and (var2.get() == 0):
        l.config(text='I don\'t love either')
    else:
        l.config(text='I love both')

var1 = tk.IntVar()
var2 = tk.IntVar()
# Define Checkbutton
# onvalue means the represented value when selected
c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0,
                            command=print_selection)
c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0,
                            command=print_selection)
c1.pack()
c2.pack()


window.mainloop()
