# Glei Hoxhalli, Marguerite Centeno

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter
from tkinter import *
from ThreePointCalculator import ThreePointCalculator
from TopTenPositionCalculator import TopTenPositionCalculator

class AllTkinterWidgets:
      def __init__(self, master):
        frame = Frame(master)
        frame.pack(anchor = NW)

       # -------------------- Entry boxes ---------------------
        self.startYear = IntVar()
        self.endYear = IntVar()
        self.ef = Frame(frame, bd=2, relief='groove')
        self.startYearLabel = Label(self.ef, text='Start Year:')
        self.startYearLabel.pack(side=LEFT)
        self.startYearEntry = Entry(self.ef, textvariable=self.startYear, bg='white')
        self.startYearEntry.pack(side=LEFT, padx = 5)
        self.endYearLabel = Label(self.ef, text='End Year:')
        self.endYearLabel.pack(side=LEFT)
        self.endYearEntry = Entry(self.ef, textvariable=self.endYear)
        self.endYearEntry.pack(side=LEFT, padx=5)
        self.calculateButton = Button(self.ef, text='Calculate', command=self.calculate)
        self.calculateButton.pack(side=LEFT, padx= 5)
        self.ef.pack(expand=0, fill=X, pady=5, side=BOTTOM)
        
    
       # --------------------- Display frame ------------------------
        self.percentChange = DoubleVar()
        self.df = Frame(frame, bd=2, relief='groove')
        self.percentChangeLabel = Label(self.df, text='Change in 3P% Average:')
        self.percentChangeLabel.pack(side=LEFT, padx=5)
        self.percentChangeDisplay = Entry(self.df, textvariable=self.percentChange, bg='white')
        self.percentChangeDisplay.configure(state='readonly')
        self.percentChangeDisplay.pack(side=LEFT, padx=5)
        self.df.pack( fill=X, pady=5, before=self.ef, side=BOTTOM)


       # --------------------- Canvas frame ------------------------
        self.cf = Frame(frame, bd=2, relief='groove')
        self.figure = Figure(figsize=(6, 6))
        self.averagePlot = self.figure.add_subplot(211)
        self.averagePlot.set_title ("Average 3P% of Top 10 Players", fontsize=12)
        self.averagePlot.set_ylabel("3P%", fontsize=12)
        self.averagePlot.set_xlabel("Year", fontsize=12)
        self.modePlot = self.figure.add_subplot(212)
        self.modePlot.set_title ("Most Common Position of Top 10 Players", fontsize=12)
        self.modePlot.set_ylabel("Position", fontsize=12)
        self.modePlot.set_xlabel("Year", fontsize=12)
        self.figure.tight_layout(pad=2)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.cf)
        self.canvas.get_tk_widget().pack()
        self.cf.pack( fill=X, pady=5, before=self.df, side=BOTTOM)
      
        
       # -------------------- Function defs ------------------------

      def clear(self):
          self.percentChange.set(0.0)

      def calculate(self):
         self.clear()
         try:
            startYear = self.startYear.get()
            endYear = self.endYear.get()
            years = range(startYear, endYear + 1)

            threePointCalculator = ThreePointCalculator()
            averages = threePointCalculator.calculate(startYear, endYear)

            topTenCalculator = TopTenPositionCalculator()
            modes = topTenCalculator.calculate(startYear, endYear)

            self.percentChange.set(averages[-1] - averages[0])
            self.drawPlot(years, averages, modes)

         except:
            self.percentChange.set('Error')

      def drawPlot(self, years, averages, modes):
         self.averagePlot.cla()
         self.averagePlot.scatter(years, averages)
         self.averagePlot.set_title ("Average 3P% of top 10 Players", fontsize=12)
         self.averagePlot.set_ylabel("3P%", fontsize=12)
         self.averagePlot.set_xlabel("Year", fontsize=12)
         self.modePlot.cla()
         self.modePlot.scatter(years, modes);
         self.modePlot.set_title ("Most Common Position of top 10 Players", fontsize=12)
         self.modePlot.set_ylabel("Position", fontsize=12)
         self.modePlot.set_xlabel("Year", fontsize=12)
         self.canvas.draw()

root = Tk()
root.geometry('800x800')
root.configure(bg='white')
all = AllTkinterWidgets(root)
root.title('Computational Thinking ~ Assignment 4')
root.pack_propagate(0)
root.mainloop()
