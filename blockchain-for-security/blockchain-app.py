import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()
        
        # Create first block aka genesis block
        self.create_block(proof=1, previous_hash=1)
        
    
    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block
    
    
    def create_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1  
      
    def last_block(self):
        return self.chain[-1]
    
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def proof_of_work(self, last_block):
        """
        Bitcoin's SHA-256 mining algorithm:
        - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
        - p is the previous proof, and p' is the new proof
        """
        last_proof = last_block['proof']
        last_hash = self.hash(last_block)
        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1
        return proof
    
    @staticmethod
    def valid_proof(prev_proof, proof, last_hash):
        guess = f'{prev_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
    def valid_chain(self, chain):
        prev_block = chain[0]
        index = 1
        while index < len(chain):
            block = chain[index]
            if block['previous_hash'] != self.hash(prev_block):
                return False
            if not self.valid_proof(prev_block['proof'], block['proof']):
                return False
            prev_block = block
            index += 1
        return True