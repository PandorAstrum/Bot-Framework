# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Execution file to create deploy or add functionality"
"""
import argparse

from core.commandparse import CreateOperation, Context

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # required arguments
    parser.add_argument("operation", help="Specify an operation (addfunc, make, stats)", choices=["create", "add", "make", "stats", "deploy"])
    # optional arguments
    parser.add_argument("--add", help="Add a functionality to the bot")
    parser.add_argument("--make", help="create the Bot into the bot directory")
    parser.add_argument("--stats", help="Show the statistics of the bot")
    parser.add_argument("--deploy", help="Deploy the bot into discord")
    parser.add_argument("--create", help="Create a source file of the bot")
    args = parser.parse_args()

    _strategy_create = CreateOperation()
    parser.create = Context(_strategy_create)
    parser.create.context_interface()

    # _strategy_add = AddOperation()
    # parser.add = Context(_strategy_add)
    # #
    #
    # _strategy_make = MakeOperation()
    # parser.make = Context(_strategy_make)
    # # parser.make.context_interface()
    #
    # _strategy_stats = StatsOperation()
    # parser.stats = Context(_strategy_stats)
