"""
ovládanie práce s json súborom
"""

import json


def list_of_all():
    """ výpiše zoznam všetkých dlžníkov aj výškou dlhu"""
    with open("dlznici") as f:
        data = json.load(f)
        return data

def list_one(name):
    """vypíše cech zadaného dlžníka"""
    if borrower_in_database(name):
        with open("dlznici") as f:
            data = json.load(f)

    else:
        print("Dlžník nieje na zozname")


def new_borrower(name, value):
    """pridá nového dlžníka do zoznamu"""
    pass

def takes_cech(name, value):
    """zvýšenie cechu dlžníkovy"""
    pass

def return_cech(name, value):
    """vrátenie cechu"""
    pass

def delete_borrower(name):
    """zmazanie dlžníka zo zonamu"""
    pass

def borrower_in_database(name):
    """kontrola či už je na zozname dlžnikov"""
    with open("dlznici") as f:
        data = json.load(f)
        if name in data:
            return True
        else:
            return False


