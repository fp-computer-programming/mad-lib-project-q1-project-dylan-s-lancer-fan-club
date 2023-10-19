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
say("perfect this is exectly what I needed")
#fakes the loadtime to make the paragraph feel more impactful
say("calculateing...")
time.sleep(3)
print("----------------------------------------------------")
say(f"{bob} was ready to host the bakesale")
say(f"{he} was {quite} {exited} becuse since {forever} {he} wanted to host a {bakesale}")
say(f"now was {bob}s chance to make a {difrence} and {cotribute} to the {world}")
say(f"he built a {shed} to {sell} the {product}")
say(f"then he put the {cookies} on the {shelf}")
say(f"but {name} had other plans for him")
print("----------------------------------------------------")
say("huh that was very goo but that ending was something")
say("I dont remember puting that there")
say("that was weierd lets continue on maby it will fix itself")
say("lets get some more words")

