# Local Development Environment Setup Guide

> **Phase 1 Setup Reference**

This guide provides step-by-step instructions for cloning, setting up, and verifying the GrantOS repository on local developer environments.

---

## 📋 1. Prerequisites

Ensure your development machine has the following tools installed:
- **Git**: 2.30+
- **Node.js**: 18.x or 20.x LTS (`node -v`)
- **npm**: 9.x or 10.x (`npm -v`)
- **Python**: 3.11+ (`python --version` or `python3 --version`)
- **pip**: 23.x+ (`pip --version`)

---

## 🚀 2. Repository Initialization

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Vivek-the-creator/GrantOS.git
   cd GrantOS
   ```

2. **Configure Environment Variables**:
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

---

## 💻 3. Frontend Setup (`frontend/`)

1. **Install Frontend Dependencies**:
   From the repository root:
   ```bash
   cd frontend
   npm install
   ```

2. **Run Development Server**:
   ```bash
   npm run dev
   ```
   Alternatively, from the root directory:
   ```bash
   npm run dev:frontend
   ```
   Open [http://localhost:3000](http://localhost:3000) in your browser. You should see the GrantOS landing page shell.

---

## 🐍 4. Backend Setup (`backend/`)

1. **Create Python Virtual Environment**:
   ```bash
   cd backend
   python -m venv venv
   ```

2. **Activate Virtual Environment**:
   - **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start FastAPI Backend Server**:
   ```bash
   python -m uvicorn app.main:app --reload --port 8000
   ```
   Alternatively, from the root directory (with activated venv):
   ```bash
   npm run dev:backend
   ```

5. **Verify Health Endpoint**:
   Visit [http://localhost:8000/health](http://localhost:8000/health) or run:
   ```bash
   curl http://127.0.0.1:8000/health
   ```
   Expected response:
   ```json
   {
     "status": "ok",
     "service": "GrantOS API Engine",
     "phase": 1,
     "version": "0.1.0"
   }
   ```

---

## ⛓️ 5. Blockchain Toolchain Setup (`blockchain/`)

1. **Install Blockchain Dependencies**:
   From the repository root:
   ```bash
   cd blockchain
   npm install
   ```

2. **Compile Contracts**:
   ```bash
   npx hardhat compile
   ```

3. **Run Verification Test Suite**:
   ```bash
   npx hardhat test
   ```
   Alternatively, from the root directory:
   ```bash
   npm run test:blockchain
   ```
   Expected output: All test cases pass cleanly (`HealthCheck ping returns pong`).

---

## 🛠️ 6. Troubleshooting Common Issues

- **PowerShell Execution Policy (Windows)**:
  If activating `venv` fails on Windows, run:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
- **Port Conflicts**:
  - Web defaults to port `3000`.
  - API defaults to port `8000`.
  - Hardhat node (when running local chain in later phases) defaults to `8545`.

---

*Setup Guide Complete for Phase 1.*
