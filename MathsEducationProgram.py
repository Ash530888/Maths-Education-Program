from __future__ import division, print_function, absolute_import
import sqlite3
import PySimpleGUI as sg
import getpass
##from Crypto.Hash import SHA256
##import Quiz
import sys
import operator as op
import math
import random
from fractions import Fraction
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

##def getKey(password):
##    ##Defines function that hashes the password to get the key.
##    hasher=SHA256.new(password.encode('utf-8'))
##    return hasher.digest()
##    ##Hashing the password allows the password to be stored securely
##    ##Again, improving the integrity and confidentiality of the program

def DatabaseCheck():
     global username
     while True:
          username=input("Enter your username: ")
##          password=getpass.getpass()
          password=input("Password: ")
##        User prompted for login details

          with sqlite3.connect("MathsPersonalDetails.db") as db:
               cursor=db.cursor()
               find_user=("SELECT * FROM personalDetails WHERE username=? AND password=?")
##               cursor.execute(find_user,[(username),(getKey(password))])

          cursor.execute(find_user,[(username),(password)])
          results=cursor.fetchall()
##            Collects user with username and password inputted if it exists
          if results:
               print("Welcome "+results[0][3])
               if login=='1':
                    Teacher()
               elif login=='2':
                    Student()
##            If a user was found they're directed to the correct menu and welcomed to their account
          else:
               print("username and password not recognised")
               again=input("Do you want to try again? (y/n): ")
##                User asked if they would like to try logging in again or not
               if again.lower()=="n":
                    print("Goodbye")
                    sys.exit()
##                    If they dont want to try logging in again the program ends

def equalSign(e):
    index=0
    for i in e:
        if i!="=":
            index+=1
    return index


def Formulae():
    valid=True
    while valid==True:
        print("What formula would you like to work with?")
        Ftype=input("""
        1) v = u + at
        2) s = ut + 1/2at2
        3) v2 = u2 + 2as
        4) s = (u + v/2)t\n""")
##        Options displayed to user
##        Instructions displayed to user
        if Ftype=='1' or Ftype=='2' or Ftype=='3' or Ftype=='4':
            print("Leave the component you're looking for blank.\n")
            valid=False
        if Ftype=='1':
            v=input("v= ")
            u=input("u= ")
            a=input("a= ")
            t=input("t= ")
            if len(v)==0:
                print("v=",float(u)+float(a)*float(t))
            elif len(u)==0:
                print("u=",float(v)-float(a)*float(t))
            elif len(a)==0:
                print("a=",(float(v)-float(u)/float(t)))
            elif len(t)==0:
                print("t=",(float(v)-float(u))/float(a))
        elif Ftype=='2':
            s=input("s= ")
            u=input("u= ")
            t=input("t= ")
            a=input("a= ")
            if len(s)==0:
                print("s=",float(u)*float(t)+(1/2)*(float(a)*float(t)**2))
            elif len(u)==0:
                print("u=",(float(s)-(1/2)*(float(a)*float(t)**2))/float(t))
            elif len(t)==0 and float(u)==0:
                print("t=",(float(s)-(1/2)*(float(a)*float(t)**2))/float(u))
            elif len(t)==0 and float(u)!=0:
                t1=(-float(u)+math.sqrt(float(u)**2-(2*float(a)*float(s))))/float(a)
                t2=(-float(u)-math.sqrt(float(u)**2-(2*float(a)*float(s))))/float(a)
                if t1>0:
                    print("t=",t1)
                else:
                    print("t=",t2)
##                Checks which value of t is valid
            elif len(a)==0:
                print("a=",math.sqrt((2*(float(s)-(float(u)*float(t)))/float(a))))
        elif Ftype=='3':
            v=input("v= ")
            u=input("u= ")
            a=input("a= ")
            s=input("s= ")
            if len(v)==0:
                print("v=",math.sqrt(float(u)**2+(2*float(a)*float(s))))
            elif len(u)==0:
                print("u=",math.sqrt(float(v)**2-(2*float(a)*float(s))))
            elif len(a)==0:
                print("a=",(float(v)**2-float(u)**2)/(2*float(s)))
            elif len(s)==0:
                print("a=",(float(v)**2-float(u)**2)/(2*float(a)))
        elif Ftype=='4':
            s=input("s= ")
            v=input("v= ")
            u=input("u= ")
            t=input("t= ")


            if len(s)==0:
                print("s=",((float(u)+float(v))/2)*float(t))
            elif len(u)==0:
                print("u=",((2*float(s))/float(t))-float(v))
            elif len(v)==0:
                print("v=",((2*float(s))/float(t))-float(u))
            elif len(t)==0:
                print("t=",((2*float(s))/(float(u)+float(v))))
        else:
            print("Invalid Input")
        ##      If statement checks user input and carries out what they want
