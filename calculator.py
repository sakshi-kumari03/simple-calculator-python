import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count= len(button_values)  
column_count = len(button_values[0])  

color_blue ="#7A75BE"
color_pink = "#F177A8"
color_orange ="#FD998A"
color_yellow ="#F6DEC4"
color_white = "white"
color_black ="#333333"


window = tkinter.Tk() 
window.title("Calculator")
window.resizable(False,False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text ='0', font =("Arial", 45), background= color_blue,
                      foreground=color_white, anchor ="e", width=column_count)


label.grid(row=0, column =0, columnspan=column_count,sticky ="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text = value, font =("Arial",30),
                                width = column_count-1, height=1,
                                command = lambda value = value:button_clicked(value))
        
        if value in top_symbols:
            button.config(foreground=color_white, background=color_pink)
        elif value in right_symbols:
            button.config(foreground=color_white,background=color_orange)
        else:
            button.config(foreground=color_black, background=color_yellow)
        button.grid(row =row+1,column=column)
frame.pack()


A="0"
operator = None
B= None


def clear_all():
    global A,B,operator
    A="0"
    operator = None
    B= None

def remove_decimal(num):
    if num% 1 ==0:
        num = int(num)
    return str(num)


def button_clicked(value):
    global right_symbols, top_symbols, label, A, B,operator

    if value in right_symbols:
        if value =="=":
            if A is not None and operator is  not None:
                B= label["text"]
                num1 = float(A)
                num2 = float(B)

                if operator =="+":
                    label["text"]= remove_decimal(num1 + num2)
                elif operator =="-":
                    label["text"]= remove_decimal(num1 - num2)
                elif operator =="×":
                    label["text"]= remove_decimal(num1 * num2)
                elif operator=="÷":
                    label["text"]= remove_decimal(num1 / num2)
                
                clear_all()

        elif value in "+-÷×":
            if operator is None:
                A= label["text"]
                label["text"]="0"
                B="0"
            
            operator = value

    elif value in top_symbols:
        if value =="AC":
            clear_all()
        elif value =="+/-":
            result = float(label["text"]) *-1
            label["text"] = remove_decimal(result)
        elif value =="%":
            result = float(label["text"]) / 100
            label["text"] = remove_decimal(result)
    else: 
        if value ==".":
            if value not in label["text"]:
                label["text"]+= value
        elif value in "0123456789":
            if label["text"] =='0':
                label["text"]= value  
            else:
                label["text"] += value  
    
window.mainloop()  

