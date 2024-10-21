import random

print("""
ELIctric Walker - alpha1.0.1 Oct21-2024

IDCraft Community
Game Rule:
1. There are x classes totally (x depends on your input later)
2. These classes are arranged linearly
3. Eli will walk randomly through these classes:
   for each minute, if Eli stands at the door of a class,
   he have the probability of 33.3% to walk into the class,
   else he will just move away to the next class;
   if Eli stands in a class, he can only walk outside this class.
4. Eli's moving direction between classes is constant until he
   reaches the end of the row of classes
5. For each minute, you have three choices:
   play the game, you will get 1 score, if you have played for
   several minutes, you will get some extra scores of the number
   the time in minute that you kept playing;
   listen to the class, nothing will happen;
   peek outside the class, you will get Eli's specific position
   if he is outside the class and the distance between you and
   Eli is lower or equal to 5 classes; you will find a weird
   silence in some nearby classes if Eli is inside a class and
   distant from you lower or equal to 3 classes; or you will get
   nothing
6. If you are playing while Eli comes into your class, your device
   will be taken and you will be deducted 15 scores. In the rest of
   class, you will not be able to play anymore.
""")
while True:
   t = 40
   score = 0
   co_score = 1
   classes = input("How many classes you want to have? (At least 3) ")
   classes = abs(int(classes))
   if classes < 3:
      classes = 3
   print("Now you have "+str(classes)+" classes")
   clas = random.randint(1,classes)
   eli = [False, random.randint(1,classes), random.choice([1,-1])]
   print("==========Game Start==========")
   print("You are in class "+str(clas))
   while t:
       if not eli[0]:
           if not random.randint(0,2):
               eli[0] = not eli[0]
           else:
               eli[1] += eli[2]
               if eli[1] == classes+1:
                   eli[1] = classes-1
                   eli[2] = -eli[2]
               elif not eli[1]:
                   eli[1] = 2
                   eli[2] = -eli[2]
       else:
           eli[0] = not eli[0]
       print("==Another new minute==")
       print("Time remained: "+str(t)+" minute")
       print("Your score: "+str(score))
       o = int(input("For this minute, you want to: 1.play 2.listen 3.peek "))
       if o == 1:
           if eli == [True, clas, eli[2]]:
               print("You lost your device!")
               score -= 15
               break
           else:
               print("Another fun time!")
               score += co_score
               co_score += 1
       elif o == 2:
           print("Your teammates wants to talk with you in voice")
           co_score = 1
       elif o == 3:
           if abs(clas-eli[1]) <= 5 and not eli[0]:
               print("Eli walking! He is at the door of class "+str(eli[1]))
           elif abs(clas-eli[1]) <= 3 and eli[0]:
               print("It's a weird silence in some nearby class")
           else:
               print("You didn't see anything")
           co_score = 1
       else:
           print("You studied for a another minute")
           co_score = 1
       if eli == [True, clas, eli[2]]:
           print("Eli came in in this minute! You were not caught!")
       t -= 1
       input()
   print("Class is over")
   if score < 0:
       score = 0
   print("You got "+str(score)+" score")
   print("==========Game Over==========")
   if int(input("Do you want to play it again? 1.yes 2.no "))-1:
      break