##The while loop ensures that the input is valid- this avoids crashes in the program.
    
    if login=='2':
        Student()
    elif login=='3':
        NoLogin()
    ##If statement returns the user to the correct menu depending on what type of login they have


def ncr(n, r):
    global choose
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    choose=numer / denom

def BiExpansion():
    expansion=[]
    part=''
    print("Binomial expansion in ascending order!")
    print("(a+bx)^n")
    a=int(input("Enter the value of 'a': "))
    b=int(input("Enter the value of 'b': "))
    n=int(input("Enter the value of 'n': "))
##    The user is prompted to enter the value of each comonent of equation
    terms=int(input("How many terms would you like to find?: "))


    for i in range(0,terms):
        ncr(n,i)
        if i==0:
            part=choose*(a**(n-i))*(b**i)
##            This will give the first term
        else:
            part=str(choose*(a**(n-i))*(b**i))+"x^"+str(i)
        expansion.append(part)

    terms=''
    for i in expansion:
          terms=terms+str(i)+"+"

    terms=terms[:-1]
    print("\n("+str(a)+"+"+str(b)+"x)^"+str(n)+"= "+terms)

    if login=='2':
        Student()
    elif login=='3':
        NoLogin()

def Fractions():
     fractions=[]
##     The variable 'fractions' is an array and will store the fractions in the calculation
     calc=1
##     The variable 'calc' is initially stored as 1 but it will store the answer to the calculation
     calcType=int(input("""
     1)Addition
     2)Multiplication
     3)Division
     4)Subtraction\n"""))
##     User selects whether they want to add or multiply etc.
     num=int(input("How many fractions are involved in this calc?"))
##     User asked how many fractions are involved in the calculation
     for i in range(num):
          fraction=input("Enter a fraction")
          fractions.append(fraction)
##          fractions appended to the array
     if calcType==1:
          calc=calc-1
          for i in fractions:
               calc=calc+Fraction(i)
##               fractions added
     elif calcType==2:
          for i in fractions:
               calc=calc*Fraction(i)
##               fractions multiplied
     elif calcType==3:
          for y in fractions:
              if y == fractions[0]:
                  calc=calc*Fraction(fractions[0])
##                         First of all the fraction to be divided needs to be saved in 'calc'
              else:
                  calc=calc/Fraction(y)
##                    fractions divided
     elif calcType==4:
          for y in fractions:
              if y==fractions[0]:
                   calc=calc*Fraction(fractions[0])
##                       First of all the fraction to be subtracted from needs to be saved in 'calc'
              else:
                  calc=calc-Fraction(y)
##                 fractions subtracted

     print("ANSWER= ",calc)
     if login=='2':
          Student()
     elif login=='3':
         NoLogin()


def Algebra():
    action=int(input("""
    1)expand
    2)factorise
    3)solve simultaneous equations\n"""))
    if action==3:
         equa1=input("equation 1 in the form ax+by=c: ")
         equa2=input("equation 2 in the form ax+by=c: ")
##         User prompted to enter two equations to solve simultaniously
         a=np.array([[int(equa1[0]),int(equa1[3])],[int(equa2[0]),int(equa2[3])]])
         index1=equalSign(equa1)
         index2=equalSign(equa2)
##         indexes found
         b=np.array([int(equa1[index1:]),int(equa2[index2:])])
         x=np.linalg.solve(a,b)
         print("x=",x[0],"\ny=",x[1])
##         Values of x and y displayed
    elif action==1:
         equa=input("Equation to expand in the form (x+a)(x+b): ")
##         User prompted to enter equation
         terms=[]
         expanded=""
         part=""
         num=0
         power=0
         for i in equa:
              if i=="x":
                   power+=1
                   part="x^"+str(power)
##                   power of x calculated
         terms.append(part)
         for i in equa:
              try:
                  num+=int(i)
              except:
                  part=str(num)+"x"
