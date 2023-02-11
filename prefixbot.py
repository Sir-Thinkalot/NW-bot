import hikari

import lightbulb

bot = lightbulb.BotApp(prefix="!", token="MTA3Mzc4NDQ5ODUwMTcxMzk5MA.GldrMd.6X0hIRhc1mYDIiaSn-O7PN5XRPE2PbP3PqlCBY", intents=hikari.Intents.ALL_UNPRIVILEGED|hikari.Intents.MESSAGE_CONTENT)


@bot.listen(hikari.ShardReadyEvent)
async def ready_listener(_):
    print("The bot is ready!")

@bot.command()
@lightbulb.command("ping", "Checks that the bot is alive")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    """Checks that the bot is alive"""
    await ctx.respond("Pong!")


@bot.command()
@lightbulb.option("num2", "Second number", int)
@lightbulb.option("num1", "First number", int)
@lightbulb.command("add", "Adds the two given numbers together")
@lightbulb.implements(lightbulb.PrefixCommand)
async def add(ctx: lightbulb.Context) -> None:
    """Adds the two given numbers together"""
    num1, num2 = ctx.options.num1, ctx.options.num2
    await ctx.respond(f"{num1} + {num2} = {num1 + num2}")


@bot.command()
@lightbulb.option("user", "User to greet", hikari.User)
@lightbulb.command("greet", "Greets the specified user")
@lightbulb.implements(lightbulb.PrefixCommand)
async def greet(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Hello {ctx.options.user.mention}!")


bot.run()