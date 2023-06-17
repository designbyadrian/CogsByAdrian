from .crier import Crier

async def setup(bot):
  await bot.add_cog(Crier())