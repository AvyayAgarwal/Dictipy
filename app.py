import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif(word.upper() in data):
		return data[word.upper()]
	elif (len(get_close_matches(word, data.keys())) > 0):
		print("Did you rather mean any of the follwing? Enter the number [1 - 3] corresponding to your choice.")
		for x in range(0, 3):
			print(str(x+1) + " - " + str(get_close_matches(word, data.keys())[x]))
		response = input("Response - ")
		response = response - 1
		if (response in range(0, 3)):
			return data[get_close_matches(word, data.keys())[response]]
		else:
			return "Non-existent word. Please check your input"
	else:
		return "Non-existent word. Please check your input"

word = input("Enter word: ")

result = translate(word)

if type(result) == str:
	print(result)
else:
	for i in result:
		print(i)