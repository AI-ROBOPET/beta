#!/bin/bash
# deploy_nft.sh
# Script to deploy the NFT smart contract on the blockchain.

# Variables
CONTRACT_PATH="src/nfts/nft_contract.sol"
OUTPUT_DIR="build"
PRIVATE_KEY="your-private-key"
NETWORK_URL="https://mainnet.infura.io/v3/your-infura-project-id"

# Check for Solidity compiler
if ! command -v solc &> /dev/null
then
    echo "Error: Solidity compiler (solc) is not installed."
    exit 1
fi

# Compile the contract
echo "Compiling the contract..."
solc --optimize --combined-json abi,bin -o $OUTPUT_DIR $CONTRACT_PATH

# Extract the ABI and bytecode
ABI_FILE="$OUTPUT_DIR/AI_ROBOPET.abi"
BYTECODE_FILE="$OUTPUT_DIR/AI_ROBOPET.bin"
ABI=$(jq -r '.contracts["src/nfts/nft_contract.sol:AI_ROBOPET"].abi' < $OUTPUT_DIR/combined.json)
BYTECODE=$(jq -r '.contracts["src/nfts/nft_contract.sol:AI_ROBOPET"].bin' < $OUTPUT_DIR/combined.json)

# Save ABI and bytecode
echo $ABI > $ABI_FILE
echo $BYTECODE > $BYTECODE_FILE
echo "ABI and bytecode saved."

# Deploy the contract using web3.py
echo "Deploying the contract..."
python3 <<EOF
from web3 import Web3
import json

private_key = "$PRIVATE_KEY"
network_url = "$NETWORK_URL"
contract_bytecode = "$BYTECODE"
contract_abi = $ABI

web3 = Web3(Web3.HTTPProvider(network_url))
account = web3.eth.account.privateKeyToAccount(private_key)
nonce = web3.eth.getTransactionCount(account.address)

contract = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
transaction = contract.constructor().buildTransaction({
    'chainId': 1,  # Mainnet
    'from': account.address,
    'nonce': nonce,
    'gas': 2000000,
    'gasPrice': web3.toWei('20', 'gwei')
})

signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print(f"Contract deployed at address: {tx_receipt.contractAddress}")
EOF

echo "Deployment completed."
