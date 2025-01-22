# nft_generator.py
"""
Module for generating and managing NFTs in the AI ROBOPET ecosystem.
"""

from web3 import Web3
import json

class NFTGenerator:
    def __init__(self, contract_address, abi_path, private_key, provider_url):
        """
        Initialize the NFT generator with contract and blockchain details.
        
        :param contract_address: Address of the NFT smart contract
        :param abi_path: Path to the ABI JSON file for the contract
        :param private_key: Private key for signing transactions
        :param provider_url: URL of the blockchain provider (e.g., Infura)
        """
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract_address = Web3.toChecksumAddress(contract_address)
        with open(abi_path, "r") as abi_file:
            self.abi = json.load(abi_file)
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.abi)
        self.private_key = private_key
        self.account = self.web3.eth.account.privateKeyToAccount(private_key)

    def mint_nft(self, recipient_address, metadata_uri):
        """
        Mint a new NFT for a specified recipient.
        
        :param recipient_address: Address of the NFT recipient
        :param metadata_uri: URI pointing to the metadata of the NFT
        :return: Transaction receipt
        """
        nonce = self.web3.eth.getTransactionCount(self.account.address)
        transaction = self.contract.functions.mint(
            Web3.toChecksumAddress(recipient_address),
            metadata_uri
        ).buildTransaction({
            "from": self.account.address,
            "nonce": nonce,
            "gas": 2000000,
            "gasPrice": self.web3.toWei("20", "gwei")
        })
        signed_txn = self.web3.eth.account.signTransaction(transaction, private_key=self.private_key)
        tx_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return self.web3.eth.waitForTransactionReceipt(tx_hash)

    def get_nft_owner(self, token_id):
        """
        Retrieve the owner of a specific NFT.
        
        :param token_id: ID of the NFT
        :return: Owner's address
        """
        return self.contract.functions.ownerOf(token_id).call()

    def get_token_uri(self, token_id):
        """
        Retrieve the metadata URI of a specific NFT.
        
        :param token_id: ID of the NFT
        :return: Metadata URI
        """
        return self.contract.functions.tokenURI(token_id).call()
