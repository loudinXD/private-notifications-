#   PRESENT RUNNING ON DIS
import os
import discord
import asyncio
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')


client = discord.Client()
list_of_ids = [781864134564118539, 853098156689457152, 752419226098073661, 700081717964308541,
               676462202223460364, 829169078202662942, 756520343258136636, 771273320766504970]


@client.event
async def on_ready():
    for i in list_of_ids:
        print(i)
        user = await client.fetch_user(i)
        await user.send("goal_view bot coming soon")

if __name__ == '__main__':
    client.run(token)
    