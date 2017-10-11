import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# Create a Label
l = tk.Label(window, bg='yellow', width=20, text=None)
l.pack()

# Function for Scale
def print_selection(v):
    # config() means to 改变相应参数
    l.config(text='you have selected ' + v)

# Define a Scale
# Since 'from' is a built-in function in python, we define it as 'from_'
# 'orient' 表示拖条的方向
# 'length' 代表像素数，条的长度
# 'showvalue' 决定在拖动的时候，在拖扭旁边有没有显示值，1为True，0为False(用数字表示时)
# 'tickinterval' 代表标签的单位长度
# ‘resolution’ 代表保留几位小数
s = tk.Scale(window, label='try me', from_=5, to_=11, orient=tk.HORIZONTAL,
        length=200, showvalue=False, tickinterval=3, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
