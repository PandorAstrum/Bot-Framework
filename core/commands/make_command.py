# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from .abc_command import AbcCommand


class ConcreteMakeCommand(AbcCommand):
    """
    Define a binding between a Receiver object and an action.
    Implement Execute by invoking the corresponding operation(s) on
    Receiver.
    """

    @property
    def name(self):
        return 'make'

    @property
    def description(self):
        return 'Generate the bot from JSON settings'

    def execute(self, args):
        self._receiver.action(self, args)

    def operation(self):
        print(f"I am {self.name}")
