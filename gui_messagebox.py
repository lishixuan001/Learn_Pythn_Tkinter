import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    ''' Different messagebox has different logos'''
    # tk.messagebox.showinfo(title='Hi', message='information')
    # tk.messagebox.showwarning(title='Hi', message='warning')
    # tk.messagebox.showerror(title='Hi', message='error')
    # print(tk.messagebox.askquestion(title='Hi', message='question')) # return 'yes'/'no'
    # # if return == 'yes' # 用户交互
    # print(tk.messagebox.askyesno(title='Hi', message='yesno')) # return True/False
    # print(tk.messagebox.asktrycancel(title='Hi', message='trycancel')) # return True/False
    print(tk.messagebox.askokcancel(title='Hi', message='okcancel')) # return True/False

tk.Button(window, text='hit me', command=hit_me).pack()


window.mainloop()
