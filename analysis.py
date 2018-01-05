#Hello!

#In the long run, MCB will use TensorFlow to observe and predict behavioral patterns of spies using player metadata from past games.
#By comparing a player's activity to old profiles of both spies and loyal servants of King Arthur, the algorithm will identify spies by the third mission.

#More challenging is the implementation of a social algorithm, which also considers how players objectively interact to identify the four spies faster 
#and more accurately.
#As of now, MCB is in the training stage. 


#Currently, this program uses a primitive system known as Suslevel™.  
#As the program tracks plays, players will be given SusPoints™ for suspicious behavior which has been previously identified
#I expect all of my direct students to create an analysis file. I'm going to weave them all together and see what happens.  
#If you don't, I'm going to be disappoint. 

#Some examples:
def probablyGood(player, Mission):
  if Mission.outcome == 1 and 1 < Mission.number < 4:  #If the second or third mission passes, the players are kind of sorta likely to be good
      for i in len(Mission.players):
        Mission.players[i].suslevel -= 2:              #Decrease SusLevel accordingly
    
def badApprove(player, Mission):
  if player_approvedmission() and missionOutcome == 0:  #If the player approved the mission and it failed
      player.suslevel += 1
      if player not in Mission.Team and Mission.count != 4:  #If the player approved without being on the mission.  
          player.suslevel +=1
  if Mission.captain == player.getnumber():         #A tad more suspicious if the player in question made the team
      player.suslevel += 2

#And so on and so forth.  After missions are run, analysis functions will study players and log their actions for future reference.
#