##                  Number before x calculated 
         terms.append(part)
         num=1
         for i in equa:
              try:
                  num=num*int(i)
              except:
                  part=str(num)
        
         terms.append(part)
         for i in terms:
             expanded=expanded+i+"+"
##             components of expanded equation put together

         expanded=expanded[:-1]
         print(equa,"=",expanded)
##         Expanded equation displayed
    if login=='2':
        Student()
    elif login=='3':
        NoLogin()

def Circles_calc():
##    print("(x – h)^2 + (y – k)^2 = r^2")
    h=input("h= ")
    k=input("k= ")
    r=input("r= ")
##    The user enters the values of relevent components
    print("Centre: ("+h+","+k+")")
    print("Radius: "+r)
##    The radius and coordinates of the centre are returned to the user

    if login=='2':
        Student()
    elif login=='3':
        NoLogin()
    
def Discriminant():
    print("ax^2+bx+c")
    a=int(input("a= "))
    b=int(input("b= "))
    c=int(input("c= "))
##    User prompted to input values of a, b and c
    discriminant=b**2-(4*a*c)
##    Calculates the discriminant

    print("Discriminant: ",discriminant)
##    Value of discriminant displayed to user

    if discriminant<0:
        print(a,"x^2+",b,"x+",c,"has no roots")
    elif discriminant==0:
        print(a,"x^2+",b,"x+",c,"only has one root")
    elif discriminant>0:
        print(a,"x^2+",b,"x+",c,"has two roots")
##  If statement decides how many roots the quadratic equation has and the user is informed

    if login=='2':
        Student()
    elif login=='3':
        NoLogin()

def Calculations():
    valid=True
    while valid==True:
        calc=input("""
        1)Binomial expansion
        2)Fractions
        3)Algebraic methods
        4)Circles
        5)Discriminant\n""")
        if calc=='1' or calc=='2' or calc=='3' or calc=='4' or calc=='5':
            valid=False
        if calc=='1':
            BiExpansion()
        elif calc=='2':
            Fractions()
        elif calc=='3':
            Algebra()
        elif calc=='4':
            Circles_calc()
        elif calc=='5':
            Discriminant()
        else:
            print("Invalid Input")
    ##      If statement checks user input and direct to correct function depending on input
##The while loop ensures that the input is valid- this avoids crashes in the program.
    if login=='2':
        Student()
    elif login=='3':
        NoLogin()
    ##If statement returns the user to the correct menu depending on what type of login they have
    

def plot():
    fig, ax = plt.subplots()
    ax.plot(x, y)
##plots coordinates

    plt.show()
##Displays graph to user on grid


def circles(x, y, s, c='b', vmin=None, vmax=None, **kwargs):
    if np.isscalar(c):
        kwargs.setdefault('color', c)
        c = None

    if 'fc' in kwargs:
        kwargs.setdefault('facecolor', kwargs.pop('fc'))
    if 'ec' in kwargs:
        kwargs.setdefault('edgecolor', kwargs.pop('ec'))
    if 'ls' in kwargs:
        kwargs.setdefault('linestyle', kwargs.pop('ls'))
    if 'lw' in kwargs:
        kwargs.setdefault('linewidth', kwargs.pop('lw'))

##    If statements focus on the presentation (e.g. colour) of the circle

    zipped = np.broadcast(x, y, s)
    patches = [Circle((x_, y_), s_)
               for x_, y_, s_ in zipped]
    collection = PatchCollection(patches, **kwargs)
    if c is not None:
        c = np.broadcast_to(c, zipped.shape).ravel()
        collection.set_array(c)
        collection.set_clim(vmin, vmax)

    ax = plt.gca()
    ax.add_collection(collection)
    ax.autoscale_view()
    plt.draw_if_interactive()
    if c is not None:
        plt.sci(collection)

    plt.show()
##    Displays the plotted circle on a grid

def Graphs():
    global x
    global y

    x = np.linspace(-10, 10, 1000)
    valid=True
    while valid==True:
        type=input("""Would you like to enter an equation in the form...
        1) Linear'y=mx+c'
        2) Quadratic 'ax^2+bx+c'
        3) Cubic 'ax3 + bx + cx + d '
        4) Circle\n""")
