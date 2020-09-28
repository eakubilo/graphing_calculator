from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)
import math
import numpy


def sin(x):
    return numpy.sin(x)
def cos(x):
    return numpy.cos(x)
def tan(x):
    return numpy.tan(x)
def sqrt(x):
    return numpy.sqrt(x)
def plot(window, func):
    counter = 0
    k = len(window.winfo_children())
    while counter < k:
        if counter == 2:
            window.winfo_children()[2].destroy()
            k-=1
        else:
            counter+=1
        
    fig = Figure(figsize=(5,5), dpi = 100)

    x = numpy.arange(-100.,100.,.0001)

    plot1 = fig.add_subplot(111)
    plot1.set_ylim(-1,1)
    plot1.set_xlim(-1,1)
    plot1.plot(x,eval(func))
    plot1.grid(b=True, which = "both", axis = "both")
    canvas = FigureCanvasTkAgg(fig,master = window)
    
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas,window)

    toolbar.update()

    canvas.get_tk_widget().pack()

