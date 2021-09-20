# import discord
# from discord.ext import commands
# import random
# import requests
# import bs4
# import webbrowser

# class MembersCog(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.Cog.listener()
#     async def on_message(self, message):
#         if message.author == self.bot.user:
#             return

#         print(message.author.name + ': ' + str(message.author.id))  #gives user id
#         if message.author.id == 305189175093886981:
#             rand = random.uniform(0, 1)
#             print(rand)
#             if rand < 0.1:
#                 await message.channel.send('boop')
#             else:
#                 return
#         response_lst = [
#             'i refuse to speak to you',
#             '?????????',
#             'stfu',
#         ]

#         lol_list = ['lol', 'lmao', 'haha', 'xd']
#         if message.content == 'hi':
#             response = random.choice(response_lst)
#             await message.channel.send(response)
#         for word in message.content.lower:
#             if word in lol_list:
#                 await message.channel.send(':joy:')

#     @commands.command(name='bruh')
#     async def shut_up(self, ctx):
#         response_lst = [
#             '',
#         ]

#         response = random.choice(response_lst)
#         await ctx.send(response)

#     @commands.command(name='slader')
#     async def slader(self, ctx):
#         embed=discord.Embed(title="slader", url="https://www.slader.com/textbook/9780133311617-calculus-graphical-numerical-algebraic-fifth-edition/", color=0xffffff)
#         await ctx.send(embed=embed)

#     @commands.command(pass_context=True)
#     async def hw(self, ctx, *, args):
#         r = requests.get('https://docs.google.com/spreadsheets/u/1/d/1bn99zMyRzNDyOganM75vWBauc3Aur85ewXpumIZe73I/pubhtml?gid=0&range=A1%3AG36&output=html')
#         r.raise_for_status()
#         html = bs4.BeautifulSoup(r.text, features="html.parser")
#         table = html.find('table')
#         formatted_table = [[td.text for td in row.find_all("td")] for row in table.find_all("tr")]
#         subjects = []
#         contexts = []
#         for i in formatted_table[3:16]:
#             subjects.append(i[0])
#             contexts.append(i[1:])

#         value = []
#         value_str = ''
#         divider = '----------------'
#         day_val = {
#             'mon': 0,
#             'tues': 1, 
#             'wed': 2,
#             'thurs': 3, 
#             'fri': 4,
#         }

#         subject_val = {
#             'bible11': 0,
#             'english3': 1,
#             'ush': 2,
#             'precalc': 3,
#             'apchem': 4,
#             'physics': 5,
#             'apstat': 6,
#             'apcalc': 7,
#             'apenglish': 8,
#             'bible12': 9,
#             'english4': 10,
#             'government': 11,
#             'yearbook': 12,

#         }
#         if args == 'page':
#             await ctx.send("here you go :)")
#             embed=discord.Embed(title="HW page", url="https://docs.google.com/spreadsheets/u/1/d/1bn99zMyRzNDyOganM75vWBauc3Aur85ewXpumIZe73I/pubhtml?gid=0&range=A1%3AG36&output=html", color=0xffffff)

#         if args in day_val:
#             for s, c in zip(subjects, [i[day_val[args]] for i in contexts]):
#                 value.append('*' + str(s) + '*' + ' : ' + c + '\n' + divider)             
#             value = '\n'.join(value) 
#             embed=discord.Embed(title='Homework by date', color=0x9d5cff)
#             embed.add_field(name=args, value=value, inline=False)

#         elif args in subject_val:  #subject name and all of its content
#             for index, c in zip(day_val.keys(), contexts[subject_val[args]]):
#                 value_str += '*{}*: {}'.format(index, c) + '\n'
#                 embed=discord.Embed(title='Homework by subject', color=0x9d5cff)
#                 embed.add_field(name=args, value=value_str, inline=False)

#         await ctx.send(embed=embed)

#     @hw.error
#     async def hw_handler(self, ctx, error):
#         if isinstance(error, commands.CommandInvokeError):
#             await ctx.send(error)
#             await ctx.send("Invalid arguments. Please enter date or subject")
#         elif isinstance(error, commands.MissingRequiredArgument):
#             await ctx.send("Enter some arguments you dumb fuck")

# def setup(bot):
#     bot.add_cog(MembersCog(bot))