import React from "react";

export default function HomePage() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center p-6 md:p-12 relative overflow-hidden bg-slate-950">
      {/* Background Gradient Orbs */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[350px] bg-gradient-to-tr from-sky-600/20 to-indigo-600/20 blur-[120px] rounded-full pointer-events-none" />

      <div className="max-w-4xl w-full text-center z-10 space-y-8">
        {/* Phase Badge */}
        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-900/90 border border-slate-800 text-xs font-medium text-sky-400">
          <span className="w-2 h-2 rounded-full bg-sky-400 animate-pulse" />
          Phase 1 Infrastructure Ready — Separated Workspaces
        </div>

        {/* Hero Title */}
        <div className="space-y-3">
          <h1 className="text-4xl md:text-6xl font-extrabold tracking-tight bg-gradient-to-r from-white via-slate-200 to-slate-400 bg-clip-text text-transparent">
            GrantOS
          </h1>
          <p className="text-xl md:text-2xl font-medium text-sky-400">
            Programmable Public-Fund Infrastructure
          </p>
          <p className="max-w-2xl mx-auto text-slate-400 text-sm md:text-base leading-relaxed">
            A purpose-specific public grant governance, policy evaluation, monitoring, and zero-trust auditability platform sitting above legal monetary settlement rails.
          </p>
        </div>

        {/* Architectural Tier Status Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-6 text-left">
          <div className="glass-card p-5 rounded-xl border border-slate-800 bg-slate-900/50">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-mono text-slate-500 uppercase tracking-wider">Frontend (`frontend/`)</span>
              <span className="text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-400 border border-emerald-800">ACTIVE</span>
            </div>
            <h3 className="text-sm font-semibold text-slate-200 mb-1">Next.js App Router</h3>
            <p className="text-xs text-slate-400">Next.js 14, TypeScript, Tailwind CSS dev shell initialized.</p>
          </div>

          <div className="glass-card p-5 rounded-xl border border-slate-800 bg-slate-900/50">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-mono text-slate-500 uppercase tracking-wider">Backend (`backend/`)</span>
              <span className="text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-400 border border-emerald-800">READY</span>
            </div>
            <h3 className="text-sm font-semibold text-slate-200 mb-1">FastAPI Engine</h3>
            <p className="text-xs text-slate-400">Python 3.11 asynchronous API engine serving GET /health.</p>
          </div>

          <div className="glass-card p-5 rounded-xl border border-slate-800 bg-slate-900/50">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-mono text-slate-500 uppercase tracking-wider">Blockchain (`blockchain/`)</span>
              <span className="text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-400 border border-emerald-800">READY</span>
            </div>
            <h3 className="text-sm font-semibold text-slate-200 mb-1">MST Hardhat Environment</h3>
            <p className="text-xs text-slate-400">Solidity 0.8.24 compiler and HealthCheck test runner verified.</p>
          </div>
        </div>

        {/* Footer info */}
        <div className="pt-8 border-t border-slate-800/80 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-4">
          <div>GrantOS Monorepo Setup v0.1.0</div>
          <div>Development Phase 1 / Phase 2 Ready</div>
        </div>
      </div>
    </main>
  );
}
