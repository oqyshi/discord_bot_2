import datetime

import discord

TOKEN = BOT_TOKEN

client = discord.Client()
hours, minutes, flag = 0, 0, False
time = None
clock = '⏰'


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    global hours, minutes, flag, time
    if message.author == client.user:
        return
    if "help" in message.content.lower():
        await message.channel.send(f'You can set a timer if type "set_timer '
                                   f'in __ hours __ minutes"')
    if 'set_timer' in message.content.lower():
        hours = int(message.content.split('in ')[1].split(' hours')[0])
        minutes = int(message.content.split('hours ')[1].split(' minutes')[0])
        flag = True
        time = datetime.datetime.now()
        await message.channel.send(f'The timer should start in {hours} hours and {minutes} minutes.')
    if flag:
        while True:
            delta = datetime.datetime.now() - time
            if delta.seconds >= hours * 3600 + minutes * 60:
                hours, minutes, flag = 0, 0, False
                time = None
                break
        await message.channel.send(f'{clock} Time X has come!')


client.run(TOKEN)
# set_timer in 0 hours 1 minutes
