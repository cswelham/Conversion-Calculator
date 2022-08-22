from tkinter import *   #imports tkinter for GUI
from tkinter.ttk import * 

class GUI():
    
    def __init__(self, parent):

        entryFont = ('Arial',10, 'bold')
        labelFont = ('Arial',10, 'bold')
        buttonFont = ('Arial', 10)
          
        parent.resizable(0,0)
    
        #length
        tabControl = Notebook(parent)          
        tab1 = Frame(tabControl)            
        tabControl.add(tab1, text='Length')      
        tabControl.pack(expand=1, fill="both")

        self.entryLengthInput = Entry(tab1, width=12, font=entryFont)
        self.entryLengthOutput = Entry(tab1, width=12, font=entryFont)
        self.entryLengthInput.grid(row=0, column=0, columnspan=4)
        self.entryLengthOutput.grid(row=0, column=9, columnspan=4)
            
        self.varLength1 = StringVar(tab1)
        self.varLength1.set("Choose")
        self.varLength2 = StringVar(tab1)
        self.varLength2.set("Choose")
        
        menuLengthInput = (OptionMenu(tab1, self.varLength1, "Choose", "Millimeters", "Centimeters", "Inches", "Miles", "Meters", "Kilometers", "Feet", "Yards")
                     .grid(row=1, column=1, columnspan=4, sticky=NSEW))
        menuLengthOutput = (OptionMenu(tab1, self.varLength2, "Choose", "Millimeters", "Centimeters", "Inches", "Miles", "Meters", "Kilometers", "Feet", "Yards")
                      .grid(row=1, column=9, columnspan=4, sticky=NSEW))

        convertLengthButton = (Button(tab1, text="Convert", command=self.convertLength).grid(row=2, column=1, sticky=NSEW))
        resetLengthButton = (Button(tab1, text="Reset", command=self.reset).grid(row=2, column=9, sticky=NSEW))

        self.lengthUnits = ["Millimeters", "Centimeters", "Inches", "Miles", "Meters", "Kilometers", "Feet", "Yards"]
        self.lengthAmounts = [1000, 100, 39.37007874, 0.0006213689, 1, 0.001, 1.0936132983, 1.09361]

        #weight         
        tab2 = Frame(tabControl)            
        tabControl.add(tab2, text='Weight')      
        tabControl.pack(expand=1, fill="both")

        self.entryWeightInput = Entry(tab2, width=12, font=entryFont)
        self.entryWeightOutput = Entry(tab2, width=12, font=entryFont)
        self.entryWeightInput.grid(row=0, column=0, columnspan=4)
        self.entryWeightOutput.grid(row=0, column=9, columnspan=4)
            
        self.varWeight1 = StringVar(tab2)
        self.varWeight1.set("Choose")
        self.varWeight2 = StringVar(tab2)
        self.varWeight2.set("Choose")
        
        menuWeightInput = (OptionMenu(tab2, self.varWeight1, "Choose", "Metric Tons", "Kilograms", "Pounds", "Ounces", "Grams", "Tons")
                     .grid(row=1, column=1, columnspan=4, sticky=NSEW))
        menuWeightOutput = (OptionMenu(tab2, self.varWeight2, "Choose", "Metric Tons", "Kilograms", "Pounds", "Ounces", "Grams", "Tons")
                      .grid(row=1, column=9, columnspan=4, sticky=NSEW))

        convertWeightButton = (Button(tab2, text="Convert", command=self.convertWeight).grid(row=2, column=1, sticky=NSEW))
        resetWeightButton = (Button(tab2, text="Reset", command=self.reset).grid(row=2, column=9, sticky=NSEW))

        self.weightUnits = ["Metric Tons", "Kilograms", "Pounds", "Ounces", "Grams", "Tons"]
        self.weightAmounts = [0.00110231, 1, 2.20462, 35.264, 1000, 0.001]

        #temperature          
        tab3 = Frame(tabControl)            
        tabControl.add(tab3, text='Temperature')      
        tabControl.pack(expand=1, fill="both")

        self.entryTempInput = Entry(tab3, width=12, font=entryFont)
        self.entryTempOutput = Entry(tab3, width=12, font=entryFont)
        self.entryTempInput.grid(row=0, column=0, columnspan=4)
        self.entryTempOutput.grid(row=0, column=9, columnspan=4)
            
        self.varTemp1 = StringVar(tab3)
        self.varTemp1.set("Choose")
        self.varTemp2 = StringVar(tab3)
        self.varTemp2.set("Choose")
        
        menuTempInput = (OptionMenu(tab3, self.varTemp1, "Choose", "Celsius", "Farenheit", "Kelvin")
                     .grid(row=1, column=1, columnspan=4, sticky=NSEW))
        menuTempOutput = (OptionMenu(tab3, self.varTemp2, "Choose", "Celsius", "Farenheit", "Kelvin")
                      .grid(row=1, column=9, columnspan=4, sticky=NSEW))

        convertTempButton = (Button(tab3, text="Convert", command=self.convertTemp).grid(row=2, column=1, sticky=NSEW))
        resetTempButton = (Button(tab3, text="Reset", command=self.reset).grid(row=2, column=9, sticky=NSEW))

        self.tempUnits = ["Celsius", "Farenheit", "Kelvin"]
        self.tempAmounts = [1, 0, 273.15]

    def exitCalc(self):
        root.destroy()

