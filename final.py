from tkinter import *
from PIL import Image,ImageTk
from random  import randint
import  os 

root =Tk()
root.title('Stone Paper Scissor')
root.configure(background ='#008080')
# #9b59b6


#pictures
stone_img = ImageTk.PhotoImage(Image.open("rock107_1.jpeg"))
paper_img = ImageTk.PhotoImage(Image.open("paper107_1.jpeg"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor107_1.jpeg"))
stone_img_comp = ImageTk.PhotoImage(Image.open("rock107_1.jpeg"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper107_1.jpeg"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor107_1.jpeg"))

#insert picture
user_label = Label(root,image=paper_img)
comp_label = Label(root,image=paper_img_comp)
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerScore = Label(root,text=0,font=100,bg="#307D7E",fg='white')
computerScore = Label(root,text=0,font=100,bg="#307D7E",fg='white')
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=75,text="USER",
                       bg="#307D7E",fg='white')
comp_indicator = Label(root,font=75,text="COMPUTER",
                       bg="#307D7E",fg='white')
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg=Label(root,font=50,bg="#307D7E",fg='white')
msg.grid(row=3,column=2)

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



#update choices

choices = ["stone","paper","scissors"]
def updateChoice(x):#scissor or paper
#for computer
    compChoice = choices[randint(0,2)]
    if compChoice == 'stone':
        comp_label.configure(image=stone_img_comp)
    elif compChoice == 'paper':
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)



#for user
    if x == 'stone':
        user_label.configure(image=stone_img)
    elif x == 'paper':
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkwin(x,compChoice)



#buttons
rock=Button(root,width=20,height=2,text="ROCK",
            bg='#FF3E4D',fg='white',command=lambda:updateChoice("stone")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",
             bg='#FF3E4D',fg='white',command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",
               bg='#FF3E4D',fg='white',command=lambda:updateChoice("scissors")).grid(row=2,column=3)


root.mainloop()

