# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Command Line arguments functions"
"""
import json
from abc import ABCMeta, abstractmethod
from PyInquirer import style_from_dict, Token, prompt, Separator
from core.config import BOT_FOLDER
from core.utility import get_curr_date_time, get_outputFile
from core.utility import custom_style_3


class Context:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.print_action()
        self._strategy.do_operation()


class AbsOperation(metaclass=ABCMeta):
    """
        Declare an interface common to all supported algorithms. Context
        uses this interface to call the algorithm defined by a
        ConcreteStrategy.
    """

    @abstractmethod
    def print_action(self):
        pass

    @abstractmethod
    def do_operation(self):
        pass


class CreateOperation(AbsOperation):
    """
    Implement the algorithm using the Strategy interface.
    """

    def print_action(self):
        print("Create a source file for the bot =====================")

    def do_operation(self):
        # ask question and store the value
        questions = [
            # bot name
            {
                'type': 'input',
                'name': 'bot_name',
                'message': 'Bot Name : ',
            },
            # bot prefix
            {
                'type': 'input',
                'name': 'bot_prefix',
                'message': 'Bot command Prefix : ',
            },
            # bot choice
            {
                'type': 'list',
                'name': 'bot_choice',
                'message': 'Choose bot type : ',
                'choices': ['Type Simple', 'Type Custom'],
                'filter': lambda val: val.lower()
            },
            # add functionality
            {
                'type': 'checkbox',
                'qmark': '😃',
                'message': 'Select functions to add : ',
                'name': 'bot_func',
                'choices': [
                    Separator('= Bot Events ='),
                    {'name': 'on_ready', 'checked': True},
                    {'name': 'on_resumed'},
                    {'name': 'on_error'},
                    {'name': 'on_message', 'checked': True},
                    {'name': 'on_massage_edit'},
                    {'name': 'on_massage_delete'},
                    {'name': 'on_reaction_add'},
                    {'name': 'on_reaction_clear'},
                    {'name': 'on_reaction_remove'},
                    {'name': 'on_channel_create'},
                    {'name': 'on_channel_update'},
                    {'name': 'on_channel_delete'},
                    {'name': 'on_member_join'},
                    {'name': 'on_member_update'},
                    {'name': 'on_member_remove'},
                    {'name': 'on_server_join'},
                    {'name': 'on_server_update'},
                    {'name': 'on_server_remove'},
                    {'name': 'on_server_role_create'},
                    {'name': 'on_server_role_update'},
                    {'name': 'on_server_role_delete'},
                    {'name': 'on_server_available'},
                    {'name': 'on_server_unavailable'},
                    {'name': 'on_server_emoji_update'},

                    {
                        'name': 'on_server_join'
                    },
                    Separator('= Bot Commands ='),
                    {
                        'name': 'Mozzarella',
                        'checked': True
                    },
                    {
                        'name': 'Cheddar'
                    },
                    {
                        'name': 'Parmesan'
                    },
                    Separator('= The usual ='),
                    {
                        'name': 'Mushroom'
                    },
                    {
                        'name': 'Tomato'
                    },
                    {
                        'name': 'Pepperoni'
                    },
                    Separator('= The extras ='),
                    {
                        'name': 'Pineapple'
                    },
                    {
                        'name': 'Olives',
                        'disabled': 'out of stock'
                    },
                    {
                        'name': 'Extra cheese'
                    }
                ],
                'validate': lambda answer: 'You must choose at least one events or commands.' \
                    if len(answer) == 0 else True
            }
            # deploy channel
        ]
        answers = prompt(questions, style=custom_style_3)
        print(answers['bot_func'])
        # TODO: based on the value create json settings of the bot
        # {
        #     "bot": [{
        #         "func": {
        #             "func1": {
        #                 "id": 2,
        #                 "type": "command",
        #                 "desc": "First function",
        #                 "usage": "command channel",
        #                 "help": "help command"
        #             },
        #             "func2": {
        #                 "id": 3,
        #                 "type": "func",
        #                 "desc": "Some text",
        #                 "usage": "command channel",
        #                 "help": "help command"
        #             }
        #         },
        #         "discord": {
        #             "channel": "value",
        #             "username": "value",
        #             "password": "value"
        #         }
        #     }]
        # }
        # data = {}
        # bot_id = 1
        # bot_basic = {
        #     "creation_date": str(get_curr_date_time()),
        #     "bot_command_prefix": str(answers['bot_prefix']),
        #     "name": f"{answers['bot_name']}",
        #     "type": f"{answers['bot_choice']}",
        #     "modification_date": ""
        # }
        # bot_func_collection = []
        # bot_discord = {}
        # data['bot'].append({
        #     'bot_id': bot_id,
        #     'basic': bot_basic,
        #     'func': bot_func_collection,
        #     'discord': bot_discord
        # })
        #
        # _filename = BOT_FOLDER + "\\" + get_outputFile(file_name=answers['bot_name'])
        # with open(_filename, 'w') as outfile:
        #     json.dump(data, outfile)


class AddOperation(AbsOperation):
    """
    Implement the algorithm using the Strategy interface.
    """

    def print_action(self):
        print("Adding Functions to the Bot")

    def do_operation(self):
        pass


class MakeOperation(AbsOperation):
    """
    Implement the algorithm using the Strategy interface.
    """

    def print_action(self):
        print("Generating the bot")

    def do_operation(self):
        pass


class StatsOperation(AbsOperation):
    """
    Implement the algorithm using the Strategy interface.
    """

    def print_action(self):
        print("Showing statistics of the bot")

    def do_operation(self):
        pass

class ModifyOperation(AbsOperation):
    """
    Implement the algorithm using the Strategy interface.
    """

    def print_action(self):
        print("Modifying a specified bot")

    def do_operation(self):
        pass