##        print("Enter the equation of the graph with y being the subject.")
        if type=='1' or type=='2' or type=='3' or type=='4':
            valid=False
        if type=='1':
            m=int(input("m= "))
            c=int(input("c= "))
            y=m*x+c
##            Calculates the value of y given the values of the components of the equation
            plot()
        elif type=='2':
            a=int(input("a= "))
            b=int(input("b= "))
            c=int(input("c= "))
            y=a*x**2+b*x+c
##            Calculates the value of y given the values of the components of the equation
            plot()
        elif type=='3':
            a=int(input("a= "))
            b=int(input("b= "))
            c=int(input("c= "))
            d=int(input("d= "))
            y=a*x**3+b*x+c*x+d
##            Calculates the value of y given the values of the components of the equation
            plot()
        elif type=='4':
            print("(x – h)^2 + (y – k)^2 = r^2")
            h=int(input("h= "))
            k=int(input("k= "))
            r=int(input("r= "))
            circles(h,k,r)
##            Passes h,k and r as arguments for the function 'circles'
        else:
            print("Invalid Input")

    if login=='2':
        Student()
    elif login=='3':
        NoLogin()
    ##If statement returns the user to the correct menu depending on what type of login they have

def Quiz():
    score=0
    topic=int(input("""
    1)Binomial expansion
    2)Circles
    3)Algebraic methods (Basic mathematical skill)
    4)Trigonometry
    5)Fractions (Basic mathematical skill)\n"""))
##    The user selects what topic they want to work on

    print("""You'll be presented with 5 Exam Questions on your chosen topic
    Good Luck!""")

    if topic ==1:
         topic="Binomial expansion\n"
    elif topic==2:
         topic="Circles\n"
    elif topic==3:
         topic="Algebra\n"
    elif topic==4:
         topic="Trigonometry\n"
    elif topic==5:
         topic="Fractions\n"
##    Topic editted so that it matches the format of the text files
    

    q=open("Questions.txt","r")
    a=open("Answers.txt","r")
    ws=open("WorkedSolutions.txt","r")
##    Questions and answers files stored as variables
    questions=[]
    answers=[]
    solutions=[]

    for i in q:
         questions.append(i)

    for i in a:
         answers.append(i)

    for i in ws:
         solutions.append(i)
##    Comtents of text files saved in lists


    for i in range(len(questions)):
         if questions[i]==topic:
              for y in range(1,6):
##                   Displays the 5 questions on chosen topic
                   print(questions[i+y])
                   answer=input(": ")
                   answer+="\n"
                   if answer==answers[i+y]:
##                        If the answer is correct...
                        score+=1
                        print("correct")
                   else:
                        print("incorrect")
                        print("Working out ",solutions[i+y])
        
    q.close()
    a.close()
    print("You scored",score,"out of 5.")

    if login=='2':
##        If the user has a student account...
        if score<=2:
             with sqlite3.connect("Topics.db") as db:
                  cursor=db.cursor()
             insertData=('INSERT INTO WeakTopics(UserName,Topic) VALUES(?,?)')
             cursor.execute(insertData,[(username),(topic[:-1])])
             db.commit()
             
        topic=topic[:-2]
##        Takes away the "\n" from the topic name
        with sqlite3.connect("Scores.db") as db:
             cursor=db.cursor()
        find_score=('SELECT Score from ScoreTable WHERE Username=?')
        cursor.execute(find_score,[(username)])
        result=cursor.fetchall()
        for i in result:
             for y in i:
                  try:
                       result=int(y)
                  except:
                       result=result
        try:
             score+=result
             insertData=('UPDATE ScoreTable SET Score=? WHERE Username=?')
             cursor.execute(insertData,[(score),(username)])
        except:
             score=score
             insertData=('INSERT INTO ScoreTable(UserName,Score) VALUES(?,?)')
             cursor.execute(insertData,[(username),(score)])
##        Inserts the user's username and score
        db.commit()
        cursor.execute('SELECT * from ScoreTable ORDER BY Score DESC')
##        Orders the users by score
        Scores=cursor.fetchall()
        print("| Username  | Score  |")
        for i in Scores:
             print("|",i[0]," "*(8-len(i[0])),"|",i[1]," "*(5-len(str(i[1]))),"|")

          
        Student()
    elif login=='3':
##        If the user has a teacher account...
        NoLogin()

