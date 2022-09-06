"""
lusee-readthedocs: a sandbox for experimenting with documentation for LuSEE-Night
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_packages(kind=None):
    """
    Return a list of LuSEE packages.

    :param kind: Optional programming language
    :type kind: str
    :raise lusee.InvalidKindError: If the kind is invalid.
    :return: package list.
    :rtype: str
    """
    return "luseepy"

def return_true():
    """
    Test function to check RTD functionality

    :return: boolean value.
    :rtype: boolean
    """
    return True