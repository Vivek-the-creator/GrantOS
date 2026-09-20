# GrantOS Blockchain Toolchain & Smart Contracts (`blockchain/`)

> **Solidity & Hardhat Development Environment**  
> **Status**: Phase 1 Toolchain Verification Active

---

## 🎯 Overview

The `blockchain` workspace contains the Solidity smart contracts, Hardhat compilation scripts, unit tests, and Web3 deployment tasks for the MST Blockchain trust and audit layer.

In Phase 1, only the toolchain environment and a minimal verification contract (`HealthCheck.sol`) are active.

---

## 📁 Directory Architecture

```
blockchain/
├── contracts/
│   └── HealthCheck.sol      # Toolchain verification contract (placeholder)
├── test/
│   └── HealthCheck.ts       # Compilation & deployment unit test
├── scripts/                 # Deployment & task scripts (Phase 9+)
├── hardhat.config.ts        # Hardhat configuration (Solidity 0.8.24)
├── tsconfig.json            # TypeScript configuration
├── package.json             # Hardhat dependencies
└── README.md                # This documentation file
```

---

## 🚀 Running Verification Tests

1. **Install Dependencies**:
   ```bash
   cd blockchain
   npm install
   ```

2. **Compile Contracts**:
   ```bash
   npx hardhat compile
   ```

3. **Execute Test Suite**:
   ```bash
   npx hardhat test
   ```
   Output: `Should deploy HealthCheck placeholder contract and return 'pong' from ping() (passing)`.

---

*Phase 1 Blockchain Environment Ready.*