class Logic(GUI):

    def reset(self):
        self.entryLengthInput.delete(0, END)
        self.entryLengthOutput.delete(0, END)
        self.entryWeightInput.delete(0, END)
        self.entryWeightOutput.delete(0, END)
        self.entryTempInput.delete(0, END)
        self.entryTempOutput.delete(0, END)
        self.varLength1.set("Choose")
        self.varLength2.set("Choose")
        self.varWeight1.set("Choose")
        self.varWeight2.set("Choose")
        self.varTemp1.set("Choose")
        self.varTemp2.set("Choose")
    
    def convertLength(self):
        if self.varLength1.get() in self.lengthUnits:
            self.entryLengthOutput.delete(0, END)
            initialPlace = self.lengthUnits.index(self.varLength1.get())
            initialConverter = self.lengthAmounts[initialPlace]
            userInput = self.entryLengthInput.get()
            initialTotal = float(userInput) / float(initialConverter)
        if self.varLength2.get() in self.lengthUnits:
            finalPlace = self.lengthUnits.index(self.varLength2.get())
            finalConverter = self.lengthAmounts[finalPlace]
            finalTotal = float(initialTotal) * float(finalConverter)
            self.entryLengthOutput.insert(0, finalTotal)

    def convertWeight(self):
        if self.varWeight1.get() in self.weightUnits:
            self.entryWeightOutput.delete(0, END)
            initialPlace = self.weightUnits.index(self.varWeight1.get())
            initialConverter = self.weightAmounts[initialPlace]
            userInput = self.entryWeightInput.get()
            initialTotal = float(userInput) / float(initialConverter)
        if self.varWeight2.get() in self.weightUnits:
            finalPlace = self.weightUnits.index(self.varWeight2.get())
            finalConverter = self.weightAmounts[finalPlace]
            finalTotal = float(initialTotal) * float(finalConverter)
            self.entryWeightOutput.insert(0, finalTotal)

    def convertTemp(self):
        if self.varTemp1.get() in self.tempUnits:
            self.entryTempOutput.delete(0, END)
            initialPlace = self.tempUnits.index(self.varTemp1.get())
            initialConverter = self.tempAmounts[initialPlace]
            userInput = self.entryTempInput.get()
            if self.varTemp1.get() == "Celsius":
                initialTotal = float(userInput) / float(initialConverter)
            elif self.varTemp1.get() == "Farenheit":
                initialTotal = (float(userInput) - 32) * 5/9
            else:
                intialTotal = float(userInput) - float(initialConverter)
        if self.varTemp2.get() in self.tempUnits:
            finalPlace = self.tempUnits.index(self.varTemp2.get())
            finalConverter = self.tempAmounts[finalPlace]
            if self.varTemp2.get() == "Celsius":
                finalTotal = float(initialTotal) * float(finalConverter)
            elif self.varTemp2.get() == "Farenheit":
                finalTotal = (float(initialTotal) * 9/5) + 32
            else:
                finalTotal = float(initialTotal) + float(initialConverter)
            self.entryTempOutput.insert(0, finalTotal)
            
if __name__ == "__main__":
    root = Tk()
    test = Logic(root)  
