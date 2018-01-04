# Merlin's Crystal Ball
A calculator for the popular social deduction game Avalon.  Input mission teams, player votes on key missions, and mission outcomes, and recieve a dynamic probability assesment of which players are malicious Minions of Mordred.

In a game based on social deduction,  visual cues, deception, and unpredictability,  can a minions intent be revealed by careful objective analysis?


An open source project with Tensorflow and supervised learning! The objective of this program is to help the Resistance win the 5th mission by analyzing the game and predicting the spies among the Loyal Servants of King Arthur. 

Thanks to a larger percentage of Camelot GDP being devoted to R&D, His Majesty King Arthur's elite Praetorian Guard has developed a means of detecting and predicting spies, thus claiming victory for the forces of light and avoiding attempts on  Merlin's life.

If you are unfamiliar with the game, linked below are the game and its instruction manual. 

http://upload.snakesandlattes.com/rules/r/ResistanceAvalon.pdf.

https://www.amazon.com/Resistance-Avalon-Social-Deduction-Game/dp/B009SAAV0C 

10 Player compatibility only.  For now, votes on propsed teams that don't pass are ignored, although they are a key part of the game.   
Right now I'm adding snippet "plays" which can be taken into account, and adding objects for players, teams, and missions. Working on adding Troll-compensators and a a Percival portal. 


With a neural network in progress, we are using a primitive means of analysis to discern patterns and predict future activity.
Currently, analysis is performed via SusPoint™.  Every time any player makes a suspicious action, their SusLevel™ increases. 
The current hypothesis is, by identifying enough plays, can we force spies to need to rack up an insurmountable number of points in order to claim victory?


# Framework is laid out as below:
  1. Each player is assigned a number 0-9, inclusive, with 0 being the user, 1 being the player directly to his/her left, etc.
  2. Votes will be a binary 0/1 system for reject/approve.  One voting round is documented as an array as such: 1100010101
  3. Mission Objects will consist of the players and return a boolean pass/fail, with both a prediction and an outcome.  
    3a. A mission input would be (players, with captain first):  input: 34982  output: Success, Prediction: Success.
     3b. If the prediction is incorrect, the program will refactor accordingly, namely, noting that there was likely a spy/no spy on the team. 


# Some example plays: (Mission Number:Outcome[0 for fail, 1 for sucess])

1:1 2:1 3:0  <- Possible Double Spy or Troll

1:0          <-N00b player or unanticipated spy disruption efforts

1:1 2:0      <- More or less a standard game.   Implies either mission one had a sleeper, or the new player was the spy.  Can be determined by voting pattern. 

One full mission would look like this. (Mission number and outcome, final team and vote patterns, and possibly a triple array of proposed teams and votes) 

1:1 [1, 2, 3] [1110010111] [[[7,8,9], [0100100011]], [[6,7,8], [0001011001]]]

2:_ [a, b, c] [xxxxxxxxxxx] [[[1, 2, 3, 5], [1101000000]]]

Missions, teams, and probability of minion-hood in development!
  
  

Please feel free to comment your favorite plays/determinators of a player's spy-ness below!
Also, pls ~~like, comment, and subscribe.~~ star, comment, and watch! 


-MeltingMettle
  
  
# Contributions needed:
Percival, more plays/player analysis methods, GUI, player number variation
  
