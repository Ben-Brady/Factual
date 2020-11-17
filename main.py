import discord
import FactGen
import Loggy

import time
import random
import fnmatch

TOKEN = ('NzA0MzIwNjkyMTY1OTM1MjE0.Xqbbwg.Dx-R3YZo8N4_gKz43gr0lpMNZ34')
prefix = ('!factual')

HHelp = ("\
>Help - Displays this menu or gives more information about another command (e.g. !Factual Help Fact)\n\
>Fact - Generates a random Fact (e.g. !Factual Fact)\n\
>Prefix - Changes the bot's prefix(e.g. !Factual Prefix !F)\n\
")

Commands = ("help","fact","prefix")

client = discord.Client()

# ------------------------------------ #
#               Commands               #
# ------------------------------------ #

# ------------------------------------ #
#             Chose Command            #
# ------------------------------------ #

def FindCommand(message):
    for command in Commands:
        if fnmatch.fnmatch(message.content.lower(),("*"+command)) == True:
            Loggy.Add("FindCommand: Running command - "+command,message.author)
            return command
        else:
            Loggy.Add("FindCommand: No Command Selected",message.author)
            return

# ------------------------------------ #
#             Main Section             #
# ------------------------------------ #
@client.event
async def on_ready():
    Loggy.Add("Discord: Bot Started","Discord")
    
@client.event
async def on_message(message):
    Loggy.Add("Discord: Message detected",message.author)
    
#Own Message?
    if message.author == client.user:
        return 

#Detect Prefix
    if fnmatch.fnmatch(str(message.content).lower(),(prefix+"*")) == True:
        Loggy.Add ("Detect Prefix: Prefix Detected",message.author)
        Command = FindCommand(message)
    else:
        Loggy.Add ("Detect Prefix: Non-Bot message",message.author)
        return


#Fact Command
    if Command == "fact":
        Loggy.Add ("Command - Fact: Starting",message.author)
        await message.channel.send(FactGen.GenerateFact())
        return

#Help Command
    if Command == "help":
        Loggy.Add ("Command - Help: Starting",message.author)
        await message.channel.send(HHelp)
        return


#Prefix Command
    if Command == "prefix":
        Loggy.Add ("Command - Prefix: ",message.author)
        await message.channel.send("> W.I.P. Not Avaliable Right Now")
        return

#Empty Command
    else:
        Loggy.Add (("Empty("+str(Command)+"): Starting"),message.author)
        await message.channel.send('> Please enter a valid command\n> Try "'+prefix+' help"')
        
client.run(TOKEN)