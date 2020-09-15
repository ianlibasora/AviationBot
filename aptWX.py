#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# convert to async for discord pot



class Weather(object):
   """Aviation METAR/TAF request lib"""

   @staticmethod
   def metar(APT="EIDW"):
      """
      Returns requested airport METAR
      Default airport set to Dublin (EIDW)
      """

      uri = f"https://aviationweather.gov/metar/data?ids={APT}"
      while True:
         web = requests.get(uri)
         if web.ok:
            soup = BeautifulSoup(web.text, "html.parser")
            try:
               return soup.code.text
            except AttributeError:
               print("Error occured")
               continue
         else:
            print(f"Web error occured. code {web.status_code}")
            break

   @staticmethod
   def taf(APT="EIDW"):
      """
      Returns requested airport TAF
      Default airport set to Dublin (EIDW)
      """

      uri = f"https://aviationweather.gov/taf/data?ids={APT}"
      while True:
         web = requests.get(uri)
         if web.ok:
            soup = BeautifulSoup(web.text, "html.parser")
            try:
               return soup.code.text
            except AttributeError:
               print("Error occured")
               continue
         else:
            print(f"Web error occured. code {web.status_code}")
            break


def main():
   print(" --- Airport METAR / TAF testing --- ")

   print(Weather.metar("EGLL"))
   print(Weather.metar("KLAX"))
   print(Weather.metar())


if __name__ == "__main__":
   main()
