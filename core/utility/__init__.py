# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Utility File to help various thing"
"""

import os
import glob
from datetime import datetime
from inspect import getmembers, isclass, isabstract


def get_curr_date_time(_strft="%Y_%b_%d_%H.%M.%S"):
    """
    functions for getting current time
    :param _strft: format to use on time
    :return: datetime now with provided format
    """
    return datetime.now().strftime(_strft)


def get_output_file(_file_name='', _extension="json"):
    """
    function for get the output file name and format
    :param _file_name: string
    :param _extension: string
    :return: string
    """
    return f"{_file_name}.{_extension}"








class AutoLoader(object):
    loaded_module= {}
    def __init__(self, package, abs_cls):
        self.load_module(package, abs_cls)

    def load_module(self, package, abs_cls):
        classes = getmembers(package, lambda m: isclass(m) and not isabstract(m))

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, abs_cls):
                self.loaded_module.update([[name, _type]])

    def create_instance(self, question_cls):
        if question_cls in self.loaded_module:
            print("found and initializing")
            return self.loaded_module[question_cls]()
        else:
            return None

    def initialize_each(self):
        tmp = []
        for i in self.loaded_module.values():
            tmp.append(i())
        return tmp






def search_file(_path, _file, _full):
    """
    function for searching json file ends with bot in a specified folder
    :param _bot: path <STRING> to look for the json file
    :param _file: <STRING> name of file with extension
    :return: <LIST> of bot.json
    """
    _dir = _path
    if _full:
        _files = glob.glob(os.path.join(_dir, _file))
        return _files
    else:
        _files = glob.glob(_file.replace('\\','.'))
        return _files


def get_this_directory():
    _file_directory = os.path.dirname(__file__)
    return _file_directory

