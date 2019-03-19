import os
from importlib import import_module


def get_web3(network: str, project_id: str):
    # Infura websocket API requires Project ID token as of March 23rd
    os.environ['WEB3_INFURA_PROJECT_ID'] = project_id

    # Dynamically load the correct autoloader (based on network)
    infura_module = import_module("web3.auto.infura.%s" % network)

    # Return w3 autoloader for network
    return getattr(infura_module, 'w3')