def StudentDetails():
    with sqlite3.connect("MathsPersonalDetails.db") as db:
        cursor=db.cursor()
    sur=input("Enter the surname of the student whose personal details you want to view: ")
    
##    cur.execute('SELECT Score from ScoreTable WHERE Username
    cursor.execute('SELECT * from personalDetails WHERE StudentORTeacher="S" AND Surname=?',[(sur)])
    LoginDetails=cursor.fetchall()
##    Selects all users who are students

    print("| Student number | Surname | Forename | Username |")

    for record in LoginDetails:
        print("|",i[0]," "*(15-len(i[0])),"|",i[1]," "*(7-len(i[1])),"|",i[2]," "*(8-len(i[2])),"|",i[3]," "*(9-len(i[3])))
##Presents the teacher with all the personal details of their students
    Teacher()
##Returns the teacher to the teacher menu to see what they want to do next

def ProgressTrack():
##     action=input("Would you like to see the progress of 1)individual students or 2)your classes: ")
     print("Track Progress")

     if login=='2':
        Student()
     elif login=='1':
        Teacher() 

def SetHomework():
     state="SET"
##     The state of the homework is "set" since the treacher is using the program to set homework. It will change to "turned in" when the user completes the homework.
     with sqlite3.connect("Homework.db") as db:
          curs=db.cursor()
     curs.execute('SELECT * from HW')
     hw=curs.fetchall()
##     The contents of the homework database is saved 
     print(hw)
     print("| Username | Quiz          | State     |")
     for i in hw:
          print("|",i[0]," "*(8-len(i[0])),"|",i[1]," "*(12-len(i[1])),"|",i[2]," "*(9-len(i[2])))
##     contents of homework database displayed in table form
     UN=''
     WorkingD=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
     action=input("If you want to set homework for all students type 'all' otherwise type the surname of the student you want to set homework for: ")
     print("The program will automatically set a quiz for the students based on their performance")
     date=int(input("""DUE DATE...
                   1)Monday
                   2)Tuesday
                   3)Wednesday
                   4)Thursday
                   5)Friday
                   6)Saturday
                   7)Sunday
                   : """))


     if action.upper()=="ALL":
##          If the user wants to set homework for all students...
          with sqlite3.connect("MathsPersonalDetails.db") as db1:
               cursor=db1.cursor()
          cursor.execute('SELECT UserName from personalDetails WHERE StudentORTeacher="S"')
          UNs=cursor.fetchall()
##          Usernames collected and saved
          for i in UNs:
               for z in i:
                    UN=z
                    with sqlite3.connect("Topics.db") as db2:
                         cur=db2.cursor()
                    cur.execute('SELECT Topic from WeakTopics WHERE Username=?',[(UN)])
                    topics=cur.fetchall()
##                    The weak topics for all relevant students are collected and saved
                    topic=topics[random.randint(0,len(topics))-1]
##                    A weak topic is chose at random
                    for y in topic:
                         t=y
                         insertData=('INSERT INTO HW(UserName,Quiz,State) VALUES(?,?,?)') 
                         curs.execute(insertData,[(UN),(t),(state)])
                         db.commit()
##                         homework database added to
                         t="HOMEWORK- "+y
                         day=WorkingD[date-1]
                         with sqlite3.connect("RevTime.db") as db3:
                              c=db.cursor()
                         c.execute('UPDATE TimeTable SET Quiz=? WHERE Day=?', [(t),(day)])
                         db3.commit()
##                         Students' timetables updated to notify the user that they have homework due
     else:
          with sqlite3.connect("MathsPersonalDetails.db") as db1:
               cursor=db1.cursor()
          cursor.execute('SELECT UserName from personalDetails WHERE Surname=?',[(action)])
          UNs=cursor.fetchall()
##          Usernames collected and saved
          for i in UNs:
               for z in i:
                    UN=z
                    print(UN)
                    with sqlite3.connect("Topics.db") as db2:
                         cur=db2.cursor()
                    cur.execute('SELECT Topic from WeakTopics WHERE Username=?',[(UN)])
                    topics=cur.fetchall()
                    print(topics)
##                    The weak topics for all relevant students are collected and saved
                    topic=topics[random.randint(0,len(topics))-1]
