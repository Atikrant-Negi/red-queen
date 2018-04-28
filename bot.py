import discord
import datetime
import inspect
import random
import time
import os

from contextlib import redirect_stdout
from discord.ext import commands

ownerid = "388273713721901056"
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

@bot.command(pass_context=True, hidden=True)
@checks.is_owner()
async def deb(ctx, *,code:str):
    code = code.strip('` ')
    py = "```\n{}\n```"
    res = None
    env = {
        'bot'    :bot,
        'ctx'    :ctx,
        'message':ctx.message,
        'server' :ctx.message.server,
        'author' :ctx.message.author
    }
    env.update(globals())
    try:
        res = eval(code,env)
        if inspect.isawaitable(res):
            res = await res
    except Exception as e:
        await bot.say(py.format(type(e).__name__ + ': ' + str(e)))
        return
    await bot.say(py.format(res))
bot.run(os.getenv('TOKEN'))
