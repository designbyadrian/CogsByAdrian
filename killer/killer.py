import discord
import random
import time
from redbot.core import commands


class Killer(commands.Cog):
    """Do unto others as you would have them do unto you"""

    def getActors(self, bot, killer, target):
        return {'id': bot.id, 'nick': bot.display_name, 'formatted': bot.mention}, {'id': killer.id, 'nick': killer.display_name, 'formatted': "<@{}>".format(killer.id)}, {'id': target.id, 'nick': target.display_name, 'formatted': target.mention}

    # SLAP
    @commands.command()
    async def slap(self, ctx, *, user: discord.Member):
        """Open hand, not a closed fist!"""

        bot, killer, target = self.getActors(
            ctx.bot.user, ctx.message.author, user)

        diceroll = random.randint(0, 100)

        if target['id'] == bot['id']:  # tryng to slap the bot, eh?

            message1 = "{} looks at {}... ✋😏 🤖".format(
                killer['nick'], bot['nick'])
            message2 = "but {} suddenly slaps {} with his silver sword! 😵💫 🍆🤖".format(
                bot['nick'], killer['nick'])

        elif killer['id'] == target['id']:  # wants to slap themselves

            message1 = "{} looks themselves in the mirror... 🖼😐".format(
                killer['nick'])

            if diceroll > 89:
                message2 = "and smashes their head against it! ✨🖼💥😫"

            elif diceroll > 10:
                message2 = "and gently pats their cheeks to wake up! 🖼😊"

            else:
                message2 = "and trips on the wet floor! Ouch! 🤕"

        else:  # wants to slap another user

            message1 = "{} raises their hand... ✋😏".format(killer['nick'])

            if diceroll > 89:
                message2 = "and mutilates {}! Oh my god, there's blood everywhere! 😵💥🤛😡".format(
                    target['formatted'])

            elif diceroll > 50 and diceroll < 55:
                message2 = "and gives {} a romantic spanking 😊🍑 👋😍".format(
                    target['formatted'])

            elif diceroll > 10:
                message2 = "and slaps {} senseless! 😫💫👋😠".format(
                    target['formatted'])

            else:
                message2 = "and misses! So stupid! 👋😟💨 😛"

        await ctx.send(message1)
        time.sleep(1)
        await ctx.send(message2)

    # PUNCH
    @commands.command()
    async def punch(self, ctx, *, user: discord.Member):
        """Open up a can of whoop-ass on a user!"""

        bot, killer, target = self.getActors(
            ctx.bot.user, ctx.message.author, user)

        diceroll = random.randint(0, 100)

        if target['id'] == bot['id']:  # tryng to punch the bot, eh?

            message1 = "{} waves their fists at {}... 🤖 ✊🧐".format(
                killer['nick'], bot['nick'])
            message2 = "but {} casts Igni on {}! 🤖 🔥😫🔥".format(
                bot['nick'], killer['formatted'])

        elif killer['id'] == target['id']:  # wants to punch themselves

            message1 = "{} looks at their own fist... 😒✊".format(
                killer['nick'])

            if diceroll > 89:
                message2 = "and bashes their head through the nearest wall! 😫▮💥"
            elif diceroll > 69:
                message2 = "and bashes their head against it until its broken! 😡💫🤟"
            elif diceroll > 10:
                message2 = "and repeatedly hits themselves with their pathetic little hands 🤜😣🤛"
            else:
                message2 = "tries to throw a punch, but misses and breaks their ankle! ☹️🦵"

        else:  # wants to punch another user

            message1 = "{} raises their fists towards {}... 😧 ✊😠".format(
                killer['formatted'], target['formatted'])

            if diceroll > 89:
                message2 = "\"Omae wa mou shindeiru\", says {}, before {} explodes into a cloud of blood and guts. 💥🤯💥 👈😎".format(
                    killer['formatted', target['formatted']])

            elif diceroll > 59:
                message2 = "and a flurry of punches break every bone in {}'s body! Ora! Ora! Ora! Ora! 😣🤛🤛🤛 😡".format(
                    target['formatted'])
            elif diceroll > 10:
                message2 = "and punches {} right in the face! Hard! 😣🤛 😠".format(
                    target['formatted'])
            else:
                message2 = "and trips on a banana peel! Doofus! 🤣👉 😖🍌"

        await ctx.send(message1)
        time.sleep(1)
        await ctx.send(message2)

    # STAB
    @commands.command()
    async def stab(self, ctx, *, user: discord.Member):
        """Turn a user into shish kebab!"""

        bot, killer, target = self.getActors(
            ctx.bot.user, ctx.message.author, user)

        diceroll = random.randint(0, 100)

        if target['id'] == bot['id']:  # tryng to shoot the bot, eh?

            message1 = "{} raises their dagger at Geraldo... 😠🔪 🤖".format(
                killer['nick'])
            message2 = "but Geraldo teleports behind {} and strikes! 😵💫 ⚔️🤖 {}".format(
                killer['formatted'], '`"Nothing personell, kid"`')

        elif killer['id'] == target['id']:  # wants to slap themselves

            message1 = "{} holds a knife against their abdomen...".format(
                killer['nick'])

            if diceroll > 89:
                message2 = "and cuts their own head off! How is that even possible!? 🙃👕"
            elif diceroll > 10:
                message2 = "and commits sudoku! 🔪😵"
            else:
                message2 = "and accidentally cuts their finger on a hentai magazine! 📕😫 {}-no skebe!".format(
                    target['nick'])

        else:  # wants to slap another user

            message1 = "{} raises their dagger... 😏🔪 😶".format(killer['nick'])

            if diceroll > 89:
                message2 = "and turns {} into a sheesh kebab! RIP in pieces! 😡🔪 👣 😵 🤚 👕 👖 ✋".format(
                    target['formatted'])
            elif diceroll > 10:
                message2 = "and stabs {}! Yikes! 😠🔪💥 ✋😵🤚".format(
                    target['formatted'])
            elif diceroll > 5:
                message2 = "but {} dodges like a ninja! 😛💨 😟🔪".format(
                    target['formatted'])
            else:
                message2 = "and cuts his own hand off! What an amateur! 😟🔪🤚 😝"

        await ctx.send(message1)
        time.sleep(1)
        await ctx.send(message2)

    # SHOOT
    @commands.command()
    async def shoot(self, ctx, *, user: discord.Member):
        """Shoot another user (or yourself) dead!"""

        bot, killer, target = self.getActors(
            ctx.bot.user, ctx.message.author, user)

        diceroll = random.randint(0, 100)

        if (target['id'] == bot['id']):  # tryng to shoot the bot, eh?

            message1 = "{} aims their gun, pulls the trigger...".format(
                killer['nick'])
            message2 = "but {} shot first! 😵 💥🔫🤖".format(bot['nick'])

        elif killer['id'] == target['id']:  # wants to kill themselves

            message1 = "{} holds a gun to their head, pulls the trigger...".format(
                killer['nick'])

            if diceroll > 89:
                message2 = "and explodes! Boom! Splat! What a mess! 💥😵💥"
            elif diceroll > 30:
                message2 = "and commits sudoku! 💥😵🔫"
            elif diceroll > 20:
                message2 = "and KYSed themselves! 💥😵🔫"
            elif diceroll > 10:
                message2 = "and somehow didn't miss! At least this idiot is good for something! 💥😵🔫"
            else:
                message2 = "and misses! What an idiot! Should've aimed at the temple! 💥🔫😯"

        else:  # wants to kill other user

            message1 = "{} aims their gun, pulls the trigger...".format(
                killer['nick'])

            if diceroll > 89:
                message2 = "and {} explodes into a red, gut-ridden, eyeball-strewn paste. Fun!!! 💥🔴 🔫🤠".format(
                    target['formatted'])
            elif diceroll > 75:
                message2 = "and shoots {} in the head! Bang! 💥😵 🔫😆".format(
                    target['formatted'])
            elif diceroll > 10:
                message2 = "and shoots {} dead! 😱 💥🔫😁".format(
                    target['formatted'])
            elif diceroll > 5:
                message2 = "and misses {}! Doh! 😗 💨🔫😣".format(
                    target['formatted'])
            else:
                message2 = "and shoots themselves instead of {}! LOL! 🤣 💥😵🔫".format(
                    target['formatted'])

        await ctx.send(message1)
        time.sleep(1)
        await ctx.send(message2)

    # LOVE
    @commands.command()
    async def love(self, ctx, *, user: discord.Member):
        """Show some affection for once!"""

        bot, killer, target = self.getActors(
            ctx.bot.user, ctx.message.author, user)

        diceroll = random.randint(0, 100)

        if target['id'] == bot['id']:  # love the bot
            message = "{} loves Geraldo 😍 🤖".format(killer['nick'])
        elif killer['id'] == target['id']:  # loves themselves
            message = "{} loves themselves, because nobody else does 😕".format(
                killer['nick'])
        else:
            if diceroll > 90:
                message = "Three cummie, four cummie, five cummie, six, {} loves {} but they also love dicks 💦".format(
                    killer['formatted'], target['formatted'])
            elif diceroll > 10:
                message = "{} loves {} aww... 😍 😊".format(
                    killer['formatted'], target['formatted'])
            else:
                message = "{} loves {}, but not in return 😭 😑".format(
                    killer['formatted'], target['formatted'])

        await ctx.send(message)

    # SEX
    @commands.command()
    async def sex(self, ctx, *, user: discord.Member):
        """Sex a user, because there's no NSFW channel!"""

        bot, killer, target = self.getActors(
            ctx.bot.user, ctx.message.author, user)

        diceroll = random.randint(0, 100)

        if target['id'] == bot['id']:  # sex the bot
            if diceroll > 89:
                message = "{} is taken by Geraldo on top of a stuffed unicorn 😝🦄🤖".format(
                    killer['formatted'])
            else:
                message = "Everbody wants to sex {}, get in line, loser!".format(
                    bot['nick'])
        elif killer['id'] == target['id']:  # sex themselves
            message = "{} does as they are told and f***s themselves 😓".format(
                killer['formatted'])
        else:
            message = "This is a Christmas Discord, get a room! 🎄"

        await ctx.send(message)

    # SUCC
    @commands.command()
    async def succ(self, ctx, *, user: discord.Member):
        """Succ a user like a lollipop"""

        bot, killer, target = self.getActors(
            ctx.bot.user, ctx.message.author, user)

        diceroll = random.randint(0, 100)

        if target['id'] == bot['id']:  # succ the bot
            if diceroll > 89:
                message = "{} enjoys {}'s magic juice 😙🍆🤖".format(
                    killer['formatted'], bot['nick'])
            else:
                message = "You already succ CDPR's dick every day!"
        elif killer['id'] == target['id']:  # succ themselves
            message = "{} succs themselves. Impressive, I guess...".format(
                killer['formatted'])
        else:
            if diceroll > 80:
                message = "Sucks to be you, {}".format(killer['formatted'])
            else:
                message = "This is a Christmas Discord, get a room! 🎄"

        await ctx.send(message)
