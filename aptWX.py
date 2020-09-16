#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp

"""
Airport METAR/TAF Lib

By Joseph Libasora
Last updated: 19.SEPT.2020, Python 3.8.2
"""

class Weather(object):
   """
   Aviation METAR/TAF request lib
   
   Synchronous/Asynchronous requests
   """

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


def main():
   print(" --- Airport METAR / TAF testing --- ")

   # print(Weather.sync_metar("EGLL"))
   # print(Weather.sync_taf("KLAX"))
   print(Weather.sync_metar())


async def amain():
   print(" --- Airport METAR / TAF testing --- ")

   print(await Weather.async_metar())
   print(await Weather.async_taf("KLAX"))


if __name__ == "__main__":
   # main()
   asyncio.run(amain())
