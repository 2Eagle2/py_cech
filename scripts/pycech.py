# -*- coding: utf-8 -*-

import json_controller
import argparse


def main():
    """script entry point

    :return: None
    """
    try:
        with open("../Readme.md", "rt", encoding="UTF-8") as readme:
            __doc__ = "".join(readme.readlines())
    except FileNotFoundError:
        __doc__ = "search for Readme.md for more information"

    a_parser = argparse.ArgumentParser(description=__doc__)
    a_parser.add_argument('--status', dest='status', action='store_true',
                        help='show every loan')
    a_parser.add_argument('--name', dest='name', default=None, type=str,
                        help='source file or console if not specified')
    a_parser.add_argument('--take', dest='take', default=None, type=float,
                        help='output file or console if not specified')
    a_parser.add_argument('--return', dest='give', default=None, type=float,
                        help='output file or console if not specified')

    args = vars(a_parser.parse_args())

    pycech(**args)


def pycech(status, name, give, take):
    if status:
        pass
    if name is not None:
        assert not ((give is not None) and (take is not None)),\
            "cannot take and return at the same time"

        if give is not None:
            print(name + " - " + str(give))
            pass

        if take is not None:
            print(name + " + " + str(take))
            pass


if __name__ == "__main__":
    main()