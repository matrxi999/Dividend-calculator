from tkinter import *
import dividend

window = Tk()
window.title("Dividend calculator")

def dividend_amount():

    symbol = str(e10_value.get())

    total_div = float(e9_value.get())*dividend.get_div_value(symbol)

    total_div_wo_tax = total_div * (1-float(e11_value.get())*0.01)

    total_div_per_y = total_div * float(e12_value.get())

    total_div_per_y_wo_tax = total_div_per_y * (1-float(e11_value.get())*0.01)

    t1.delete("1.0", END)
    t1.insert(END,total_div)

    t2.delete("1.0", END)
    t2.insert(END,total_div_wo_tax)

    t3.delete("1.0", END)
    t3.insert(END,total_div_per_y)

    t4.delete("1.0", END)
    t4.insert(END,total_div_per_y_wo_tax)


# Create the Label widgets
e1 = Label(window, text = "Enter the amount oh shares")
e2 = Label(window, text = "Enter the stock symbol")
e3 = Label(window, text = "Enter the tax rate")
e4 = Label(window, text = "Enter the dividend frequency")

e5 = Label(window, text = "Total amount of dividend")
e6 = Label(window, text = "Total amount of dividend after tax")
e7 = Label(window, text = "Total amount of dividend per year")
e8 = Label(window, text = "Total amount of dividend per year after tax")

e9_value = StringVar()
e9 = Entry(window, textvariable = e9_value)
e10_value = StringVar()
e10 = Entry(window, textvariable = e10_value)
e11_value = StringVar()
e11 = Entry(window, textvariable = e11_value)
e12_value = StringVar()
e12 = Entry(window, textvariable = e12_value)

# Create the Text Widgets
t1 = Text(window, height = 1, width = 20)
t2 = Text(window, height = 1, width = 20)
t3 = Text(window, height = 1, width = 20)
t4 = Text(window, height = 1, width = 20)

# Create the Button Widget
b1 = Button(window, text = "Calculate", command = dividend_amount)

# grid method is used for placing
# the widgets at respective positions
# in table like structure
e1.grid(row = 0, column = 0)
e2.grid(row = 1, column = 0)
e3.grid(row = 2, column = 0)
e4.grid(row = 3, column = 0)
e5.grid(row = 5, column = 0)
e6.grid(row = 6, column = 0)
e7.grid(row = 7, column = 0)
e8.grid(row = 8, column = 0)

e9.grid(row = 0, column = 2)
e10.grid(row = 1, column = 2)
e11.grid(row = 2, column = 2)
e12.grid(row = 3, column = 2)

b1.grid(row = 4, column = 0)

t1.grid(row = 5, column = 2)
t2.grid(row = 6, column = 2)
t3.grid(row = 7, column = 2)
t4.grid(row = 8, column = 2)

# Start the GUI
window.mainloop()