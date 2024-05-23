import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.nodes = set()
        
        # Create first block aka genesis block
        self.create_block(proof=1, previous_hash=1)
        
    def create_block(self, proof, previous_hash):
        pass
    
    def create_transaction(self, sender, recipient, amount):
        pass
    
    def hash(block):
        pass
