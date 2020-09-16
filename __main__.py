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
   """Reports when bot is ready"""
   print("AviationBot ready")

@client.command()
async def ping(ctx):
   """Returns latency between bot and server"""
   print(f"Pong {round(client.latency * 1000)}ms")
   await ctx.send(f"Pong {round(client.latency * 1000)}ms")

@client.command(aliases=["METAR"])
async def metar(ctx, APT="EIDW"):
   """Returns METAR for airport passed as arguement"""
   print(f"METAR {APT}")
   await ctx.send(await Weather.async_metar(APT))

@client.command(aliases=["TAF"])
async def taf(ctx, APT="EIDW"):
   """Returns TAF for airport passed as arguement"""
   print(f"TAF {APT}")
   await ctx.send(await Weather.async_taf(APT))


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
