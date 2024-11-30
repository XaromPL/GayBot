import discord
from discord.ext import commands
import os
import asyncio
from config import token, prefix

intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix=prefix, intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} is online!')
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commands have been synchronized.")
    except Exception as e:
        print(e)
    
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            
async def main():
    await load()
    await bot.start(token)

asyncio.run(main())