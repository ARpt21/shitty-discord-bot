import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.command
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.event
async def on_ready():
    print('Bot Boy Ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined .')

@client.event
async def on_member_remove(member):
    print(f'{member} has left .')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!')

@client.command(aliases=['hey_bot'])
async def ran_response(ctx, *, question):
    responses=  ['It is certainly not.',
                'Asked 69 virgin boys and got 420 responses and their response is yes.',
                'Without a doubt u r idiot if u ask that',
                'Yes – definitely.',
                'u r stoopid if u cant tell urself',
                'As I see it, yes.',
                'Most likely.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy',
                'try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Dont count on it.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.',
                'stfu i got no time for u',
                'idk bro']
    await ctx.send(f'Q: {question}\nAns: {random.choice(responses)} ' )


client.run('NzE2OTkyNjk5OTA2OTE2Mzc0.XtUZYA.gotnz-ITBr0EyDQAzwJ7lBWSa3A')