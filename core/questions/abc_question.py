# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import abc


class AbcQuestions(metaclass=abc.ABCMeta):
    """
    Specify an abstract interface for creating parts of a Product
    object.
    """

    @abc.abstractmethod
    def _build_type(self):
        pass

    @abc.abstractmethod
    def _build_identifier(self):
        pass

    @abc.abstractmethod
    def _build_message(self):
        pass

    @abc.abstractmethod
    def _build_choices(self):
        pass

    @abc.abstractmethod
    def _build_filter(self):
        pass



# class AbcQuestions(metaclass=abc.ABCMeta):
#     def __init(self):
#         self.questions = {}
#
#     @property
#     @abc.abstractmethod
#     def type(self):
#         pass
#
#     @property
#     @abc.abstractmethod
#     def identifier(self):
#         pass
#
#     @property
#     @abc.abstractmethod
#     def message(self):
#         pass
#
#     @property
#     @abc.abstractmethod
#     def questions(self):
#         pass