import tkinter as tk

# Start a new window
window = tk.Tk()
# Give the window a title
window.title('my window')
# Set the window's geometry(size)
window.geometry('200x100')

# # Put some label on the window
# # Create the label
# l = tk.Label(window, text='OMG! this is TK', bg='green', font=('Arial',12), width=15, height=2)

# Create a variable string
var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial',12), width=15, height=2)
# Put it on
l.pack()

# Define a global variable
"""
Note that since the window refresh itself everytime, the index variable
should be defined globally.
"""
on_hit = False
# Define the command function for the button
def hit_me():

    global on_hit
    on_hit = False
    if on_hit == False:
        var.set('you hit me')
        on_hit = True
    else:
        var.set('')
        on_hit = False

# Create a button
b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
# Put it on
b.pack()

# Let the window to refresh itself constantly
window.mainloop()
