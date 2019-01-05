# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from core.questions.abc_question import AbcQuestions


class ConcreteNameQuestion(AbcQuestions):


    def _build_type(self):
        return 'input'

    def _build_identifier(self):
        return 'bot_name'

    def _build_message(self):
        return 'Bot Name :'

    def _build_choices(self):
        pass

    def _build_filter(self):
        pass

# @property
    # def identifier(self):
    #     return 'bot_name'
    #
    # @property
    # def questions(self):
    #     return {
    #                'type': 'input',
    #                'name': 'bot_name',
    #                'message': 'Bot Name :'
    #            }

