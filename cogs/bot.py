# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import sys, traceback

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

initial_extensions = ['cogs.member',
                      'cogs.owner',
                      'cogs.help',
                      'cogs.error']

bot = commands.Bot(command_prefix='!', description='Rex\'s cute bot', help_command=None)


if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    await bot.change_presence(activity=discord.Game(name="Wild Rift"))
    print(f'{bot.user.name} has appeared from nowhere!')


bot.run(TOKEN, bot=True, reconnect=True)
# move below
