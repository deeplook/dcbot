# -*- coding: utf-8 -*-

"""
An experimental DeltaChat simplebot plugin for accessing some HERE.com services.

Implemented using the following example as a template:

https://github.com/SimpleBot-Inc/simplebot_plugins/blob/master/plugins/simplebot_xkcd/simplebot_xkcd/__init__.py

Run locally from the repo root with::

    repo2docker --debug -e HEREMAPS_API_KEY=$HEREMAPS_API_KEY .
"""

import io
import os
import random
from math import radians, degrees, log, cos, tan, pi, atan, sinh
from typing import Tuple

from deltabot import DeltaBot
from deltabot.bot import Replies
from deltabot.commands import IncomingCommand
from deltabot.hookspec import deltabot_hookimpl
import requests


version = '0.1.0'
API_KEY = os.getenv("HEREMAPS_API_KEY")


# ======== Hooks ===============

@deltabot_hookimpl
def deltabot_init(bot: DeltaBot) -> None:
    bot.commands.register(name='/here', func=cmd_here)


# ======== Commands ===============

def cmd_here(command: IncomingCommand, replies: Replies) -> None:
    """Show a maptile for the given address or Berlin, Germany if not provided.
    """
    if command.payload:
        address = command.payload
    else:
        address = "Berlin, Germany"
    # print(address)
    replies.add(**get_maptile(address))


# ======== Utilities ===============

def deg2tile(lat_deg: float, lon_deg: float, zoom: int) -> Tuple[int, int]:
    lat_rad = radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - log(tan(lat_rad) + (1 / cos(lat_rad))) / pi) / 2.0 * n)
    return (xtile, ytile)


def geocode(address: str) -> dict:
    # print(address)
    base_url = "https://geocode.search.hereapi.com/v1"
    url = f"{base_url}/geocode?q={address}&apiKey={API_KEY}"
    res = requests.get(url).json()
    pos = res["items"][0]["position"]
    return pos


def get_traffic_tile(pos: dict) -> bytes:
    # print(pos)
    s = random.randint(1, 4)
    base_url = f"https://{s}.traffic.maps.ls.hereapi.com/maptile/2.1"
    z = 13
    x, y = deg2tile(pos["lat"], pos["lng"], z)
    url = f"{base_url}/traffictile/newest/normal.day/{z}/{x}/{y}/256/png8?apiKey={API_KEY}"
    res = requests.get(url).content
    return res


def get_maptile(address: str) -> dict:
    pos = geocode(address)
    image = get_traffic_tile(pos)
    return dict(text=f"Address: {address}\nLat/lon: {pos['lat']}/{pos['lng']}",
                filename="file.png",
                bytefile=io.BytesIO(image))
