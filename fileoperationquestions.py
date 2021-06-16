#!/usr/bin/env python
# coding: utf-8

# In[ ]:


myFile = open("class_scores.txt","r")
newFile = open("addedScores.txt","w")
testScores = []
testScorePerson = []
for i in range(0,4):
    testScorePerson = myFile.readline().split()
    testScorePerson[1] = str(int(testScorePerson[1]) + 5)
    print(testScorePerson)
    testScores.append(testScorePerson)
    print(testScores)
for element in testScores:
    newElement = " ".join(element)
    newElement = "\n"+newElement
    newFile.write(newElement)
    print(newElement)


# In[ ]:


myFile = open("grades.txt","r")
testScores = []
passCounter = 0
for i in range(0,4):
    testScorePerson = myFile.readline().split()
    if (int(testScorePerson[1])>33 and int(testScorePerson[2])>33 and int(testScorePerson[3])>33):
        passCounter+=1
print(passCounter)


# In[ ]:


myFile = open("logfile.txt","r")
logPerson = []
logon = 0
logoff =  0
diff = 0
hour = 0
for i in range(0,4):
    logPerson = myFile.readline().split()
    logon = logPerson[1]
    logoff = logPerson[2]
    logon = logon.split(":")
    logoff = logoff.split(":")
    logon = "".join(logon)
    logoff = "".join(logoff)
    diff = int(logoff)-int(logon)
    diff = str(diff)
    mins = str(diff[0])+str(diff[1])
    if int(diff[0])>=1 or int(mins)>60:
        if int(diff)>12 and int(diff)<60:
            diff=diff
        elif int(mins)>60:
            hour+=1
        else:
            hour+=1
print(hour)


# In[ ]:


userInput = input("Your sentence: ")
userInput = userInput.split()
letters = []
for element in userInput:
    for i in range(0,len(element)):
        newString = element[i].lower()
        if newString not in letters:
            letters.append(newString)
newLetters = "".join(letters)
if len(letters)==26 and newLetters.isalpha():
    print(True)
else:
    print(False)


# In[1]:


from random import randint
question = ""
userInput = ""
operator = 0
num1 = 0
num2 = 0
ans = 0
i = 0
score = 0
print("Welcome to XYZ school examination center!")
print("Kindly enter your name and grade for the test!")
name = input("Name: ")
grade = input("Grade: ")
print("All the best!")
while(i!=10):
    operator = randint(0,4)
    if operator==0:
        num1 = randint(1,99)
        num2 = randint(1,99)
        ans = num1+num2
        print(name, ",your question is",num1,"+",num2,"?")
        userInput = int(input("Answer: "))
        if userInput==ans:
            score+=1
        i+=1
    elif operator==1:
        num1 = randint(1,99)
        num2 = randint(1,99)
        ans = num1-num2
        print(name, ",your question is",num1,"-",num2,"?")
        userInput = int(input("Answer: "))
        if userInput==ans:
            score+=1
        i+=1
    elif operator==2:
        num1 = randint(1,99)
        num2 = randint(1,99)
        ans = num1*num2
        print(name, ",your question is",num1,"x",num2,"?")
        userInput = int(input("Answer: "))
        if userInput==ans:
            score+=1
        i+=1
    elif operator==3:
        num1 = randint(1,99)
        num2 = randint(1,99)
        ans = float(num1/num2)
        print(name, ",your question is",num1,"÷",num2,"?")
        userInput = float(input("Answer: "))
        if userInput==ans:
            score+=1
        i+=1
print("Calculating results...")
print("Printing...")
print("Name:",name)
print("Grade:",grade)
print("Score: ",score,"/ 10")
print("Percentage: ",(score/10)*100)


# In[3]:


#Factorial Finder
num = int(input("Number: "))
if num==0:
    print("Factorial is ",1)
for i in range(1,num):
    if num>0:
        num = num*i
print(num)


# In[6]:


def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)
print(factorial(3))


# In[4]:


unit1 = input("Current unit: ")
unit2 = input("Change unit: ")
value = int(input("Current value: "))
dict = {"cm":{"mm":10,"cm":1,"m":0.01,"km":0.0001},
       "mm":{"mm":1,"cm":0.1,"m":0.001,"km":0.0000001},
    "m":{"mm":1000,"cm":100,"m":1,"km":0.001},
         "km":{"mm":1000000,"cm":100000,"m":1000,"km":1}
       }
print(value*dict[unit1][unit2])


# In[10]:


logFile = {
    "Shivansh":"S123",
    "Vivaan":"V123",
    "Kanishk":"K123",
    "Sahib":"Sa123",
    "Arnav":"A123",
    "Aarav":"Aa123",
    "Dhruv":"D123",
    "Krishnav":"Kr123",
    "Divya":"Di123",
    "Abhishek":"Ab123",
}
userName = input("Username: ")
password = input("Password: ")
if userName in logFile:
    if logFile[userName]==password:
        print("Logged into the system!")
    else:
        print("Password is invalid!")
else:
    print("Not a valid user!")


# In[ ]:


#Write a program to play the following game. There is a list of several country names and the
#program randomly picks one. The player then has to guess letters in the word one at a time.
#Before each guess the country name is displayed with correctly guessed letters filled in and
#the rest of the letters represented with dashes. For instance, if the country is Canada and the
#player has correctly guessed a, d, and n, the program would display -ana-da. The program
#should continue until the player either guesses all of the letters of the word or gets five letters wrong.
countries = ["canada","india","zimbabwe","israel","iraq","brazil"]
from random import randint
num = randint(0,4)
country = countries[num]
string = "_ "*len(country)
newString = ""
guessed = False 
counter = 0
while guessed==False:
    print("Here is the country ",string, country)
    userInput = input("Your Letter: ")
    if counter<5:
        if userInput in country:
            for i in range(0,len(country)):
                if country[i]==userInput:
                    string = string[:i]+userInput+string[i+1:]
                else:
                    counter+=1
    
            


# In[ ]:





# In[ ]:





# In[ ]:




