#In a game based on social deduction,  visual cues, deception, and unpredictability,  can a minions intent be revealed by careful objective analysis?
#
#In the long run, MCB will use TensorFlow to observe and predict behavioral patterns of spies using player metadata from past games.
#Currently, this program uses a primitive system known as Suslevel™.  
#As the program tracks plays, players will be given SusPoints™ for suspicious behavior which has been previously identified
#

def badApprove(player, Mission):
  if player_approvedmission() and missionOutcome == 0:  #If the player approved the mission and it failed
      player.suslevel += 1
      if player not in Mission.Team and Mission.count != 4:  #If the player approved without being on the mission.  
          player.suslevel +=1
  if Mission.captain == player.getnumber():         #A tad more suspicious if the player in question made the team
      player.suslevel += 2

#And so on and so forth.  After missions are run, analysis functions will study players and log their actions for future reference.
#
