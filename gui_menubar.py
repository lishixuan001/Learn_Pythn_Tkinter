import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, text='', bg='yellow')
l.pack()

# Function for 'File'
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter += 1

# Define menubar
menubar = tk.Menu(window)

'''Filemenu'''
# Define choices in Menu
filemenu = tk.Menu(menubar, tearoff=0)
# Add 'filemenu' into Menu with name 'File'
menubar.add_cascade(label='File', menu=filemenu)
# Add choices under 'File'
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
# Make a seperation line between choices' display
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

'''Editmenu'''
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

'''Submenu'''
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import',menu=submenu, underline=0)
submenu.add_command(label='Submenu1',command=do_job)

# Put Menu to window
window.config(menu=menubar)


window.mainloop()
