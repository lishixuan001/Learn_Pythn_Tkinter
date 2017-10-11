import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

'''放置--pack'''
# tk.Label(window, text=1).pack(side='top')
# tk.Label(window, text=1).pack(side='bottom')
# tk.Label(window, text=1).pack(side='left')
# tk.Label(window, text=1).pack(side='right')

'''建立grid(方格的形式)--grid'''
# for i in range(4):
#     for j in range(3):
#         # 'padx' 代表x方向的扩展
#         # 'ipadx' 代表内部的扩展
#         tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

'''放置在特定的点--place'''
tk.Label(window, text=1).place(x=10, y=100, anchor='nw')

window.mainloop()
