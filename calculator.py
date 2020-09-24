from tkinter import *
from tkinter import messagebox as mb


def onclick_input(number):
    length = len(entry.get())
    entry.insert(length, number)

def onclick_symbol(symbol):
    if entry.get() and entry.get()[-1] not in '+-*/':
        onclick_input(symbol)

def equal(*args):
    expression = entry.get()
    key_tracker = True
    if expression:
        for i in expression:
            if i not in '0123456789+-*/.':
                key_tracker = False
                break
        if key_tracker:
            if expression[-1] in '+-*/.':
                mb.showerror('Error', 'An expression can\'t end with symbol!')
            else:
                try:
                    answer = eval(expression)
                    entry.delete(0, END)
                    entry.insert(0, answer)
                except SyntaxError:
                    mb.showerror('Error', 'Syntax error!')
                except ZeroDivisionError:
                    mb.showerror('Error', 'Zero division is not allowed!')
        else:
            mb.showerror('Error', 'You typed unallowed symbols!')

def clear_all():
    entry.delete(0, END)

def backspace():
    length = len(entry.get())
    entry.delete(length-1)


root = Tk()
root.title('Calculator')
root.resizable(False, False)

entry = Entry(root, width=34, bd=2, font='24')
entry.grid(row=0, column=0, columnspan=5, padx=5, pady=10)

button0 = Button(
    root, text="0", width=13, height=3, font='24',
    command = lambda: onclick_input(0)
    )
button1 = Button(
    root, text="1", width=6, height=3, font='24',
    command = lambda: onclick_input(1)
    )
button2 = Button(
    root, text="2", width=6, height=3, font='24',
    command = lambda: onclick_input(2)
    )
button3 = Button(
    root, text="3", width=6, height=3, font='24',
    command = lambda: onclick_input(3)
    )
button4 = Button(
    root, text="4", width=6, height=3, font='24',
    command = lambda: onclick_input(4)
    )
button5 = Button(
    root, text="5", width=6, height=3, font='24',
    command = lambda: onclick_input(5)
    )
button6 = Button(
    root, text="6", width=6, height=3, font='24',
    command = lambda: onclick_input(6)
    )
button7 = Button(
    root, text="7", width=6, height=3, font='24',
    command = lambda: onclick_input(7)
    )
button8 = Button(
    root, text="8", width=6, height=3, font='24',
    command = lambda: onclick_input(8)
    )
button9 = Button(
    root, text="9", width=6, height=3, font='24',
    command = lambda: onclick_input(9)
    )

button_eq = Button(
    root, text="=", width=6, height=3, font='24',
    bg='#49a2e6', fg='#fff',
    activebackground='#49a2e6', activeforeground='#fff',
    command = equal
    )
button_clear = Button(
    root, text="C", width=6, height=3, font='24',
    bg='#f05959', fg='#fff',
    activebackground='#f05959', activeforeground='#fff',
    command = clear_all
    )
button_backspace = Button(
    root, text="<=", width=6, height=3, font='24',
    bg='#f05959', fg='#fff',
    activebackground='#f05959', activeforeground='#fff',
    command = backspace
    )
button_plus = Button(
    root, text="+", width=6, height=3, font='24',
    bg='#828385', fg='#fff',
    activebackground='#828385', activeforeground='#fff',
    command = lambda: onclick_symbol('+')
    )
button_minus = Button(
    root, text="-", width=6, height=3, font='24',
    bg='#828385', fg='#fff',
    activebackground='#828385', activeforeground='#fff',
    command = lambda: onclick_symbol('-')
    )
button_multiply = Button(
    root, text="x", width=6, height=3, font='24',
    bg='#828385', fg='#fff',
    activebackground='#828385', activeforeground='#fff',
    command = lambda: onclick_symbol('*')
    )
button_divide = Button(
    root, text="/", width=6, height=3, font='24',
    bg='#828385', fg='#fff',
    activebackground='#828385', activeforeground='#fff',
    command = lambda: onclick_symbol('/')
    )
button_empt = Button(
    root, text='', width=13, height=3, font='24',
    bg='#828385', fg='#fff',
    activebackground='#828385', activeforeground='#fff',
    state=DISABLED
    )

button0.grid(row=4, column=0, columnspan=2)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button_backspace.grid(row=1, column=3)
button_clear.grid(row=1, column=4)
button_plus.grid(row=2, column=3)
button_minus.grid(row=2, column=4)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=3, column=4)
button_eq.grid(row=4, column=2)
button_empt.grid(row=4, column=3, columnspan=2)

root.bind('<Return>', equal)

root.mainloop()
