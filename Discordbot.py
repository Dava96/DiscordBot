import random
import requests
from discord import Game
from discord.ext.commands import Bot

bot_prefix = ("?", "!", "") # two different prefix's in a tuple
token = "##################################"
client = Bot(command_prefix=bot_prefix)

@client.command(name="8ball",
				description="Answers with a random quote from the list", # displays when you do !help 8ball
				brief="Answers from the beyond",# displays when you do !help
				aliases=["eight_ball", "ateball", "8-ball"], # alternative ways of calling the command
				pass_context=True) 
async def eight_ball(context):
	possible_responses = [
	"Yes",
	"No",
	"Maybe",
	"Hello"
	]
	await client.say(random.choice(possible_responses) + ", " + context.message.author.mention) # ats the who started the command


	
@client.event
async def on_ready():
	await client.change_presence(game=Game(name="with humans")) # changes the game name
	print("We are logged in as " + client.user.name)
	
@client.command()
async def setgame(gamename):
	newgame = gamename
	await client.change_presence(game=Game(name=newgame))
	print("Game changed to", newgame)

@client.command(description="Shows what the price of bitcoin is in usd by",
				brief="BTC in usd",
				aliases=['BTCUSD', 'btcusd'])
async def bitcoinUSD():
	url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
	response = requests.get(url)
	value = response.json()['bpi']['USD']['rate']
	await client.say("Bitcoin price is: $" + value)
	
@client.command(description="Shows what the price of bitcoin is in GBP by",
				brief="BTC in GBP",
				aliases=['BTCGBP, btcgbp'])
async def bitcoin():
	url = 'https://api.coindesk.com/v1/bpi/currentprice/GBP.json'
	response = requests.get(url)
	value = response.json()['bpi']['GBP']['rate']
	await client.say("Bitcoin price is: £" + value)		

#quikmaths	

@client.command()
async def square(number): # function with one argument (whatever you input)
	squared_value = int(number) * int(number) # checks if the number is an int and times it by itself
	await client.say(str(number) + " squared is " + str(squared_value)) # converts it back to a string
	
@client.command()
async def add(number1, number2):
	total = int(number1) + int(number2)
	await client.say(str(number1) + " add " + (str(number2) + " equals " + str(total)))

@client.command()
async def times(number1, number2):
	total = int(number1) * int(number2)
	await client.say(str(number1) + " times " + (str(number2) + " equals " + str(total)))
	
@client.command()
async def divide(number1, number2):
	total = int(number1) / int(number2)
	await client.say(str(number1) + " divide " + (str(number2) + " equals " + str(total)))

@client.command()
async def minus(number1, number2):
	total = int(number1) - int(number2)
	await client.say(str(number1) + " minus " + (str(number2) + " equals " + str(total)))

#googler
@client.command()
async def google(query):
	result = query.replace("_", "+")
	await client.say("I googled " + (result) + " for you")
	await client.say("https://www.google.com/search?ei=cRctW4qFFoT3kwXc06TgAw&q=" + (result))
	
@client.command()
async def spotify(query):
	result = query.replace("_", "%20")
	await client.say("Searching spotify for " + (result))
	await client.say("https://open.spotify.com/search/results/" + (result))
	
@client.command()
async def youtube(query):
	result = query.replace("_", "+")
	await client.say("Searching youtube for " + (result))
	await client.say("https://www.youtube.com/results?search_query=" + (result))


client.run('') # makes the bot run
