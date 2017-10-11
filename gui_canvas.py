import tkinter as tk


window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# Define Canvas
canvas = tk.Canvas(window, bg='blue', height=100, width=200)
imgPath = 'ins.gif'
image_file = tk.PhotoImage(file=imgPath)

# Create image
# '0,0' shows where to put the image
# 'anchor' 锚定的点
image = canvas.create_image(0,0, anchor='nw', image = image_file)
x0, y0, x1, y1 = 50, 50, 80, 80

# Create graphs
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
# 'start' and 'extent' shows the start and end arc(角度)
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
# Pack the canvas
canvas.pack()

def moveit():
    # Every time x moves 0, and y moves 2
    canvas.move(rect, 0, 2)

# Define Button
b = tk.Button(window, text='move', command=moveit).pack()



window.mainloop()
