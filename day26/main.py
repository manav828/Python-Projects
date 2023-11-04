from tkinter import *

window = Tk()

window.title('button click ')
window.minsize(height=200,width=300)
window.config(padx = 10,pady=20)

# text = 'click the button'
#
# my_lable = Label(text='bdjhbwbjdfguwgg')
# my_lable.grid(column=0,row=0)
#
# def button_click():
#     input_text = input.get()
#
#     my_lable.config(text=input_text)
#
# button1 = Button(text='click me' ,command=button_click)
# button1.grid(column=1,row=1)
#
# button = Button(text='new button' ,command=button_click)
# button.grid(row=0,column=2)
#
# input = Entry(width=15)
# input.grid(column=3,row=2)

def km_convert():
    input_txt = int(input.get())
    print('input_txt')
    km = input_txt*1.6
    km_text.config(text=km)



input = Entry(width=10)
input.grid(row=1,column=2)



miles = Label(text='Miles')
miles.grid(row=1,column=3)

text1 = Label(text='is equal to')
text1.grid(row=2,column=0)
#
km_text = Label(text='0')
km_text.grid(row=2,column=2)
#
text2 = Label(text='Km')
text2.grid(row=2,column=3)
#
button = Button(text='Calculate' , command=km_convert)
button.grid(column=2,row=3)










window.mainloop()