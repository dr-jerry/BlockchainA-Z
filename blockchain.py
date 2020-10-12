import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now)
                 , 'proof': proof
                 , 'previous_hash' : previous_hash}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def trial(self, new_proof, previous_proof):
        hash_trial = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
        return hash_trial[:4] == '0000'
        
    def proof_of_work(self, previous_proof):
        new_proof=0
        check_proof = False
        while check_proof is False:
            new_proof += 1
            check_proof = self.trial(new_proof, previous_proof)
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(encode_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(self.chain):
            block = block_index[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            if not self.trial(block['proof'], previous_block['proof']):
                return False
            previous_block = block
            block_index += 1
        return True



bc = Blockchain()
block = bc.create_block(bc.proof_of_work(0),0)
print(block)
