import discord
import os
import datetime
import random
from discord.ext import commands
bot = commands.Bot(description="I am red queen ,still not red",command_prefix="Rq:")
Now = datetime.datetime.utcnow()

@bot.command(pass_context=True)
async def ping(ctx):
    """Ping the bot"""
    tm = Now - ctx.message.timestamp
    await bot.say(":ping_pong: Pong! Took {0}ms to scan the system".format(random.randint(10,200)))

@bot.command()
async def say(msg):
    """Say something through the bot"""
    await bot.say(msg)

@bot.command()
async def now():
    """Get current date and time"""
    await bot.say(Now)
bot.run(os.getenv('TOKEN'))
