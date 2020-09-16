# Discord Aviation Bot

Simple Discord bot for retrieving airport METAR / TAF data in Python

## Dependencies
- [discord.py](https://pypi.org/project/discord.py/)
- [requests](https://pypi.org/project/requests/)
- [aiohttp](https://pypi.org/project/aiohttp/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

All modules can be installed using pip. 

Example:
```
pip install requests
```

## Commands Available
Commands are all prefixed by "."
- METAR / metar - Accepts airport ICAO code as an arguement, returns latest airport METAR report
- TAF / taf - Accepts airport ICAO code as an arguement, returns latest airport METAR report
- WX / wx / report - Accepts airport ICAO code as an arguement, returns latest airport METAR & TAF report

### Notes
- Bot token is stored in a ".token.txt" file
- This is to safeguard bot tokens going public
- As such, the bot will not run without said file being present

### Assets Used

[Plane](https://www.flaticon.com/free-icon/plane_129500) icon by [Freepik](https://www.flaticon.com/authors/freepik) from [flaticon.com](https://www.flaticon.com/)

---
By Joseph Libasora

Last updated: 16.SEPT.2020, Python 3.8.2
