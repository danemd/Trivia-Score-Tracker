#! python3
# triviaScorer.py - Keeps track of users trivia scores and shows team standings

teams = {}

#Creates a key for every team with a default value(score) of zero
for i in range (20):
    teamIn = input("Enter team name (blank to continue).")
    if teamIn == '':
        break
    teams[teamIn] = 0

#Identifies number of rounds to be played
numRounds = input("How many rounds of questions?")
numRounds = int(numRounds)

#function for tallying up points per round. 
import collections
import operator
def pointTally(team, rounds):
    for i in range(rounds):
        #Allows for latecomers to jump into game after each round
        while True:
            newTeam = input('Enter new team (blank to continue).')
            if newTeam == '':
                break
            team[newTeam] = 0
        for key in teams:
            roundScore = (input("How many points did " + \
                                    str(key) + " score in Round " \
                                    + str(i + 1) + "?"))
            #If anything other than a point value is entered it will keep
            #prompting for a number
            while roundScore.isalpha():
                roundScore = (input('Please enter in a number for ' \
                                        + str(key) + "'s points."))
            if roundScore.isdecimal():
                roundScore = int(roundScore)
                teams[key] = teams[key] + roundScore
        sorted_team = sorted(team.items(), key=lambda kv: kv[1])    
        sorted_dict = collections.OrderedDict(sorted_team)
        print("\n" + "The scores for Round " + str(i + 1) + " are:" + "\n")
        for k, d in sorted_dict.items():
            print(k + ":", d)
        print("\n")
pointTally(teams, numRounds)
