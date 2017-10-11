import tkinter as tk

# Start a new window
window = tk.Tk()
# Give the window a title
window.title('my window')
# Set the window's geometry(size)
window.geometry('250x300')

# Define a variable
var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()

# Define function for button1
def print_selection():
    # Get what is seleted 'lb.curselection()'
    value = lb.get(lb.curselection())
    # Set the variable shown in the display window
    var1.set(value)

# Create a button
b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
# Put it on
b1.pack()

# Define second variable
var2 = tk.StringVar()
# Define some choices in Listbox
var2.set((11,22,33,44))
# Set the default choices
lb = tk.Listbox(window, listvariable=var2)

# Plug in some new choices in exsiting ones
list_items = [1,2,3,4]
for item in list_items:
    # plug in each item at the end of the exsiting ones
    lb.insert('end', item)
# pulg in new item base on index
lb.insert(1, 'first_plug_in')
lb.insert(2, 'second_plug_in')
# Delete a pluged-in item
lb.delete(2) # input is the index
lb.pack()

# Let the window to refresh itself constantly
window.mainloop()
