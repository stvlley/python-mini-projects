print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play! >:)")
score = 0
# questions

answer = input("What does HTML stand for? ")
if answer.lower() == "hyper text markup language":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :(")

answer = input("What does HTTP stand for? ")
if answer.lower() == "hyper text transfer protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :(")   

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :(")   

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! :(")

print("You got "+ str(score) + " questions correct!") 
print("You got "+ str((score / 4) * 100) + "%.")    