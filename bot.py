# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


#implementation of the bot printing the server it is running on and the members that are currently in it
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Ora Ora Ora Ora',extra=None))
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'-{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'\nGuild Members:\n - {members}')


#implementation of the bot sending a direct message to a user that just connecte to the server
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the depths of Mordor!'
    )
    print(f'Sent a welcome message {member.name} for joining the server.')



client.run(TOKEN)





