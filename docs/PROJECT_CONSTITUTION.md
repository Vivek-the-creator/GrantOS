# GrantOS Technical & Product Constitution

> **Version**: 1.0.0  
> **Status**: RATIFIED (Phase 0)  
> **Scope**: Foundational System Governance & Architectural Boundaries

---

## 📜 Preamble

GrantOS is established as an open, programmable, public-fund management and governance platform. Public funding represents trust, civic purpose, and societal investment. A public grant is not merely a transfer of liquidity; it is a binding societal contract containing intent, eligibility, rules, limits, validity, and auditability.

This Constitution serves as the supreme architectural and operational reference for GrantOS. All system designs, API schemas, smart contracts, AI modules, and code implementations across all project phases **must strictly adhere** to the tenets, boundaries, and authority matrices defined herein.

---

## 🏛️ SECTION 1: CORE TENETS

### Tenet 1: Purpose-Bound Liquidity
Monetary disbursements made under a GrantOS grant are intrinsically purpose-bound. Money allocated for a specified public purpose (e.g., higher education, rural healthcare, agricultural equipment) must be verified against spending rules at the point of transaction intent. Ungoverned cash-out leaks violate the core mission of GrantOS.

### Tenet 2: Deterministic Policy Authority
Financial spending rules, merchant category permissions, caps, and expiry conditions must be evaluated deterministically. Given identical state and inputs, the GrantOS Policy Engine must produce identical, explainable, and testable outputs without variance or probabilistic uncertainty.

### Tenet 3: Advisory Artificial Intelligence
Artificial Intelligence serves exclusively as an advisory, assisting, and scanning capability (e.g., OCR extraction, anomaly detection, document comparison). AI models **shall never hold independent authority** to approve grants, reject applications, revoke funds, or declare users fraudulent without explicit human officer review and governance.

### Tenet 4: Immutable Trust via Blockchain
The lifecycle state transitions of grant programs, policy definitions, milestone approvals, tranche releases, and transaction hashes must be anchored on a tamper-resistant blockchain (MST Blockchain). The ledger guarantees zero-trust auditability for citizens, regulators, and government authorities.

### Tenet 5: Off-Chain Privacy by Design
Personally Identifiable Information (PII), sensitive tax documents, identity records, private invoices, and raw medical/educational credentials **shall never be committed to a public blockchain ledger**. Sensitive data remains off-chain in encrypted storage vaults, represented on-chain solely through cryptographic hash proofs and anonymous UUID references.

### Tenet 6: Agnostic Payment Abstraction
GrantOS is strictly decoupled from specific monetary technologies. It operates above payment settlement rails (e₹/CBDC, UPI, Bank DBT, or Sandbox adapters), providing policy evaluation and governance without replacing standard fiat currency or central bank infrastructure.

---

## 🚫 SECTION 2: BOUNDARY DECLARATIONS (WHAT GRANTOS IS AND IS NOT)

To prevent scope creep, misrepresentation, and architectural degradation, the following boundary declarations are absolute:

| Domain | What GrantOS IS | What GrantOS IS NOT |
| :--- | :--- | :--- |
| **Monetary Nature** | A governance and spending policy layer over standard fiat currency (₹ INR). | **NOT** a cryptocurrency, token project, ICO, or altcoin. |
| **Financial Authority** | An authorization and policy verification engine for grant spending. | **NOT** a commercial bank, wallet provider, or licensed payment gateway. |
| **Data Processing** | A verification system using hashes, rules, and AI assistance. | **NOT** a surveillance system that exposes citizen identity data publicly. |
| **Rule Enforcement** | A deterministic Python policy engine evaluating rule tables. | **NOT** an LLM black-box deciding who gets public funding. |
| **Blockchain Usage** | An immutable audit trail and state machine for grant lifecycle events. | **NOT** a general-purpose database replacement or high-volume storage layer. |

---

## ⚖️ SECTION 3: STRICT COMPONENT AUTHORITY MATRIX

