# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from core.utility import get_this_directory, json_format

dir = get_this_directory()

for j in json_format['bot']:
    print(j['bot_id'])