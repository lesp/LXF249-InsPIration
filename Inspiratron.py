from googlesearch import search
from random import choice
import webbrowser
import easygui as eg

eg.msgbox(msg="Tell me what you would like in a project and I shall search Google for you. This will trigger 3 pop up windows", title="InPIration", ok_button="Inspire Me!")
things = []
suggestion = []

for i in range(3):
    things.append(eg.enterbox(msg="READY >>> "))

inspiration = str(things[0]+" "+things[1]+" "+things[2])
print(inspiration) #Debug

for item in search(inspiration, tld="co.uk", num=3, stop=1, pause=2):
    print(item)
    suggestion.append(item)

for i in range(len(suggestion)):
    links = "\n".join(suggestion[0:])
    
eg.textbox(msg="Hey I found these that might be of interest, I'll open one at random after you close this message", text=links)
    
webbrowser.open(choice(suggestion))
