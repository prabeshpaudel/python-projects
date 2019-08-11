import tkinter as tk
import parser

root = tk.Tk()
root.title("Calculator")
#get the user input and place in the input field
i=0
def get_variable(num):
    global i
    display.insert(i,num)
    i+=1

def clear_all():
    display.delete(0,tk.END)

def undo():
    entire_string= display.get()
    if len(entire_string)>0:
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)

    else:
        clear_all()
        display.insert(0,"error")

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i+=length

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)

    except Exception:
        clear_all()
        display.insert(0, "error")

def factorial():
    number = int(display.get())
    a=1
    for i in range(1,number+1):
        a=a*i
    clear_all()
    display.insert(0,a)


#adding the input field
display = tk.Entry(root)
display.grid(row = 1, columnspan = 6, sticky = tk.W + tk.E, padx=10, pady=10)

#adding buttons
button1 = tk.Button(root, text= "1", command = lambda : get_variable(1))
button1.grid(row = 2, column = 0, padx=3, pady=3)

button2 = tk.Button(root, text= "2", command = lambda : get_variable(2))
button2.grid(row = 2, column = 1, padx=3, pady=3)
button3 = tk.Button(root, text= "3", command = lambda : get_variable(3))
button3.grid(row = 2, column = 2, padx=3, pady=3)

button4 = tk.Button(root, text= "4", command = lambda : get_variable(4))
button4.grid(row = 3, column = 0, padx=3, pady=3)
button5 = tk.Button(root, text= "5", command = lambda : get_variable(5))
button5.grid(row = 3, column = 1, padx=3, pady=3)
button6 = tk.Button(root, text= "6", command = lambda : get_variable(6))
button6.grid(row = 3, column = 2, padx=3, pady=3)

button7 = tk.Button(root, text= "7", command = lambda : get_variable(7))
button7.grid(row = 4, column = 0, padx=3, pady=3)
button8 = tk.Button(root, text= "8", command = lambda : get_variable(8))
button8.grid(row = 4, column = 1, padx=3, pady=3)
button9 = tk.Button(root, text= "9", command = lambda : get_variable(9))
button9.grid(row = 4, column = 2, padx=3, pady=3)

button0 = tk.Button(root, text= "0", command = lambda : get_variable(0))
button0.grid(row = 5, column = 1, padx=3, pady=3)

#adding other buttons
ac_button = tk.Button(root, text= "AC", command= lambda : clear_all())
ac_button.grid(row = 5, column = 0, padx=3, pady=3)

equal_button = tk.Button(root, text= "=", command= lambda : calculate())
equal_button.grid(row = 5, column = 2, padx=3, pady=3)

#adding +/-/x//
plus_button = tk.Button(root, text= "+", command = lambda : get_operation("+"))
plus_button.grid(row = 2, column = 3, padx=3, pady=3)

minus_button = tk.Button(root, text= "-", command = lambda : get_operation("-"))
minus_button.grid(row = 3, column = 3, padx=3, pady=3)

multiply_button = tk.Button(root, text= "x", command = lambda : get_operation("*"))
multiply_button.grid(row = 4, column = 3, padx=3, pady=3)

divide_button = tk.Button(root, text= "/", command = lambda : get_operation("/"))
divide_button.grid(row = 5, column = 3, padx=3, pady=3)

#adding other operators
pi_button = tk.Button(root, text= "pi", command = lambda : get_operation("*3.14"))
pi_button.grid(row = 2, column = 4, padx=3, pady=3)

percent_button = tk.Button(root, text= "%", command = lambda : get_operation("%"))
percent_button.grid(row = 3, column = 4, padx=3, pady=3)

parentheses_open_button = tk.Button(root, text= "(", command = lambda : get_operation("("))
parentheses_open_button.grid(row = 4, column = 4, padx=3, pady=3)

exp_button = tk.Button(root, text= "exp", command = lambda : get_operation("**"))
exp_button.grid(row = 5, column = 4, padx=3, pady=3)

#______________________________________________________

delete_button = tk.Button(root, text= "<-", command = lambda : undo())
delete_button.grid(row = 2, column = 5, padx=3, pady=3)

factorial_button = tk.Button(root, text= "x!", command = lambda : factorial())
factorial_button.grid(row = 3, column = 5, padx=3, pady=3)

parentheses_close_button = tk.Button(root, text= ")", command = lambda : get_operation(")"))
parentheses_close_button.grid(row = 4, column = 5, padx=3, pady=3)

square_button = tk.Button(root, text= "x^2", command = lambda : get_operation("**2"))
square_button.grid(row = 5, column = 5, padx=3, pady=3)

root.mainloop()
