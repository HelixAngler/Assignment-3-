#Import SlotSys Package
from SlotSys import *
#Function to Simulate Loading, Opening, and End of The Program
def Titling():
    print("Loading")
    sleep(2)
    print(3)
    sleep(1)
    print(2)
    sleep(1)
    print(1)
    sleep(1)
    opening="Welcome to slot-machine-inspired betting game"
    bye="Thanks for Playing"
    return opening,bye
opening,bye=Titling()
#Print The Opening Statement
print(opening)
#Main Process
while True:
    #Initial Dictionary
    databass = {}
    #Trigger The Package Classes
    working = main(databass)
    working.runup()
    working.result()
    #Restart The Program or Exit
    again=input("Play again? Y for yes, N or others for no").upper()
    if again=="Y":
        continue
    else:
        break
#Closing Statement
print(bye)