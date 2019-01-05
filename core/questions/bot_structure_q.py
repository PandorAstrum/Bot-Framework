# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""

from core.questions.abc_question import AbcQuestions


class ConcreteStructureQuestion(AbcQuestions):


    def _build_type(self):
        return 'list'

    def _build_identifier(self):
        return 'bot_structure'

    def _build_message(self):
        return 'Bot Folder Structure :'

    def _build_choices(self):
        return ['Type Simple', 'Type Complex', 'Type Custom']

    def _build_filter(self):
        return lambda val: val.lower()

