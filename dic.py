import json
from difflib import get_close_matches
data = json.load(open("data.json",'r'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0 :
        yn = raw_input("did u mean %s instead ? if YES press y if no press no" % get_close_matches(word,data.keys(),n=1))
        if yn == "y":
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "word donot exist please double check it"
    else:
        return "word donot exist"
print("Enter the word :")
x = raw_input()

output = translate(x)

if type(output) == list
    for item in output:
        print(item)
else:
    print(output)


