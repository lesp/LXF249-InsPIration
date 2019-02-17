from googlesearch import search
from random import choice
import webbrowser


print("Tell me three things that you would like in a project")
things = []
suggestion = []

for i in range(3):
    things.append(input("READY >>> "))

inspiration = str(things[0]+" "+things[1]+" "+things[2])
print(inspiration) #Debug
print("Hey I found these that might be of interest, I'll open one at random too")

for item in search(inspiration, tld="co.uk", num=3, stop=1, pause=2):
    print(item)
    suggestion.append(item)

webbrowser.open(choice(suggestion))
