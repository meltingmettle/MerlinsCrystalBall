
"""
Have a few minutes of free time, so writing out some goals and concepts.

Some of these situations are pretty tricky, because players will sometimes act contrary to their own short-term interests in favor 
of a further goal. 

(IE approving a double spy mission to identify spies)
(Merlin making a faulty team to hide his identity as Merlin vs. Morgana making a faulty team to win for the spies)
(Also, note that Merlin must include another spy, while Morgana will probably make herself the only spy)

There will be some retroactive analysis based on training data, but also some predictive computation.
Hopefully, this program will eventually mimic what a player reasons and thinks, plus discernment of hidden patterns, and with better memory than your average student.

Note that, in the short term, this is indistinguishable from approving a faulty mission to fail and win a round for the spy team.


Scenarios to identify, in somewhat increasing order of difficulty:
  1. When a particular player is likely the culprit of a failed mission
  2. When a spy passes a mission to hide his/her identity 
  3. When two or more players have a sudden "change in behavior" from new information
  4. When two or more players are acting similarly
  5. When two or more players are favoring each other
  6. When a player seems to know most of the identities in the game
  7. When a player is likely to be Merlin. (Extremely difficult to discern from a spy, except that he acts alone.
     (Note that, like a spy, Merlin knows everything and is trying to hide his identity)
  
Long story short, discerning the long - term behavioral pattern of spies against the pattern of the loyal servants.

"""



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
