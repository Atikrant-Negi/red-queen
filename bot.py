iemport discord
import os
from discord.ext import commands
bot = commands.Bot(description="I am red queen ,still not red",command_prefix="r_q:")

@bot.command()
async def ping():
    """Ping the bot"""
    await bot.say("pong!")
    
bot.run(os.getenv('TOKEN'))
