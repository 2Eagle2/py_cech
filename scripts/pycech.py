# -*- coding: utf-8 -*-

import argparse
from scripts import cech


def main():
    """script entry point

    :return: None
    """
    try:
        with open("../README.md", "rt", encoding="UTF-8") as readme:
            __doc__ = "".join(readme.readlines())
    except FileNotFoundError:
        __doc__ = "search for Readme.md for more information"

    a_parser = argparse.ArgumentParser(description=__doc__)
    a_parser.add_argument('--status', dest='status', action='store_true',
                        help='show every loan')
    a_parser.add_argument('--clear', dest='clear', action='store_true',
                        help='show every loan')
    a_parser.add_argument('--name', dest='name', default=None, type=str,
                        help='name of borrower')
    a_parser.add_argument('--take', dest='take', default=None, type=float,
                        help='increase loan to given borrower')
    a_parser.add_argument('--return', dest='give', default=None, type=float,
                        help='decrease loan to given borrower')

    args = vars(a_parser.parse_args())

    pycech(**args)


def pycech(status, clear, name=None, give=None, take=None) -> None:
    """Check inputs and call appropriate action according to parameters

    :param status: flag for list all
    :param clear: flag for clear all
    :param name: identify user
    :param give: amount of money user return
    :param take: amount of money user borrow
    :return: None
    """

    if status and clear:
        raise RuntimeError("can not have both status and clear")

    if (status or clear) and any([var is not None for var in [name, give, take]]):
        raise RuntimeError("cannot specify any other switch with status or clear command ")

    if ((give is not None) and (take is not None)):
        raise RuntimeError("cannot take and return at the same time")

    if ((give is not None) or (take is not None)) and name is None:
        raise RuntimeError("must specify who take or return money")

    if status:
        list_of_users = cech.list_of_all()
        print_users(list_of_users)
        pass

    elif clear:
        cech.delete_all()
        pass

    elif name is not None:
        user_cech = cech.list_one(name)

        if give is not None:
            print(name + " - " + str(give))
            pass

        elif take is not None:
            print(name + " + " + str(take))
            pass

        else:
            print(name + " have loan ")

    else:
        # empty arg list do not print anything
        pass


def print_users(*users):
    print(users)


if __name__ == "__main__":
    main()