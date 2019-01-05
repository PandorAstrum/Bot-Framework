# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""

from core.questions.abc_question import AbcQuestions


class ConcreteTypeQuestion(AbcQuestions):


    def _build_type(self):
        return 'list'

    def _build_identifier(self):
        return 'bot_for'

    def _build_message(self):
        return 'Bot for :'

    def _build_choices(self):
        return ['Discord', 'Messenger', 'General']

    def _build_filter(self):
        return lambda val: val.lower()



