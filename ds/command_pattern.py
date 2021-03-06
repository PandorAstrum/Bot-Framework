# -*- coding: utf-8 -*-
"""
** Encapsulate a request as an object, thereby letting you parameterize
clients with different requests, queue or log requests, and support
undoable operations.

** UML LAYOUT (Command Design Pattern)

|===================|       |=======================|       |===========================|
|   Client(object)  |       |    Invoker(object)    |------>|   AbsCommand(interface)   |
|      *main()      |       |-----------------------|       |---------------------------|
|-------------------|       | -Attribute            |       | -Attribute                |
| -Attribute        |       | -Operation            |       | -Operation                |
| -Operation        |       |   +store_commands()   |       |   +execute()              |
|===================|       |   +execute_command()  |       |   +undo()                 |
    |       |               |=======================|       |===========================|
    |       |                                                           |
    |       |                                                           |
    |       |               |======================|          |=======================|
    |       |-------------->|   Receiver(object)   |<---------|    ConcreteCommand    |
    |                       |----------------------|          |-----------------------|
    |                       | -Attribute           |          | -Attribute            |
    |                       | -Operation           |          | -Operation            |
    |                       |   +action()          |          |   +execute()          |
    |                       |======================|          |   +undo()             |
    |-------------------------------------------------------->|=======================|

"""

import abc


class Invoker(object):
    """
    Ask the command to carry out the request.
    """

    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()


class AbsCommand(metaclass=abc.ABCMeta):
    """
    Declare an interface for executing an operation.
    """

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass


class ConcreteCommand(AbsCommand):
    """
    Define a binding between a Receiver object and an action.
    Implement Execute by invoking the corresponding operation(s) on
    Receiver.
    """

    def execute(self):
        self._receiver.action()


class Receiver:
    """
    Know how to perform the operations associated with carrying out a
    request. Any class may serve as a Receiver.
    """

    def action(self):
        pass


def main():
    receiver = Receiver()
    concrete_command = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.store_command(concrete_command)
    invoker.execute_commands()


if __name__ == "__main__":
    main()
