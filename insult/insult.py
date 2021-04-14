import aiohttp
import discord
from redbot.core import commands


class Insult(commands.Cog):
    """Polite user messaging."""

    def __init__(self):
        self.headers = {
            'X-Mashape-Key': 'kPgrTWlClqmshjyMDorgCZ0TcS6kp1ePfLUjsnCYR170S2VdWj',
            'Accept': 'text/plain',
        }

        self.params = {
            'mode': 'random',
        }

    def getActors(self, bot, offender, target):
        return {'id': bot.id, 'nick': bot.display_name, 'formatted': bot.mention}, {'id': offender.id, 'nick': offender.display_name, 'formatted': "<@{}>".format(offender.id)}, {'id': target.id, 'nick': target.display_name, 'formatted': target.mention}

    @commands.command()
    async def insult(self, ctx, user: discord.Member):
        """Tell user what you think of them!"""
        if not user:
            await ctx.send_help()
            return

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get('https://evilinsult.com/generate_insult.php?lang=en&type=text', params=self.params) as resp:

                if (resp.status == 200):

                    bot, offender, target = self.getActors(
                        ctx.bot.user, ctx.message.author, user)

                    text = await resp.text()

                    if target['id'] == bot['id']:
                        insult = "{}, {}".format(
                            offender['formatted'], text.lower())
                    else:
                        insult = "{}, {}".format(
                            target['formatted'], text.lower())

                    await ctx.send(insult)

                else:
                    await ctx.send("I've got nothing to say to the likes of you (Code {})".format(resp.status))
