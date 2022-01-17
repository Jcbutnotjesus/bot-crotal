import sys
import discord

TOKEN=''
f=open("TOKEN","r")
TOKEN=f.read()

if TOKEN == '' :
    sys.exit("Token non défini")

client = discord.Client()

@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))
    sys.stdout.flush()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'vive':
        await message.channel.send(f'la mère russie, {message.author.display_name}!')

    elif message.content.lower() =="comment tu t'appelles ?":
        await message.channel.send(f'Crotal {message.author.display_name}!')

    elif  message.content.lower() =="ping":
        await message.channel.send(f'pong')

    elif  message.content.lower() =="pong":
        await message.channel.send(f'ping')
        return

client.run(TOKEN)