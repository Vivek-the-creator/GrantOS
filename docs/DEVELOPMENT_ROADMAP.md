# GrantOS Development Roadmap (Phases 0 – 18)

> **Execution Master Plan**  
> **Version**: 1.0.0 (Phase 0 Complete)

---

## 🗺️ Master Roadmap Overview

GrantOS is implemented strictly through an 18-phase incremental strategy. Each phase is self-contained, verifiable, and builds logically upon prior foundation layers.

```
Phase 0 ──► Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4 ──► Phase 5 ──► Phase 6
[CURRENT]  Repo Setup   Database    Auth/Roles  Gov Admin   Student/AI  Policy Eng
                                                                           │
Phase 13 ◄─ Phase 12 ◄─ Phase 11 ◄─ Phase 10 ◄─ Phase 9 ◄── Phase 8 ◄── Phase 7
AI Anomaly NGO Micro   Chain Audit MST Integration Contracts Balance Model Merchant Sim
    │
    ▼
Phase 14 ──► Phase 15 ──► Phase 16 ──► Phase 17 ──► Phase 18
Auditor UI   Security     Integration  Demo Eng    Deployment
```

---

## 📅 Detailed Phase Breakdown

### Phase 0: Project Constitution & Documentation (CURRENT)
- **Goal**: Establish project vision, architectural constitution, boundaries, workflows, and complete documentation suite.
- **Deliverables**:
  - `README.md`
  - `docs/PROJECT_CONSTITUTION.md`
  - `docs/ARCHITECTURE.md`
  - `docs/WORKFLOWS.md`
  - `docs/DEVELOPMENT_ROADMAP.md`
- **Acceptance Criteria**: All documents created, internally consistent, zero application code written.

---

### Phase 1: Repository & Monorepo Setup
- **Goal**: Establish clean monorepo folder structure, configuration files, and developer tooling.
- **Deliverables**: Folder structure (`apps/web`, `apps/server`, `contracts/`, `packages/shared`), `.gitignore`, ESLint, Prettier, Python `venv` / `poetry` setup, Hardhat configuration.
- **Acceptance Criteria**: Repository builds cleanly without dependencies errors; zero logic implemented.

---

### Phase 2: Database & Backend Foundation
- **Goal**: Scaffold FastAPI service engine, PostgreSQL connection, SQLAlchemy ORM models, and Alembic migrations.
- **Deliverables**: SQLAlchemy models (`User`, `GrantProgram`, `PolicyRule`, `Application`, `GrantBalance`, `Milestone`, `Transaction`), DB seed scripts.
- **Acceptance Criteria**: Database migrations run cleanly; test suite confirms CRUD functionality.

---

### Phase 3: Authentication & Roles
- **Goal**: Implement multi-role authentication system.
- **Deliverables**: Firebase Auth integration / JWT middleware, role enforcement decorators (`@require_role`), user registration API.
- **Acceptance Criteria**: Users register and receive JWTs with embedded role claims (`GOV_ADMIN`, `BENEFICIARY_STUDENT`, etc.).

---

### Phase 4: Government Grant Management
- **Goal**: Build frontend & backend features for Government Administrators to create grant programs and policies.
- **Deliverables**: Next.js Gov Admin dashboard, grant program creation form, policy rule builder UI, backend API endpoints.
- **Acceptance Criteria**: Admin can create "Education Grant 2026" with spending rules and persist to DB.

---

### Phase 5: Student Application & AI Verification
- **Goal**: Enable student applications and document verification assistance.
- **Deliverables**: Student application wizard, file upload component (R2/S3 integration), Python EasyOCR extraction worker, risk score generator.
- **Acceptance Criteria**: Student uploads marksheet; AI extracts text fields, generates risk score, and displays in Officer review queue.

---

### Phase 6: Core Policy Engine
- **Goal**: Build pure, deterministic Python rule evaluation engine.
- **Deliverables**: `PolicyEngine` module evaluating active state, beneficiary status, balance, merchant MCC, category rules, and spending caps.
- **Acceptance Criteria**: Comprehensive unit test suite demonstrating deterministic `APPROVED` for valid engineering tuition and `BLOCKED` for restaurant dining.

---

### Phase 7: Merchant & Spending Simulator
- **Goal**: Build interactive merchant interface and payment simulation endpoint.
- **Deliverables**: Merchant registration portal, MCC simulator dropdown, spending simulator tool.
- **Acceptance Criteria**: User can trigger payment requests from specific merchant categories to test policy evaluation.

---

### Phase 8: Grant Representation & Balance Model
- **Goal**: Build double-entry ledger tracking grant balance allocations, encumbrances, and disbursements.
- **Deliverables**: Ledger models, balance query endpoints, real-time balance update sockets/hooks.
- **Acceptance Criteria**: Balance updates immediately after an approved transaction and prevents double-spending.

