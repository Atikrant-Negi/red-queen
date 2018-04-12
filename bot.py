import discord
from discord.ext import commands
bot = commands.Bot(description="I am red queen ,still not red",command_prefix="r_q")
bot.run(os.getnv('TOKEN'))
