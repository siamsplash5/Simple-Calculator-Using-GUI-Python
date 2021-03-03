from tkinter import *


def clear():
    inputDisplay.delete(0, END)


def checking_error(equation):
    for i in range(0, len(equation) - 1):
        if '0' <= equation[i] <= '9' or '0' <= equation[i + 1] <= '9':
            continue
        else:
            return False
    return True


def equation_solver(equation):
    is_ok = checking_error(equation)

    if not is_ok:
        return False
    else:
        numbers = []
        symbol = []
        equation += '='
        length = len(equation)
        tmp = ""

        for i in range(0, length):
            if '0' <= equation[i] <= '9':
                tmp = tmp + equation[i]
            elif equation[i] != ' ':
                num = int(tmp)
                tmp = ""
                numbers.append(num)
                symbol.append(equation[i])

        m = len(symbol)
        index = 1
        ans = numbers[0]
        for i in range(0, m - 1):
            if symbol[i] == '+':
                ans = ans + numbers[index]
            elif symbol[i] == '-':
                ans = ans - numbers[index]
            elif symbol[i] == '*':
                ans = ans * numbers[index]
            elif symbol[i] == '/':
                ans = ans / numbers[index]

            index = index + 1

        return ans


def clicked(number):
    if number == "=":
        the_equation = inputDisplay.get()
        ans = equation_solver(the_equation)
        if ans == False:
            outputDisplay.delete(0, END)
            outputDisplay.insert(0, "Syntax ERROR!")
        else:
            outputDisplay.delete(0, END)
            outputDisplay.insert(0, string=ans)
    else:
        current_number = inputDisplay.get()
        inputDisplay.delete(0, END)
        inputDisplay.insert(0, str(current_number) + str(number))


window = Tk()
window.title("Calculator")
window.geometry('240x320')
window.configure(bg="#616A6B")
inputDisplay = Entry(window, justify="right", font=('Time New Romans', 10, 'bold'), width=30, borderwidth=5,
                     bg="#D5F5E3", fg="black")
inputDisplay.grid(row=0, column=0, columnspan=4, padx=5, pady=10)
inputDisplay.get()

outputDisplay = Entry(window, justify="right", font=('Time New Romans', 10, 'bold'), width=30, borderwidth=5,
                      bg="#D5F5E3", fg="black")
outputDisplay.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

bt1 = Button(window, text="1", padx=17, pady=5, command=lambda: clicked(1), bg="#161515", fg="white", borderwidth=4,
             font=('Arial', 9, 'bold'))
bt2 = Button(window, text="2", padx=17, pady=5, command=lambda: clicked(2), bg="#161515", fg="white", borderwidth=4,
             font=('Arial', 9, 'bold'))
bt3 = Button(window, text="3", padx=17, pady=5, command=lambda: clicked(3), bg="#161515", fg="white", borderwidth=4,
             font=('Arial', 9, 'bold'))
bt4 = Button(window, text="4", padx=17, pady=5, command=lambda: clicked(4), bg="#161515", fg="white", borderwidth=4,
             font=('Arial', 9, 'bold'))
bt5 = Button(window, text="5", padx=17, pady=5, command=lambda: clicked(5), bg="#161515", fg="white", borderwidth=4,
             font=('Arial', 9, 'bold'))
bt6 = Button(window, text="6", padx=17, pady=5, command=lambda: clicked(6), bg="#161515", fg="white", borderwidth=4,
             font=('Arial', 9, 'bold'))
bt7 = Button(window, text="7", padx=17, pady=5, command=lambda: clicked(7), bg="#161515", fg="white", borderwidth=4,
             font=('Arial', 9, 'bold'))
bt8 = Button(window, text="8", padx=17, pady=5, command=lambda: clicked(8), bg="#161515", fg="white", borderwidth=4,
             font=('Arial', 9, 'bold'))
bt9 = Button(window, text="9", padx=17, pady=5, command=lambda: clicked(9), bg="#161515", fg="white", borderwidth=4,
             font=('Arial', 9, 'bold'))
bt0 = Button(window, text="0", padx=17, pady=5, command=lambda: clicked(0), bg="#161515", fg="white", borderwidth=4,
             font=('Arial', 9, 'bold'))

btAdd = Button(window, text="+", padx=17, command=lambda: clicked("+"), pady=5, bg="#161515", fg="white", borderwidth=4,
               font=('Arial', 9, 'bold'))
btSub = Button(window, text="-", padx=17, command=lambda: clicked("-"), pady=5, bg="#161515", fg="white", borderwidth=4,
               font=('Arial', 9, 'bold'))
btMul = Button(window, text="*", padx=17, command=lambda: clicked("*"), pady=5, bg="#161515", fg="white", borderwidth=4,
               font=('Arial', 9, 'bold'))
btDiv = Button(window, text="/", padx=17, command=lambda: clicked("/"), pady=5, bg="#161515", fg="white", borderwidth=4,
               font=('Arial', 9, 'bold'))
btEqual = Button(window, text="=", padx=17, command=lambda: clicked("="), pady=5, bg="#161515", fg="white",
                 borderwidth=4, font=('Arial', 9, 'bold'))
btCLR = Button(window, text="CLR", padx=10, pady=5, command=clear, bg="#161515", fg="white", borderwidth=4,
               font=('Arial', 10, 'bold'))

bt7.grid(row=1, column=0)
bt8.grid(row=1, column=1)
bt9.grid(row=1, column=2)
btDiv.grid(row=1, column=3)

bt4.grid(row=2, column=0)
bt5.grid(row=2, column=1)
bt6.grid(row=2, column=2)
btMul.grid(row=2, column=3)

bt1.grid(row=3, column=0)
bt2.grid(row=3, column=1)
bt3.grid(row=3, column=2)
btSub.grid(row=3, column=3)

btCLR.grid(row=4, column=0)
bt0.grid(row=4, column=1)
btEqual.grid(row=4, column=2)
btAdd.grid(row=4, column=3)

window.mainloop()
