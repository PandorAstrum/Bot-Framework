# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from .abc_question import AbcQuestions
from .bot_name_q import ConcreteNameQuestion
from .bot_for_q import ConcreteTypeQuestion
from .bot_structure_q import ConcreteStructureQuestion

class Director(object):
    """
    Construct an object using the Builder interface.
    """

    def __init__(self, builder):
        self._builder = builder
        self._question = {}

    def construct(self):
        self._question['type'] = self._builder._build_type()
        self._question['name'] = self._builder._build_identifier()
        self._question['message'] = self._builder._build_message()
        if self._builder._build_choices() is not None:
            self._question['choices'] = self._builder._build_choices()
        if self._builder._build_filter() is not None:
            self._question['filter'] = self._builder._build_filter()

    def get_question(self):
        return self._question