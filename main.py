import os
import discord
from stay_awake import stay_awake
from facts import get_fact
from quote import get_quote


stay_awake() # Opens our Flask app

token = os.environ['TOKEN'] # Discord token

bot = discord.Client() 


# Prints status when ready
@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))



# Makes bot respond to specific text commands.
@bot.event
async def on_message(message):
    # This prevents the bot from replying infinitely to itself.
    if message.author == bot:
        return

    if message.content.startswith('$hello') :
        await message.channel.send('Hello!')

    if message.content.startswith('$help'):
      await message.channel.send('Help ees on da wayyy!')

    # Experiments with tagging users
    if message.content.startswith('$hola'):
      await message.channel.send("Hey,  <@" + str(message.author.id) + "> !")

    # Retrieves random shark fact
    if message.content.startswith('$fact'):
      await message.channel.send(get_fact())

    # Retrieves random Bob Ross quote
    if message.content.startswith('$bobross'):
      await message.channel.send(get_quote())


bot.run(token) # Runs bot
