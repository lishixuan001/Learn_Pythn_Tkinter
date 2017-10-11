import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

tk.Label(window, text='on the window').pack()

# Define main Frame
frm = tk.Frame(window)
frm.pack()

# Left Frame
frm_l = tk.Frame(frm)
# Right Frame
frm_r = tk.Frame(frm)

# Pack的参数，上下左右(基于主Frame)
frm_l.pack(side='left')
frm_r.pack(side='right'

tk.Label(frm_l, text='on the frm_l1').pack()
tk.Label(frm_l, text='on the frm_l2').pack()
tk.Label(frm_r, text='on the frm_r1').pack()


window.mainloop()
