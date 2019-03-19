import os
import sys
from importlib import import_module


def get_web3(network: str, project_id: str):
    # Infura websocket API requires Project ID token as of March 23rd
    print("Setting Infura Project ID to", project_id, file=sys.stderr)
    os.environ['WEB3_INFURA_PROJECT_ID'] = project_id

    # Dynamically load the correct autoloader (based on network)
    print("Connecting to the", network, "network (using Infura)", file=sys.stderr)
    infura_module = import_module("web3.auto.infura.%s" % network)

    # Return w3 autoloader for network
    return getattr(infura_module, 'w3')
