#test python program for an item guesser on SUME
import SUME_CAT as cat

print("Welcome to SUME")
print("")

#all this does is create/work with the user's file
#user's file should only contain the coordinates
name = input("Please enter username: ")
name = name + '.txt'
user = open(name)
