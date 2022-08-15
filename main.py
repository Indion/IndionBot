#Edu-Bot 


#Libraries
import sys 
from tkinter import *
import pyfiglet as pyg  
import random
import wikipedia
import time
from PyDictionary import PyDictionary
import matplotlib.pyplot as plt
import numpy as np

#Color Codes
#STRING ~ Green
#SYNC ~ black
#stdin ~ black
#BUILTIN ~ Purple
#console ~ Maroon
#COMMENT ~ Red
#stdout ~ Blue
#TODO ~ Black
#stderr ~ Red
#hit ~ White text, Black Bg
#DEFINITION ~ Blue
#KEYWORD ~ Orange
#ERROR ~ Black text , Red Bg
#sel ~ Black text, grey BG


#Functions
try :
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")


#Lists
greet = ["Hello ✋" , "Hi ✋" ,"Hola ✋" , "Namaste 🙏" , "Khamma Ghani 🙏"]
facts = ["An Adult giraffe's kick is so powerful that it can kill a lion" , "Squirrels can climb trees faster than they can run on the ground" ,
         "Human thigh bones are stronger than concrete !", "Your heart beats over 100,000 times a day" , "You are born with 300 bones , but by the time you become an adult you have 206",
         "Camels have three eyelids to protect themselves from blowing sand." , "An Average lead pencil can write upto 50,000 English words" , "Honey is the only food that does not spoil"]

#Head
res= pyg.figlet_format("Welcome to \n Indion Bot")     
print(res)
color.write("Your All new Personal Companion in Learning" , "ERROR")

#Main Code
color.write(random.choice(greet) , "KEYWORD")
color.write("This is Your Edu-Bot , Indion Bot\n" , "KEYWORD")
name = input("May I know your Name :")
if (name.lower() == "ojas"):
    color.write("Hey, Boss So How may I help You today ?","KEYWORD")
else:
    color.write("Hey,"+name+"  "+"So How may I help You today ?","KEYWORD")
color.write("I can\n"
        "1. Provide you some cool Wikipedia Summaries\n"
        "2. Get Visualized track of your grades in exam\n"
        "3. Tell You the meaning of English Words\n"
        "4. List out Some Random Facts\n"
        "5. A Quick Trivia\n"
        )
while True:
    a = int(input("Try Typing  1 , 2 , 3....."))
    if (a == 1):
        time.sleep(1)
        srh=input("Okay 🙂, please type what you want to know about ")
        print(wikipedia.summary(srh, sentences=3))
        color.write("======================================================================\n" , "STRING")
    elif (a == 2):
        color.write("Cool..so first tell me your grades : [Out of Hundred]\n" , "KEYWORD")
        maths1 = float(input("Enter you marks of previous maths test"))
        maths2 = float(input("Enter you marks of latest maths test"))

        science1 = float(input("Enter you marks of previous science test"))
        science2 = float(input("Enter you marks of latest science test"))

        sst1 = float(input("Enter you marks of previous Social Studies test"))
        sst2 = float(input("Enter you marks of latest Social Studies test"))
        X = ["Maths 1st" , "Maths 2nd" , "Science 1st" , "Science 2nd" , "Social Science 1st" , "Social Science 2nd"]
        Y = [maths1 , maths2 , science1 , science2 , sst1 , sst2]
        mycol = ["red" , "red" , "green" , "green" , "blue" , "blue"]
        plt.bar(X,Y, color = mycol)
        plt.legend(['Maths' , 'Science' , 'SST'])
        plt.title(name+"'s Marks Analysis")
        plt.show()

        color.write("======================================================================\n" , "STRING")
    elif (a == 3):
        dictionary=PyDictionary()
        print("Don't Worry I Will Help You 😊😊")
        time.sleep(1)
        word=input("Enter the word for which you are searching: ")
        e_mean=dictionary.meaning(word)
        print(e_mean)
        h_mean=dictionary.translate(word, "hi")
        print(word, "in hindi is > ",h_mean)
        color.write("======================================================================\n" , "STRING")
    elif (a == 4):
        color.write("Okay...here is one for you\n", "BUILTIN")
        time.sleep(1)
        print(random.choice(facts))
        color.write("======================================================================\n" , "STRING")
    elif (a == 5):
        print("Rules : 1.Answer as directed \n 2.Each Correct response will fetch 1 point , whereas a wrong one will cost deduction of 1 point ")
        print("So get ready...get ready for the first one\n")
        score = 0
        first = input("When did the Constitution of India got ready (year)?")
        if (first == "1949"):
            color.write("Well Done\n" , "STRING")
            score +=1
            print("Current score : ", score)
        else:
            color.write("Ohh...Its Wrong\n" , "COMMENT")
            score -=1
            print("Current score : ", score)
        time.sleep(2)    
        second = input("How many neutrons are there in a Hydrogen atom [H]?")
        if (second == "0"):
            color.write("Kudos\n" , "STRING")
            score +=1
            print("Current score : ", score)
        else:
            color.write("Dont Worry , keep playing\n" , "COMMENT")
            score -=1
            print("Current score : ", score)
        time.sleep(2)
        third = input("Name the capital of Italy?")
        r = third.lower()
        if (r == "rome"):
            color.write("You seem to be a Genius !\n" , "STRING")
            score +=1
            print("Current score : ", score)
        else:
            color.write("Check your Atlas regularly\n" , "COMMENT")
            score -=1
            print("Current score : ", score)
        time.sleep(2)
        fourth = input("How many roots are possible for a quadratic equation ? [Number]")
        if (fourth == "2"):
            color.write("Oh...Maths seems to be your favourite Subject\n" , "STRING")
            score +=1
            print("Current score : ", score)
        else:
            color.write("Keep the spirit high  , you will surely get the next one correct\n" , "COMMENT")
            score -=1
            print("Current score : ", score)
        time.sleep(2)
        fifth = input("What is the cross product of Force & Displacement called ?[Hint : Mind it , its Cross Product]")
        t = fifth.lower()
        if (t == "torque"):
            color.write("You nailed it ! Congrats\n" , "STRING")
            score +=1
            print("Current score : ", score)
        else:
            color.write("Don't loose hope , better luck next time !\n" , "COMMENT")
            score -=1
            print("Current score : ", score)
        time.sleep(2)
        color.write("======================================================================\n" , "STRING")
    else :
        color.write("Sorry That Service do not exist in my database !")
