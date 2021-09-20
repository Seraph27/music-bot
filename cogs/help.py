import discord
from discord.ext import commands

class HelpCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *, command=None):
        if command:
            description = {
                # 'spam': ('spams the channel the message is sent', '*spam '),
                # 'stopspam': ('stops the spam', '*stopspam '),
                # 'spam_g': ('spams all channel in a guild', '*spam_g <channel_id> '),
                # 'stop_g': ('stops the spam',  '*stop_g'),
                'play': ('plays the song',  '*play <url or song name>'),
                'np': ('now playing',  '*np'),
                'queue': ('stops the spam',  '*queue'),
                'skip': ('skips the current song',  '*skip'),
                'join': ('joins the voice channel requester is in',  '*join'),
                'leave': ('leaves the voice channel',  '*leave'),
                'pause': ('pauses the song',  '*pause'),
                'resume': ('resumes the song',  '*resume'),

            }
            if command in description.keys():
                embed = discord.Embed(title=command, description=description[command][0], color=0xbf7aff)
                embed.add_field(name= "**Syntax**", value = description[command][1])

        else:
            embed = discord.Embed(title = "Help", description = "Type !help <command> for a more detailed explaination", color=0x7d7aff)
            member_cog = self.bot.get_cog('MembersCog')
            member_commands = member_cog.get_commands()
            embed.add_field(name= "Member Commands", value = '\n'.join([c.name for c in member_commands]))
            musicbot_cog = self.bot.get_cog('VoiceChatCog')
            musicbot_commands = musicbot_cog.get_commands()
            embed.add_field(name= "Music Commands", value = '\n'.join([c.name for c in musicbot_commands]))
            embed.set_footer(text="for you idiots :)")

        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(HelpCog(bot))
