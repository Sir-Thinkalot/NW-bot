import lightbulb 
import hikari
import asyncio
import requests
import os
from discord import SyncWebhook # Import SyncWebhook
token = os.environ['token']

bot = lightbulb.BotApp(
    token=token
)




#@bot.listen(hikari.GuildMessageCreateEvent)
#async def print_message(event):
#    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started.')
    webhook = SyncWebhook.from_url('https://discord.com/api/webhooks/1054075338533109780/8ZeIdyQydFwUyDOD6rNWxFopZ31Gbg1EmTo6tOlyGIF37pH-f5oPvcGLbmNsWe5yOjd_') # Initializing webhook
    webhook.send(content="Bot online :white_check_mark:") # Executing webhook.





# goes to the directory of extensions and then loads the files in the folder. 
bot.load_extensions_from('./extensions/stopwatch')
bot.load_extensions_from('./extensions')

bot.run(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(
        name="nothing",
        url="https://www.twitch.tv/",
        type=hikari.ActivityType.STREAMING,
    ),
)

