import random
import time
import os

		

def mainMenu():
	print("Pick your mode")
	print("[1] EASY")
	print("[2] MEDIUM")
	print("[3] HARD")
	print("[0] EXIT")
	mode= int(input("Mode:"))
	return mode


def easyMenu():
	easyChoice=0
	print("="*50)
	print(" ")
	print("EASY MODE")
	print(" " * 30)
	# print scores
		# easyScoresFile = open("easyRanks", "r")
	try:
		with open("easyRanks", "r") as easyScoresFile:
			print("**HIGH SCORES**")
			print(" " * 30)
			for line in easyScoresFile:
				line = line[:-1].split(",")
				print(line[0], "Name: ", line[1], "Last Pattern: ", line[2], "Score: " , line[3])
				# easyScoresFile.close()
	except:
		print("DO YOUR BEST!!")
	print(" " * 30)
	print("="*50)
	print("[1] START")
	print("[2] EXIT")
	print("="*50)
	easyChoice= int(input("Enter choice:"))
	return easyChoice


def easy(word):


	playerStuffs=[]
	count=1
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
		print("="*50)
		print("RECALL THE PATTERN!!")
		print("="*50)
		print(" ")
		playerGuess= input("WHAT IS THE PATTERN:").lower()
		os.system("clear")

		if playerGuess==letters:
			print("="*50)
			print(30 * " ")
			print ("YOU GUESS RIGHT!! KEEP GOING!!")
			playerScore+=10
			wordsGuess.append(pattern)
			print("YOUR SCORE IS:" + str(playerScore)+ "!!!")
			print(" ")
			print("="*50)

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
				print("="*50)
				print("AWW YOU ARE WRONG!!")
				print("="*50)
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
	easyScoresList = []
	easyScoresFile= open("easyRanks", "r")
	lines = easyScoresFile.readlines() #list nung mga lines sa file
	stripped_lines = []
	for line in lines:
		stripped_line = line.strip() #forda tanggal ng "/n"
		stripped_lines.append(stripped_line)
	for line in stripped_lines:
		rankList = line.split(",")
		if rankList[1] != "-1-" and rankList[1] != "-2-" and rankList[1] != "-3-":
			easyScoresList.append(rankList)
	return easyScoresList

#easyDict={'RANK 1': ["-1-", " ", 0 , " "], 'RANK 2' : ["-2-", " ", 0 , " "], 'RANK 3': ["-3-", " ", 0 , " "]}

def easyRanking(scoreAndlastword): 		#nagrereceive ng list [score, lastword na naguess]																

	easyScoresList = None
	try:
		easyScoresFile= open("easyRanks", "r")
		easyScoresList = readFileIntoList() #tinatawag si readFileIntoList
		#print(f"filler: {easyScoresList}")
	except:
		easyScoresList = []
		print("WOW!YOU ARE AMAZING!!!!")
		print("")
		print("")
		print("="*50)

	easyDict={'RANK 1': ["-1-", " ", 0 ], 'RANK 2' : ["-2-", " ",0], 'RANK 3': ["-3-", " ",0]}

	# # create and write
	easyScoresFile= open("easyRanks", "w")
	for k,v in easyDict.items():
		easyScoresFile.write(k+ "," + v[0] + "," + v[1] + ","+ str(v[2])  + "\n")
	easyScoresFile.close()

	
	with open('easyRanks', 'r') as easyRanks:
		lines= easyRanks.readlines()

	for line in lines:
		data= line[:-1].split(",")
		ndata= int(data[3])
		if ndata > scoreAndlastword[1]:
			easyScoresList.append(data)
			
		elif ndata < scoreAndlastword[1]:
			print("="*50)
			print(" ")
			print('YOU SCORE HIGH!!!')
			print(" ")
			print("="*50)
			data[3]=scoreAndlastword[1] #score
			data[1]= input("ENTER YOUR NAME:") #name

			data[2]=scoreAndlastword[0] #last wword
			ndata= scoreAndlastword[1]
			easyScoresList.append(data)
			os.system("clear")
			break
		else:
			easyScoresList.append(data)

	easyScoresFile.close()


	for i in range(len(easyScoresList)):  #gagawing integer si score na nasa index 3 kase string pa sya currently sa list
		easyScoresList[i][3] = int(easyScoresList[i][3])

	easyScoresList = bubbleSort(easyScoresList) #forda sorting
	for i in range(len(easyScoresList)): #forda overwrite sa list
		easyScoresList[i][0] = "RANK " + str(i + 1)  

	easyScoresFile= open("easyRanks", "w")
	if len(easyScoresList) > 3:
		iterator = 3
	else:
		iterator = len(easyScoresList)

	for i in range(iterator):
		easyDict[easyScoresList[i][0]]= easyScoresList[i][1], easyScoresList[i][2],easyScoresList[i][3] #forda tiga lagay ng 3 item lists sa list


	for k,v in easyDict.items():
		easyScoresFile.write(k+ "," + str(v[0]) + "," + str(v[1]) + ","+ str(v[2])  + "\n")
	#print(easyDict)
	
	easyScoresFile.close()




	

