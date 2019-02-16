import discord
from redbot.core import commands


class Crier(commands.Cog):
    """Town Crier
       Announces whatever you type into target channel.

       (You might want to set up permissions properly using the Permissiosn cog)"""

    def __init__(self):
        self.numbers = [':zero:', ':one:', ':two:', ':three:',
                        ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:']

    @commands.command()
    async def say(self, ctx, channel: discord.TextChannel, *, message: str):
        """Echo message into other channel. Emojis and @s work as well.

           Usage: [p]say #channelName Hear ye!"""

        try:
            await channel.send_filtered(message)
        except discord.Forbidden:
            await ctx.send('❌ I\'m not allowed to do that, Dave')
        except discord.HTTPException:
            await ctx.send('❌ Something went wrong')

    @commands.command()
    async def shout(self, ctx, channel: discord.TextChannel, *, message: str):
        """Writes out message as 🇧 🇮 🇬 letters into other channel.

           Excludes all characters except A-Z 0-9

           Usage: [p]shout #channelName Hear ye!"""

        blocks = ""

        for c in message:
            if c.isalpha():
                blocks += ":regional_indicator_{}: ".format(c).lower()
            elif c.isdigit():
                blocks += self.numbers[int(c)]
            else:
                blocks += " "

        try:
            await channel.send(blocks)
        except discord.Forbidden:
            await ctx.send('❌ I\'m not allowed to do that, Dave')
        except discord.HTTPException:
            await ctx.send('❌ Something went wrong')
