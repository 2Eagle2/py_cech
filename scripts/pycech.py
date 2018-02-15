# -*- coding: utf-8 -*-

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
    a_parser.add_argument('--clear', dest='clear', action='store_true',
                        help='show every loan')
    a_parser.add_argument('--name', dest='name', default=None, type=str,
                        help='source file or console if not specified')
    a_parser.add_argument('--take', dest='take', default=None, type=float,
                        help='output file or console if not specified')
    a_parser.add_argument('--return', dest='give', default=None, type=float,
                        help='output file or console if not specified')

    args = vars(a_parser.parse_args())

    pycech(**args)


def pycech(status, clear, name=None, give=None, take=None) -> None:
    if status:
        if clear or any([var is not None for var in [name, give, take]]):
            raise RuntimeError("can not have any other switch with status")

    elif clear:
        if status or any([var is not None for var in [name, give, take]]):
            raise RuntimeError("can not have any other switch with clear")
        pass

    elif name is not None:
        if ((give is not None) and (take is not None)):
            raise RuntimeError("cannot take and return at the same time")

        if give is not None:
            print(name + " - " + str(give))
            pass

        elif take is not None:
            print(name + " + " + str(take))
            pass

        else:
            print(name + " have loan ")

    else:
        if ((give is not None) or (take is not None)):
            raise RuntimeError("must specify name of who take or return money")



if __name__ == "__main__":
    main()