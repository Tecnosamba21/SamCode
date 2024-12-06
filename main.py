from tkinter import *


#Colors (const)
BLACK = "#000000"
WHITE = "#ffffff"

# Window and configurations
window = Tk()
window.title("SamCode")

writebox = Text(window, bg=BLACK, foreground=WHITE, font="Arial")
writebox.pack(fill=BOTH, expand=True)

window.mainloop()