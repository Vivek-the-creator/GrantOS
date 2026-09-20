import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "GrantOS — Programmable Public-Fund Infrastructure",
  description: "End-to-end management, governance, policy evaluation, and audit infrastructure for purpose-specific public grants.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className="antialiased bg-slate-950 text-slate-100 selection:bg-sky-500 selection:text-white">
        {children}
      </body>
    </html>
  );
}
