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


def mediumMenu():
	mediumChoice=0
	print("="*50)
	print(" ")
	print("MEDIUM MODE")
	print(" " * 30)
	# print scores
		# mediumScoresFile = open("mediumRanks", "r")
	try:
		with open("mediumRanks", "r") as mediumScoresFile:
			print("**HIGH SCORES**")
			print(" " * 30)
			for line in mediumScoresFile:
				line = line[:-1].split(",")
				print(line[0], "Name: ", line[1], "Last Pattern: ", line[2], "Score: " , line[3])
				# mediumScoresFile.close()
	except:
		print("DO YOUR BEST!!")
	print(" " * 30)
	print("="*50)
	print("[1] START")
	print("[2] EXIT")
	print("="*50)
	mediumChoice= int(input("Enter choice:"))
	return mediumChoice


def medium(word):


	playerStuffs=[]
	count=2
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
			playerScore+=15
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
				time.sleep(3)
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
	mediumScoresList = []
	mediumScoresFile= open("mediumRanks", "r")
	lines = mediumScoresFile.readlines() #list nung mga lines sa file
	stripped_lines = []
	for line in lines:
		stripped_line = line.strip() #forda tanggal ng "/n"
		stripped_lines.append(stripped_line)
	for line in stripped_lines:
		rankList = line.split(",")
		if rankList[1] != "-1-" and rankList[1] != "-2-" and rankList[1] != "-3-":
			mediumScoresList.append(rankList)
	return mediumScoresList

#mediumDict={'RANK 1': ["-1-", " ", 0 , " "], 'RANK 2' : ["-2-", " ", 0 , " "], 'RANK 3': ["-3-", " ", 0 , " "]}

def mediumRanking(scoreAndlastword): 		#nagrereceive ng list [score, lastword na naguess]																

	mediumScoresList = None
	try:
		mediumScoresFile= open("mediumRanks", "r")
		mediumScoresList = readFileIntoList()
		#print(f"filler: {mediumScoresList}")
	except:
		mediumScoresList = []
		print("WOW!YOU ARE AMAZING!!!!")
		print("")
		print("")
		print("="*50)

	mediumDict={'RANK 1': ["-1-", " ", 0 ], 'RANK 2' : ["-2-", " ",0], 'RANK 3': ["-3-", " ",0]}

	# # create and write
	mediumScoresFile= open("mediumRanks", "w")
	for k,v in mediumDict.items():
		mediumScoresFile.write(k+ "," + v[0] + "," + v[1] + ","+ str(v[2])  + "\n")
	mediumScoresFile.close()

	
	with open('mediumRanks', 'r') as mediumRanks:
		lines= mediumRanks.readlines()

	for line in lines:
		data= line[:-1].split(",")
		ndata= int(data[3])
		if ndata > scoreAndlastword[1]:
			mediumScoresList.append(data)
			
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
			mediumScoresList.append(data)
			os.system("clear")
			break
		else:
			mediumScoresList.append(data)

	mediumScoresFile.close()


	for i in range(len(mediumScoresList)):  #gagawing integer si score na nasa index 3 kase string pa sya currently sa list
		mediumScoresList[i][3] = int(mediumScoresList[i][3])

	mediumScoresList = bubbleSort(mediumScoresList) #forda sorting
	for i in range(len(mediumScoresList)): #forda overwrite sa list
		mediumScoresList[i][0] = "RANK " + str(i + 1)  

	mediumScoresFile= open("mediumRanks", "w")
	if len(mediumScoresList) > 3:
		iterator = 3
	else:
		iterator = len(mediumScoresList)

	for i in range(iterator):
		mediumDict[mediumScoresList[i][0]]= mediumScoresList[i][1], mediumScoresList[i][2],mediumScoresList[i][3] #forda tiga lagay ng 3 item lists sa list


	for k,v in mediumDict.items():
		mediumScoresFile.write(k+ "," + str(v[0]) + "," + str(v[1]) + ","+ str(v[2])  + "\n")
	#print(mediumDict)
	
	mediumScoresFile.close()