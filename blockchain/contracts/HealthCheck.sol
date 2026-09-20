// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/**
 * @title HealthCheck
 * @notice Development placeholder contract used exclusively in Phase 1 to verify the Hardhat compilation toolchain.
 * @dev THIS IS NOT A BUSINESS CONTRACT. GrantOS smart contract business logic will be implemented in Phase 9.
 */
contract HealthCheck {
    string private constant PONG = "pong";

    event Pinged(address indexed sender, uint256 timestamp);

    function ping() external pure returns (string memory) {
        return PONG;
    }
}
