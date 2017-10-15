#Import Random and Time library
from random import *
from time import *
#Randomizer Class
class randomizer(object):
    def __init__(self,running,parti):
        for i in running:
            #First Roll
            slot1=randrange(1,13)
            print("%s got %d as the first number"%(i,slot1))
            sleep(1)
            #Second Roll
            slot2=randrange(1,13)
            print("%s got %d as the second number"%(i,slot2))
            sleep(1)
            #Third Roll
            slot3=randrange(1,13)
            print("%s got %d as the third number\n"%(i,slot3))
            sleep(1)
            #Accumulate Numbers in One Round
            self.slot=slot1+slot2+slot3
            print("%s got %d in this round\n\n"%(i,self.slot))
            #Accumulate Total Numbers with Previous Rounds
            parti[i]=parti[i]+self.slot
            sleep(3)
#Participant Class
class name(object):
    def __init__(self,shell):
        self.participant=shell
        #How Many Participants
        while True:
            try:
                self.howmany=int(input("How many person that participate"))
                break
            except:
                print("Invalid")
                continue
        #Insert Participants
        for countup in range(1,self.howmany+1):
            n=input("Player %d name: "%countup)
            self.participant[n]=0
#Main Class
class main(name,randomizer):
    def __init__(self,shell):
        #Declare name Superclass
        name.__init__(self,shell)
        #Filtering Player Names
        self.players=[]
        for k in self.participant.keys():
            self.players.append(k)
    def runup(self):
        #Three Round Loop
        for rounding in range(1,4):
            print("Round %d\n\n"%rounding)
            sleep(3)
            #Initialize the randomizer Class
            randomizer.__init__(self,self.players,self.participant)
    def result(self):
        #Filter Points
        data=[]
        for val in self.participant.values():
            data.append(val)
        #Filter Unique Numbers
        macl=[]
        for system in set(data):
            macl.append(system)
        #Sort Numbers
        macl.sort()
        #Check Who is The Winner by Matching the Highest Number with The Values Inside Keywords
        for ke in self.participant.keys():
            if self.participant[ke]==macl[-1]:
                print("%s is the winner with the score of %d"%(ke,macl[-1]))
        return(self.participant)