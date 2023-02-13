import speech_recognition as sr
import discord
from discord.ext import commands


prefix = "!" # Put your initial before the !
intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix = commands.when_mentioned_or(prefix),
    help_command = None,
    intents = intents,
)

with open("TOKEN.txt", 'r') as file:
    TOKEN = file.read()

@bot.event
async def on_ready():
    print("Bot connected.")

@bot.command
async def ping(ctx):
    await ctx.send("Pong")


bot.run(TOKEN)