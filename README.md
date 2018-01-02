# Merlin'sCrystalBall
A calculator for the popular social deduction game Avalon.  Input mission teams, player votes on key missions, and mission outcomes, and recieve a dynamic probability assesment of which players are malicious Minions of Mordred.


An open source project with Tensorflow and supervised learning!

10 Player compatibility only.  For now, votes on propsed teams that don't pass are ignored, although they are a key part of the game. 

Right now I'm adding snippet "plays" which can be taken into account, and adding objects for players, teams, and missions. 

Working on adding Troll-compensators. 




Framework is laid out as below:
  Each player is assigned a number 0-9, inclusive, with 0 being the user, 1 being the player directly to his/her left, etc.
  Propsed teams
  Votes will be a binary 0/1 system for reject/approve.  (One voting round looks like: 1100010101
  Mission Objects will consist of the players and return a boolean pass/fail, with both a prediction and an outcome.  
    (So a missiobinput would be (players):  input: 34982  output: Success, Prediction: Success.
     If the prediction is incorrect, the program will refactor accordingly, namely, noting that there was likely a spy/no spy on
     the team. 
  
Please feel free to comment your favorite plays/determinators of a player's spy-ness below!
Also, pls ~~like, comment, and subscribe.~~ star, comment, and watch! 


-MeltingMettle
  
  
  
  
