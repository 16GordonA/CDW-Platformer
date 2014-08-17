'''
main.py

Creates the outermost frame for the world

@authors: Dan Dangond, Akiva Gordon, Pravina Samaratunga
'''

from Tkinter import Tk

class windowCommands:
    def __init__(self):
        pass

    def initialize(self):
        root = Tk()
        self.center(root)
        root.mainloop()
    
    def center(self, window):
	window.update()
	
	w=window.winfo_width()
	h=window.winfo_height()
	
	ws = window.winfo_screenwidth()
	hs = window.winfo_screenheight()
	
	x = (ws/2) - (w/2)    
	y = (hs/2) - (h/2) - 40
	
	window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def correct_size(self, window, h = 600, w = 800):
        window.geometry('%dx%d' % (w,h))

cmd = windowCommands()
window = cmd.initialize()
