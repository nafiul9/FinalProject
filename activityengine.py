#!/usr/bin/env python3

import sys
import re
import pickle
import quitgame


# Saves a greeting for use later
#greeting = print("WELCOME TO--*ahem*--welcome to the game. What did you do, today?")

# Gets whatever the user did that day as input.


# Generates an empty list to be populated by the user's activities
#activitydict = {"walk" : 5}


def main():

	# Links categories and related activities
	activitydict = {"fitness" : {"walk" : 5, "run" : 10}, "intellect" : {}, "intellect" : {}, "happiness" : {}}

	# Aggregates experience by category
	expdict = {"fitness" : 0, "intellect" : 0, "naturalism": 0, "happiness" : 0}

	optionlist = {
	"New Game" : getactivities(),
	"Quit Game" : quitsave(),
	}

	print("Hi, and welcome!  What would you like to do first? (You can do these things: ")

	newinput = input("")


	def getactivities():
		greeting = print("What did you do, today?")
		activity = input("")
		count = 0
		
		# Determines whether or not the activity has been done before
		for category in activitydict.keys():
			if activity in activitydict[category]:
				count += 1
				print("You've done that one before!")
				current = activitydict[category][activity]
				print("{0} experience points have been added to {1}!".format(current, category))
				expdict[category] += current
		
		# Indicates that the activity hasn't been done before
		if count == 0:
			while True:
				
				# Assigns a quantity of experience points to your activity
				print("That's a new one--how many experience points is it worth?  (Give a number between 1 and 50!)")
				activityexp = input("")
				try:
				    activityexpint = int(activityexp)
				    break
				except ValueError:
				    print("Could not convert data to an integer.")
				activitydict[activity.lower()] = activityexp
			for category in expdict.keys():
				print(category.title())
			while True:

				# Assigns a category to the activity for future use
				print("To which category should I assign that exp?  You can assign it to any of the above categories:\n")
				catchoice = input("")
				if catchoice.lower() in expdict.keys():
					expdict[catchoice] += activityexpint
					print("{0} exp added to {1}!".format(activityexp, catchoice))
					break
				else:
					print("Ooops--that one didn't register.  Try entering it again!")



if __name__ == "__main__":
	main()