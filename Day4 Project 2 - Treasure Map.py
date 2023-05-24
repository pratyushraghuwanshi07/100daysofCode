# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
pos_list = list(position)
column  = int(pos_list[0])
row = int(pos_list[1])
if column == 1:
    map[row-1][0] = "X"
elif column == 2:
    map[row-1][1] = "X"
elif column == 3:
    map[row-1][2] = "X"
else:
    pass



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

