import easyFunctions
import os
import mediumFunctions
import hardFunctions


alphabet= "abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
ranks= ["RANK 1", "RANK 2" , "RANK 3"] 
mediumChar= "a11b22c33d4e5f6g7h8i9j0k1l2m34n4o5p6q7r3s24t5u7v9wx0y9z"
hardChar="a11@@@1b!!!!!22c$$$$33%%%%d4e^^^^5f6g&&&&7h8i****9j0k1l2m(((34n))4o5__p6++q7r3s24t5u7v9wx0y9z"



while True:
	mode= easyFunctions.mainMenu()
	os.system('clear')
	if mode == 1:
		choice= easyFunctions.easyMenu()
		if choice==1:
			os.system('clear')
			playerStuffs= easyFunctions.easy(alphabet) #nagrereturn ng list [last guess, score]
			easyFunctions.easyRanking(playerStuffs)
		else:
			os.system('clear')

	if mode == 2:
		choice= mediumFunctions.mediumMenu()
		if choice==1:
			os.system('clear')
			playerStuffs= mediumFunctions.medium(mediumChar)
			mediumFunctions.mediumRanking(playerStuffs)
		else:
			os.system('clear')

	if mode == 3:
		choice= hardFunctions.hardMenu()
		if choice==1:
			os.system('clear')
			playerStuffs= hardFunctions.hard(hardChar)
			hardFunctions.hardRanking(playerStuffs)
		else:
			os.system('clear')
	if mode ==0:
		break
