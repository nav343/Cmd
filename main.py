import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
from nextcord.interactions import Interaction
# from webserver import keep_alive

load_dotenv()
TOKEN = os.getenv('API_TOKEN')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$>'))

bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Activity(
        type=nextcord.ActivityType.listening, name='$>help'))
    print('Bot is ready')
    for cmds in bot.all_commands.keys():
        print(cmds)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


for fname in os.listdir('./cogs'):
    if fname.endswith('.py'):
        bot.load_extension(f'cogs.{fname[:-3]}')


@bot.slash_command(name='ping', description='Sends the latency of the bot')
async def ping(interaction: Interaction):
    await interaction.response.send_message(
        f"`~/cmd/bin`: Pong {round(bot.latency * 1000)}ms :bulb: !!!")

# Running it
#keep_alive()
bot.run(TOKEN)