##                    A weak topic is chose at random
                    for y in topic:
                         t=y
                         insertData=('INSERT INTO HW(Username,Quiz,State) VALUES(?,?,?)')
                         curs.execute(insertData,[(UN),(t),(state)])
                         db.commit()
##                         homework database added to
                         t="HOMEWORK- "+y
                         day=WorkingD[date-1]
                         with sqlite3.connect("RevTime.db") as db3:
                              c=db3.cursor()
                         c.execute('UPDATE TimeTable SET Quiz=? WHERE Day=?', [(t),(day)])
                         db3.commit()
##                         Students' timetables updated to notify the user that they have homework duet
                         
     with sqlite3.connect("Homework.db") as db:
          curs=db.cursor()
     curs.execute('SELECT * from HW')
     hw=curs.fetchall()
     print(hw)
     print("| Username | Quiz          | State     |")
     for i in hw:
          print("|",i[0]," "*(9-len(i[0])),"|",i[1]," "*(13-len(i[1])),"|",i[2]," "*(9-len(i[2])))
     
     Teacher()

def Timetable():
     global t
     day=''
     t=''
     with sqlite3.connect("RevTime.db") as db:
          cursor=db.cursor()
     Days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
     for i in Days:
          day=i
          busy=input("Will you be available to revise on "+i+"? y/n: ")
          if busy.upper()=="Y":
               with sqlite3.connect("Topics.db") as db:
                  cur=db.cursor()
               cur.execute('SELECT Topic from WeakTopics WHERE Username=?',[(username)])
               topics=cur.fetchall()
               topic=topics[random.randint(0,len(topics))-1]
               for y in topic:
                    t=y
                    cursor.execute('UPDATE TimeTable SET Quiz=? WHERE Day=?', [(t),(day)])
          elif busy.upper()=="N":
               with sqlite3.connect("Topics.db") as db:
                  cur=db.cursor()
                  cursor.execute('UPDATE TimeTable SET Quiz="NONE" WHERE Day=?', [(day)])

     cursor.execute('SELECT * from TimeTable')
     sched=cursor.fetchall()
     print("| Day        | Quiz          |")
     for i in sched:
          print("|",i[0]," "*(9-len(i[0])),"|",i[1]," "*(12-len(i[1])),"|")
     
     Student()

def Student():
    print("What would you like to do next?")
    valid=True
    while valid==True:
        action=input("""
        1)Mechanics formulae
        2)Develop graphs
        3)Quiz
        4)Timetable
        5)Calculations
        6)Logout\n""")
##    User options displayed in a list
        if action=='1' or action=='2' or action=='3' or action=='4' or action=='5' or action=='6':
            valid=False
        if action=='1':
            Formulae()
        elif action=='2':
            Graphs()
        elif action=='3':
            Quiz()
        elif action=='4':
            Timetable()
        elif action=='5':
            Calculations()
        elif action=='6':
            print("Goodbye")
            sys.exit()
##            Exits program
        else:
            print("Invalid Input")
##      If statement checks user input and direct to correct function depending on input
##The while loop ensures that the input is valid- this avoids crashes in the program.

def Teacher():
    print("What would you like to do next?")
    valid=True
    while valid==True:
        action=input("""
        1)Track your students' progress
        2)Set homework
        3)View Students details
        4)Logout\n""")
##    User options displayed in a list
        if action=='1' or action=='2' or action=='3':
            valid=False
        if action=='1':
            ProgressTrack()
        elif action=='2':
            SetHomework()
        elif action=='3':
            StudentDetails()
        elif action=='4':
            print("Goodbye")
            sys.exit()
##            Exits program
        else:
            print("Invalid Input")
##      If statement checks user input and direct to correct function depending on input
##The while loop ensures that the input is valid- this avoids crashes in the program.

def NoLogin():
    print("What would you like to do next?")
    valid=True
    while valid==True:
        action=input("""
        1)Mechanics formulae
        2)Develop graphs
        3)Quiz
        4)Calculations
        5)Logout\n""")
##    User options displayed in a list
        if action=='1' or action=='2' or action=='3' or action=='4':
            valid=False
        if action=='1':
            Formulae()
        elif action=='2':
            Graphs()
        elif action=='3':
            Quiz()
        elif action=='4':
            Calculations()
        elif action=='5':
            print("Goodbye")
            sys.exit()
##            Exits program
        else:
            print("Invalid Input")
