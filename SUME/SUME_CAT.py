#This is the have all of the functions that will work with each category.
#fucntions that will open and work with the allCats_SUME.txt file that stores all of the categories 
#for each category function i think i will just use linear functions with slope of 1, easy to work with 


#category checker, takes functions and coordinates as parameters to return true or false if coordinates fit into cat
#function will have to be plugged in as slope and y-intercept
#y must always be greater than x since the slope will be positive
def catCheck(yInt, x, y):
    if(y == (x + yInt)):
        return True
    else:
        return False

#jiachen, define a function  that will check which category it belongs to
#the above function is used more to check if it fits into the category itself
#but it has not much use

def whichCat(x, y):
    catList = open("allCats_SUME.txt", "r")
    line = catList.readlines()
    return line[y-x]
#work with the line in the txt file that catIndex has
#this line would be the index that has all of the coordinates of the same category

            
#defined a function that will take the coordinates of the item to the user's file
def addToUser(userFile, itemFile):
    user = open(userFile, 'a')
    item = open(itemFile, 'r')
    for line in item:
        user.write(line)
        #boom in 5 min i am now, tech billionare


addToUser('baseUserFile.txt', 'dataCatFile.txt')
