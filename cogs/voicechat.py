import discord
from discord.ext import commands, tasks
import random
import webbrowser
from youtube_dl import YoutubeDL
import ffmpeg
import os

ffmpeg_options = {
'options': '-vn',
"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
}

class VoiceChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_playing = False
        self.music_queue = []
        self.np = ""
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        self.voice_client = None

        # optional
        self.uploader = None
        self.uploader_url = None
        self.title = None
        self.thumbnail = None
        self.description = None
        self.duration = None
        self.tags = None
        self.url = None
        self.views = None
        self.likes = None
        self.dislikes = None
        self.stream_url = None

    @commands.command()
    async def play(self, ctx, *args):
            
        query = " ".join(args)
        guild = ctx.guild
        self.voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("請加入頻道 Connect to a voice channel!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("下載不了破網路 cannot download song your internet is shit")
            else:
                await ctx.send("加入列單 added song to queue")
                self.music_queue.append([song, voice_channel])
                
                if self.is_playing == False:
                    await self.play_music()

    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']  
            self.title = self.music_queue[0][0]['title']   
            print(self.music_queue)
            self.music_queue.pop(0)
            print(self.voice_client)
            self.voice_client.play(discord.FFmpegPCMAudio(m_url, **ffmpeg_options,  executable="C:/ffmpeg/bin/ffmpeg.exe"), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True
            m_url = self.music_queue[0][0]['source']
            self.title = self.music_queue[0][0]['title']   
            self.music_queue.pop(0)

            self.voice_client.play(discord.FFmpegPCMAudio(m_url, **ffmpeg_options, executable="C:/ffmpeg/bin/ffmpeg.exe"), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @commands.command()
    async def np(self, ctx):
        if self.title == "":
            await ctx.send("Nothing is playing rn ???")
        else:
            embed = discord.Embed(title = "**Now Playing**", description = "You are listening to this, dumbass", color=0x7d7aff) 
            embed.add_field(name= "`Now Playing`", value = self.title)
            await ctx.send(embed=embed)

    @commands.command()
    async def queue(self, ctx):
        embed = discord.Embed(title = "**Queue**", description = "Lists the upcoming songs", color=0x7d7aff) 
        embed.add_field(name= "`Now Playing`", value = self.title)

        if(len(self.music_queue) == 0):
            embed.add_field(name= "`Up Next`", value = "No songs queued", inline=False)
        elif(len(self.music_queue) > 0):
            counter = 1
            embed.add_field(name= "`Up Next`", value = '**' + str(counter) + '**: ' + self.music_queue[0][0]['title'], inline=False)
            if(len(self.music_queue) > 1):
                for i in range(1, len(self.music_queue)):
                    counter+=1
                    embed.add_field(name='\u200b', value='**' + str(counter) + '**: ' + self.music_queue[i][0]['title'], inline=False)

        await ctx.send(embed=embed)

    def search_yt(self, item):  

        with YoutubeDL(self.ydl_opts) as ydl:
            try: 
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception: 
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command(name='skip', pass_context=True)
    async def skip(self, ctx):
        voice_client = self.voice_client
        if voice_client == None:
            await ctx.send('nothing is playing are you deaf?')
        else:
            if voice_client.is_playing():
                voice_client.stop()
                await ctx.send('skipping ' + self.title)

    @commands.command(pass_context=True)
    async def pause(self, ctx):
        voice_client = self.voice_client
        if voice_client.is_playing():
            voice_client.pause()
        else:
            await ctx.send('there\'s no music for you to pause')

    @commands.command(pass_context=True)
    async def resume(self, ctx):
        voice_client = self.voice_client
        if not voice_client.is_playing():
            voice_client.resume()
        else:
            await ctx.send('the music is already playing you fucking idiot')

    

def setup(bot):
    bot.add_cog(VoiceChatCog(bot))