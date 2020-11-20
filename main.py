import discord
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
import FactGen
import Loggy

import time
import random
import fnmatch

TOKEN = ('NzA0MzIwNjkyMTY1OTM1MjE0.Xqbbwg.Dx-R3YZo8N4_gKz43gr0lpMNZ34')

HHelp = ("\
> Help - Displays this menu or gives more information about another command\n\
> Fact - Generates a random Fact\n\
> Prefix - Changes the bot's prefix\n\
")

Help = [\
'> Help - Gives additional information about a given command',\
'> Fact - Generates a random ',\
"> Prefix(Admin Req) - Changes the bot's prefix"\
]

Commands = ("help","fact","prefix")

bot = commands.Bot(command_prefix='!FB ')

# ------------------------------------ #
#               Commands               #
# ------------------------------------ #

# ------------------------------------ #
#             Chose Command            #
# ------------------------------------ #

def OrderCommand(message):
    MessageFiltered = (((message.content).lower()).split())
    MessageLength = len(MessageFiltered)

#Detect Pefix
    if (MessageFiltered[0] == Prefix):
        Loggy.Add("OrderCommand: Running command - "+Commands,message.author)
        return MessageFiltered[1]
    
    elif MessageLength > 1:
        Loggy.Add("OrderCommand: No Command Selected",message.author)
        return

# ------------------------------------ #
#             Main Section             #
# ------------------------------------ #
@bot.event
async def on_ready():
    Loggy.Add("Discord: Bot Started","Discord")

#Fact Command
@bot.command(name="Fact")
async def Generate_Fact(ctx):
        Loggy.Add ("Command - Fact: Starting",ctx.author)
        await ctx.channel.send(FactGen.GenerateFact())
        return

#Help Command
@bot.command(name="Help")
async def Help_Menu(ctx):
        Loggy.Add ("Command - Help: Starting",ctx.author)
        msg = (HHelp)
        await ctx.channel.send(msg)
        return


#Prefix Command
@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def Prefix(ctx,prefix):
    Loggy.Add ("Command - Prefix Change to "+prefix+": ",ctx.author)
    bot.command_prefix = prefix
    msg = "Prefix changed to ``{prefix}``"
    await ctx.send(msg)
    return

@Prefix.error
async def Prefix_error(error, ctx):
    if isinstance(error, CheckFailure):
        Loggy.Add ("Command - Prefix Failure: ",ctx.author)
        msg = "> This is an Admin only command {}".format(ctx.message.author.mention)  
        await bot.send_message(ctx.message.channel, msg)
        
bot.run(TOKEN)