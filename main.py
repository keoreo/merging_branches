from tkinter import *

def Result():
    x.set(c1_count_var.get() / c2_count_var.get())


root = Tk()
root.title("К")
root.geometry("640x480")

c1_count_var = DoubleVar()
c2_count_var = DoubleVar()
x = DoubleVar()

c1_count = Label(text="Первое число", font="12")
c1_count.place(x=375, y=130)

c1_count_entry = Entry(width='5', textvariable=c1_count_var)
c1_count_entry.place(x=380, y=160)

c2_count = Label(text="Второе число", font="12")
c2_count.place(x=375, y=230)

c2_count_entry = Entry(width='5', textvariable=c2_count_var)
c2_count_entry.place(x=380, y=260)

btn = Button(root, text="Сложить", command=Result)
btn.place(x=100, y=100)

Output = Label(textvariable=x, font="20")
Output.place(x=100, y=200)

root.mainloop()