Every decision within GrantOS is assigned to a specific system component with zero overlap:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          DECISION AUTHORITY MATRIX                          │
├───────────────────────┬───────────────────────┬─────────────────────────────┤
│ System Component      │ Primary Responsibility│ Authority Level             │
├───────────────────────┼───────────────────────┼─────────────────────────────┤
│ Policy Engine         │ Real-time transaction │ ABSOLUTE & AUTHORITATIVE    │
│ (Custom Python)       │ category & cap rules  │ (Deterministic pass/fail)   │
├───────────────────────┼───────────────────────┼─────────────────────────────┤
│ Human Government      │ Application review,   │ FINAL GOVERNANCE            │
│ Administrator         │ milestone sign-off    │ (Human-in-the-loop sign-off)│
├───────────────────────┼───────────────────────┼─────────────────────────────┤
│ Assisting AI Service  │ Document OCR, risk    │ ADVISORY ONLY               │
│ (EasyOCR / LLM)       │ score, anomaly alerts │ (Flags for human review)    │
├───────────────────────┼───────────────────────┼─────────────────────────────┤
│ MST Blockchain &      │ State registry, policy│ IMMUTABLE VERIFIER          │
│ Smart Contracts       │ hashes, tranche logs  │ (Tamper-proof ledger)       │
├───────────────────────┼───────────────────────┼─────────────────────────────┤
│ Payment Abstraction   │ Settling funds via    │ EXECUTOR ONLY               │
│ Adapter               │ e₹ / UPI / Bank / Sim │ (Triggers actual transfer)  │
└───────────────────────┴───────────────────────┴─────────────────────────────┘
```

---

## 🔒 SECTION 4: PRIVACY & DATA PROTECTION SPECIFICATION

1. **Storage Tiering**:
   - **Tier 1 (Public On-Chain)**: Grant Program UUID, Encrypted State Enums, Policy Hashes, Milestone Completion Signatures, Transaction Proof Hashes.
   - **Tier 2 (Private Off-Chain DB)**: User account records, application metadata, merchant profiles, transaction logs, anomaly scoring logs.
   - **Tier 3 (Encrypted Storage Vault)**: PDF certificates, identity scans, income proofs, site photos, drone audit footage.

2. **Cryptographic Proof Chain**:
   $$\text{On-Chain Hash} = \text{SHA256}(\text{GrantUUID} \parallel \text{BeneficiaryRefHash} \parallel \text{PolicyHash} \parallel \text{State} \parallel \text{Timestamp})$$

3. **Data Erasure & Anonymization**:
   - In accordance with privacy regulations, deleting a beneficiary's off-chain profile removes PII from Tier 2 & Tier 3 storage. The on-chain hash remains structurally valid but cryptographically un-linkable to any physical identity.

---

## 🔄 SECTION 5: STATE IMMUTABILITY & LIFECYCLE RULES

1. **State Transition Integrity**: A grant cannot jump lifecycle states without satisfying defined prerequisites. For example, a grant in `CREATED` state cannot move to `RELEASED` without an explicit `APPROVED` state transition logged by an authorized Government Officer key.
2. **Policy Immutability**: Once a grant program policy is committed to the blockchain (`CREATED` state), its core spending rules and merchant category restrictions **cannot be silently altered**. Any policy modification requires a formal `POLICY_AMENDMENT` event logged on-chain.
3. **Audit Trail Completeness**: Every spending request evaluated by the Policy Engine (whether `APPROVED` or `BLOCKED`) generates an audit log payload containing the exact rule evaluation trace, timestamp, merchant MCC, and balance state.

---

## 🛠️ SECTION 6: AMENDMENT OF THE CONSTITUTION

This Constitution can only be amended prior to Phase 16 (Full Integration) through a formal Phase Revision Review requiring:
1. Updating this document (`docs/PROJECT_CONSTITUTION.md`) with explicit changelog rationale.
2. Cross-verifying consistency across `README.md`, `ARCHITECTURE.md`, `WORKFLOWS.md`, and `DEVELOPMENT_ROADMAP.md`.
3. Updating Phase acceptance criteria accordingly.

---

*Approved and ratified for GrantOS Phase 0 Development.*
