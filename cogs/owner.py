from discord.ext import commands


class OwnerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def c_load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def c_unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def c_reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
   
    @commands.command(name='shutdown', hidden=True)
    @commands.is_owner()
    async def shutdown(self,ctx):
        try:
            await ctx.send('**shutting down**')
            await self.bot.logout()
        except:
            print("EnvironmentError")
            self.bot.clear()
        else:
            await ctx.send("You do not own this bot!")
            
def setup(bot):
    bot.add_cog(OwnerCog(bot))