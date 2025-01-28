import os
import discord

from os import getenv
from discord.ext import commands
from slotmachine import SlotMachine
from test import jackpots
from dotenv import load_dotenv
from PIL import Image
load_dotenv(override=True)

bot = commands.Bot(
    command_prefix=getenv('PREFIX'),
    intents=discord.Intents.all()
)

slot1 = SlotMachine(3, {"777": 300, "888": 300, "999": 300})
slot2 = SlotMachine(4, {
  '7': 1,
  '77': 10,
  '777': 150,
  '7777': 1000
  })

print(slot1.simulation(100000, 20000, 2))
print(slot2.simulation(1000000, 20000, 2))

bot.run(getenv('TOKEN'))