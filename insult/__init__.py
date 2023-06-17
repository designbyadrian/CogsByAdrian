from .insult import Insult

async def setup(bot):
  bot.add_cog(Insult())