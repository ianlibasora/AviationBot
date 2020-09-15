#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# convert to async for discord pot



class Weather(object):
   # uri = f"https://aviationweather.gov/metar/data?ids={APT}"

   @staticmethod
   def metar(APT="EIDW"):
      """Default airport set to Dublin (EIDW)"""

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


def main():
   print(" --- Airport METAR / TAF testing --- ")

   print(Weather.metar("EGLL"))




if __name__ == "__main__":
   main()

