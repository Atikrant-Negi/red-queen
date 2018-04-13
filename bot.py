import discord
import os
import datetime
from discord.ext import commands
bot = commands.Bot(description="I am red queen ,still not red",command_prefix="Rq:")
now = datetime.datetime.utcnow()

@bot.command(pass_context=True)
async def ping(ctx):
    """Ping the bot"""
    tm = now - ctx.message.timestamp
    await bot.say(":ping_pong: Pong! Took {0}ms to scan the system".format(tm(microseconds=1)))

@bot.command()
async def say(msg):
    """Say something through the bot"""
    await bot.say(msg)

bot.run(os.getenv('TOKEN'))
