from tkinter import *
from PIL import Image,ImageTk
from random  import randint
root =Tk()
root.geometery('40x1000')
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
empty1 = Label(root,text='                                                    ',bg="#5CDB95")
empty1.grid(row=0,column=2)
#indicators
user_indicator = Label(root,font='Impact 32 bold',text="USER",
                       bg="#05386B",fg='#379683')
comp_indicator = Label(root,font='Impact 32 bold',text="COMPUTER",
                       bg="#05386B",fg='#379683')
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg=Label(root,font='Impact 32 bold',bg="#5CDB95",fg='#05386B')
msg.place(x=525,y=59)
#.grid(row=2,column=2)
#rules

#.place(x=450,y=400)
empty2=Label(root,pady=150,bg="#5CDB95").grid(row=5,column=3)
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
