from tkinter import * # import whole module
class CurrencyConveter: # create a class
    def __init__(self): # special method in python class
        window=Tk() # create the application window
        window.title("Currency Converter") # add title to application window
        window.configure(bg="yellow")  # add background colour to application window
        # adding labels towidgets to application window
        Label(window,font="Helvetica 12 bold",bg="yellow",text="Amount to Convert : ").grid(row=1,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="yellow",text="Conversion Rate : ").grid(row=2,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="yellow",text="Converted Amount :").grid(row=3,column=1,sticky=W)
        # create objects and add entry function
        self.amountConvertVar=StringVar()
        Entry(window,textvariable=self.amountConvertVar,justify=RIGHT).grid(row=1,column=2,padx=15)
        self.conversionRateVar=StringVar()
        Entry(window,textvariable=self.conversionRateVar,justify=RIGHT).grid(row=2,column=2,padx=15)
        self.convertedAmountVar=StringVar()
        ConvertedAmount=Label(window,font="Helvetica 12 bold",bg="yellow",textvariable=self.convertedAmountVar).grid(row=3,column=2,sticky=E)
        # create convert and clear buttons when clicked they will call their respective functions
        btConvertAmount=Button(window,text="Convert",font="Helvetica 12 bold",bg="blue",fg="white",command=self.ConvertedAmount).grid(row=4,column=2,sticky=E)
        btClear=Button(window,text="Clear",font="Helvetica 12 bold",bg="red",fg="white",command=self.Clear).grid(row=4,column=6,padx=25,pady=25,sticky=E)
        window.mainloop() # run the application program
    # functions for the conversion 
    def ConvertedAmount(self):
        amt=float(self.conversionRateVar.get())
        convertedAmountVar=float(self.amountConvertVar.get())*amt
        self.convertedAmountVar.set(format(convertedAmountVar,'10.2f'))
    # function to clear input data
    def Clear(self):
        self.amountConvertVar.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")
CurrencyConveter()





        
