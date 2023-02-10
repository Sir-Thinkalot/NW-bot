import lightbulb
import hikari
from tinydb import TinyDB, Query 
from hikari import Embed
import time
plugin = lightbulb.Plugin('stopwatch', 'A stopwatch timer')
bot = lightbulb.BotApp
db = TinyDB('extensions/stopwatch/times.json')
App = Query()


@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    print("Timer command used")




@plugin.command
@lightbulb.option(name="stopwatch", choices=["start", "stop"], description="Starts or stops a timer ", required=True)
@lightbulb.command('stopwatch', 'A stopwatch command')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def help(ctx):
  if ctx.options.stopwatch == "start":
    db.insert({'start': time.time(), 'id':ctx.author.id})
    await ctx.respond("Timer started")
  
  elif ctx.options.stopwatch == "stop":
    results = db.search(App.id == ctx.author.id)
    if results == []:
      await ctx.respond("You do not have a timer going.")
    else:
      end_time = time.time()-results[0]['start']
      mins = end_time // 60
      sec = end_time % 60
      hours = mins // 60
      mins = mins % 60
      await ctx.respond(
        hikari.Embed(
          title="Time Elapsed",
          description="Time Lapsed = Hour: {0} Minute: {1} Seconds: {2}".format(int(hours),int(mins),sec)
          
        )
      )
      db.remove(App.id == ctx.author.id)
      #await ctx.respond("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

    
    
  
  


def load(bot):
    bot.add_plugin(plugin)
