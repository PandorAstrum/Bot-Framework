# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""

from .abc_command import AbcCommand
from core import utility
from PyInquirer import prompt, Separator
from core.config import BOT_FOLDER, matrix_style
from core.questions import Director
from core import questions


class ConcreteCreateCommand(AbcCommand):
    """
    Define a binding between a Receiver object and an action.
    Implement Execute by invoking the corresponding operation(s) on
    Receiver.
    """

    @property
    def name(self):
        return 'create'

    @property
    def description(self):
        return 'Create the JSON Settings for bot'

    def execute(self, args):
        self._receiver.action(self, args)

    def operation(self):
        # TODO: ask question here
        _question_loader = utility.AutoLoader(questions, questions.AbcQuestions)
        _question = []
        _question_classes = _question_loader.initialize_each()

        for i in _question_classes:
            _director = Director(i)
            _director.construct()
            _question.append(_director.get_question())

        # TODO: Seperate question set and serialize with id

        _answer_set = prompt(_question, style=matrix_style)


        # if _first_set_answers['bot_type'] == "discord":
        #     _second_set_questions = [
        #         # bot prefix
        #         {'type': 'input',
        #          'name': 'bot_prefix',
        #          'message': 'Bot command Prefix :', },
        #             # add functionality
        #             {'type': 'checkbox',
        #              'qmark': '😃',
        #              'message': 'Select functions to add :',
        #              'name': 'bot_func',
        #              'choices': [
        #                  Separator('= Bot Events ='),
        #                  {'name': 'on_ready', 'checked': True},
        #                  {'name': 'on_resumed'},
        #                  {'name': 'on_error'},
        #                  {'name': 'on_message', 'checked': True},
        #                  {'name': 'on_massage_edit'},
        #                  {'name': 'on_massage_delete'},
        #                  {'name': 'on_reaction_add'},
        #                  {'name': 'on_reaction_clear'},
        #                  {'name': 'on_reaction_remove'},
        #                  {'name': 'on_channel_create'},
        #                  {'name': 'on_channel_update'},
        #                  {'name': 'on_channel_delete'},
        #                  {'name': 'on_member_join'},
        #                  {'name': 'on_member_update'},
        #                  {'name': 'on_member_remove'},
        #                  {'name': 'on_server_join'},
        #                  {'name': 'on_server_update'},
        #                  {'name': 'on_server_remove'},
        #                  {'name': 'on_server_role_create'},
        #                  {'name': 'on_server_role_update'},
        #                  {'name': 'on_server_role_delete'},
        #                  {'name': 'on_server_available'},
        #                  {'name': 'on_server_unavailable'},
        #                  {'name': 'on_server_emoji_update'},
        #                  Separator('= Bot Commands ='),
        #                  {'name': 'help', 'checked': True},
        #                  {'name': 'logout', 'checked': True},
        #                  {'name': 'join'},
        #                  {'name': 'leave'},
        #                  {'name': 'clear'},
        #                  {'name': 'displayEmbed'},
        #                  {'name': 'play'},
        #                  {'name': 'pause'},
        #                  {'name': 'stop'},
        #                  {'name': 'resume'},
        #                  {'name': 'queue'},
        #                  Separator('= Custom Command ='),
        #                  {'name': 'hug'},
        #                  {'name': 'roll'},
        #                  Separator('= The extras ='),
        #                  {'name': 'Pineapple'}
        #              ],
        #              'validate': lambda answer: 'You must choose at least one events or commands.' if len(answer) == 0 else True
        #              },
        #             # discord invite
        #             {'type': 'input',
        #              'name': 'bot_channel',
        #              'message': 'Discord Channel :', },
        #             # discord token
        #             {'type': 'input',
        #              'name': 'bot_token',
        #              'message': 'Token :', },
        #             # user.json
        #             {'type': 'confirm',
        #              'message': 'Do you want to generate USER file?',
        #              'name': 'user_file',
        #              'default': True},
        #             # API integration
        #             {'type': 'checkbox',
        #              'qmark': '😃',
        #              'message': 'Select API to add :',
        #              'name': 'bot_api',
        #              'choices': [
        #                  Separator('= APIs ='),
        #                  {'name': 'Leauge of legends'},
        #                  {'name': 'PUBG'}
        #              ]
        #              },
        #     ]

        #     # add functionality
        #     {'type': 'checkbox',
        #      'qmark': '😃',
        #      'message': 'Select functions to add :',
        #      'name': 'bot_func',
        #      'choices': [
        #          Separator('= Bot Events ='),
        #          {'name': 'on_ready', 'checked': True},
        #          {'name': 'on_resumed'},
        #          {'name': 'on_error'},
        #          {'name': 'on_message', 'checked': True},
        #          {'name': 'on_massage_edit'},
        #          {'name': 'on_massage_delete'},
        #          {'name': 'on_reaction_add'},
        #          {'name': 'on_reaction_clear'},
        #          {'name': 'on_reaction_remove'},
        #          {'name': 'on_channel_create'},
        #          {'name': 'on_channel_update'},
        #          {'name': 'on_channel_delete'},
        #          {'name': 'on_member_join'},
        #          {'name': 'on_member_update'},
        #          {'name': 'on_member_remove'},
        #          {'name': 'on_server_join'},
        #          {'name': 'on_server_update'},
        #          {'name': 'on_server_remove'},
        #          {'name': 'on_server_role_create'},
        #          {'name': 'on_server_role_update'},
        #          {'name': 'on_server_role_delete'},
        #          {'name': 'on_server_available'},
        #          {'name': 'on_server_unavailable'},
        #          {'name': 'on_server_emoji_update'},
        #          Separator('= Bot Commands ='),
        #          {'name': 'help', 'checked': True},
        #          {'name': 'logout', 'checked': True},
        #          {'name': 'join'},
        #          {'name': 'leave'},
        #          {'name': 'clear'},
        #          {'name': 'displayEmbed'},
        #          {'name': 'play'},
        #          {'name': 'pause'},
        #          {'name': 'stop'},
        #          {'name': 'resume'},
        #          {'name': 'queue'},
        #          Separator('= Custom Command ='),
        #          {'name': 'hug'},
        #          {'name': 'roll'},
        #          Separator('= The extras ='),
        #          {'name': 'Pineapple'}
        #      ],
        #      'validate': lambda answer: 'You must choose at least one events or commands.' if len(answer) == 0 else True
        #      },
        #     # discord invite
        #     {'type': 'input',
        #      'name': 'bot_channel',
        #      'message': 'Discord Channel :', },
        #     # discord token
        #     {'type': 'input',
        #      'name': 'bot_token',
        #      'message': 'Token :', },
        #     # user.json
        #     {'type': 'confirm',
        #      'message': 'Do you want to generate USER file?',
        #      'name': 'user_file',
        #      'default': True},
        #     # API integration
        #     {'type': 'checkbox',
        #      'qmark': '😃',
        #      'message': 'Select API to add :',
        #      'name': 'bot_api',
        #      'choices': [
        #          Separator('= APIs ='),
        #          {'name': 'Leauge of legends'},
        #          {'name': 'PUBG'}
        #      ]
        #      },
        #     # confirm
        #     {'type': 'confirm',
        #      'message': 'Do you want to continue?',
        #      'name': 'continue',
        #      'default': True}
        # ]
        # _answers = prompt(questions, style=matrix_style)
        # while _answers['continue'] == "No":
        #     pass

        print("Source file created at bot folder for statistics run main file with stats flag")
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
        data = {}
        # _previous_bot = search_bot(BOT_FOLDER)
        # _bot_id = int(len(_previous_bot) + 1)
        # _bot_basic = {
        #     "creation_date": str(get_curr_date_time()),
        #     "bot_command_prefix": str(_answers['bot_prefix']),
        #     "name": f"{_answers['bot_name']}",
        #     "type": f"{_answers['bot_choice']}",
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
        print(f"I am {self.name}")