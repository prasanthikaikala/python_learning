cricket_players={"ravi","raghu","hari","sushma"}
football_players = {"Harish","suresh","ramesh","raghu","sushma"}
tt_players = {"suresh","ramesh","hari","sushma"}

#all players
res1= cricket_players.union(football_players)
res2= res1.union(tt_players)
print(res2)
result = cricket_players.union(football_players).union(tt_players)
print(result)
#players play all games
result1 = cricket_players.intersection(football_players).intersection(tt_players)
print(result1)
#players play crikcet & football
result2=cricket_players.intersection(football_players)
print("players play crikcet & football:",result2)

#players play cricket & tt
result3=cricket_players.intersection(tt_players)
print("players play crikcet & tt:",result3)
#Players play tt & football
result4=tt_players.intersection(football_players)
print("players play tt & football:",result4)
#players play crikcet but not football
result5=cricket_players-football_players
print("players play crikcet but not football:",result5)
#players play tt but not crikcet
result6=tt_players-cricket_players
print("players play tt but not cricket:",result6)
#players play football but not tt
result7=football_players-tt_players
print("players play football but not tt:",result7)
