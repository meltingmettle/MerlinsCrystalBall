#import tensorflow as tf


class Mission: 
    def __init__(self, missionnumber, players, votes, outcome = None, prediction = None):
        self.votes = votes
        self.players = []
        self.number = missionnumber
        self.proposedteams = []
        

    def __str__(self):
        print("number:outcome, players, votes, failedvotes")
        return None

class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.spyprobability = 44
        self.suslevel = 0
        self.missions = []
        self.votingpattern = []

    def setname(self,name):
        self.name = name
    
    def getname(self):
        return self.name
    
    def getnumber(self):
        return self.number

    def investigate(self):
        #Print suslevel, along with actions from the entire game
        return None
    def __str__():
        print(self.name)
        return self.name
        
class Game:

    players = []                                                #Remember to reference this as Game.players
    for i in range(10):
        players.append(Player("Player" + str(i), i))

    currentmission = 1                                          #Reference this as Game.currentmission. Remember what abstraction is?

    missions = [None, None, None, None, None]
    missionResults = [None, None, None, None]
    captain = None
    
    
    def __init__(self):
        count = int(input("How many players?"))
        #assert number below 10
        af = str(input("autofill? yes or no?"))
        if af == "no":
            name0 = str(input("What's your name?"))
            Game.players[0].setname(name0)
            name1 = str(input("Who's sitting to your left?"))
            Game.players[1].setname(name1)
            for i in range(2, count):
                name = input("Who's sitting to his/her left?")
                Game.players[i].setname(name)              
        captain = input("Who's making the first team? Number please!")
        #Assert number below 10
        print(str(Game.players[captain].getname()) + " is making the first team!")
        round()

    def nextMission(self):
        Game.currentmission += 1
        Game.captain += 1
        round()

def round():
    #assert the team "leader" changed up by one
    #Assert game isn't over
    #assert no double players on the same team
    #check which mission reject this is
    #assert mission has right amount of people
    #assert right number of votes

    failedvotes = []
    team = input("Who's on this team? (lump number)")
    votes = input("Votes?")  #Track each player's vote for each team
    team = toArray(team)
    if passorfail(votes) > 5:
        predictedOutcome = input("Pass or fail? 0 or 1?")
        Game.missionResults.append(predictedOutcome)
        missionstart = Mission(Game.currentmission, team, votes, predictedOutcome)
        Game.missions[Game.currentmission] = missionstart
        
        if Game.currentmission > 5:
            return gameEnd()
        else:
            Game.nextMission
    else:
        #add votes to failed team log
        print("Vote failed.  Make new team.")
        failedvotes.append([team, votes])
        round()

def last_hope(): #Call this iff it's the 5th mission. Will return a detailed game analysis which will point out the spies
    return "rip"

def recognize(play):
    return None #will recognize and return classic plays


def status():
    print("Everything that's happened so far in an orderly and readable format")
    return None

def passorfail(v):
    total = 0
    total = sum(toArray(v))
    approval = []
    rejector = []
    index = 0
    while v > 0:
        total += v % 10 
        if v % 10 == 0:
            rejector.append(Game.players[index].getname())
        else:
            approval.append(Game.players[index].getname())
        v = v // 10
    print(str(total) + " approves and " + "\n" + str(10 - total) + " rejections")
    print(str(approval) + " approved the mission and " + "\n" + str(rejector) + "rejected.")
    index = 0
    return total

def investigate(player):
    print("Table of each player and their likelyhood of being a spy")

def gameEnd():
    #Write results and data to a file
    if sum(Game.missionResults) >=3:
        print("Resistance wins!")
        print("\n")
        print("Hide yo merlin!")
    else: 
        print("Spies win!")
        print("\n")
        print("dumpstered.")
    return None

def toArray(x):
    result = []
    while x != 0:
        result.append(x%10)
        x = x//10
    return result



play = Game()


#How to tell if someone's a spy:
#Mission fails
#votes
#votes on mission passes/fails


#Add plays


# name = input("What's your name? ")
# print("Nice to meet you " + name + "!")
# age = input("Your age? ")
# print("So, you are already " + str(age) + " years old, " + name + "!")