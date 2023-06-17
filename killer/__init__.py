from .killer import Killer

async def setup(bot):
  await bot.add_cog(Killer())
