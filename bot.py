# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')



client = discord.Client()


#implementation of the bot printing the server it is running on and the members that are currently in it
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Brewing coffee',extra=None))
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'-{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


#implementation of the bot sending a direct message to a user that just connected to the server
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to the depths of Mordor!')
    print(f'Sent a welcome message {member.name} for joining the server.')




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    gilfoyle_quotes = [
        'I’m effectively leveraging your misery. I’m like the Warren Buffet of fucking with you.',
        'I’m sure you can find your way out with one of your two faces.',
        'Pretend you’ve seen a woman before.', 
        'I wrote that code. You said you were in love with her mind. You realize what’s going on right? It’s not her you’re sexually attracted to. It’s my code... Just face it, Dinesh, you’re gay for my code. You’re code gay.', 
        'At least it didn’t happen in a public and brutally embarrassing way.', 
        'I think we should dig our own well and build our own generator. I also think we should store years worth of food and ammunition in a blast cellar. But we don’t. So good luck when the sh*t hits the fan.', 
        'Makes me feel like I’ve died and gone to hell.', 
        'People like to lie. It’s a war of all against all. The history of humanity is a book written in blood. We’re all just animals in a pit.', 
        'It’s not magic, it’s talent and sweat. People like me ensure your packets get delivered unsniffed. So what do I do? I make sure that one bad config on one key component doesn’t bankrupt the entire f*cking company. That’s what the f*ck I do.',
    ]

    if message.content == 'gilfoyle!':
        response = random.choice(gilfoyle_quotes)
        await message.channel.send(response)


    if 'star platinum' in message.content.lower():
        await message.channel.send('ORA ORA ORA ORA ORA')

'''
#Spams ora ora in a text channel. Just uncomment to use
    while 'muda muda' in message.content.lower():
        await message.channel.send('ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ')
'''

client.run(TOKEN)


