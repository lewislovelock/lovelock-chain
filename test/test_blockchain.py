import unittest
import json
import os
from server import app, Blockchain

class TestBlockchain(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.blockchain = Blockchain()
        self.blockchain.chain_file = 'test_chain.json'
        if os.path.exists(self.blockchain.chain_file):
            os.remove(self.blockchain.chain_file)

    def tearDown(self):
        if os.path.exists(self.blockchain.chain_file):
            os.remove(self.blockchain.chain_file)

    def test_mine_block(self):
        response = self.app.get('/mine')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('message', data)
        self.assertIn('index', data)
        self.assertIn('transactions', data)
        self.assertIn('proof', data)
        self.assertIn('previous_hash', data)
        self.assertEqual(data['message'], 'New Block Forged')

    def test_new_transaction(self):
        payload = {
            'sender': 'sender_address',
            'recipient': 'recipient_address',
            'amount': 10
        }
        response = self.app.post('/transactions/new', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn('message', data)
        self.assertTrue(data['message'].startswith('Transaction will be added to Block'))

    def test_new_transaction_missing_values(self):
        payload = {
            'sender': 'sender_address',
            'recipient': 'recipient_address'
        }
        response = self.app.post('/transactions/new', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), 'Missing values')

    def test_full_chain(self):
        response = self.app.get('/chain')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('chain', data)
        self.assertIn('length', data)
        self.assertIsInstance(data['chain'], list)
        self.assertIsInstance(data['length'], int)

    def test_register_nodes(self):
        payload = {
            'nodes': ['http://127.0.0.1:5001']
        }
        response = self.app.post('/nodes/register', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn('message', data)
        self.assertIn('total_nodes', data)
        self.assertIsInstance(data['total_nodes'], list)

    def test_register_nodes_missing_values(self):
        payload = {}
        response = self.app.post('/nodes/register', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), "Error: Please supply a valid list of nodes")

    def test_consensus(self):
        response = self.app.get('/nodes/resolve')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('message', data)
        self.assertIn('chain', data)
        self.assertIsInstance(data['chain'], list)

if __name__ == '__main__':
    unittest.main()