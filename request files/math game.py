import random
from tkinter import *
from PIL import ImageTk,Image 

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num1=[5,10,15,20,25,30]
num2=[5]
score = 0 
def submt(var1):
    global score
    if var1.get() == str(resultPLUS()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.4, rely=0.2)
        score+=1
        game_score.config(text = "Your Score : " + str(score))
        
        

    elif var1.get() == str(resultSUB()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.4, rely=0.2)
        score+=1
        game_score.config(text = "Your Score : " + str(score))


    elif var1.get() == str(resultMUL()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.4, rely=0.2)
        score+=1
        game_score.config(text = "Your Score : " + str(score))

    elif var1.get() == str(resultDIV()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.4, rely=0.2)
        score+=1
        game_score.config(text = "Your Score : " + str(score))
        
    else:
        wrong = Label(app, text="Wrong!!!", fg="red", font=("Courier", 16))
        wrong.place(relx=0.4, rely=0.2)
    
    solving.delete(0,END)

def try_again():
    try_again.num1update = random.choice(num)
    try_again.num2update = random.choice(num)

    newQ = Label(app, text=f"{try_again.num1update}+{try_again.num2update}", font=("Courier", 16), bg = 'slateblue1')
    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23 )

def sub():
    try_again.num1update = random.choice(num)
    try_again.num2update = random.choice(num)

    new1 = Label(app, text=f"{try_again.num1update} - {try_again.num2update}", font=("Courier", 16), bg = "coral2")
    new1.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

def mul():
    try_again.num1update = random.choice(num)
    try_again.num2update = random.choice(num)

    new1 = Label(app, text=f"{try_again.num1update} * {try_again.num2update}", font=("Courier", 16), bg = 'mediumpurple2')
    new1.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

def div():
    try_again.num1update = random.choice(num1)
    try_again.num2update = random.choice(num2)

    new1 = Label(app, text=f"{try_again.num1update} / {try_again.num2update}", font=("Courier", 16),bg = 'dark orange2')
    new1.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


def resultPLUS():
    try_again
    return try_again.num1update + try_again.num2update 

def resultSUB():
    sub
    return try_again.num1update - try_again.num2update 

def resultMUL():
    mul
    return try_again.num1update * try_again.num2update 

def resultDIV():
    div
    return try_again.num1update // try_again.num2update 


app = Tk()
app.title("Math4Kids")
app.iconbitmap("C:\\Users\\Intel\\Desktop\\Python pgms\\Other Games\\icon.ico")
game_description = Label(app, text = ' x + CIPHER - RING ÷ - ' , font = ('Bradley Hand ITC',25), fg= "red",bg = 'palegreen2')
game_description.pack()

# canvas = Canvas(app, width=240, height=300)
# canvas.pack()
app.geometry("600x300")
app.resizable(True, True)
start = Button(app, text="Start", command=try_again)
start.place(relx=0.5, rely=0.2)
app.config(background = 'Palegreen2')

solving = Entry(app,font = ("AppleGothic",10))
solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

submit = Button(app, text="Submit", command=lambda: submt(solving), bg = 'coral2',fg = "palegreen2")
submit.place(relx=0.48, rely=0.7,)

add = Button(app, text="Addition", command=try_again, bg = 'slateblue1', fg = 'palegreen2')
add.place(relx=0.53, rely=0.9)

sub = Button(app, text=" Subraction ", command=sub, bg = 'coral2', fg = 'palegreen2')
sub.place(relx=0.65, rely=0.9)

mul = Button(app, text=" Multiplition ", command=mul, bg = 'mediumpurple2', fg = 'palegreen2')
mul.place(relx=0.37, rely=0.9)

div = Button(app, text=" Division ", command=div, bg ='darkorange2', fg = 'palegreen2')
div.place(relx=0.24, rely=0.9)

game_score = Label(app, text = "Your Score : " + str(score), font = 'ComicSansMS ', fg = "deep pink", bg = 'palegreen2')
game_score.place(relx=0.8, rely=0.02)

pi = Label(app,text = '𝛑',font =('arial',100), bg ='palegreen2')
pi.place(relx=0.1, rely=0.2)

app.mainloop()