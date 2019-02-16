import json
from difflib import get_close_matches

# load data from json file
data = json.load(open('data.json'))

# function which will provide information
def translate(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        print("Did you mean %s instead? " %
              get_close_matches(w, data.keys())[0])
        ans = input('Enter y or n:')
        if ans.lower() == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "did not find that word"
    else:
        return "The word doesn't exist. please double check it."


# input from user
word = input('Enter Word: ')

output = translate(word.lower())
if type(output) == list:
    for item in output:
        print("-> " + item)
else:
    print(output)
