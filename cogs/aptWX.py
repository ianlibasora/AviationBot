#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import aiohttp
import discord
from discord.ext import commands

"""
Airport METAR/TAF Discord Cog

By Joseph Libasora
Last updated: 19.SEPT.2020, Python 3.8.2
"""

class Weather(commands.Cog):
   """
   Aviation METAR/TAF request lib for Discord
   
   Synchronous/Asynchronous requests
   """

   def __init__(self, client):
      """Init"""
      self.client = client

   @commands.Cog.listener()
   async def on_ready(self):
      """Reports when aptWX cog is ready"""
      # print("AviationBot aptWX cog ready")

   @commands.command()
   async def WX_ping(self, ctx):
      """Returns latency between WX and main"""
      # print("Pong aptWX.")
      await ctx.send("Pong aptWX")
   
   @commands.command(aliases=["METAR"])
   async def metar(self, ctx, APT="EIDW"):
      """Returns METAR for airport passed as arguement"""
      # print(f"METAR {APT.upper()}")
      embed = discord.Embed(
         title=f"{APT.upper()} METAR", 
         colour=discord.Colour.red(),
         description=await Weather.async_metar(APT)
      )
      embed.set_author(name="AVWeather", icon_url="https://cdn.discordapp.com/attachments/755454464303038536/755786158558150807/plane.png")
      await ctx.send(embed=embed)

   @commands.command(aliases=["TAF"])
   async def taf(self, ctx, APT="EIDW"):
      """Returns TAF for airport passed as arguement"""
      # print(f"TAF {APT.upper()}")
      embed = discord.Embed(
         title=f"{APT.upper()} TAF", 
         colour=discord.Colour.red(),
         description=await Weather.async_taf(APT)
      )
      embed.set_author(name="AVWeather", icon_url="https://cdn.discordapp.com/attachments/755454464303038536/755786158558150807/plane.png")
      await ctx.send(embed=embed)

   @commands.command(aliases=["WX", "wx"])
   async def report(self, ctx, APT="EIDW"):
      """Returns airport METAR/TAF passed as arguement"""
      # print(f"Report {APT.upper()}")
      embed = discord.Embed(
         title=f"{APT.upper()} Weather Report", 
         colour=discord.Colour.red()
      )
      embed.set_author(name="AVWeather", icon_url="https://cdn.discordapp.com/attachments/755454464303038536/755786158558150807/plane.png")
      embed.add_field(name="METAR", value=await Weather.async_metar(APT), inline=False)
      embed.add_field(name="TAF", value=await Weather.async_taf(APT), inline=False)
      await ctx.send(embed=embed)

   # ------ Static methods not bound to discord ------
   @staticmethod
   def sync_metar(APT="EIDW"):
      """
      Returns (sync) requested airport METAR
      Default airport set to Dublin (EIDW)
      """

      uri = f"https://aviationweather.gov/metar/data?ids={APT}"
      web = requests.get(uri)
      if web.ok:
         soup = BeautifulSoup(web.text, "html.parser")
         try:
            return soup.code.text
         except AttributeError:
            return "Invalid airport"
      else:
         return f"Web error occured. code: {web.status_code}"

   @staticmethod
   def sync_taf(APT="EIDW"):
      """
      Returns (sync) requested airport TAF
      Default airport set to Dublin (EIDW)
      """

      uri = f"https://aviationweather.gov/taf/data?ids={APT}"
      web = requests.get(uri)
      if web.ok:
         soup = BeautifulSoup(web.text, "html.parser")
         try:
            return soup.code.text
         except AttributeError:
            return "Invalid airport"
      else:
         return f"Web error occured. code: {web.status_code}"

   @staticmethod
   async def async_metar(APT="EIDW"):
      """
      Returns (sync) requested airport METAR
      Default airport set to Dublin (EIDW)
      """

      uri = f"https://aviationweather.gov/metar/data?ids={APT}"
      timeout = aiohttp.ClientTimeout(total=10)
      async with aiohttp.ClientSession(timeout=timeout) as sesh:
         async with sesh.get(uri) as web_resp:
            if web_resp.status == 200:
               web = await web_resp.text()
               soup = BeautifulSoup(web, "html.parser")
               try:
                  return soup.code.text
               except AttributeError:
                  return "Invalid airport"
            else:
               return "Warning, Error occured. code: {web_resp.status}"
      return "Warning, request timeout"

   @staticmethod
   async def async_taf(APT="EIDW"):
      """
      Returns (async) requested airport TAF
      Default airport set to Dublin (EIDW)
      """
      
      uri = f"https://aviationweather.gov/taf/data?ids={APT}"
      timeout = aiohttp.ClientTimeout(total=10)
      async with aiohttp.ClientSession(timeout=timeout) as sesh:
         async with sesh.get(uri) as web_resp:
            if web_resp.status == 200:
               web = await web_resp.text()
               soup = BeautifulSoup(web, "html.parser")
               try:
                  return soup.code.text
               except AttributeError:
                  return "Invalid airport"
            else:
               return "Warning, Error occured. code: {web_resp.status}"
      return "Warning, request timeout"

def setup(client):
   client.add_cog(Weather(client))


def main():
   print(" --- Airport METAR / TAF testing --- ")

   # print(Weather.sync_metar("EGLL"))
   # print(Weather.sync_taf("KLAX"))
   # print(Weather.sync_metar())


async def amain():
   print(" --- Airport METAR / TAF testing --- ")

   print(await Weather.async_metar())
   # print(await Weather.async_taf("KLAX"))


if __name__ == "__main__":
   import asyncio
   # main()
   asyncio.run(amain())
