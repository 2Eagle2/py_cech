"""
ovládanie práce s json súborom
"""

import json


def list_of_all():
    """
    výpiše zoznam všetkých dlžníkov aj výškou dlhu
    :return:
    """
    with open("dlznici.json") as f:
        data = json.load(f)
        return data

def list_one(name):
    """
    vypíše cech zadaného dlžníka
    :param name:
    :return:
    """
    if borrower_in_database(name):
        with open("dlznici.json") as f:
            data = json.load(f)

    else:
        print("Dlžník nieje na zozname")


def new_borrower(name, value):
    """
    pridá nového dlžníka do zoznamu
    :param name:
    :param value:
    :return:
    """
    pass

def takes_cech(name, value):
    """
    zvýšenie cechu dlžníkovy
    :param name:
    :param value:
    :return:
    """
    pass

def return_cech(name, value):
    """vrátenie cechu
    :param name:
    :param value:
    :return:
    """
    pass

def delete_borrower(name):
    """
    zmazanie dlžníka zo zonamu
    :param name:
    :return:
    """
    pass

def borrower_in_database(name):
    """
    kontrola či už je na zozname dlžnikov
    :param name:
    :return:
    """
    with open("dlznici.json") as f:
        data = json.load(f)
        if name in data:
            return True
        else:
            return False


def delete_all():
    """
    zmazanie vsetkých dlžníkov
    :return:
    """
    pass
