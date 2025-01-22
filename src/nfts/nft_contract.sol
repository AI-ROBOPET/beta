// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title AI ROBOPET NFT Contract
 * @dev ERC721 implementation for AI ROBOPET ecosystem NFTs
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AIRobopetNFT is ERC721URIStorage, Ownable {
    uint256 private _tokenIds;

    constructor() ERC721("AI ROBOPET", "ARP") {}

    /**
     * @dev Mint a new NFT.
     * @param recipient The address of the recipient
     * @param tokenURI The URI of the metadata
     * @return The new token ID
     */
    function mintNFT(address recipient, string memory tokenURI) 
        public 
        onlyOwner 
        returns (uint256) 
    {
        _tokenIds++;
        uint256 newItemId = _tokenIds;

        _mint(recipient, newItemId);
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    }
}
