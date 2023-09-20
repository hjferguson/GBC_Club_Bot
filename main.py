import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_member_join(member):
    # Send a salute emoji to the new member
    welcome_channel = member.guild.text_channels[0]  # Replace with your desired channel
    await welcome_channel.send(f"Welcome {member.mention}! 🎉")

