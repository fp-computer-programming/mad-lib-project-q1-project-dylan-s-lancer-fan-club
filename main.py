#imports simple tools 
import time 
import random 
import math

#defins my say comand: a simple comand that lets me wait a secont before the next line airs to let the game feel beter 
def say (sean):
    time.sleep(1)
    print(str(sean))
    
#greets the player and explains the rules  
say("hello user,")
name = input("what is your name?:")
say(f"Thank you for playing my game {name}.")
say(f"The rules of the game are quite simple.")
say(f"I will ask you for a word like a number noun or verb.")
say(f"After I do so please give me a word that matches this description.")
say(f"I hope you are ready becuse we are about to start")

#asks the player for the words in the game
lone = input("adjective")
bob = input("name")
he = input(f"{bob}s pronuns ex:he/him")
pronouns = "/".split(he)
he = pronouns[0]
him = pronouns[1]
decided = input("synonem for concluded")
bakesale = input("event")
gatherd = input("past tense verb")
cookingsuplies = input("thing")
store = input("location")
baked = input("past tense verb")
cookies = input("plural thing")
hishome = input("location")
#compliments the player and then prints the paragraph
say("wow those were some very good words, good job")
say ("are you ready?")
#fakes the loadtime to make the paragraph feel more impactful
say("calculateing...")
time.sleep(3)
print("----------------------------------------------------")
say(f"once apon a time there was a {lone} jesuite named {bob}")
say(f"one day {he} {decided} {he} wanted to host a {bakesale}")
say(f"but to host a {bakesale} {bob} needed a few things")
say(f"first {he} {gatherd} {cookingsuplies} at the {store}")
say(f"then {he} {baked} {cookies} at {hishome}.")
say(f"finaly {he} was ready to start the {bakesale}")
print("----------------------------------------------------")
ran = random.randint(1,3)
say(f"wow that was very {'good' if ran == 1 else 'funny' if ran == 2 else 'interesting'}")
say("but we need more words to continue the story")
say(f"sorry I have to do this to you {name} but i am going to have to ask you for more words")
say("hope you are not to disapointed")
#asks the user for more words
quite = input("adjective")
exited = input("adjective")
forever = input("time")
world = input("oranisation")
difrence = input("synonim for difrence")
cotribute = input("synonim for add")
shed = input("location")
sell = input("verb")
product = input("noun")
shelf = input(f"noun found in {shed}")
start = input("to begin")
say("perfect this is exectly what I needed")
#fakes the loadtime to make the paragraph feel more impactful
say("calculateing...")
time.sleep(3)
print("----------------------------------------------------")
say(f"{bob} was ready to host the {bakesale}")
say(f"{he} was {quite} {exited} becuse since {forever} {he} wanted to host a {bakesale}")
say(f"now was {bob}s chance to make a {difrence} and {cotribute} to the {world}")
say(f"he built a {shed} to {sell} the {product}")
say(f"then he put the {cookies} on the {shelf}")
say(f"time to {start} the sale")
print("----------------------------------------------------")
say("huh that was fun")
say("im kinda mad that we do this much work for so little payoff")
say("I think i have a plan.")
say("For now lets get some more words")
#
open = input("to open")
customer = input("client")
becky = input("name")
tom = input("name")
day = input("time of day")
nice = input("kind")
very = input("adjective")
succsess = input("succsess")
ten = input("number")
nine = input("number")
obj = input("noun")
good = input("quality")
#
say("calculateing...")
time.sleep(3)
print("----------------------------------------------------")
say(f"Now that {bob} {open} the {bakesale} {he} {start}ed to recive {customer}")
say(f"first he saw {becky}, {becky} was {nice} and orderd {ten} {cookies}")
say(f"{becky}, told him the shack was {quite} {nice}")
say(f"next he saw {tom}, {tom} orderd {nine} {cookies}")
say(f"{tom} told {bob} the {cookies} were {quite} {good} and gave him a tip")
say(f"this was the most succsess {bob} had ever experienced and it made him feel like a {obj}")
say(f"{bob} was {very} {exited} at the {succsess} of his shop and {decided} to give it another {day}.")
print("----------------------------------------------------")
say("ok thats was good but i have a plan for how to get moore bang for our buck with these words")
say("here is the plan")
say("I have built a robot that will take all of the words we have and use them to make a better sentance")
say("what do you say? wana try it out?")
say("great!")
say("BOOTING WORD MASHER.exe")
word_wall = [open,customer,becky,tom,day,nice,very,succsess,ten,nine,obj,good] 
print("----------------------------------------------------")
i = 0
while i<10:
    say(word_wall[random.radint(0,len(word_wall)])
    i += 1


print("----------------------------------------------------")




