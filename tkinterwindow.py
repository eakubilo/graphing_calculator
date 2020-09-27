from tkinter import *
from mathplot import plot

window = Tk()

window.title('Plotting in Tkinter')

window.geometry =("500x500")

plot_button = Button(master = window, command = lambda: plot(window), height = 2, width = 10, text = "Plot")

plot_button.pack()

window.mainloop()