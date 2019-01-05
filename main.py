# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Execution file for the Command line"
"""
import argparse
from core.commands import Invoker, Receiver
from core.commands.create_command import ConcreteCreateCommand
from core.commands.make_command import ConcreteMakeCommand


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # required arguments
    parser.add_argument("operation", help="Specify an operation (addfunc, make, stats)", choices=["create", "make"])

    args = parser.parse_args()

    _invoker = Invoker()
    _receiver = Receiver()
    _create_command = ConcreteCreateCommand(_receiver)
    _make_command = ConcreteMakeCommand(_receiver)
    _invoker.store_command(_create_command)
    _invoker.store_command(_make_command)
    _invoker.execute_commands(args.operation)
