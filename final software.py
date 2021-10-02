from tkinter.ttk import Progressbar
from tkinter import *
from PIL import ImageTk,Image
import random
import tkinter.font as font
import random
from tkinter import messagebox
from tkinter import filedialog
import os
import pygame as pg
import random
from itertools import product
from pygame.locals import *
from pygame.color import Color
import pyttsx3 as audio
from random  import randint
import math as m
import tkinter.font as tkFont




colors = ["Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink", "Magenta"]
timer = 60
score = 0
score1 = 0

displayed_word_color = ''



w=Tk()


width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


w.overrideredirect(1)


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

def mathgame():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num1=[5,10,15,20,25,30]
    num2=[5]
    score1 = 0

    def submt(var1):
        global score1
        if var1.get() == str(resultPLUS()):
            correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
            correct.place(relx=0.4, rely=0.2)
            score1 +=1
            game_score1.config(text = "Your Score : " + str(score1))



        elif var1.get() == str(resultSUB()):
            correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
            correct.place(relx=0.4, rely=0.2)
            score1 +=1
            game_score1.config(text = "Your Score : " + str(score1))


        elif var1.get() == str(resultMUL()):
            correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
            correct.place(relx=0.4, rely=0.2)
            score1 +=1
            game_score1.config(text = "Your Score : " + str(score1 ))

        elif var1.get() == str(resultDIV()):
            correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
            correct.place(relx=0.4, rely=0.2)
            score1 +=1
            game_score1.config(text = "Your Score : " + str(score1))

        elif var1.get() == str(resultfactorial()):
            correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
            correct.place(relx=0.4, rely=0.2)
            score1 +=1
            game_score1.config(text = "Your Score : " + str(score1))

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

    def factorial():
        try_again.num1update = random.choice(num)
        try_again.num2update = random.choice(num)

        new1 = Label(app, text=f"({try_again.num1update} + {try_again.num2update}) ! ", font=("Courier", 16),bg = 'dark orange2')
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

    def resultfactorial():
        factorial
        return m.factorial(try_again.num1update+try_again.num2update)


    app = Toplevel()
    app.title("Math4Kids")

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
    add.place(relx=0.55, rely=0.9)

    sub = Button(app, text=" Subraction ", command=sub, bg = 'coral2', fg = 'palegreen2')
    sub.place(relx=0.67, rely=0.9)

    mul = Button(app, text=" Multiplition ", command=mul, bg = 'mediumpurple2', fg = 'palegreen2')
    mul.place(relx=0.39, rely=0.9)

    div = Button(app, text=" Division ", command=div, bg ='darkorange2', fg = 'palegreen2')
    div.place(relx=0.26, rely=0.9)

    factorial = Button(app, text=" Factorial ", command=factorial, bg ='tan2', fg = 'palegreen2')
    factorial.place(relx=0.13, rely=0.9)

    game_score1 = Label(app, text = "Your Score : " + str(score1), font = 'ComicSansMS ', fg = "deep pink", bg = 'palegreen2')
    game_score1.place(relx=0.8, rely=0.02)

    pi = Label(app,text = '𝛑',font =('arial',100), bg ='palegreen2')
    pi.place(relx=0.1, rely=0.2)

    com.destroy()

    app.mainloop()

