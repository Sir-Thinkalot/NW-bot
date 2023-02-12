import os

import hikari
import lightbulb as lb

with open("./Protected/Token") as f:
    _token = f.read().strip()

bot = lb.BotApp(
    token = _token,
    prefix = "$",
    intents = hikari.Intents.ALL|hikari.Intents.MESSAGE_CONTENT
)

bot.load_extensions_from('./NW-Bot/extensions')

# bot.unload_extensions

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.instal()

    bot.run(
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(
            name="Naruto World",
            type=hikari.ActivityType.PLAYING)
    )