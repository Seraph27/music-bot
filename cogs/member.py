import discord

from discord.ext import commands, tasks
import random
import webbrowser

class MembersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        target_id = [  #put user ID and tellsl them to stfu
            

        ]
        if message.author.id in target_id:
            await message.channel.send('<@!' + str(message.author.id) + '>請閉嘴謝謝' + '<:OkayChamp:873928347908993064>')

    @commands.command(name="hi")
    async def hi(self, ctx):
        await ctx.reply("fuck you <a:xqcFinger:881263597399998524>", tts=True)

    @commands.command(name="copy")
    async def copy(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)
        
    @commands.command(name="spam")  #spam single channel
    async def start_spam(self, ctx):
        if not self.spam.is_running():
            self.spam.start(ctx.channel)

    @commands.command(name="stopspam")
    async def stop_spam(self, ctx):
        if self.spam.is_running():
            self.spam.stop()
                
    @tasks.loop(seconds=3)
    async def spam(self, channel):
        response_lst = [
            '<a:xqcFinger:881263597399998524>'
            'duahhuiadwdauhikdhaknadkhnkhncda',
            '???????????',
            'trash trash',
            '-36',
        ]
        response = random.choice(response_lst)
        await channel.send(response)
    
    @commands.command(name="spam_g") #spams all channel
    async def start_spam_g(self, ctx, arg1):
        if not self.spam_g.is_running():
            guild = self.bot.get_guild(int(arg1))

            if guild == None:
                await ctx.send("no channel id with this exists")
            else:
                self.spam_g.start(guild)

    @commands.command(name="stop_g")
    async def stop_spam_g(self, ctx):
        if self.spam_g.is_running():
            self.spam_g.stop()
                
    @tasks.loop(seconds=3)
    async def spam_g(self, guild):
        response_lst = [
            'daoiwjojaid',

        ]
        for channel in guild.text_channels:
            response = random.choice(response_lst)
            await channel.send(response)
    


def setup(bot):
    bot.add_cog(MembersCog(bot))