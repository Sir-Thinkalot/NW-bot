import lightbulb
import hikari
from tinydb import TinyDB, Query 
from hikari import Embed
import time
plugin = lightbulb.Plugin('init', 'Initiative tracker')
bot = lightbulb.BotApp
db = TinyDB('extensions/init/init.json')
App = query()

@plugin.command
@lightbulb.option(name="init", description="Add yourself to Initiative", type=int, required=True)
@lightbulb.option(name="name", description="Name", type=str, required=False)
@lightbulb.command('init', 'init command')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)


async def init():
