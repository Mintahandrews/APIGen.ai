"use client";

import { motion } from "framer-motion";
import Header from "@/components/components/header";
import { Book, Code2, Terminal, Zap } from "lucide-react";
import Link from "next/link";

export default function DocsPage() {
  return (
    <div className="relative min-h-screen w-full h-full flex flex-col items-center overflow-hidden">
      <Header />

      <main className="relative pt-32 pb-16 container mx-auto px-4 z-10 max-w-6xl">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-16"
        >
          <h1 className="text-6xl bp3:text-4xl font-light mb-4">
            <span className="bg-gradient-to-b from-[#8096D2] to-[#b7b9be] bg-clip-text text-transparent font-semibold">Documentation</span>
          </h1>
          <p className="text-gray-700 dark:text-white/70 max-w-2xl mx-auto transition-colors">
            Everything you need to know about generating API clients
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-16">
          <Link href="/generator">
            <div className="bg-gray-50 dark:bg-white/5 backdrop-blur-md border border-gray-200 dark:border-white/10 rounded-2xl p-8 hover:border-[#8096D2]/50 transition-all cursor-pointer">
              <Zap className="w-12 h-12 text-[#8096D2] mb-4" />
              <h3 className="text-2xl font-semibold mb-2 text-gray-900 dark:text-white transition-colors">Quick Start</h3>
              <p className="text-gray-700 dark:text-white/70 transition-colors">
                Get started in minutes. Upload your OpenAPI spec and generate your first client.
              </p>
            </div>
          </Link>

          <div className="bg-gray-50 dark:bg-white/5 backdrop-blur-md border border-gray-200 dark:border-white/10 rounded-2xl p-8 transition-all">
            <Terminal className="w-12 h-12 text-[#8096D2] mb-4" />
            <h3 className="text-2xl font-semibold mb-2 text-gray-900 dark:text-white transition-colors">CLI Tool</h3>
            <p className="text-gray-700 dark:text-white/70 mb-4 transition-colors">
              Use the command-line interface for CI/CD integration.
            </p>
            <code className="text-sm bg-gray-200 dark:bg-black/50 p-2 rounded block text-gray-900 dark:text-white transition-colors">
              python cli/generator_cli.py generate spec.yaml -l python
            </code>
          </div>

          <div className="bg-gray-50 dark:bg-white/5 backdrop-blur-md border border-gray-200 dark:border-white/10 rounded-2xl p-8 transition-all">
            <Code2 className="w-12 h-12 text-[#8096D2] mb-4" />
            <h3 className="text-2xl font-semibold mb-2 text-gray-900 dark:text-white transition-colors">API Reference</h3>
            <p className="text-gray-700 dark:text-white/70 mb-4 transition-colors">
              Complete API documentation for integration.
            </p>
            <a href="http://localhost:8000/docs" target="_blank" className="text-[#8096D2] hover:underline">
              View API Docs →
            </a>
          </div>

          <div className="bg-gray-50 dark:bg-white/5 backdrop-blur-md border border-gray-200 dark:border-white/10 rounded-2xl p-8 transition-all">
            <Book className="w-12 h-12 text-[#8096D2] mb-4" />
            <h3 className="text-2xl font-semibold mb-2 text-gray-900 dark:text-white transition-colors">Examples</h3>
            <p className="text-gray-700 dark:text-white/70 transition-colors">
              Sample OpenAPI specifications and generated clients for all supported languages.
            </p>
          </div>
        </div>

        <div className="bg-gray-50 dark:bg-white/5 backdrop-blur-md border border-gray-200 dark:border-white/10 rounded-2xl p-8 transition-all">
          <h2 className="text-3xl font-semibold mb-6 text-gray-900 dark:text-white transition-colors">Supported Languages</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {[
              { name: "Python", icon: "🐍", href: "/languages/python" },
              { name: "JavaScript", icon: "📜", href: "/languages/javascript" },
              { name: "Go", icon: "🔷", href: "/languages/go" },
              { name: "Rust", icon: "🦀", href: "/languages/rust" },
              { name: "C#", icon: "💎", href: "/languages/csharp" },
              { name: "Java", icon: "☕", href: "/languages/java" },
              { name: "PHP", icon: "🐘", href: "/languages/php" },
            ].map((lang) => (
              <Link key={lang.name} href={lang.href}>
                <div className="bg-black/30 p-4 rounded-xl hover:bg-black/50 transition-all cursor-pointer text-center">
                  <div className="text-4xl mb-2">{lang.icon}</div>
                  <div className="font-semibold">{lang.name}</div>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}
