import tkinter as tk

# Start a new window
window = tk.Tk()
# Give the window a title
window.title('my window')
# Set the window's geometry(size)
window.geometry('200x200')

# Create an window for Entry
# If want to hide text while entry, do something like show='*'
e = tk.Entry(window, show=None)
e.pack()

# Define function for button1
def insert_point():
    var = e.get()
    t.insert('insert', var)

'''
Hidden Case
We can insert it to certain place (certain line and column)
def insert_place():
    var = e.get()
    # The '1.1' here means to insert at first row, first column
    t.insert(1.1, var)
'''


# Create a button
b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
# Put it on
b1.pack()

# Define function for button2
def insert_end():
    var = e.get()
    t.insert('end', var)

b2 = tk.Button(window, text='insert end', width=15, height=2, command=insert_end)
b2.pack()

# Initialize a text, which can be changed by user, appearing at the bottom part
t = tk.Text(window, height=2) # height=2 means the window automatically give two-line space
t.pack()

# Let the window to refresh itself constantly
window.mainloop()
