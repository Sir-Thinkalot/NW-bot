import lightbulb 
import hikari
import asyncio
import requests
import os
from discord import SyncWebhook # Import SyncWebhook
token = 'MTA3Mzc4NDQ5ODUwMTcxMzk5MA.GldrMd.6X0hIRhc1mYDIiaSn-O7PN5XRPE2PbP3PqlCBY'

bot = lightbulb.BotApp(
    token=token,
    prefix="$",
    intents=hikari.Intents.ALL|hikari.Intents.MESSAGE_CONTENT
)

#@bot.listen(hikari.GuildMessageCreateEvent)
#async def print_message(event):
#    print(event.content)

# @bot.listen(hikari.StartedEvent)
# async def bot_started(event):
#     print('Bot has started.')
#     webhook = SyncWebhook.from_url('https://discord.com/api/webhooks/1054075338533109780/8ZeIdyQydFwUyDOD6rNWxFopZ31Gbg1EmTo6tOlyGIF37pH-f5oPvcGLbmNsWe5yOjd_') # Initializing webhook
#     webhook.send(content="Bot online :white_check_mark:") # Executing webhook.

# goes to the directory of extensions and then loads the files in the folder. 
# bot.load_extensions_from('./extensions/stopwatch')
# bot.load_extensions_from('./extensions')

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
@lightbulb.command("ping", "Checks that the bot is alive")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    """Checks that the bot is alive"""
    await ctx.respond("Pong!")

@bot.command()
@lightbulb.command("start", "Start the bot")
@lightbulb.implements(lightbulb.PrefixCommand)
async def start(ctx: lightbulb.Context) -> None:
    channel = await bot.rest.fetch_channel(ctx.channel_id)
    await ctx.respond('Ready and reporting for duty!')
    msg = 'Use $init(x) or $init(name, x) to add to the initative \nUse $sort once everone has been added to initiatve to sort the order \nUse $remove(name) to remove someone from iniative \nUse $end to stop and use $start to restart'
    await channel.send(msg)

bot.run(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(
        name="Your Mom",
        type=hikari.ActivityType.PLAYING
    )
)

