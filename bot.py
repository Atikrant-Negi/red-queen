import discord
import os
from discord.ext import commands
bot = commands.Bot(description="I am red queen ,still not red",command_prefix="r_q:")

@bot.command()
async def ping():
    """Ping the bot"""
    await bot.say(":ping_pong: Pong! Took {0}ms to scan the system".format(round(bot.latency,1)))

@bot.command()
async def say(msg):
    """Say something through the bot"""
    await bot.say(msg)

bot.run(os.getenv('TOKEN'))
