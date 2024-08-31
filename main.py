import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 
from typing import Final
from discord import Message
import asyncio 



# Load token and user ID from external file
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


# Bot setup
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())


# Handling the startup and command sync
@bot.event
async def on_ready():
    print(f'{bot.user} is now running')
    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced{len(synced_commands)} commands.")
    except Exception as e:
        print("an error with syncing commands has occurred: ", e) 





#load cogs
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

#start bot          
async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)
        
asyncio.run(main())
        
        
        




