#import tensorflow as tf

#@author MeltingMettle
#Variables representing a number have no upper case (ie missionnumber)
#Variables representing an array or other data structure (ie playerList)



#Hello friends! Contributions welcome!
#Search "Problem" to jump to a section which needs help. 

#If you're one of my students, good luck! XD See what you can learn/understand/try and hit me up if you have any questions.
#With only 5 possible missions and 10 players, it was possible to hard-code the system, 

#For a diagram of the overall design, check out this link:
#https://drive.google.com/file/d/1SY5mLkqdEXX0b6QFNpmRfYuoAh7tHsK6/view?usp=sharing

#Function is described in the README.md

class Mission:                                              #A Mission class to track the game progress in chunks. There will be between 3-5 of these.
    def __init__(self, missionnumber, players = None, votes = None, outcome = None, prediction = None):
        self.votes = votes
        self.players = []                                   #In this case, Mission.playes represents the team. :3 Game.players is all the players.  My bad, dog.  Will refactor when switch software
        self.number = missionnumber
        self.proposedTeams = []
        self.outcome = None                                 #Notice the type  changes between instantiation and assignment.  A big no-no in Java
        self.attemptsToMakeTeam = 1                         #Start this at index 1 because the first mission doesn't say what attempt


    def getOutcome():
        return self.outcome

    def approvedTeam(self, team, votes):
        self.players = team
        self.votes = votes

    def rejectedTeam(self, team, votes):
        self.attemptsToMakeTeam += 1
        self.proposedTeams.append([team, votes])

    def passed(self):
        self.outcome = 1
        Game.successmissions += 1
        Game.missionResults[Game.currentmission] = 1
        
    def failed(self):
        self.outcome = 0
        Game.failmissions += 1
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
        #and [1,0,0,0,0,0,0,0,0,0] would be "Max approved!  Emmett, Amanda, Janet, Ethan, Alex, JC, Wilson [...] rejected!"

        #A slightly harder problem would be to link this up with analysis.py and note which players earned SusPoints 
        return None

    def missionFinalAnalysisReturn(self):
        #Return what is to be written to file
        if self.outcome == None:
            return None
        metadata = [self.outcome, list(self.players), list(self.votes), self.attemptsToMakeTeam, list(self.proposedTeams)]
        print(metadata)
        return metadata

    def __str__(self):
        print("number:outcome, players, votes, failedvotes")
        return None

class Player:                                               #The Player object.  Stores player metadata and name.
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.spyprobability = 44
        self.suslevel = 0
        self.missions = []
        self.votingPattern = []                             #Note which teams Player approved and which team player rejected
        self.fullVoteAnalysis = []                          
        self.missionParticipation = []
        self.spy = 1

    def setname(self,name):
        self.name = name
    
    def recordIntel(self, intel):
        self.fullVoteAnalysis.append(intel)
      
    def wasSpy():
        self.spy = 0
    
    def recordPlayerAction(sus):
        return None
    
    def getname(self):
        return self.name
    
    def getnumber(self):
        return self.number

    def investigate(self):
        #Print suslevel, along with actions from the entire game
        return None

    def playerFinalAnalysisReturn():    #Format [0/1 spy/resistance, [participated missions], [mission outcomes], [fullvote analysis]]
        #Return what is to be written to file
        return [self.spy, self.missions, self.fullVoteAnalysis]

    def __str__():
        print(self.name)
        return self.name
        
class Game:                                                 #The Mainframe; Much of the data is stored in here.
    #Problem 2
    #TODO when does the game end?
    players = []                                                #Remember to reference this as Game.players
    playerCount = None
    currentmission = 1                                          #Reference this as Game.getCurrentMission(). Remember what abstraction is?
    missionsRejectedTeams = [[], [], [], [], []]
    missionResults = [None, None, None, None, None]             #A tad inefficient, but it's useful later on.
    missions = [None, None, None, None, None]
    teamSize = [3, 4, 4, 5, 5]                                  #For later use, with 5-9 players option.  Later on, we'll fill this based on the input of how many players
    successmissions = 0
    failmissions = 0
    captain = None
    legit = False
    spies = []
    winners = None
    
    def __init__(self):
        count = int(input("How many players? ")) 
        while count > 10 or count < 5:
            count = int(input("How many players?? Please input number between 5-10 ")) 
        Game.playerCount = count
        #assert number below 10
        af = str(input("Autofill players? yes or no? (All input must be in quotes for now)")) 
        if af == "no":
            name0 = str(input("What's your name? "))
            Game.players[0].setname(name0)
            name1 = str(input("Who's sitting to your left?"))
            Game.players[1].setname(name1)
            for i in range(2, count):
                name = input("Who's sitting to his/her left?")
                Game.players[i].setname(name)  
        else:
            for i in range(10):
                Game.players.append(Player("Player" + str(i), i))            
        realGame = input("Is this an actual game? Specify 'actual': ")    #Avoid accidentally training network with invalid games
        if realGame == "actual":
            Game.legit = True

        captain = input("Who's making the first team? Number please! ")
        Game.captain = captain
        #Assert number is between 0-9
        print(str(Game.players[captain].getname()) + " is making the first team! ")
        round()

    def getCurrentMission(self):
        return self.currentmission
    
    def finalGoogleReturn(endgame):
        return endgame
        
        
    #Also return the player objects of the spies
   
    def gameFinalAnalysisReturn():
        #Format:  [winningteam, [spies], total missions, [all missions], [all players], string date and game summary]
        #Return what is to be written to file
        finalAnalysisList = [Game.winners, Game.currentmission, Game.spies]                                  #Format [winningTeam, totalMissions, spies, Mission Analyses]  Possibly add date/game tag later
        for mission in Game.missions:
            if mission != None:
                finalAnalysisList.append(mission.missionFinalAnalysisReturn())
        return None




