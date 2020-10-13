import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:
    def __init__(self, previous_block, data):
        self.timestamp = str(datetime.datetime.now)
        self.data = data;
        self.previous_block = previous_block
        if (previous_block != None) :
            self.previous_hash = previous_block.current_hash
        else :
            self.previous_hash = "0" * 64
        self.nonce, self.current_hash = self.mine()
        print(self.nonce)

    def make_block(self, nonce) :
        return self.data + self.timestamp + self.previous_hash + str(nonce)
        
    def mine(self) :
        nonce = 0;
        while (not self.verify_hash(hashlib.sha256(self.make_block(nonce).encode()).hexdigest())):
            nonce += 1
        return nonce, hashlib.sha256(self.make_block(nonce).encode()).hexdigest()

    def verify_hash(self, hash_trial):
        return hash_trial[:4] == '00000'

    def is_chain_valid(self):
        if (hashlib.sha256(self.make_block(self.nonce).encode()).hexdigest() == self.current_hash and self.verify_hash(self.current_hash)):
            if (self.previous_hash == '0' * 64):
                return True
            else:
                return self.previous_block.is_chain_valid()
        else:
            return False


genesis = Blockchain(None, "genesis")
bc1 = Blockchain(genesis, "jeroen passed blockchain exam")
bc2 = Blockchain(bc1, "david transfers 500 btc to jeroen")
bc3 = Blockchain(bc2, "david votes for Trump")
print(bc3.current_hash + " is valid " + str(bc3.is_chain_valid()))

bc1.data = "jeroen passed valid contracts exam"
print( bc3.is_chain_valid())
