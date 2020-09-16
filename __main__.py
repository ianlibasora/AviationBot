#!/usr/bin/env python3

from aptWX import Weather
import discord
from discord.ext import commands
import sys

"""
Discord Aviation Bot in Python

By Joseph Libasora
Last updated: 16.SEPT.2020, Python 3.8.2
"""

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
   print("AviationBot ready")

@client.event
async def on_message(message):
   if message.author == client.user:
     return

   if message.content.startswith('$hello'):
     await message.channel.send('Hello!')






def main():
   global token
   try:
      with open("./.token.txt") as fd:
         token = fd.read().strip()
   except FileNotFoundError:
      sys.exit("Warning, Error occured. No '.token.txt' file found!")

if __name__ == "__main__":
   main()
   client.run(token)
