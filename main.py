#import tensorflow as tf

#@author MeltingMettle
#Variables representing a number have no upper case (ie missionnumber)
#Variables representing an array or other data structure (ie playerList)



#Hello friends! Contributions welcome!

#If you're one of my students, good luck! XD See what you can learn/understand/try and hit me up if you have any questions.



class Mission:                                              #A Mission class to track the game progress in chunks. There will be between 3-5 of these.
    def __init__(self, missionnumber, players, votes, outcome = None, prediction = None):
        self.votes = votes
        self.players = []
        self.number = missionnumber
        self.proposedTeams = []
        self.outcome = None                                 #Notice the type  changes between instantiation and assignment.  A big no-no in Java
        
    def passed(self):
        self.outcome = 1
        Game.missionResults[Game.currentmission] = 1
        

    def failed(self):
        self.outcome = 0
        Game.missionResults[Game.currentmission] = 0
        
    def addProposedTeam(self, calvinism):                   #Should add a double array with players and votes
        self.proposedTeams.append(calvinism)

    def analyzeMission():
        #Problem 1

        #Return all useful data from mission and print
        #This is very do-able! :) Just print the lists, and use a function to match/
        #the player numbers to names.  (IE. Game.players[2].getName() will return "Adam")
        #(Players are indexed and named by their position on Game's Array players.)

        #Given missionX.propsedTeams, which looks like:
        #[[[1,4,2,6], [1,0,0,0,0,0,0,0,0,0]], ....]    
        # #Triple list, each item is a double list with each propsed mission and vote count
        
        
        #So [1,4,2,6] would become "Max made a team with Emmett, Amanda, Ethan, and Player6"
        #and [1,0,0,0,0,0,0,0,0,0] woud be "Max approved!  Emmett, Amanda, Janet, Ethan, Alex [...] rejected!"
        return None

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
        self.votingPattern = []
        self.fullVoteAnalysis = []

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
    #Problem 2
    #TODO when does the game end?
    players = []                                                #Remember to reference this as Game.players
    for i in range(10):
        players.append(Player("Player" + str(i), i))
    currentmission = 1                                          #Reference this as Game.getCurrentMission(). Remember what abstraction is?
    missionsCount = [None, None, None, None, None]
    missionResults = [None, None, None, None, None]
    teamSize = [3, 4, 4, 5, 5]                                  #For later use, with 5-9 players option
                                                                #Later on, we'll fill this based on the input of how many players
    successmissions = 0
    failmissions = 0
    captain = None
    
    
    def __init__(self):
        count = int(input("How many players?")) 
        #assert number below 10
        af = str(input("autofill? yes or no? (All input must be in quotes for now))) 
        if af == "no":
            name0 = str(input("What's your name?"))
            Game.players[0].setname(name0)
            name1 = str(input("Who's sitting to your left?"))
            Game.players[1].setname(name1)
            for i in range(2, count):
                name = input("Who's sitting to his/her left?")
                Game.players[i].setname(name)              
        captain = input("Who's making the first team? Number please!")
        #Assert number is between 0-9
        print(str(Game.players[captain].getname()) + " is making the first team!")
        round()

    def getCurrentMission(self):
        return currentmission

    def nextMission(self):
        Game.currentmission += 1
        Game.captain += 1
        round()

def round():
    #Problem 3: Check inputs and display error without exiting program
    #Bonus if you can get python to intake strings without user needing to add quotes.

    #assert the team "leader" changed up by one
    #Assert game isn't over
    #assert no double players on the same team
    #check which mission reject this is
    #assert mission has right amount of people
    #assert right number of votes
    Game.currentmission = shield                                #Mission index tracker to make code more readable
    failedVotes = []
    print("Knowledge is power! ")
    pause = input("Would you like to analyze the game? yes/no? ")
    if str(pause) == "yes": 
        print("too bad. You're going to lose anyways. ;)")
        #Actually open menu of players or missions to analyze, or an option to review  the whole game
    else:
        print("Very well.  It's your funeral.")

    print("\n")  #NewLine

    print("We are on Mission #" + str(shield) + " which needs a team of " + str(Game.teamSize[shied]))
    team = input("Who's on this team? (lump number)")
    #Take in votes and players on the team
    votes = input("Votes?")  #Track each player's vote for each team
    team = toArray(team)
    votes = toArray(votes)
    #Begin the Mission and index the Game class's trackers. 
    roundMission = Mission(shield, team, votes)
    Game.missionsCount[shield] = roundMission
    

    #Here's the tricky oart. Let's see if we can write each mission's result to the Mission class
    #but also each player. (For later analysis) 
    #Instead of analysing the whole game, it would be more efficient to analyze players one by one
    #Instead of writing the entire game to file, let's try writing a player's profile and end loyalty
    
    def NSA(bigbrother):                    #Record ALL the actions!!
        return None

    def recordAction(playernumber):         #Document a player's decisions this round.
        Game.players[playernumber].
        return None

    def recordToGame(teamAndVotes):         #Note what's going on for the round's Mission object
        roundMission.addProposedTeam(teamAndVotes)
        return None

    
    #Now we continue with the actual game
    if passorfail(votes) > 5:
        #Save the mission result and update all the stuffs
        missionresult = input("Pass or fail? 0 or 1?")
        Game.missionResults.append(missionresult)
        roundMission.passed()
        if Game.currentmission > 5:
            return gameEnd()
        else:
            Game.nextMission()
    else:
        roundMission.failed()
        print("Vote failed.  Make new team.")  
        recordToGame[team, votes])       #add votes to failed team log
        round()


def last_hope(): #Call this iff it's the 5th mission. Will return a detailed game analysis which will point out the spies
    return "rip"

def recognize(play):
    #Problem 4:  I expect you all to try something for this. :) Check out analysis.py.
    #Will recognize and return classic plays
    #using the anaylsis that YOU wrote and pushed into the repo ^-^
    return None 


def status():
    print("Everything that's happened so far in an orderly and readable format")
    return None

def passorfail(v):
    total = sum(v)
    print(str(total) + " approves and " + str(10-total) + "rejects")
    return total



    #This got messier than US politics.  For kicks, see if you can try to figure out what I was trying to do
    # total = 0
    # total = sum(toArray(v))
    # approval = []
    # rejector = []
    # index = 10
    # counter = 0
    # while counter < 10:
    #     total += v % 10 
    #     if v % 10 == 0:
    #         rejector.append(Game.players[index].getname())
    #     elif v % 10 == 1:
    #         approval.append(Game.players[index].getname())
    #     else:
    #         print("Your vote don't matter mate")
    #     v = v // 10
    #     counter += 1
    #     index -= 1
    
    # print(str(total) + " approves and " + "\n" + str(10 - total) + " rejections")
    # print(str(approval) + " approved the mission and " + "\n" + str(rejector) + "rejected.")
    # index = 0
    # return total

def investigate(player):
    print("Table of each player and their likelyhood of being a spy")

def gameEnd():
    #Problem 5:    
    #Write results and data to a file
    #print everything for review
    #I'll probably do this one myself but feel free if you want to learn stuff
    #Also, think of how to design the file so it  can be read and analyzed later!
    if sum(Game.missionResults) >= 3:
        print("Resistance wins!")
        print("\n")
        print("Hide yo merlin!   ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)")
    else: 
        print("Spies win!")
        print("\n")
        print("dumpstered. ( ͡° ͜ʖ ͡°)")
    return None

def writeToFile():
    #Write the entire game to the rtf file for later analysis

def toArray(x):
    result = []
    votecount = 10
    while votecount > 0:
        result.append(x%10)
        x = x//10
        votecount -= 1
    return list(reversed(result))



play = Game()

#Problem 6: Create a GUI 
#Never done this kind of thing myself and ain't nobody got time for that

#Problem 7: Learn how to create a neural network using TensorFlow! 
#I'm working on this too. This is a really interesting challenge if you're interested!


#How to tell if someone's a spy:
#Mission fails
#votes
#votes on mission passes/fails


#Add plays


# name = input("What's your name? ")
# print("Nice to meet you " + name + "!")
# age = input("Your age? ")
# print("So, you are already " + str(age) + " years old, " + name + "!")