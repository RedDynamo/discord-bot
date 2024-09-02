from discord.ext import commands
from discord import app_commands
from discord import Embed
import discord
import motor.motor_asyncio
from typing import Final
import os

MONGODB_URI: Final[str] = os.getenv('MONGODB_URI')
YOUR_USER_ID: Final[int] = int(os.getenv('YOUR_USER_ID'))

class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
        self.db = self.client['Jobs']
        self.collection = self.db['Applications']
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")
    
    #command to add data to the database        
    @app_commands.command(name="add_data", description="Add data to the database")
    @app_commands.describe(job="Job Title", date="Date", status="Status")
    async def add_data(self, interaction: discord.Interaction, job: str, date: str, status: str):
        data = {
            "job": job,
            "date": date,
            "status": status
        }
        await self.collection.insert_one(data)
        await interaction.response.send_message("Data added to the database!")
    
    #command to shutdown the bot    
    @app_commands.command(name="shutdown", description="Turn off the bot")
    async def shutdown(self, interaction: discord.Interaction):
        if interaction.user.id != YOUR_USER_ID:
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
            return
        await interaction.response.send_message("Shutting down the bot...")
        await self.bot.close()
    
    #command to display the data in the database    
    @app_commands.command(name="display", description="Display current job applications statuses")
    async def display(self, interaction: discord.Interaction):
        try:
            jobs = await self.collection.find().to_list(length=100)  # Adjust length as needed
            if not jobs:
                await interaction.response.send_message("No job applications found.")
                return
            
            embed = Embed(title="Current Job Applications", color=0x7289DA)

            message = "Current Job Applications:\n"
            for job in jobs:
                embed.add_field(name=f"Job: {job['job']}", value=f"Date: {job['date']}\nStatus: {job['status']}", inline=False)

            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {e}", ephemeral=True)
            
    #command to edit data in the database
    @app_commands.command(name="edit_data", description="Edit data in the database")
    async def edit_data(self, interaction: discord.Interaction, job: str, date: str, status: str):
        data = {
            "job": job,
            "date": date,
            "status": status
        }
        await self.collection.update_one({"job": job}, {"$set": data})
        await interaction.response.send_message("Data updated in the database!")

# Setup
async def setup(bot):
    await bot.add_cog(Cogs(bot))