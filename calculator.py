from tkinter import *

window = Tk()

def dividend_amount():
    total_div = float(e9_value.get())*float(e10_value.get())

    total_div_wo_tax = total_div * (1-float(e11_value.get())*0.01)

    print("Total amount of dividend: " + str(total_div))
    print("Total amount of dividend without tax: " + str(total_div_wo_tax))
    print("Total amount of dividend per year: " + str(total_div*div_freq))
    print("Total amount of dividend per year without tax: " + str(total_div_wo_tax*div_freq))


shares_amount = 20.6
div_per_share = 0.22
tax = 19
div_freq = 4

dividend_amount(shares_amount, div_per_share, tax, div_freq)

# Create the Label widgets
e1 = Label(window, text = "Enter the amount oh shares")
e2 = Label(window, text = "Enter the dividend payout")
e3 = Label(window, text = "Enter the tax rate")
e4 = Label(window, text = "Enter the dividend frequency")

e5 = Label(window, text = "Total amount of dividend")
e6 = Label(window, text = "Total amount of dividend without tax")
e7 = Label(window, text = "Total amount of dividend per year")
e8 = Label(window, text = "Total amount of dividend per year without tax")

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

t5 = Text(window, height = 1, width = 20)
t6 = Text(window, height = 1, width = 20)
t7 = Text(window, height = 1, width = 20)
t8 = Text(window, height = 1, width = 20)
