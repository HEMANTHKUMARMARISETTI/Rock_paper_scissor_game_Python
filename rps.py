import random
print("---------------RULES---------------\n")
print("rock - paper = paper wins\npaper - scissor=scissor wins\nscissor - rock =  rock wins\n")
print("please enter rock/paper/scissor carefully or player will get a minus points\n.................................\n................Thank you................\n.................................")
name=str(input("enter Player name : "))
count1,count2=0,0
count=0
game=int(input("How many Games u want to play : "))
for i in range(1,game+1):
    choice=str(input("Start the Game yes/no : "))
    if(choice=='yes'):
       print("\n------->Game Number : ",i)
       computer=random.choice(['rock','paper','scissor'])
       player=str(input('Enter Your Choice rock/paper/scissor : '))
       if(player=='rock' and computer=='paper'):
          print("computer Wins\n")
          print("Computer chooses : ",computer,"\n.................................")
          count1=count1+1
          continue
       elif(player=='paper' and computer=='rock'):
          print(name, "Wins\n")
          count2=count2+1
          print("Computer chooses : ",computer,"\n.................................")
          continue
       elif(player=='paper' and computer=='scissor'):
          print("Computer Wins\n")
          count1=count1+1
          print("Computer chooses : ",computer,"\n.................................")
          continue
       elif(player=='scissor' and computer=='paper'):
          print(name, "Wins\n")
          count2=count2+1
          print("Computer chooses : ",computer,"\n.................................")
          continue
       elif(player=='scissor' and computer=='rock'):
          print("computer Wins\n")
          count1=count1+1
          print("Computer chooses : ",computer,"\n.................................")
          continue
       elif(player=='rock' and computer=='scissor'):
          print(name, "Wins\n")
          count2=count2+1
          print("Computer chooses : ",computer,"\n.................................")
          continue
       elif(player==computer):
          print("Match Tied\n")
          count=count+1
          print("Computer chooses : ",computer,"\n.................................")
          continue
       else:
          print('player must enter a vaid term\n')
          count2=count2-1
          print("Computer chooses : ",computer,"\n.................................")
          continue
    else:
        print("Ok , Thank you")
        print("Player exited ,Computer Wins Legally")
        count2=0
        break
print("POINTS_____________________") 
print(name," : ",count2)
print("Computer : ",count1)
print("Tied : ",count)
if(count1>count2):
    print("computer Wins")
elif(count1<count2):
    print(name," Wins")
else:
    print("MAtch Draw")
     
