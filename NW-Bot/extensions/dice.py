import lightbulb
import hikari
from hikari import Embed
import random

plugin = lightbulb.Plugin('roll', 'Roll a dice')
bot = lightbulb.BotApp


@plugin.command
@lightbulb.option(name="dice", description="Number of Dice", type=int, required=True)
@lightbulb.option(name="sides", description="Number of Sides", type=int, required=True)
@lightbulb.option(name="expression", description="Expression", type=str, required=False)
@lightbulb.command('roll', 'roll command')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def roll(ctx):
  response_embed=(
    hikari.Embed(
      title="Roll Results"
      )
    )
  total = 0
  if ctx.options.dice > 20:
    print("Sorry but you can't have more than 20 values in an embed! This is a discord limit!")
    return
  for x in range(ctx.options.dice):
    
      
    random_num = random.randint(1, ctx.options.sides)
    if ctx.options.expression == None:
      response_embed.add_field(name="Roll Result", value=random_num)
      total = total + random_num
    else:
      stripped = ctx.options.expression.strip('+')
      stripped = int(stripped)
      response_embed.add_field(name="Roll Result", value=random_num + stripped)
      total = total + random_num + stripped
      


  response_embed.add_field(name="Total", value=total)
  await ctx.respond(response_embed)
  print("Roll command successfully ran")
  print(response_embed)
    

def load(bot):
    bot.add_plugin(plugin)

  
  
