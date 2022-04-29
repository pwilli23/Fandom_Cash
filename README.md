# Fandom_Cash: Building the Brand One Token at a Time

![workflow](./images/workflow.png)

  art credit: [@kevinclee26](https://github.com/kevinclee26)

---
## Executive Summary

---
## What's Being Created

---
## Technologies

This application is written in Solidity with [Remix 0.22.2 IDE](https://remix-ide.readthedocs.io/en/latest/index.html)

Other dependencies:

 - [ERC20](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol) - *a standard for Fungible Tokens.*
 - [ERC20Detailed](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol) - *sets values for `name`, `symbol` and `decimals`.*
 - [ERC20Mintable](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol) - *Extension of {ERC20} that adds a set of accounts with the {MinterRole}, which have permission to mint (create) new tokens as they see fit.*
 - [Crowdsale](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol) - *Crowdsale is a base contract for managing a token crowdsale, allowing investors to purchase tokens with ether.*
 - [MintedCrowdsale](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol) - *Extension of Crowdsale contract whose tokens are minted in each purchase.*
 - [CappedCrowdsale](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol) - *Crowdsale with a limit for total contributions.*
 - [TimedCrowdsale](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/TimedCrowdsale.sol) - *Crowdsale accepting contributions only within a time frame.*
 - [RefundablePostDeliveryCrowdsale](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/distribution/RefundablePostDeliveryCrowdsale.sol) - *Extension of RefundableCrowdsale contract that only delivers the tokens once the crowdsale has closed and the goal met, preventing refunds to be issued to token holders.*
 - [SafeMath](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/math/SafeMath.sol) - *a library to help you check for overflows in case of addition, underflow in case of substraction as well as when performing multiplication and division.*
 
---
## Usage


---

## Contributors
John Felder - [@JohnFelder](https://github.com/JohnFelder)

Patten Williams - [@pwilli23](https://github.com/pwilli23)

Derek Hall - [@Hderek22](https://github.com/Hderek22)

Geoff Tarleton - [@blandwhite](https://github.com/blandwhite)

adapted from Starter Code supplied by UNCC FinTech Online Bootcamp by Trilogy Educational Services, a 2U, Inc. brand.

---

## License

[MIT](LICENSE)
