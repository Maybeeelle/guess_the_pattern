import random
import time
import os

		

def mainMenu():
	print("Pick your mode")
	print("[1] HARD")
	print("[2] MEDIUM")
	print("[3] HARD")
	print("[0] EXIT")
	mode= int(input("Mode:"))
	return mode


def hardMenu():
	hardChoice=0
	print("===========================================")
	print("===HARD MODE===")
	print(" " * 30)
	# print scores
		# hardScoresFile = open("hardRanks", "r")
	try:
		with open("hardRanks", "r") as hardScoresFile:
			print("HIGH SCORES")
			print(" " * 30)
			for line in hardScoresFile:
				line = line[:-1].split(",")
				print(line[0], "Name: ", line[1], "Last Pattern: ", line[2], "Score: " , line[3])
				# hardScoresFile.close()
	except:
		print("===DO YOUR BEST!!===")
	print(" " * 30)
	print("===========================================")
	print("[1] START")
	print("[2] EXIT")
	print("===========================================")
	hardChoice= int(input("Enter choice:"))
	return hardChoice


def hard(word):


	playerStuffs=[]
	count=3
	wordsGuess=[]		
	playerScore=0
	guess= True
	while guess== True:
		print("==GUESS THE PATTERN!!==")
		letters=""
		pattern=""
		count+=1
		for i in range(count):
			target= random.randint(0,(len(word)-1))
			letters= letters+word[target]
			pattern+=word[target]+ " "
		print(pattern, end=" ")
		#print(pattern)
		print("")
		t=1.00
		tdeduc=0.0099999
		print("Memorize in...")
		for i in range(1,6):
			print(str(i) ,"...")
			time.sleep(t)
			t=t-tdeduc
			tdeduc-=0.099999999

		os.system('clear')

		print("RECALL THE PATTERN!!")
		playerGuess= input("WHAT IS THE PATTERN:").lower()

		if playerGuess==letters:
			print("===========================================")
			print(30 * " ")
			print ("YOU GUESS RIGHT!! KEEP GOING!!")
			playerScore+=20
			wordsGuess.append(pattern)
			print("========YOUR SCORE IS:" + str(playerScore)+"=======")
			print(" ")
			print("===========================================")

		else:

			#print(wordsGuess)
			if len(wordsGuess)==0:
				print("AWW WRONGGG!!")
				playerStuffs.append("")
				playerStuffs.append(0)
				time.sleep(2)
				os.system('clear')
				guess=False

			else:
				index=len(wordsGuess)
				lastGuess=wordsGuess[index-1]
				playerStuffs.append(lastGuess)
				print("===========================================")
				print("AWW YOU ARE WRONG!!")
				print("===========================================")
				print("THE CORRECT PATTERN IS: " + pattern)
				print(" ")
				print("YOUR LAST GUESS IS " + lastGuess)
				print(" " * 30)
				print("YOUR SCORE IS: " + str(playerScore))
				playerStuffs.append(playerScore)
				time.sleep(3)
				os.system('clear')
				guess=False


	return playerStuffs


# [[Rank 1, name, last guess, score],[Rank 1, name, last guess, score]]

def bubbleSort(rankList):
	counter = -1
	while counter != 0:
		counter = 0
		for i in range(len(rankList) - 1):
			if rankList[i][3] < rankList[i + 1][3]:
				temp = rankList[i]
				rankList[i] = rankList[i + 1]
				rankList[i + 1] = temp
				counter += 1
	return rankList

def readFileIntoList():
	hardScoresList = []
	hardScoresFile= open("hardRanks", "r")
	lines = hardScoresFile.readlines() #list nung mga lines sa file
	stripped_lines = []
	for line in lines:
		stripped_line = line.strip() #forda tanggal ng "/n"
		stripped_lines.append(stripped_line)
	for line in stripped_lines:
		rankList = line.split(",")
		if rankList[1] != "-1-" and rankList[1] != "-2-" and rankList[1] != "-3-":
			hardScoresList.append(rankList)
	return hardScoresList

#hardDict={'RANK 1': ["-1-", " ", 0 , " "], 'RANK 2' : ["-2-", " ", 0 , " "], 'RANK 3': ["-3-", " ", 0 , " "]}

def hardRanking(scoreAndlastword): 		#nagrereceive ng list [score, lastword na naguess]																

	hardScoresList = None
	try:
		hardScoresFile= open("hardRanks", "r")
		hardScoresList = readFileIntoList()
		#print(f"filler: {hardScoresList}")
	except:
		hardScoresList = []
		print("WOW!YOU ARE AMAZING!!!!")
		print("")
		print("")
		print("================================")

	hardDict={'RANK 1': ["-1-", " ", 0 ], 'RANK 2' : ["-2-", " ",0], 'RANK 3': ["-3-", " ",0]}

	# # create and write
	hardScoresFile= open("hardRanks", "w")
	for k,v in hardDict.items():
		hardScoresFile.write(k+ "," + v[0] + "," + v[1] + ","+ str(v[2])  + "\n")
	hardScoresFile.close()

	
	with open('hardRanks', 'r') as hardRanks:
		lines= hardRanks.readlines()

	for line in lines:
		data= line[:-1].split(",")
		ndata= int(data[3])
		if ndata > scoreAndlastword[1]:
			hardScoresList.append(data)
			
		elif ndata < scoreAndlastword[1]:
			print('YOU SCORE HIGH!!!')
			print(" ")
			print(scoreAndlastword)
			data[3]=scoreAndlastword[1] #score
			data[1]= input("ENTER YOUR NAME:") #name

			data[2]=scoreAndlastword[0] #last wword
			ndata= scoreAndlastword[1]
			hardScoresList.append(data)
			break
		else:
			hardScoresList.append(data)

	hardScoresFile.close()


	for i in range(len(hardScoresList)):  #gagawing integer si score na nasa index 3 kase string pa sya currently sa list
		hardScoresList[i][3] = int(hardScoresList[i][3])

	hardScoresList = bubbleSort(hardScoresList) #forda sorting
	for i in range(len(hardScoresList)): #forda overwrite sa list
		hardScoresList[i][0] = "RANK " + str(i + 1)  

	hardScoresFile= open("hardRanks", "w")
	if len(hardScoresList) > 3:
		iterator = 3
	else:
		iterator = len(hardScoresList)

	for i in range(iterator):
		hardDict[hardScoresList[i][0]]= hardScoresList[i][1], hardScoresList[i][2],hardScoresList[i][3] #forda tiga lagay ng 3 item lists sa list


	for k,v in hardDict.items():
		hardScoresFile.write(k+ "," + str(v[0]) + "," + str(v[1]) + ","+ str(v[2])  + "\n")
	#print(hardDict)
	
	hardScoresFile.close()
