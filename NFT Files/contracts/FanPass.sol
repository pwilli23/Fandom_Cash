pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract FanRegistry is ERC721Full {
    constructor() public ERC721Full("FanPassToken", "FPT") {}

    struct Fan {
        string fanName;
        uint256 passPrice;
    }

    mapping(uint256 => Fan) public fanCollection;

    //event Transfer-Appraisal?(uint256 tokenId, uint256 passPrice, string reportURI);

    function registerFan(
        address owner,
        string memory name,
        string memory fanName,
        uint256 initialPassPrice,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        -setTokenURI(tokenId, tokenURI);

        fanCollection[tokenId] = Fan(fanName, initialPassPrice);

        return tokenId;
    }

    function newPrice(
        uint265 tokenId,
        uint256 newPassPrice,
        string memory reportURI
    ) public returns (uint256) {
        fanCollection[tokenId].passPrice = newPassPrice;

        //emit Transfer-Appraisal(tokenId, newPassPrice, reportURI);

        return fanCollection[tokenId].passPrice;
    }
}