from web3 import Web3

# Connect to the local node
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

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
# print(f"Get Value: {contract.functions.getValue('bintang').call()}")

# decode base64 data
import base64
from json import dumps, loads
data = contract.functions.getValue('bintang').call()    
data = base64.b64decode(data).decode('utf-8')
data = data.replace("'", '"')
data = loads(data)
# print(dumps(data, indent=4))
print(f"NIK: {data['NIK']}")
print(f"Nama Lengkap: {data['Nama Lengkap']}")
print(f"Tempat, Tanggal Lahir: {data['Tempat, Tanggal Lahir']}")
print(f"Alamat: {data['Alamat']}")
print(f"Pekerjaan: {data['Pekerjaan']}")
print(f"Pendidikan: {data['Pendidikan']}")
print(f"Kewarganegaraan: {data['Kewarganegaraan']}")
print(f"Agama: {data['Agama']}")
print(f"Status: {data['Status']}")
print(f"Golongan Darah: {data['Golongan Darah']}")
print(f"Jenis Kelamin: {data['Jenis Kelamin']}")
print(f"Tinggi Badan: {data['Tinggi Badan']}")
print(f"Berat Badan: {data['Berat Badan']}")

exit()

def setValue(key, value):
    # setValue Function of Smart Contract
    tx = contract.functions.setValue(key, value).buildTransaction({
        'nonce': w3.eth.getTransactionCount(my_account),
        'gas': 1000000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'chainId': 5777
    })
    signed_tx = w3.eth.account.signTransaction(tx, private_key=my_private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Transaction Hash: {w3.toHex(tx_hash)}")


identitas = {
    "NIK": "16520145",
    "Nama Lengkap": "Bintang Pratama",
    "Tempat, Tanggal Lahir": "Jakarta, 15 Agustus 2000",
    "Alamat": "Jl. Kebon Jeruk Raya No. 1",
    "Pekerjaan": "Tenaga Ahli",
    "Pendidikan": "S1",
    "Kewarganegaraan": "Indonesia",
    "Agama": "Islam",
    "Status": "Belum Menikah",
    "Golongan Darah": "O",
    "Jenis Kelamin": "Laki-laki",
    "Tinggi Badan": "170 cm",
    "Berat Badan": "60 kg",
}
# convert ke base64
import base64
identitas = base64.b64encode(str(identitas).encode('utf-8')).decode('utf-8')
data = {
    "bintang": identitas,
}
# setValue Function
for key, value in data.items():
    setValue(key, value)