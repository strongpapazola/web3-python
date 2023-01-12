from web3 import Web3
import base64

# Connect to the local node to timeout
# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
# Connect to the local node to timeout
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545", request_kwargs={'timeout': 1000}))

# Check Connection to the node
print(f"Connected to the node: {w3.isConnected()}")

# My Account
my_account = "0xcaD1cb22fC064Dd06694033F3a30F2c13e648D4a"
my_private_key = "14974d437406ad2dea1b06f0af3d5b803341d9f52189ee39bca1ad323fe69c49"

# Contract Address
contract_address = "0x4D848471Ffa8f96499fE5A7dc96EA9E202B81cb6"
contract_abi = [{"inputs": [{"internalType": "string","name": "key","type": "string"}],"name": "getValue","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "string","name": "key","type": "string"},{"internalType": "string","name": "value","type": "string"}],"name": "setValue","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [{"internalType": "string","name": "","type": "string"}],"name": "values","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"}]
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Check Function getValue of Smart Contract
# print(f"Get Value: {contract.functions.getValue('kucing').call()}")

def setValue(key, value):
    # setValue Function of Smart Contract
    tx = contract.functions.setValue(key, value).buildTransaction({
        'nonce': w3.eth.getTransactionCount(my_account),
        'gasPrice': w3.toWei('50', 'gwei'),
        'chainId': 1337
    })
    # detect gas limit
    gas_limit = w3.eth.estimateGas(tx)
    tx['gas'] = gas_limit
    signed_tx = w3.eth.account.signTransaction(tx, private_key=my_private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Transaction Hash: {w3.toHex(tx_hash)}")

# Get Image From My Computer and Convert to Base64
with open("anjing.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

# Set Value of Smart Contract
setValue("kucing", encoded_string.decode("utf-8"))

encoded_string = contract.functions.getValue('kucing').call().encode("utf-8")

# Convert Base64 to image
with open("kucing/kucing-bari-blockchain.png", "wb") as fh:
    fh.write(base64.decodebytes(encoded_string))

