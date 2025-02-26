import random

computer= random.choice([0, 1, -1])
you=input("Enter your choice between s ,g or w:")
youdict={"s":1,"w":-1,"g":0}#snake=1 water=-1 and gun=0
younum=youdict[you]
reversedict={1:"Snake",-1:"Water",0:"Gun"}
print(f"You choose {reversedict[younum]}")
print(f"Computer choose {reversedict[computer]}")

if(computer-younum==0):
    print("DRAW")
elif(computer-younum==1 or computer-younum==-2):
    print("YOU WIN")
else:
    print("YOU LOSE")