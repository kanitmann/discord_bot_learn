import discord
import os
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$random'):
        import random
        num = random.randint(1,9)
        while(True):
          await message.channel.send("Choose a number between 1 and 9 :sparkles:")
          response = await client.wait_for('message')
          n = int(response.content)
          if (n>9)or(n<1):
            await message.channel.send('Please guess between 1 to 9')
          elif(n==num):
            await message.channel.send('You guessed it correct. :heart:')
            break
          elif(n==(num-1))or(n==(num+1)):
            await message.channel.send('Very close :fire:')
          elif(n==(num-2))or(n==num+2):
            await message.channel.send('Close')
          elif (n==num-3) or (n==num-4) or (n==num+3) or (n==num+4):
            await message.channel.send('Far')
          else:
            await message.channel.send('Very far')

client.run(os.getenv('TOKEN'))