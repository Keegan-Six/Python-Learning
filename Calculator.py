from tkinter import *
root = Tk()

# memory for first number
memory1 = ""
# memory for operator
operator = ""
# chck if operator has been entered yet
operatorcheck = 0
# memory for second number
memory2 = ""

# button input redirector for numbers, redirects to master. 
def zero() :
    master("0","concatenate")
def one() :
    master("1","concatenate")
def two() :
    master("2","concatenate")
def three() :
    master("3","concatenate")
def four() :
    master("4","concatenate")
def five() :
    master("5","concatenate")
def six() :
    master("6","concatenate")
def seven() :
    master("7","concatenate")
def eight() :
    master("8","concatenate")
def nine() :
    master("9","concatenate")
def dot() :
    master(".","concatenate")
    
# button input director for operators
def equal() :
    master("=","equals")
def plus() :
    master("+","operator")
def minus() :
    master("-","operator")
def muiltiply() :
    master("x","operator")
def division() :
    master("/","operator")
    
# button input director for other functions
def percent() :
    master("%","null")

# clears current memory
def clear() :
    global memory1
    global memory2
    global operatorcheck
    global operator
    
    if (operatorcheck == 0) :
        memory1 = ""
        operator = ""
    else :
        memory2 = ""

    master("","null")

# clears all memory
def clearE() :
    global memory1
    global memory2
    global operatorcheck
    global operator
    
    memory1 = ""
    memory2 = ""
    operatorcheck = 0
    operator = ""
    master("","null")

# master computer, computes output
def master(input, operation) :
    global operatorcheck
    if (operation == "concatenate") :
        if (operatorcheck == 0) :
            global memory1
            output = memory1 + input
            label = Label(root, text = output, width = 5, height = 1)
            label.grid(row=0,column=0)
            memory1 = output
        else :
            global memory2
            output = memory2 + input
            label = Label(root, text = output, width = 5, height = 1)
            label.grid(row=0,column=0)
            memory2 = output
    elif (operation == "operator") :
        global operator
        operator = input
        label = Label(root, text = operator, width = 5, height = 1)
        label.grid(row=0,column=0)
        operatorcheck = 1
    elif (operation == "equals") :
        match operator :
            case "+":
                output = int(memory1) + int(memory2)
                label = Label(root,text = output, width = 5, height = 1)
                label.grid(row=0,column=0)
                memory2 = str(output)
            case "-":
                output = int(memory1) - int(memory2)
                label = Label(root,text = output, width = 5, height = 1)
                label.grid(row=0,column=0)
            case "x":
                output = int(memory1) * int(memory2)
                label = Label(root,text = output, width = 5, height = 1)
                label.grid(row=0,column=0)
            case "/":
                output = int(memory1) / int(memory2)
                label = Label(root, text = output, width = 5, height = 1)
                label.grid(row=0,column=0)
            case _: 
                label = Label(root,text = "uh oh", width = 5, height = 1)
                label.grid(row=0,column=0)
    else :
        label = Label(root,text = input, width = 5, height = 1)
        label.grid(row=0,column=0)
    
# used to create buttons
def createbutton(root, text, command, height, background, x, y) :
    button = Button(root, text = text, command = command, height = height, activebackground=background, padx = x, pady = y)
    return button

# GUI setup
root.title("Calculator")
root.geometry("500x500")
button1 = createbutton(root,"1",one,1,"light grey",10,5)
button2 = createbutton(root,"2",two,1,"light grey",10,5)
button3 = createbutton(root,"3",three,1,"light grey",10,5)
button4 = createbutton(root,"4",four,1,"light grey",10,5)
button5 = createbutton(root,"5",five,1,"light grey",10,5)
button6 = createbutton(root,"6",six,1,"light grey",10,5)
button7 = createbutton(root,"7",seven,1,"light grey",10,5)
button8 = createbutton(root,"8",eight,1,"light grey",10,5)
button9 = createbutton(root,"9",nine,1,"light grey",10,5)
button0 = createbutton(root,"0",zero,1,"light grey",10,5)
buttondot = createbutton(root,".",dot,1,"light grey",10,5)
buttonequals = createbutton(root,"=",equal,1,"light grey",10,5)
buttonplus = createbutton(root,"+",plus,1,"light grey",10,5)
buttonminus = createbutton(root,"-",minus,1,"light grey",10,5)
buttonmuiltiply = createbutton(root,"x",muiltiply,1,"light grey",10,5)
buttonpercent = createbutton(root,"%",percent,1,"light grey",10,5)
buttonclear = createbutton(root,"C",clear,1,"light grey",10,5)
buttonclearE = createbutton(root,"CE",clearE,1,"light grey",10,5)
buttondivision = createbutton(root,"/",division,1,"light grey",10,5)

buttonpercent.grid(row=1,column=0)
buttonclear.grid(row=1,column=1)
buttonclearE.grid(row=1,column=2)
buttondivision.grid(row=1,column=3)
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
button3.grid(row=2,column=2)
buttonmuiltiply.grid(row=2,column=3)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
buttonminus.grid(row=3,column=3)
button7.grid(row=4,column=0)
button8.grid(row=4,column=1)
button9.grid(row=4,column=2)
buttonplus.grid(row=4,column=3)
button0.grid(row=5,column=1)
buttondot.grid(row=5,column=2)
buttonequals.grid(row=5,column=3)

# runs GUI
root.mainloop()