def nextMission():                                          #Little indexing helper function
    Game.missions[Game.currentmission].missionFinalAnalysisReturn()
    Game.currentmission += 1
    if Game.captain == 9:
            Game.captain += 1
    else:
        Game.captain = 0
    round()

def round():                                                #Tl;dr of data input for each mission
    #Problem 8: Some basic implementation! Implement a method of accounting for a double, or even triple fail on a mission.
    
    #Problem 3: Check inputs and display error without exiting program (Fix all the assert comments)
    #Bonus if you can get python to intake strings without user needing to add quotes.

    #Assert captain is the first person on the team
    #assert the team "leader" changed up by one
    #Assert game isn't over
    #assert no double players on the same team
    #check which mission reject this is
    #assert mission has right amount of people
    #assert right number of votes
    #assert the input is the right type.  (Hint: use type(x))
            

    shield = Game.currentmission                               #Mission index tracker to make code more readable
    print("\n")  #NewLine


    print("We are on Mission #" + str(shield) + " which needs a team of " + str(Game.teamSize[shield - 1]))
    print(str(Game.players[Game.captain].getname()) + " is making this team!")
    print("\n")  #NewLine
    print("\n")  #NewLine
    team = input("Who's on this team? (lump number)")
    team = toArray(team)
    print(str(Game.players[team[0]].getname()) + " made a team with "  + str([Game.players[p].getname() for p in team[1:]]))
   
   
    #Take in votes and players on the team
    votes = input("Votes? y or n in quotes: ")  #Track each player's vote for each team
    while len(votes) != Game.playerCount:
        votes = input("Votes? Please input the right number of votes.") 
    voteIndex = 0
    votes = list(votes)
    for p in votes:
        if p == 'y':
                votes[voteIndex] = 1
        elif p == 'n':
            votes[voteIndex] = 0
        else: 
            while votes[voteIndex] != 'y' and votes[voteIndex] != 'n':
                print("What did " + Game.players[voteIndex].getname() + " vote? Wrong input. ")
                votes[voteIndex] = input("'y' or 'n':")
            if votes[voteIndex] == 'y':
                votes[voteIndex] = 1
            elif votes[voteIndex] == 'n':
                votes[voteIndex] = 0
        voteIndex += 1   
    
    
    for i in Players:
        analyze(i)
        print(str(i.name) +"'s sus-level is " + str(p.suslevel)) 

      #Begin the Mission and index the Game class's trackers. 
    if Game.missions[Game.currentmission] == None:
        roundMission = Mission(Game.currentmission)
        Game.missions[Game.currentmission] = roundMission
    else:
        roundMission = Game.missions[Game.currentmission]



    #Here's the tricky part. Let's see if we can write each mission's result to the Mission class
    #but also each player. (For later analysis) 
    #Instead of analysing the whole game, it would be more efficient to analyze players one by one
    #Instead of writing the entire game to file, let's try writing a player's profile and end loyalty
    
    def NSA(activeteam, outcome):                    #Record ALL the actions!!
        for p in activeteam:
            recordAction(p, outcome)
        return None

    def recordAction(playernumber, outcome):         #Document a player's decisions this round.
            #[playerVote, mission, [team, team, team, team, team], [otherVotes], missionOutcome]
                                            #[0/1, mission,[1, 2, 3, 4, 5], ['0','1','1,'1,'1...], -1/0/1] (-1 if the team is rejected)
        Game.players[playernumber].recordIntel([votes[playernumber], shield, team, votes, outcome])
        print("Record action" + str([votes[playernumber], shield, team, votes, outcome]))

    def recordToGame(missionNumber, teamAndVotes):         #Note what's going on for the round's Mission object
        missionsRejectedTeams[missionNumber].append(teamAndVotes)
        print("recorded to game")
        print(teamAndVotes)

    
    #Now we continue with the actual game
    votetotal = passorfail(votes) 
    if roundMission.attemptsToMakeTeam >= 4:
        print("\n")  #NewLine
        print("Team goes automatically!")
        votetotal = 10

    if votetotal > 5:
        #Save the mission result and update all the stuffs
        missionresult = input("Pass or fail? 0 or 1?")
        if missionresult != 0 and missionresult != 1:
            missionresult = input("Pass or fail? 0 or 1? Please put in a legit response >:c")

        roundMission.approvedTeam(team, votes)
        Game.missionResults[shield] = missionresult
        

        if missionresult == 0:
            roundMission.failed()
        elif missionresult == 1:
            roundMission.passed()
            
        NSA(team, outcome)
        recordToGame(shield, [team, votes])
        
        if Game.successmissions >= 3 or Game.failmissions >= 3:
            gameEnd()
            return None

        nextMission()
    else:
        print("Vote failed.  Make new team.")   
        print("\n")  #NewLine
        print("\n")  #NewLine
        print("This is vote attempt #" + str(Game.missions[shield].attemptsToMakeTeam + 1))
        roundMission.rejectedTeam(team, votes)
        round()



