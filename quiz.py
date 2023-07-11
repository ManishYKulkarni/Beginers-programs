print("Welcome to the quiz")
playing=input("Do you want play quiz? \n")
if playing.lower()!="yes":
    quit()
print("Let's begin the game")
score=0
answer=input("1.Who is the prime minister of india? \n")
if answer.lower()=="narendra modi":
    print("corect")
    score+=1   
else:
    print("incorrect") 
answer=input("2.Who is the actor in Bajarangi Bhaijan? \n") 
if answer.lower()=="salman khan":
    print("corect")
    score+=1   
else:
    print("incorrect")        
answer=input("3.What is the full form CPU?\n ")
if answer.lower()=="central processing unit":
    print("corect")
    score+=1   
else:
    print("incorrect")  
answer=input("4.what is full form of RAM? \n")
if answer.lower()=="random access memory":
    print("corect")
    score+=1   
else:
    print("incorrect")     

print(f"you have scored {score}")
