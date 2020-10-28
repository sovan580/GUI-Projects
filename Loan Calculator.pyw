from tkinter import * # imports the whole module
class LoanCalculator: # create a class
    # special function in a class for pythin
    def __init__(self):
        window=Tk() # create the application window
        window.title("Loan Calculator")# add title to application window
        window.configure(background="light green") # add background colour to application window
        # add labels to the widgets of the application
        Label(window,font="Helvetica 12 bold",bg="light green",text="Annual Interest Rate : ").grid(row=1,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="light green",text="Number of Years : ").grid(row=2,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="light green",text="Loan Amount : ").grid(row=3,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="light green",text="Monthly Payment : ").grid(row=4,column=1,sticky=W)
        Label(window,font="Helvetica 12 bold",bg="light green",text="Total Payment : ").grid(row=5,column=1,sticky=W)
        # add entry for input
        self.annualInterestRateVar=StringVar()
        Entry(window,textvariable=self.annualInterestRateVar,justify=RIGHT).grid(row=1,column=2)
        self.numberOfYearsVar=StringVar()
        Entry(window,textvariable=self.numberOfYearsVar,justify=RIGHT).grid(row=2,column=2)
        self.loanAmountVar=StringVar()
        Entry(window,textvariable=self.loanAmountVar,justify=RIGHT).grid(row=3,column=2)
        self.monthlyPaymentVar=StringVar()
        MonthlyPayment=Label(window,font="Helvetica 12 bold",bg="light green",textvariable=self.monthlyPaymentVar).grid(row=4,column=2,sticky=E)
        self.totalPaymentVar=StringVar()
        TotalPayment=Label(window,font="Helvetica 12 bold",bg="light green",textvariable=self.totalPaymentVar).grid(row=5,column=2,sticky=E)
        # add compute and clear buttons
        btComputePayment=Button(window,text="Compute Payment",bg="blue",fg="white",font="Helvetica 14 bold",command=self.computePayment).grid(row=6,column=2,sticky=E)
        btClear=Button(window,text="Clear",bg="red",fg="white",font="Helvetica 14 bold",command=self.clear).grid(row=6,column=3,padx=20,pady=20,sticky=E)
        # set mainloop for application to run
        window.mainloop()
    # used functions definations
    def computePayment(self):
        monthlyPayment=self.getMonthlyPayment(float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get())/1200,
            float(self.numberOfYearsVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment,"10.2f"))
        totalPayment=float(self.monthlyPaymentVar.get())*12\
            *int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment,'10.2f'))
    def getMonthlyPayment(self,loanAmount,monthlyInterestRate,numberOfYears):
        monthlyPayment=loanAmount*monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(numberOfYears*12))
        return monthlyPayment    
    def clear(self):
        self.monthlyPaymentVar.set("")
        self.annualInterestRateVar.set("")
        self.loanAmountVar.set("")
        self.numberOfYearsVar.set("")
        self.totalPaymentVar.set("")
LoanCalculator()




        




