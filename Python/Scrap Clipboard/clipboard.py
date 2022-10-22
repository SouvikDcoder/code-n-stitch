# from tkinter import Tk
import tkinter
import os

# root = Tk()
# # Main application code goes here
# root.mainloop()

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

window = tkinter.Tk()
window.title("Kuro's Clipboard Manager!")
label = tkinter.label(window, text='Hello World!').pack()
window.mainloop()