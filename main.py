# -------------- Imports ------------- #
import discord
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
import FactGen
import Loggy

import os
from dotenv import load_dotenv
load_dotenv()

# ----------- Bot Variables ---------- #

TOKEN = (os.getenv('TOKEN'))
bot = commands.Bot(command_prefix="!F ")
bot.remove_command('help')

# ----------- Main Section ----------- #

@bot.event
async def on_ready():
    Loggy.Add("Discord: Bot Started","Discord")


# ----------- Help Command ----------- #
HHelp = ("```\
Help   - Displays this menu\n\
Fact   - Generates a random fact\
```")
""" Prefix - W.I.P: Changes the bot's prefix (Admin Only)\ """
    
@bot.command(name = "Help")
async def Help(ctx):
        Loggy.Add ("Command - Help: Starting",ctx.author)
        msg = (HHelp)
        await ctx.channel.send(msg)
        return


# ----------- Fact Command ----------- #
@bot.command(name = "Fact")
async def Fact(ctx):
        Loggy.Add ("Command - Fact: Starting",ctx.author)
        await ctx.channel.send(FactGen.GenerateFact())
        return

""" # ---------- Prefix Command ---------- #
@bot.command(pass_context=True,name = "Prefix")
@has_permissions(administrator=True)
async def Prefix(ctx,prefix):
    Loggy.Add ("Command - Prefix Change to "+prefix+": ",ctx.author)
    bot.command_prefix = prefix
    msg = "`Prefix changed to "+prefix+"`"
    await ctx.send(msg)
    return

# ----------- Prefix Error ----------- #
@Prefix.error
async def Prefix_error(error, ctx):
    if isinstance(error, CheckFailure):
        Loggy.Add ("Command - Prefix Failure: ",ctx.author)
        msg = "`This is an Admin only command`"
        await bot.send_message(ctx.message.channel, msg)
         """
bot.run(TOKEN)