#Helper functions. Most of these are in progress.  
def passorfail(v):
    total = sum(v)
    print(str(total) + " approves and " + str(10-total) + " rejects")
    return total

#Change this to an individual analyze. 
"""
def analyze():
    print("Knowledge is power! ")
    print("\n")  #NewLine
    pause = input("Would you like to analyze the game? yes/no? ")
    print("\n")  #NewLine

    if str(pause) == "yes": 
        print("too bad. You're going to lose anyways. ;)")
        #Actually open menu of players or missions to analyze, or an option to review  the whole game
    else:
        print("Very well.  It's your funeral.")
    print("\n")  #NewLine
    return None
"""

def gameEnd():
    #Problem 5:    
    #Write results and data to a file
    #print everything for review
    #I'll probably do this one myself but feel free if you want to learn stuff
    #Also, think of how to design the file so it  can be read and analyzed later!
    if Game.successmissions >= 3:
        Game.winners = 1
        print("Resistance wins!")
        print("\n")
        print("Hide yo merlin!")
    elif Game.failmissions >= 3:
        Game.winners = 0
        print("Spies win!")
        print("\n")
        print("dumpstered.")
    else:
        print("not sure if trolling.....")
    print("\n")  #NewLine
    spy = input("Who were the spies? (Lump number)")
    Game.spies = toArray(spy)
    for s in Game.spies:
        Game.players[s].wasSpy()      
    print(Game.missionsRejectedTeams)
    writeToFile()
    return None


def toArray(x):
    result = []
    votecount = len(str(x))
    while votecount > 0:
        result.append(x % 10)
        x = x // 10
        votecount -= 1
    return list(reversed(result))

#Some fun user options. Also in progress

def last_hope(): #Analysis option. Call this iff it's the 5th mission. Will return a detailed game analysis which will point out the spies
    return "rip"

def uniqueList(team):       
    #Problem 9(?) Helper function! Use this to make sure that no player is listed as being on a team twice. 
    #>>> uniqueList([3, 4, 5, 4])
    #False
    #>>> uniqueList([2, 9, 3, 4])
    #True

    #Later on, we'll do  
    #if not uniqueList(proposedTeam):  
    #      print("Please make a valid team!")
    return None

def recognize(play):
    #Problem 4:  I expect you all to try something for this. :) Check out analysis.py.
    #Will recognize and return classic plays
    #using the anaylsis that YOU wrote and pushed into the repo ^-^
    return None 

def status():
    print("Everything that's happened so far in an orderly and readable format")
    return None

def investigate(player):
    print("Table of each player and their likelyhood of being a spy")

def writeToFile():
    #Write the entire game to the rtf file for later analysis
    if Game.legit:
        #Save all 10 player profiles, with player loyalty and full action log
        #Save entire game record with spies tagged
        return None
    else:
        return None


play = Game()

#Problem 6: Create a GUI 
#Never done this kind of thing myself and ain't nobody got time for that

#Problem 7: Learn how to create a neural network using TensorFlow! 
#I'm working on this too. This is a really interesting challenge if you're interested!


#How to tell if someone's a spy:
#Mission fails
#votes
#votes on mission passes/fails
