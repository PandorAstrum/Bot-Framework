# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Configuration File"
"""
from PyInquirer import style_from_dict, Token


# path to bot
BOT_FOLDER = "C:\\Users\\Ana Ash\\Desktop\\Python Discord Bot\\DiscordBotProject\\bot"


matrix_style = style_from_dict({
    Token.QuestionMark: '#008f11 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#008f11 bold',
    Token.Question: '#673AB7 bold',
    Token.Separator: '#6C6C6C',
})