# GrantOS Backend Service Engine (`backend/`)

> **FastAPI Python Backend Application**  
> **Status**: Phase 1 Foundation Active

---

## 🎯 Overview

The `backend` service powers the GrantOS backend API. It orchestrates user authorization, grant lifecycle state updates, Policy Engine rule evaluations, AI OCR/anomaly triggers, smart contract blockchain logging, and payment rail requests.

In Phase 1, only the basic application shell and `GET /health` endpoint are active.

---

## 📁 Directory Architecture

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application instance & router setup
│   └── core/
│       ├── __init__.py
│       └── config.py    # Environment configuration loader
├── requirements.txt     # Backend Python dependencies
└── README.md            # This documentation file
```

---

## 🚀 Running the API Server

1. **Activate Virtual Environment**:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Or .\venv\Scripts\Activate.ps1 on Windows
   ```

2. **Install Dependencies & Start Uvicorn Server**:
   ```bash
   pip install -r requirements.txt
   uvicorn app.main:app --reload --port 8000
   ```

3. **Verify Health**:
   ```bash
   curl http://127.0.0.1:8000/health
   ```
   Output: `{"status":"ok","service":"GrantOS API Engine","phase":1,"version":"0.1.0"}`

---

*Phase 1 Backend Foundation.*