def colorrush():



    #This fuction will be called when start button is clicked
    def startGame():
        global displayed_word_color
        if(timer == 60):
            startCountDown()
            displayed_word_color = random.choice(colors).lower()
            display_words.config(text=random.choice(colors), fg=displayed_word_color)
            color_entry.bind('<Return>', displayNextWord)


    #This function is to reset the game
    def resetGame():
        global timer, score, displayed_word_color
        timer = 60
        score = 0
        displayed_word_color = ''
        game_score.config(text = "Your Score : " + str(score))
        display_words.config(text = '')
        time_left.config(text="Game Ends in : -")
        color_entry.delete(0, END)


    #This function will start count down
    def startCountDown():
        global timer

        if(timer >= 0):
            time_left.config(text = "Game Ends in : " + str(timer) + "s")
            timer -= 1
            time_left.after(1000,startCountDown)
            if (timer == -1):
                time_left.config(text="Game Over!!!")


    #This function to display random words
    def displayNextWord(event):
        global displayed_word_color
        global score
        if(timer > 0):
            if(displayed_word_color == color_entry.get().lower()):
                score += 1
                game_score.config(text = "Your Score : " + str(score))
            color_entry.delete(0, END)
            displayed_word_color = random.choice(colors).lower()
            display_words.config(text = random.choice(colors), fg = displayed_word_color)


    my_window = Toplevel()
    my_window.title("Color Game")
    my_window.geometry("500x200")

    app_font = font.Font(family='Helvetica', size = 12)
    game_desp = "Game Description: Enter the color of the words displayed below. \n And Keep in mind not to enter the word text itself"
    myFont = font.Font(family='Helvetica')

    game_description = Label(my_window, text = game_desp, font = app_font, fg= "grey")
    game_description.pack()

    game_score = Label(my_window, text = "Your Score : " + str(score), font = (font.Font(size=16)), fg = "green")
    game_score.pack()

    display_words = Label(my_window , font = ('arial',30), pady = 10)
    display_words.pack()


    time_left = Label(my_window, text = "Game Ends in : -", font = (font.Font(size=14)), fg = "orange")
    time_left.pack()


    color_entry = Entry(my_window, width = 30)
    color_entry.pack(pady = 10)

    btn_frame = Frame(my_window, width= 80, height = 40, bg= 'red')
    btn_frame.pack(side = BOTTOM)

    start_button = Button(btn_frame, text = "Start", width = 20, fg = "black", bg = "pink", bd = 0,padx = 20, pady = 10 , command = startGame)
    start_button.grid(row=0, column= 0)

    reset_button = Button(btn_frame, text = "Reset", width = 20, fg = "black", bg = "light blue", bd = 0,padx = 20, pady = 10 , command = resetGame)
    reset_button.grid(row=0, column= 1)

    my_window.geometry('600x300')
    my_window.mainloop()

def tictactoe():


    root = Toplevel()
    root.title(' Tic-Tac-Toe')

    #root.geometry("1200x710")

    # X starts so true
    clicked = True
    count = 0




    # disable all the buttons
    def disable_all_buttons():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

    # Check to see if someone won
    def checkifwon():
        global winner
        winner = False

        if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            disable_all_buttons()

        #### CHECK FOR O's Win
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            disable_all_buttons()

        # Check if tie
        if count == 9 and winner == False:
            messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
            disable_all_buttons()

    # Button clicked function
    def b_click(b):
        global clicked, count

        if b["text"] == " " and clicked == True:
            b["text"] = "X"
            clicked = False
            count += 1
            checkifwon()
        elif b["text"] == " " and clicked == False:
            b["text"] = "O"
            clicked = True
            count += 1
            checkifwon()
        else:
            messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )

    # Start the game over!
    def reset():
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global clicked, count
        clicked = True
        count = 0

        # Build our buttons
        b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
        b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
        b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

        b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
        b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
        b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

        b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
        b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
        b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

        # Grid our buttons to the screen
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

    # Create menue
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Create Options Menu
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Rest Game", command=reset)

    reset()

    root.mainloop()

