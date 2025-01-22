# app.py
"""
Main backend application for AI ROBOPET.
"""

from flask import Flask, jsonify, request
import os
from src.agents.pet_agent import PetAgent
from src.nfts.nft_generator import NFTGenerator
from src.sdk.sdk_api import GameSDKAPI
import yaml

# Load configuration
config_path = "config/settings.yaml"
with open(config_path, "r") as file:
    config = yaml.safe_load(file)

app = Flask(__name__)

# Initialize components
sdk_api = GameSDKAPI(api_key=config["sdk"]["api_key"])
nft_generator = NFTGenerator(
    contract_address=config["blockchain"]["contract_address"],
    abi_path=config["blockchain"]["abi_path"],
    private_key=config["blockchain"]["private_key"],
    provider_url=config["blockchain"]["provider_url"],
)

# Endpoints
@app.route("/")
def home():
    return jsonify({"message": "Welcome to AI ROBOPET API!"})

@app.route("/agents/create", methods=["POST"])
def create_agent():
    data = request.json
    agent = PetAgent(
        name=data["name"],
        abilities=data.get("abilities", []),
        owner_id=data["owner_id"],
        pet_type=data["type"],
    )
    return jsonify(agent.get_details()), 201

@app.route("/nfts/mint", methods=["POST"])
def mint_nft():
    data = request.json
    try:
        receipt = nft_generator.mint_nft(data["recipient_address"], data["metadata_uri"])
        return jsonify({"status": "success", "transaction_receipt": receipt}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/sdk/agent/configure", methods=["POST"])
def configure_agent():
    data = request.json
    try:
        response = sdk_api.configure_agent(data["agent_id"], data["configuration"])
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    debug_mode = os.getenv("APP_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
