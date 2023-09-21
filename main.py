import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Define your bot's intents
intents = discord.Intents.default()
intents.members = True  # Enable the intent to track member joins

# Create a bot instance with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    # Find the welcome channel (by name or ID)
    welcome_channel = discord.utils.get(member.guild.text_channels, name='welcome')

    if welcome_channel:
        # Get the last message in the welcome channel (which is the welcome message)
        async for message in welcome_channel.history(limit=1):
            # React to the welcome message with a salute emoji
            await message.add_reaction('🫡')

# Run your bot
bot.run(DISCORD_TOKEN)
