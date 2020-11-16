import discord
from datetime import datetime
import APIImporter
import Loggy

TOKEN = ('NzA0MzIwNjkyMTY1OTM1MjE0.Xqbbwg.qphtRtNzISzN7g9tt7ThgZ9XrME')
prefix = ('!FactBot')

client = discord.Client()

# ------------------------------------ #
#                  Bot                 #
# ------------------------------------ #

#   Main Section    #
@client.event
async def on_ready():
    Loggy.Add("Bot: Started")

@client.event
async def on_message(message):
    Loggy.Add("Message detected")

#Check to see this isn't the bot's message
    if message.author == client.user:
        Loggy.Add ("Bot's own message")
        return 

#Bot Hello Command
    if message.content == (prefix+" Fact"):
        await message.channel.send("Fact:\n"+APIImporter.GenerateFact())
        return
    
#Detected Bot @
    if client.user.mention in message.content.split():
        Loggy.Add ("@FactBot detected")
        await message.channel.send("Fact:\n"+APIImporter.GenerateFact())
        return

client.run(TOKEN)