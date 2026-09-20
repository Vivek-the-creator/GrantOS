# GrantOS AI Subsystem Specification (Placeholder)

> **Status**: SPECIFICATION ONLY (No Code Implemented in Phase 1)  
> **Phase Target**: Phase 5 (Document OCR & Verification) & Phase 13 (Anomaly Detection)

---

## 🎯 Overview

The GrantOS AI Subsystem serves as an **advisory and assistance engine** designed to streamline grant application verification, document data extraction, and post-spending anomaly detection.

In accordance with the [GrantOS Constitution](file:///d:/Projects/GrantOS/docs/PROJECT_CONSTITUTION.md), **AI serves strictly an advisory role**. AI models do NOT possess independent authority to reject applicants, approve financial disbursals, or declare users fraudulent without human officer oversight.

---

## 🔮 Planned Capabilities

### 1. Document OCR & Structured Extraction (Phase 5)
- **Primary Tooling**: Python, EasyOCR / Tesseract OCR, LLM structured extraction APIs.
- **Functions**:
  - Extract text fields from uploaded PDF marksheet certificates, income certificates, and institutional invoices.
  - Parse student enrollment IDs, course names, and gross annual household income figures.
  - Compute fuzzy string match confidence scores against applicant profile data.

### 2. Anomaly & Suspicious Evidence Detection (Phase 13)
- **Functions**:
  - Scan transaction velocity to flag abnormal high-frequency spending spikes.
  - Cross-compare uploaded milestone evidence photos against known stock imagery databases to prevent duplicate invoice uploads.
  - Generate normalized `risk_score` values (0 to 100) presented to Government Officers in review queues.

---

## 📁 Directory Structure (Future Target)

```
ai/
├── README.md                  # This specification document
├── ocr/                       # EasyOCR & document parser modules (Phase 5)
├── anomaly/                   # Transaction anomaly scoring engines (Phase 13)
└── models/                    # Light ML weights & extraction schemas
```

---

*No AI logic or dependencies are active in Phase 1.*
