from solders.keypair import Keypair
import json, base58

kp = Keypair()
json.dump({
    "pubkey": str(kp.pubkey()),
    "keypair": list(bytes(kp)),
    "private_key": base58.b58encode(bytes(kp)).decode()
}, open("created_mock.json", "w"), indent=2)
print("saved created_mock.json")