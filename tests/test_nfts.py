# test_nfts.py
"""
Unit tests for NFT generation and management.
"""

import unittest
from unittest.mock import patch, MagicMock
from src.nfts.nft_generator import NFTGenerator

class TestNFTGenerator(unittest.TestCase):
    def setUp(self):
        self.contract_address = "0x1234567890abcdef1234567890abcdef12345678"
        self.abi_path = "path/to/abi.json"
        self.private_key = "0xabcdefabcdefabcdefabcdefabcdefabcdef"
        self.provider_url = "https://mainnet.infura.io/v3/your-infura-project-id"
        self.nft_generator = NFTGenerator(
            contract_address=self.contract_address,
            abi_path=self.abi_path,
            private_key=self.private_key,
            provider_url=self.provider_url,
        )

    @patch("src.nfts.nft_generator.Web3.eth.getTransactionCount")
    @patch("src.nfts.nft_generator.Web3.eth.sendRawTransaction")
    @patch("src.nfts.nft_generator.Web3.eth.waitForTransactionReceipt")
    def test_mint_nft(self, mock_wait, mock_send, mock_nonce):
        # Mock responses
        mock_nonce.return_value = 1
        mock_send.return_value = "0xtransactionhash"
        mock_wait.return_value = {"status": 1, "transactionHash": "0xtransactionhash"}

        recipient_address = "0xabcdefabcdefabcdefabcdefabcdefabcdef"
        metadata_uri = "ipfs://metadata_uri"
        receipt = self.nft_generator.mint_nft(recipient_address, metadata_uri)

        self.assertEqual(receipt["status"], 1)
        self.assertEqual(receipt["transactionHash"], "0xtransactionhash")

    @patch("src.nfts.nft_generator.Web3.eth.Contract")
    def test_get_nft_owner(self, mock_contract):
        # Mock ownerOf function
        mock_contract.return_value.functions.ownerOf.return_value.call.return_value = "0xowneraddress"
        owner = self.nft_generator.get_nft_owner(1)

        self.assertEqual(owner, "0xowneraddress")

    @patch("src.nfts.nft_generator.Web3.eth.Contract")
    def test_get_token_uri(self, mock_contract):
        # Mock tokenURI function
        mock_contract.return_value.functions.tokenURI.return_value.call.return_value = "ipfs://metadata_uri"
        token_uri = self.nft_generator.get_token_uri(1)

        self.assertEqual(token_uri, "ipfs://metadata_uri")

if __name__ == "__main__":
    unittest.main()
