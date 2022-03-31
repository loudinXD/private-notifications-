import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
list_of_members = []

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is connected to the following guild: {guild.name}(id: {guild.id})')

    for member in guild.members:
        if not member.bot:
            list_of_members.append(member)
    
client.run(TOKEN)