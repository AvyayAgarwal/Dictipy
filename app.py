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
		response = raw_input("Did you rather mean %s ?" % get_close_matches(word, data.keys())[0] + " Enter Y or N: ")
		response = response.lower()
		if (response == "y"):
			return data[get_close_matches(word, data.keys())[0]]
		elif (response == "n"):
			return "Non-existent word. Please check your input"
		else:
			return "Incorrect response"
	else:
		return "Non-existent word. Please check your input"

word = raw_input("Enter word: ")

result = translate(word)

if type(result) == str:
	print(result)
else:
	for i in result:
		print(i)