# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Utility File to help various thing"
"""

# expose current directory,
import os
from abc import ABCMeta
from datetime import datetime

from PyInquirer import style_from_dict, Token


def get_this_directory():
    _file_directory = os.path.dirname(__file__)
    return _file_directory


# get current time and date
def get_curr_date_time(_strft="%Y_%b_%d_%H.%M.%S"):
    """
    functions for getting current time
    :param strft: format to use on time
    :return: datetime now with provided format
    """
    return datetime.now().strftime(_strft)

def get_outputFile(file_name='', extension="json"):
    return f"{file_name}.{extension}"

custom_style_1 = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


custom_style_2 = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    #Token.Selected: '',  # default
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})


custom_style_3 = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

matrix_style = style_from_dict({
Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})