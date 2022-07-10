from web3 import Web3
from .meta import networks, netnames, urls, currs, contracts, decimals

def check_evm_address(address):
    try:
        address = Web3.toChecksumAddress(address.strip().lower())
        return address
    except:
        return None

def get_balance(address, network='eth'):
    address = check_evm_address(address)
    if address is None:
        return None
    else:
        network_url = urls[network]
        provider = Web3.HTTPProvider(network_url)
        web3 = Web3(provider)
        if web3.isConnected():
            balance = web3.eth.get_balance(address)
            return balance
        else:
            raise Exception(f'This url {network_url} seems to be wrong for the {network} network')
