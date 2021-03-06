#!/usr/bin/env python3

import os
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
   """Reports when main bot is ready"""
   # print("AviationBot main ready")

@client.command()
async def ping(ctx):
   """Returns latency between bot and server"""
   # print(f"Pong main. {round(client.latency * 1000)}ms")
   await ctx.send(f"Pong main. {round(client.latency * 1000)}ms")

@client.command()
async def c_load(ctx, path):
   """Loads cogs"""
   client.load_extension(f"cogs.{path}")
   await ctx.send(f"Cog: {path} loaded")
   # print(f"Cog: {path} loaded")

@client.command()
async def c_unload(ctx, path):
   """Unloads cogs"""
   client.unload_extension(f"cogs.{path}")
   await ctx.send(f"Cog: {path} unloaded")
   # print(f"Cog: {path} unloaded")

@client.command()
async def c_reload(ctx, path):
   """Reloads cog"""
   client.unload_extension(f"cogs.{path}")
   client.load_extension(f"cogs.{path}")
   await ctx.send(f"Cog: {path} reloaded")
   # print(f"Cog: {path} reloaded")

for file_n in os.listdir("./cogs"):
   if file_n.endswith(".py"):
      client.load_extension(f"cogs.{file_n[:-3]}")

def main():
   """
   Bot token management
   
   Note: 
    - Bot token is kept in the '.token.txt' file
    - This is to avoid the sharing of bot tokens
   """
   global token
   try:
      with open("./.token.txt") as fd:
         token = fd.read().strip()
   except FileNotFoundError:
      sys.exit("Warning, Error occured. No '.token.txt' file found!")

if __name__ == "__main__":
   main()
   client.run(token)
