import discord
import random
from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify


class Penis(commands.Cog):
    """Penis related commands."""

    @commands.command()
    async def penis(self, ctx, *users: discord.Member):
        """Detects user's penis length

        This is 100% accurate.
        Enter multiple users for an accurate comparison!"""
        if not users:
            await ctx.send_help()
            return

        dongs = {}
        msg = ""
        state = random.getstate()

        for user in users:
            random.seed(str(user.id))
            dongs[user] = "8{}D".format("=" * random.randint(0, 30))

        random.setstate(state)
        dongs = sorted(dongs.items(), key=lambda x: x[1])

        for user, dong in dongs:
            msg += "**{}'s size:**\n{}\n".format(user.display_name, dong)

        for page in pagify(msg):
            await ctx.send(page)
