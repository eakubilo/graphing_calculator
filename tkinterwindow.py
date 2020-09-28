from tkinter import *
from mathplot import plot

window = Tk()
canvas = 0
fig = 0
window.title('Plotting in Tkinter')

window.geometry =("500x500")

e = Entry(window)

plot_button = Button(master = window, command = lambda: plot(window,e.get()), height = 2, width = 10, text = "Plot")

plot_button.pack()
e.pack()
window.mainloop()