---

### Phase 9: Solidity Smart Contracts
- **Goal**: Develop and test smart contracts for grant state and milestone escrow.
- **Deliverables**: `GrantRegistry.sol` and `MilestoneEscrow.sol` contracts, Hardhat unit tests.
- **Acceptance Criteria**: Smart contracts compile with 100% test pass rate on Hardhat local network.

---

### Phase 10: MST Blockchain Integration
- **Goal**: Connect FastAPI backend to MST Blockchain test environment via ethers.js / Web3.
- **Deliverables**: Blockchain service module, event listeners, transaction signer, contract deployment scripts.
- **Acceptance Criteria**: Grant issuance and milestone approvals emit transactions committed to MST testnet.

---

### Phase 11: Blockchain Audit Trail
- **Goal**: Build immutable audit logging system.
- **Deliverables**: Cryptographic hash generator, on-chain proof verification endpoints, audit log recorder.
- **Acceptance Criteria**: Every transaction generates a SHA256 proof hash successfully anchored to MST Blockchain.

---

### Phase 12: NGO Milestone Funding
- **Goal**: Build end-to-end Workflow B for multi-stage NGO milestone grants.
- **Deliverables**: NGO proposal builder, milestone evidence upload manager, officer milestone approval portal, tranche release trigger.
- **Acceptance Criteria**: NGO submits site evidence; officer approves; tranche funds release and state updates on-chain.

---

### Phase 13: AI Monitoring & Anomaly Detection
- **Goal**: Build post-spending anomaly scanner.
- **Deliverables**: Anomaly scoring pipeline scanning spending frequency, unexpected location shifts, and invoice duplication.
- **Acceptance Criteria**: System flags suspicious rapid-fire transactions for officer review.

---

### Phase 14: Auditor & Transparency Dashboard
- **Goal**: Build public/regulator dashboard for zero-trust verification.
- **Deliverables**: Auditor UI, real-time transaction feed, on-chain proof verifier component, CSV export.
- **Acceptance Criteria**: Auditor can enter a Transaction Hash and receive visual verification matching MST Blockchain logs.

---

### Phase 15: Security & Privacy
- **Goal**: Enforce PII encryption, input sanitization, and security audit.
- **Deliverables**: AES-256 field-level database encryption, CORS policies, rate limiting middleware, security audit checklist.
- **Acceptance Criteria**: Zero PII visible in API response logs or on-chain payloads.

---

### Phase 16: Full Integration
- **Goal**: Wire all components (Frontend + Backend + AI + Policy + Blockchain + Payment Adapter) into a cohesive vertical slice.
- **Deliverables**: Integrated monorepo test scripts, end-to-end test suite (Cypress / Playwright).
- **Acceptance Criteria**: Both Workflow A and Workflow B execute seamlessly end-to-end without manual database intervention.

---

### Phase 17: Demo Engineering
- **Goal**: Prepare high-impact hackathon presentation artifacts.
- **Deliverables**: Demo seed data scripts, one-click demo reset trigger, guided walkthrough tooltips, presentation slide links.
- **Acceptance Criteria**: Flawless, repeatable 3-minute hackathon demonstration showing APPROVED vs. BLOCKED payment flows.

---

### Phase 18: Final Polish & Deployment
- **Goal**: Deploy web frontend to Vercel, backend to Railway/Render, database to managed PostgreSQL, and finalize documentation.
- **Deliverables**: Production deployment URLs, live demo environment, final release notes.
- **Acceptance Criteria**: Production application accessible publicly with HTTPS.

---

## 🎯 Scope Boundary Summary

| Feature | In MVP Scope (Phases 0–18) | Post-MVP Expansion |
| :--- | :---: | :---: |
| **Workflow A (Student Grant)** | ✅ | — |
| **Workflow B (NGO Milestones)** | ✅ | — |
| **Deterministic Policy Engine** | ✅ | — |
| **Assisting AI OCR & Risk Flags** | ✅ | — |
| **MST Smart Contracts & Audit** | ✅ | — |
| **Payment Sandbox Adapter** | ✅ | — |
| **Auditor Proof Dashboard** | ✅ | — |
| **Real CBDC / e₹ Live Keys** | ❌ | ✅ |
| **Real Aadhaar KYC Biometrics** | ❌ | ✅ |
| **Autonomous AI Fraud Agents** | ❌ | ✅ |
| **Custom Cryptocurrency Token** | ❌ (Strictly Prohibited) | ❌ |

---

*Roadmap Specification Complete for Phase 0.*
