import discord
from redbot.core import commands


class UserInfo(commands.Cog):
    """Displays bite-sized user info

    Do [p]userinfo for the default user info panel"""

    @commands.command()
    async def userid(self, ctx, *, user: discord.Member):
        """Get the user ID"""

        if not user:
            await ctx.send_help()
            return

        await ctx.send(user.id)
