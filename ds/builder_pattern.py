# -*- coding: utf-8 -*-
"""
** Separate the construction of a complex object from its representation so
that the same construction process can create different representations.

** UML LAYOUT (Builder Design Pattern)

|===================|       |=======================|
|  Director(object) |------>| AbcBuilder(interface) |
|-------------------|       |-----------------------|
| -Attribute        |       |-Attribute             |
| -Operation        |       |-Operation             |
|   +construct()    |       |   +build_part()       |
|===================|       |=======================|
                                        |
                                        |
                              |===================|
                              |  ConcreteBuilder  |
                              |-------------------|
                              |-Attribute         |
                              |-Operation         |
                              |   +build_part()   |
                              |===================|

"""

import abc


class Director:
    """
    Construct an object using the Builder interface.
    """

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()


class Builder(metaclass=abc.ABCMeta):
    """
    Specify an abstract interface for creating parts of a Product
    object.
    """

    @abc.abstractmethod
    def _build_part_a(self):
        pass

    @abc.abstractmethod
    def _build_part_b(self):
        pass

    @abc.abstractmethod
    def _build_part_c(self):
        pass


class ConcreteBuilder(Builder):
    """
    Construct and assemble parts of the product by implementing the
    Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
    """

    def _build_part_a(self):
        pass

    def _build_part_b(self):
        pass

    def _build_part_c(self):
        pass


def main():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)


if __name__ == "__main__":
    main()