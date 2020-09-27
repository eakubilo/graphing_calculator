from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)
import math

def plot(window):
    fig = Figure(figsize=(5,5), dpi = 100)

    y = [math.sin(1/(i/1000)) for i in range(-1000,1000) if i != 0]
    x = [i/1000 for i in range(-1000,1000) if i != 0]
    print(y,x)
    plot1 = fig.add_subplot(111)

    plot1.plot(x,y)

    canvas = FigureCanvasTkAgg(fig,master = window)

    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas,window)

    toolbar.update()

    canvas.get_tk_widget().pack()

