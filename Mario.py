#This program creates a half pyramid that takes the user input to get its height (the number of lines)
#This program is created by Ann

space = 0
hashtag = 0

height = int(input("Enter a number: "))
while height < 0 or height > 23:
    height = int(input("Enter a number: "))
for i in range (height, 0, -1): 
    space = i - 1
    hashtag = (height + 1) - space 
    print(space * ' ' + hashtag * "#")
