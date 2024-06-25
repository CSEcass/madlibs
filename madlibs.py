# MadLib by Cass
print('----MadLibs----\n')
#Upchallenge(Datetime): 
import datetime
CurrDate = datetime.datetime.now()
DateTimeStr = CurrDate.strftime('%d-%m-%y')
# User input vvv
noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
verb2 = input('Give me a better one: ')
noun2 = input('Now give me a NOUN: ')
adjective = input('I NEED an adjective: ')
adjective2 = input('Anotha 1: ')
adverb = input('I lie. I want adverbs more(ugly sobbing):')
adverb2 = input('Got any DECENT(not like the other one u just entered... yikes), adverbs: ')
Feel = input('how do u feel so far(i totally care bestie): ')
 # finished Product vvv
print('\n--------Finished product--------\n')
print(f'In a surprising turn of events on {DateTimeStr}, {noun} transformed into a {verb} battleground for \nWorld War III, leaving behind a trail of destruction and chaos with everyone {verb2} in its wake.\nThe once {adverb} {adjective} land now echoed with the sounds of {adverb2} and {adjective2}. \nAs the dust settled,\nthe protagonist found themselves grappling with overwhelming emotions and deep-seated trauma.\nThey felt {Feel}, Seeking solace and {noun2},\n they embarked on a journey of intensive therapy to confront their clinical depression and make sense\nof the turmoil that had engulfed their beloved {noun}.')
# The end