##      If statement checks user input and direct to correct function depending on input
##The while loop ensures that the input is valid- this avoids crashes in the program.

def validPW(pw):
    ##Defines function that checks if the password entered satisfies the requirements given.
    ##The requirements set out imporove the strength of the password and further protects the data
    global valid
    ##The variable 'valid' is made global
    upper=0
    lower=0
    integer=0
    for i in pw:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif i.isdigit():
            integer+=1
    ##Checks what type of data each character in the password is.
        if upper>0 and lower>0 and integer>0 and len(pw)>=8:
            valid=True
    ##If all the requirements are met, the variable 'valid' is set to True and the program can continue.
        else:
            valid=False
    ##else, 'valid' is set to False




def Register():
    found=0
    while found==0:
        UserName=input("Please enter a username: ")
        with sqlite3.connect("MathsPersonalDetails.db") as db:
            cursor=db.cursor()
        findUser=("SELECT * FROM personalDetails WHERE username= ?")
        cursor.execute(findUser,[(UserName)])
##        Selects any users who have the username the new user wants to have

        if cursor.fetchall():
##        if there are any users who have the same username as the one the new user wants...
            print("Username Taken, please try again")
##            The user is prompted to enter a different username.
        else:
            found=1
##    Makes sure that the new user has a unique username.
##    While loop repeats until the user enters a unique username


    StudentORTeacher=input("Are you a Student or Teacher? S/T: ")
    StudentORTeacher=StudentORTeacher.upper()
##    studentORTeacher will always be in uppercase
    Surname=input("Surname:")
    Forename=input("Forename:")

##    The user is prompted to enter their personal details
    print("Your password must be at least eight characters long and contain a mixture of integers,  uppercase and lowercase letters.")
    while True:
##        password=getpass.getpass("Please enter your password: ")
        password=input("Please enter your password: ")
        validPW(password)
        if valid==True :
            print("Strong password")
##            password1=getpass.getpass("Please re-enter your password: ")
            password1=input("Please re-enter your password: ")
##            The user is prompted to re-enter their password to make sure that there weren't any typos.
            if password==password1:
##                if the password is strong enough and the password they re-entered matches the original, the user is notified and the while loop ends.
                break
            else:
               print("Your passwords didn't match, please try again") 
        else:
            print("Your password isn't strong enough!\n")
            print("Your password must be at least eight characters long and contain a mixture of integers,  uppercase and lowercase letters.")

##    The user is prompted to enter their password until they enter a 'strong' one.


    insertData='''INSERT INTO personalDetails(StudentORTeacher,Surname,Forename,UserName,Password)
    VALUES(?,?,?,?,?)'''
##    The users personal data is inserted into the database

##    cursor.execute(insertData,[(StudentORTeacher),(Surname),(Forename),(UserName),(getKey(password))])

    cursor.execute(insertData,[(StudentORTeacher),(Surname),(Forename),(UserName),(password)])

    db.commit()
    
    print("You have been successfully registered.")
    LoginMenu()



def LoginMenu():
    sg.change_look_and_feel('Dark Blue 3')	
    # All the stuff inside the window.
    layout = [  [sg.Text("Welcome to The Maths Education Program! Don't have an account? Register ")],
                 [sg.Button('Teacher'), sg.Button('Student'), sg.Button('Register'),sg.Button('Cancel')] ]

     # Creates the Window
    window = sg.Window('Account', layout)
     # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):	# if user closes window or clicks cancel
             window.close()
        elif event in(None,'Register'):
             window.close()
             Register()
        elif event in(None,'Teacher') or event in(None,'Student'):
             window.close()
             DatabaseCheck()
               
     
    valid=True
####    'valid' is the variable used to determines how many times the while loop is repeated
    print("Welcome to The Maths Education Program!\n")
    while valid==True:
        login=input("""Would you like to login as a 1)teacher 2)student or 3)continue without logging in? 1,2 or 3
        Don't have an account? 4)Register
        : """)
        if login=='1' or login=='2' or login=='3' or login=='4':
            valid=False
        if login=='1' or login=='2':
            DatabaseCheck()
        elif login=='3':
            NoLogin()
        elif login=='4':
            Register()
        else:
            print("Invalid Input!")
##      If statement checks user input and direct to correct function depending on input
##The while loop ensures that the input is valid- this avoids crashes in the program.


LoginMenu()

