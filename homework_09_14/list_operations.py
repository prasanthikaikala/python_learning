"""
games=["football","coco","basketball"]
1. add "vollyball" at the end
2. find the position of "coco"
3. insert "cricket" at position 2
4. find length of the list
5. get the index of cricket
6. append "cricket" agin
7. do pop operation
8. remove "football"
9. remove item at location 1
10. extend list_b=["table tennis","carroms","chess"]
"""

games=["football","coco","basketball"]

#1. add "vollyball" at the end

games.append("vollyball")
print(games)

#2. find the position of "coco"

print('Index of coco = ', (games.index("coco")))

#3. insert "cricket" at position 2

games.insert(2, "cricket")

print('Games after inserting cricket:',games)

#4. find length of the list

print('Length of the games list: ', len(games))

#5. get the index of cricket

print('Index of cricket = ', (games.index("cricket")))

#6. append "cricket" agin

games.append("cricket")

#7. do pop operation

x1=games.pop()
print('Games list after pop: ', games)

#8. remove "football"

games.remove("football")
print('Games after removing football:',games)

#9. remove item at location 1
games.pop(1)

print('Games list after removing item at 1: ', games)

#10. extend list_b=["table tennis","carroms","chess"]

list_b=["table tennis","carroms","chess"]

games.extend(list_b)

print('Games list after extending with list_b:', games)


