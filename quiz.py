# Simple python app for testing

import math
import sys

def qna(question):
#Function to process questions
    #ans = input('What is the capital of India: 1-Delhi, 2-Kolkata, 3-others >>')
    score = 0
    q = (
       ("What is the capital of India: 1-Delhi, 2-Kolkata, 3-others",1),
       ("What is the language spoken in Netherlands: 1-German, 2-France, 3-Dutch",3),
       ("What is the heighest mountain on Earth: 1-K2, 2-Everest, 3-Kanchenjunga", 2)
    )
    #print(q[1][0])
    lngt =len(q)
    print(lngt)
    print(question)
    if (lngt!=question):
        #ques = question-1
        ans = input(q[question][0]+'>>')
        if (str(ans)==str(q[question][1])):
            print("Correct answer")
            score=score+1
        else:
           print("Wrong answer")
    return (score, lngt)

def scoreboard(score, ques, msg):
#Function to process the scoreboard and format it is diplayed in
    if (msg==1):
        print("Final core:"+str(score)+"/"+str(ques))
    else:
        print("current score:"+str(score)+"/"+str(ques))


def main():
    quiz = input('Start quiz: Y or N >>')
    score = 0
    ques = 0
    lngt = -1
    #msg = 0 #Can be used to define whether the scoreboard message is current or final
    while (quiz=='Y' and ques!=lngt):
        tscore, lngt = qna(ques)
        ques = ques+1
        score = score+tscore
        """
        ans = input('What is the capital of India: 1-Delhi, 2-Kolkata, 3-others >>')
        if (str(ans)=='1'):
            print("Correct answer")
            score=score+1
        else:
            print("Wrong answer")
        """
        scoreboard(score, ques, 0)
        quiz = input('Do you wish to continue: Y-Yes N-No/Quit>>')
        if (quiz=='N'):
            print("Chosen to End quiz ! Thanks for participating")
            scoreboard(score, ques, 1)
        elif(ques==lngt):
            print("End of question bank reached")
            scoreboard(score, ques, 1)
    print("Bye")


if __name__=="__main__":
    main()