def dots():



    TOL = 8
    CELLSIZE = 40
    OFFSET = 10
    CIRCLERAD = 2
    DOTOFFSET = OFFSET + CIRCLERAD
    GAME_H = 400
    GAME_W = 400


    class Player(object):

        def __init__(self, name, color="black"):
            self.score = 0
            self.str = StringVar()
            self.name = name
            self.color = color

        def update(self):
            self.str.set(self.name + ": %d" % self.score)



    class MyFrame(Frame):

        def __init__(self, master):
            Frame.__init__(self, master)
            self.GO_font = tkFont.Font(self, \
                                    name="GOFont", \
                                    family = "Times", \
                                    weight="bold", \
                                    size=36)
            self.canvas = Canvas(self, height = GAME_H, width = GAME_W)
            self.canvas.bind("<Button-1>", lambda e:self.click(e))
            self.canvas.grid(row=0,column=0)

            self.dots = [[self.canvas.create_oval(CELLSIZE*i+OFFSET, \
                                                CELLSIZE*j+OFFSET, \
                                                CELLSIZE*i+OFFSET+2*CIRCLERAD, \
                                                CELLSIZE*j+OFFSET+2*CIRCLERAD, \
                                                fill="black") \
                        for j in range(10)] for i in range(10)]
            self.lines = []

            self.infoframe = Frame(self)
            self.players = [Player("Player 1","blue"), Player("Player 2","red")]
            self.infoframe.players = [Label(self.infoframe, textvariable = i.str) for i in self.players]
            for i in self.infoframe.players:
                i.grid()

            self.turn = self.players[0]
            self.update_players()
            self.infoframe.grid(row = 0, column = 1, sticky = N)

            self.grid()

        def update_players(self):
            for i in self.players:
                i.update()

        def click(self, event):
            x,y = event.x, event.y
            orient = self.isclose(x,y)

            if orient:
                if self.line_exists(x,y, orient):
                    return
                l = self.create_line(x,y, orient)
                score = self.new_box_made(l)
                if score:
                    self.turn.score += score
                    self.turn.update()
                    self.check_game_over()
                else:
                    index = self.players.index(self.turn)
                    self.turn = self.players[1-index]
                self.lines.append(l)

        def create_line(self, x, y, orient):
            startx = CELLSIZE * ((x-OFFSET)//CELLSIZE) + DOTOFFSET
            starty = CELLSIZE * ((y-OFFSET)//CELLSIZE) + DOTOFFSET
            tmpx = (x-OFFSET)//CELLSIZE
            tmpy = (y-OFFSET)//CELLSIZE

            if orient == HORIZONTAL:
                endx = startx + CELLSIZE
                endy = starty
            else:
                endx = startx
                endy = starty + CELLSIZE
            #print "line drawn: %d,%d to %d,%d" % (startx,starty,endx,endy)
            return self.canvas.create_line(startx,starty,endx,endy)


        def new_box_made(self, line):
            score = 0
            x0,y0,x1,y1 = self.canvas.coords(line)
            if x0 == x1: # vertical line
                midx = x0
                midy = (y0+y1)/2
                pre = (x0 - CELLSIZE/2, midy)
                post = (x0 + CELLSIZE/2, midy)
            elif y0 == y1: # horizontal line
                midx = (x0 + x1)/2
                midy = y0
                pre = (midx, y0 - CELLSIZE/2)
                post = (midx, y0 + CELLSIZE/2)

            if len(self.find_lines(pre)) == 3:  # not 4, because newly created line is
                self.fill_in(pre)               # is not returned (?!)
                score += 1
            if len(self.find_lines(post)) == 3:
                self.fill_in(post)
                score += 1
            return score

        def find_lines(self, coords):
            x, y = coords
            if x < 0 or x > GAME_W:
                return []
            if y < 0 or y > GAME_W:
                return []
            #print "Cell center: %d,%d" % (x,y)
            lines = [x for x in self.canvas.find_enclosed(x-CELLSIZE,\
                                                        y-CELLSIZE,\
                                                        x+CELLSIZE,\
                                                        y+CELLSIZE)\
                    if x in self.lines]
            #print lines
            return lines

        def fill_in(self, coords):
            x,y = coords
            self.canvas.create_text(x,y,text=self.turn.name, fill=self.turn.color)

        def isclose(self, x, y):
            x -= OFFSET
            y -= OFFSET
            dx = x - (x//CELLSIZE)*CELLSIZE
            dy = y - (y//CELLSIZE)*CELLSIZE

            if abs(dx) < TOL:
                if abs(dy) < TOL:
                    return None  # mouse in corner of box; ignore
                else:
                    return VERTICAL
            elif abs(dy) < TOL:
                return HORIZONTAL
            else:
                return None

        def line_exists(self, x,y, orient):
            id_ = self.canvas.find_closest(x,y,halo=TOL)[0]
            if id_ in self.lines:
                return True
            else:
                return False

        def check_game_over(self):
            total = sum([x.score for x in self.players])
            if total == 81:
                self.canvas.create_text(GAME_W/2, GAME_H/2, \
                                        text="GAME OVER", font="GOFont", \
                                        fill="#888")


    mainw = Toplevel()
    mainw.f = MyFrame(mainw)
    mainw.mainloop()

def flashback():

    # initializing values
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400
    SQUARE_SIZE = 50
    SQUARE_GAP = 10
    BOARD_WIDTH = 8
    BOARD_HEIGHT = 4
    X_MARGIN = (SCREEN_WIDTH - (BOARD_WIDTH * (SQUARE_SIZE + SQUARE_GAP))) // 2
    Y_MARGIN = (SCREEN_HEIGHT - (BOARD_HEIGHT * (SQUARE_SIZE + SQUARE_GAP))) // 2

    # the board size must be even due to pairs
    assert (BOARD_HEIGHT * BOARD_WIDTH) % 2 == 0, 'The board size must be even'

    # the shapes
    DIAMOND = 'diamond'
    SQUARE = 'square'
    TRIANGLE = 'triangle'
    CIRCLE = 'circle'

    BGCOLOR = Color('black')


    # reseting the shape
    def game_won(revealed):
        return all(all(x) for x in revealed)

    # function at the sart of the game
    def start_game_animation(board):
        """Starts game by randomly showing 5 squares"""

        coordinates = list(product(range(BOARD_HEIGHT), range(BOARD_WIDTH)))
        random.shuffle(coordinates)

        revealed = [[False] * BOARD_WIDTH for i in range(BOARD_HEIGHT)]

        screen.fill(BGCOLOR)
        draw_board(board, revealed)
        pg.display.update()
        pg.time.wait(500)

        for sz in range(0, BOARD_HEIGHT * BOARD_WIDTH, 5):
            l = coordinates[sz: sz + 5]
            for x in l:
                revealed[x[0]][x[1]] = True
                draw_square(board, revealed, *x)
            pg.time.wait(500)
            for x in l:
                revealed[x[0]][x[1]] = False
                draw_square(board, revealed, *x)

    # function been followed after game won
    def game_won_animation(board, revealed):
        """ Flashes background colors when the game is won"""

        color1 = Color('white')
        color2 = BGCOLOR
        for i in range(10):
            color1, color2 = color2, color1
            screen.fill(color1)
            draw_board(board, revealed)
            pg.display.update()
            pg.time.wait(300)

    # setting up board
    def get_random_board(shape, colors):
        """ Generates the board by random shuffling"""

        icons = list(product(shape, colors))
        num_icons = BOARD_HEIGHT * BOARD_WIDTH // 2
        icons = icons[:num_icons] * 2

        random.shuffle(icons)
        board = [icons[i:i + BOARD_WIDTH]
                for i in range(0, BOARD_HEIGHT * BOARD_WIDTH, BOARD_WIDTH)]
        return board


    def get_coord(x, y):
        """ Gets the coordinates of particular square.
            The squares are number height wise and then width wise.
            So the x and y are interchanged."""

        top = X_MARGIN + y * (SQUARE_SIZE + SQUARE_GAP)
        left = Y_MARGIN + x * (SQUARE_SIZE + SQUARE_GAP)
        return top, left


    def draw_icon(icon, x, y):
        """Draws the icon of (x, y) square"""

        px, py = get_coord(x, y)
        if icon[0] == DIAMOND:
            pg.draw.polygon(screen, icon[1],
                                ((px + SQUARE_SIZE // 2, py + 5), (px + SQUARE_SIZE - 5, py + SQUARE_SIZE // 2),
                                (px + SQUARE_SIZE // 2, py + SQUARE_SIZE - 5), (px + 5, py + SQUARE_SIZE // 2)))
        elif icon[0] == SQUARE:
            pg.draw.rect(screen, icon[1],
                            (px + 5, py + 5, SQUARE_SIZE - 10, SQUARE_SIZE - 10))
        elif icon[0] == TRIANGLE:
            pg.draw.polygon(screen, icon[1],
                                ((px + SQUARE_SIZE // 2, py + 5), (px + 5, py + SQUARE_SIZE - 5),
                                (px + SQUARE_SIZE - 5, py + SQUARE_SIZE - 5)))
        elif icon[0] == CIRCLE:
            pg.draw.circle(screen, icon[1],
                            (px + SQUARE_SIZE // 2, py + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)


    def get_pos(cx, cy):
        """Gets the square (x, y) position  from the cartesian coordinates.
        The squares are number height wise and then width wise.
        So the cx and cy are interchanged."""

        if cx < X_MARGIN or cy < Y_MARGIN:
            return None, None

        x = (cy - Y_MARGIN) // (SQUARE_SIZE + SQUARE_GAP)
        y = (cx - X_MARGIN) // (SQUARE_SIZE + SQUARE_GAP)

        if x >= BOARD_HEIGHT or y >= BOARD_WIDTH or(cx - X_MARGIN) % (SQUARE_SIZE + SQUARE_GAP) > SQUARE_SIZE or (cy - Y_MARGIN) % (SQUARE_SIZE + SQUARE_GAP) > SQUARE_SIZE:
            return None, None
        else:
            return x, y

    def draw_square(board, revealed, x, y):
        """Draws a particular square"""

        coords = get_coord(x, y)
        square_rect = (*coords, SQUARE_SIZE, SQUARE_SIZE)
        pg.draw.rect(screen, BGCOLOR, square_rect)
        if revealed[x][y]:
            draw_icon(board[x][y], x, y)
        else:
            pg.draw.rect(screen, Color('grey'), square_rect)
        pg.display.update(square_rect)

    def draw_board(board, revealed):
        """Draws the entire board"""

        for x in range(BOARD_HEIGHT):
            for y in range(BOARD_WIDTH):
                draw_square(board, revealed, x, y)

    def draw_select_box(x, y):
        """Draws the highlight box around the square"""

        px, py = get_coord(x, y)
        pg.draw.rect(screen, Color('red'), (px - 5, py - 5, SQUARE_SIZE + 10, SQUARE_SIZE + 10), 5)


    # the main function
    def main():
        global screen, clock

        pg.init()

        screen = pg.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
        pg.display.set_caption('Memory Game')

        clock = pg.time.Clock()

        shape = (DIAMOND, SQUARE, TRIANGLE, CIRCLE)
        colors = (Color('red'), Color('yellow'), Color('green'), Color('blue'))

        # There should be enough symbols
        assert len(shape) * len(colors) >= BOARD_HEIGHT * BOARD_WIDTH // 2,'There are not sufficient icons'

        board = get_random_board(shape, colors)
        revealed = [[False] * BOARD_WIDTH for i in range(BOARD_HEIGHT)]  # keeps track of visibility of square

        mouse_x = None
        mouse_y = None
        mouse_clicked = False
        first_selection = None

        running = True
        start_game_animation(board)

        while running:
            screen.fill(BGCOLOR)
            draw_board(board, revealed)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == MOUSEMOTION:
                    mouse_x, mouse_y = pg.mouse.get_pos()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    mouse_clicked = True

            x, y = get_pos(mouse_x, mouse_y)

            if x is not None and y is not None:
                if not revealed[x][y]:
                    if mouse_clicked:
                        revealed[x][y] = True
                        draw_square(board, revealed, x, y)

                        if first_selection is None:
                            first_selection = (x, y)
                        else:
                            pg.time.wait(1000)
                            if board[x][y] != board[first_selection[0]][first_selection[1]]:
                                revealed[x][y] = False
                                revealed[first_selection[0]][first_selection[1]] = False
                            first_selection = None

                        if game_won(revealed):

                            game_won_animation(board, revealed)

                            board = get_random_board(shape, colors)
                            revealed = [[False] * BOARD_WIDTH for i in range(BOARD_HEIGHT)]
                            start_game_animation(board)

                    else:
                        draw_select_box(x, y)

            mouse_clicked = False
            pg.display.update()

        else:
            pg.quit()
            quit()


    if __name__ == '__main__':
        main()

def sps():
    def simple():
        root = Toplevel()
        root.title('Stone Paper Scissor')
        root.configure(background='#008080')
        # #9b59b6

        # pictures
        stone_img = ImageTk.PhotoImage(Image.open("rock107_1.jpeg"))
        paper_img = ImageTk.PhotoImage(Image.open("paper107_1.jpeg"))
        scissor_img = ImageTk.PhotoImage(Image.open("scissor107_1.jpeg"))
        stone_img_comp = ImageTk.PhotoImage(Image.open("rock107_1.jpeg"))
        paper_img_comp = ImageTk.PhotoImage(Image.open("paper107_1.jpeg"))
        scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor107_1.jpeg"))

        # insert picture
        user_label = Label(root, image=paper_img)
        comp_label = Label(root, image=paper_img_comp)
        comp_label.grid(row=1, column=0)
        user_label.grid(row=1, column=4)

        # scores
        playerScore = Label(root, text=0, font=100, bg="#307D7E", fg='white')
        computerScore = Label(root, text=0, font=100, bg="#307D7E", fg='white')
        computerScore.grid(row=1, column=1)
        playerScore.grid(row=1, column=3)

        # indicators
        user_indicator = Label(root, font=75, text="USER",
                               bg="#307D7E", fg='white')
        comp_indicator = Label(root, font=75, text="COMPUTER",
                               bg="#307D7E", fg='white')
        user_indicator.grid(row=0, column=3)
        comp_indicator.grid(row=0, column=1)

        # messages
        msg = Label(root, font=50, bg="#307D7E", fg='white')
        msg.grid(row=3, column=2)

        # update message
        def updateMessage(x):
            msg['text'] = x

        # update user score
        def updateUserScore():
            score = int(playerScore["text"])
            score += 1
            playerScore['text'] = str(score)

        # update comp score
        def updateCompScore():
            score = int(computerScore["text"])
            score += 1
            computerScore['text'] = str(score)

        # check winner
        def checkwin(player, computer):
            if player == computer:
                updateMessage("Its a tie!!")
            elif player == 'stone':
                if computer == 'paper':
                    updateMessage("You Lose!")
                    updateCompScore()
                else:
                    updateMessage("You Win!!")
                    updateUserScore()
            elif player == 'paper':
                if computer == 'scissors':
                    updateMessage("You Lose!!")
                    updateCompScore()
                else:
                    updateMessage("You win!")
                    updateUserScore()
            elif player == "scissors":
                if computer == 'stone':
                    updateMessage("You lose!")
                    updateCompScore()
                else:
                    updateMessage("You win!")
                    updateUserScore()
            else:
                pass

        # update choices

        choices = ["stone", "paper", "scissors"]

        def updateChoice(x):  # scissor or paper
            # for computer
            compChoice = choices[randint(0, 2)]
            if compChoice == 'stone':
                comp_label.configure(image=stone_img_comp)
            elif compChoice == 'paper':
                comp_label.configure(image=paper_img_comp)
            else:
                comp_label.configure(image=scissor_img_comp)

            # for user
            if x == 'stone':
                user_label.configure(image=stone_img)
            elif x == 'paper':
                user_label.configure(image=paper_img)
            else:
                user_label.configure(image=scissor_img)

            checkwin(x, compChoice)

        # buttons
        rock = Button(root, width=20, height=2, text="ROCK",
                      bg='#FF3E4D', fg='white', command=lambda: updateChoice("stone")).grid(row=2, column=1)
        paper = Button(root, width=20, height=2, text="PAPER",
                       bg='#FF3E4D', fg='white', command=lambda: updateChoice("paper")).grid(row=2, column=2)
        scissor = Button(root, width=20, height=2, text="SCISSOR",
                         bg='#FF3E4D', fg='white', command=lambda: updateChoice("scissors")).grid(row=2, column=3)

        root.mainloop()


    def advance():
        root =Toplevel()
        root.title('Stone Paper Scissor')
        root.configure(background ='#5CDB95')
        # #9b59b6


        #pictures
        stone_img = ImageTk.PhotoImage(Image.open("rock_333.png"))
        paper_img = ImageTk.PhotoImage(Image.open("paper_333.png"))
        scissor_img = ImageTk.PhotoImage(Image.open("scissors_333.png"))
        lizard_img = ImageTk.PhotoImage(Image.open("lizard_333.png"))
        spock_img = ImageTk.PhotoImage(Image.open("spock_333.png"))
        stone_img_comp = ImageTk.PhotoImage(Image.open("rock_333.png"))
        paper_img_comp = ImageTk.PhotoImage(Image.open("paper_333.png"))
        scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors_333.png"))
        lizard_img_comp = ImageTk.PhotoImage(Image.open("lizard_333.png"))
        spock_img_comp = ImageTk.PhotoImage(Image.open("spock_333.png"))
        #insert picture
        user_label = Label(root,image=paper_img)
        comp_label = Label(root,image=paper_img_comp)
        comp_label.grid(row=1,column=0)
        user_label.grid(row=1,column=5)

        #scores
        playerScore = Label(root,text=0,font='Serif 52 bold',bg="#5CDB95",fg='#05386B')
        computerScore = Label(root,text=0,font='Serif 52 bold',bg="#5CDB95",fg='#05386B')
        computerScore.grid(row=1,column=1)
        playerScore.grid(row=1,column=3)

        #empty
        empty1 = Label(root,text='                                                ',bg="#5CDB95")
        empty1.grid(row=0,column=2)
        #indicators
        user_indicator = Label(root,font='Impact 32 bold',text="USER",
                               bg="#05386B",fg='#379683')
        comp_indicator = Label(root,font='Impact 32 bold',text="COMPUTER",
                               bg="#05386B",fg='#379683')
        user_indicator.grid(row=0,column=3)
        comp_indicator.grid(row=0,column=1)

        #messages
        msg=Label(root,font=50,bg="#5CDB95",fg='#05386B')
        msg.grid(row=3,column=2)
        #rules
        #rules=ImageTk.PhotoImage(Image.open("rpsls_rules.png"))
        #rules_label = Label(root,image=rules).place(x=525,y=350)
        #update message
        def updateMessage(x):
            msg['text'] = x
        #update user score
        def updateUserScore():
            score = int(playerScore["text"])
            score += 1
            playerScore['text'] = str(score)
        #update comp score
        def updateCompScore():
            score = int(computerScore["text"])
            score += 1
            computerScore['text'] = str(score)

        #check winner
        def checkwin(player,computer):
            if player == computer:
                updateMessage("Its a tie!!")
            elif player == 'stone':
                if computer == 'paper':
                    updateMessage("You Lose!")
                    updateCompScore()
                elif computer == 'lizard':
                    updateMessage("You Win!")
                    updateUserScore()
                elif computer == 'spock':
                    updateMessage("You lose!!")
                    updateCompScore()
                else:
                    updateMessage("You Win!!")
                    updateUserScore()
            elif player == 'paper':
                if computer == 'scissors':
                    updateMessage("You Lose!!")
                    updateCompScore()
                elif computer == 'spock':
                    updateMessage("You Win!!")
                    updateUserScore()
                elif computer == 'lizard':
                    updateMessage("You lose!!")
                    updateCompScore()
                else:
                    updateMessage("You win!")
                    updateUserScore()
            elif player == "scissors":
                if computer == 'stone':
                    updateMessage("You lose!")
                    updateCompScore()
                elif computer == 'lizard':
                    updateMessage("You Win!!")
                    updateUserScore()
                elif computer == 'spock':
                    updateMessage("You Lose!!")
                    updateCompScore()
                else:
                    updateMessage("You win!")
                    updateUserScore()
            elif player == "lizard":
                if computer == 'stone':
                    updateMessage("You Lose!!")
                    updateCompScore()
                elif computer == 'paper':
                    updateMessage("You Win!!")
                    updateUserScore()
                elif computer == 'scissors':
                    updateMessage("You Lose!!")
                    updateCompScore()
                else:
                    updateMessage("You Win!!")
                    updateUserScore()
            elif player == "spock":
                if computer == 'stone':
                    updateMessage("You Win!!")
                    updateUserScore()
                elif computer == 'paper':
                    updateMessage("You Lose!!")
                    updateCompScore()
                elif computer == 'scissors':
                    updateMessage("You Win!!")
                    updateUserScore()
                else:
                    updateMessage("You Lose!!")
                    updateCompScore()
            else:
                pass



        #update choices

        choices = ["stone","paper","scissors","lizard","spock"]
        def updateChoice(x):#scissor or paper
        #for computer
            compChoice = choices[randint(0,4)]
            if compChoice == 'stone':
                comp_label.configure(image=stone_img_comp)
            elif compChoice == 'paper':
                comp_label.configure(image=paper_img_comp)
            elif compChoice == 'spock':
                comp_label.configure(image=spock_img_comp)
            elif compChoice == 'lizard':
                comp_label.configure(image=lizard_img_comp)
            else:
                comp_label.configure(image=scissor_img_comp)



        #for user
            if x == 'stone':
                user_label.configure(image=stone_img)
            elif x == 'paper':
                user_label.configure(image=paper_img)
            elif x == 'lizard':
                user_label.configure(image=lizard_img)
            elif x == 'spock':
                user_label.configure(image=spock_img)
            else:
                user_label.configure(image=scissor_img)

            checkwin(x,compChoice)



        #buttons
        rock=Button(root,width=20,height=2,text="ROCK",
                    bg='#05386B',fg='#EDF5E1',command=lambda:updateChoice("stone")).place(x=525,y=150)
        paper=Button(root,width=20,height=2,text="PAPER",
                     bg='#05386B',fg='#EDF5E1',command=lambda:updateChoice("paper")).place(x=525,y=200)
        scissor=Button(root,width=20,height=2,text="SCISSOR",
                       bg='#05386B',fg='#EDF5E1',command=lambda:updateChoice("scissors")).place(x=525,y=250)
        lizard=Button(root,width=20,height=2,text="LIZARD",
                       bg='#05386B',fg='#EDF5E1',command=lambda:updateChoice("lizard")).place(x=525,y=300)
        spock=Button(root,width=20,height=2,text="SPOCK",
                       bg='#05386B',fg='#EDF5E1',command=lambda:updateChoice("spock")).place(x=525,y=350)


        root.mainloop()


    sps = Toplevel()
    sps.title("stone paper scissors")
    sps.geometry("600x440")
    sps.configure(background = 'chocolate1')


    start_button = Button(sps, text = "SIMPLE MODE", width = 20, fg = "black", bg = "pink", bd = 0,padx = 20, pady = 10 , command = simple)
    start_button.place(relx = 0.10 ,rely = 0.2 )

    start_button = Button(sps, text = 'ADVANCE MODE', width = 20, fg = "black", bg = "cyan", bd = 0,padx = 20, pady = 10, command = advance )
    start_button.place(relx = 0.10 ,rely = 0.4 )

    game_description = Label(sps, text = ' STONE PAPER SCISSORS  ' , font = ('MV Boli',25), fg= "blue2",bg = 'chocolate1')
    game_description.pack()

    rules= Label(sps,text="RULES",font = ('Agency FB',25), fg= "light cyan",bg = 'chocolate1')
    rules.pack()
    rules.place(relx=0.63,rely=0.12)

    rules=ImageTk.PhotoImage(Image.open("rpsls_rules.png"))
    rules_label = Label(sps,image=rules).place(relx=0.45, rely=0.25)


    sps.mainloop()



def new_win():

    com = Tk()
    com.geometry('600x300')
    com.title('Select game')
    com.configure(background = 'slateblue1')
    messagebox.showinfo("Devloper Message",'Remember : Some games may not work properly if your facing such problems inform !!')


    start_button = Button(com, text = "CIPHERING", width = 20, fg = "black", bg = "pink", bd = 0,padx = 20, pady = 10 , command = mathgame)
    start_button.place(relx = 0.10 ,rely = 0.2 )

    start_button = Button(com, text = 'COLOR RUSH', width = 20, fg = "black", bg = "cyan", bd = 0,padx = 20, pady = 10, command = colorrush )
    start_button.place(relx = 0.10 ,rely = 0.4 )

    start_button = Button(com, text = "TIC TAC TOE", width = 20, fg = "black", bg = "seagreen1", bd = 0,padx = 20, pady = 10 , command = tictactoe)
    start_button.place(relx = 0.10 ,rely = 0.6 )

    start_button = Button(com, text = "DOTS", width = 20, fg = "black", bg = "cadetblue1", bd = 0,padx = 20, pady = 10 , command = dots)
    start_button.place(relx = 0.10 ,rely = 0.8 )

    start_button = Button(com, text = "FLASH - BACK ", width = 20, fg = "black", bg = "cadetblue1", bd = 0,padx = 20, pady = 10 , command = flashback)
    start_button.place(relx = 0.45 ,rely = 0.2 )

    start_button = Button(com, text="STONE PAPER SCISSORS ", width=20, fg="black", bg="cadetblue1", bd=0, padx=20, pady=10,command=sps)
    start_button.place(relx=0.45, rely=0.4)


    game_description = Label(com, text = ' CONQUER QUEST ' , font = ('Agency FB',20), fg= "seagreen1",bg = 'slateblue1')
    game_description.pack()
    game_description.place(relx = 0.73, rely = 0.8)

    game_description = Label(com, text = ' WELCOME !!  ' , font = ('Agency FB',25), fg= "tan1",bg = 'slateblue1')
    game_description.pack()



    com.mainloop()





def bar():


    l4=Label(w,text='Hold Tight....',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)

    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1

    w.destroy()
    new_win()


progress.place(x=-10,y=235)








'''

def rgb(r):
    return "#%02x%02x%02x" % r
#Frame(w,width=432,height=241,bg=rgb((100,100,100))).
'''
a='#249794'
Frame(w,width=427,height=241,bg=a).place(x=0,y=0)  #249794
b1=Button(w,width=10,height=1,text='LETS GO>> ',command=bar,border=0,fg=a,bg='white')
b1.place(x=170,y=200)


######## Label

l1=Label(w,text='GAMES',fg='white',bg=a)
lst1=('Agency FB',18,'bold')
l1.config(font=lst1)
l1.place(x=50,y=80)

l2=Label(w,text='',fg='white',bg=a)
lst2=('Agency FB',18)
l2.config(font=lst2)
l2.place(x=115,y=82)

l3=Label(w,text='BETA - EARLY ACCESS',fg='white',bg=a)
lst3=('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=50,y=110)






w.mainloop()
