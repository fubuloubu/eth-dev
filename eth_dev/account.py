from typing import Dict
from getpass import getpass

from web3 import Web3
from web3.middleware.signing import construct_sign_and_send_raw_middleware

from eth_account import Account


def unlock_keyfile_to_account(keyfile: Dict, keyfile_path: str):
    privateKey = None
    num_tries = 0
    while privateKey is None and num_tries < 3:
        passphrase = getpass("Please Input Keyfile Password ({}): ".format(keyfile_path))
        try:
            privateKey = Account.decrypt(keyfile, passphrase)
        except ValueError as e:
            print("Password didn't work! Try again!")
            num_tries += 1

    if privateKey is None:
        raise ValueError("Too many tries!")

    account = Account.privateKeyToAccount(privateKey)
    return account


def add_signing_middleware(w3: Web3, account: Account):
    _middleware = construct_sign_and_send_raw_middleware(account.privateKey)
    # TODO Change to "middleware_onion" after upgrade to web3>5.0.0a3
    w3.middleware_stack.add(_middleware)
