from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Mathematical table")
window.geometry("400x600")

def multiply():
    value = size.get()
    number1 = quantity_name.get()
    table = ""
    for i in range(1,value+1):
        answer = i*number1
        table += "{}x{}={}\n".format(i,number1,answer)
    multiplication.config(text=table)
            

multiplication = Label(window,text="",font=("Aerial",13))
multiplication.place(x=100,y=225)
mathematical_table = Label(window,text="Mathematical table",font=("Aerial",12)).place(x=130,y=50)
number_range = Label(window,text="Number and Range:",font=("Aerial",12)).place(x=10,y=100)

quantity_name = IntVar()
quantity_number = Combobox(window,textvariable=quantity_name,width=15,height=10)
quantity_number["values"] = tuple(range(101))
quantity_number.place(x=200,y=100)

size = IntVar()
ten = Radiobutton(window,text="10",variable=size,value=10)
twenty = Radiobutton(window,text="20",variable=size,value=20)
thirty = Radiobutton(window,text="30",variable=size,value=30)
size.set(10)
ten.place(x=325,y=100)
twenty.place(x=325,y=125)
thirty.place(x=325,y=150)

generate = Button(window,text="generate",width=20,command=multiply)
generate.place(x=150,y=175,height=40)



window.mainloop()
