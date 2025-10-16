"use client";

import { motion } from "framer-motion";
import Header from "@/components/components/header";
import { Code2, Zap, Globe, Sparkles, ArrowRight } from "lucide-react";
import { HoverBorderGradient } from "@/components/components/FramerButton";
import Link from "next/link";

export default function Home() {
  return (
    <div className="relative min-h-screen w-full h-full flex flex-col items-center overflow-hidden">
      <Header />

      <main className="relative pt-32 pb-16 container mx-auto px-4 z-10">
        {/* Hero Section */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="text-center space-y-6 flex flex-col gap-8 items-center justify-center"
        >
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2 }}
            className="inline-block"
          >
            <span className="relative px-4 py-2 rounded-xl flex flex-row gap-2 items-center bg-white/10 text-sm text-white/90 backdrop-blur-sm border border-white/10 overflow-hidden">
              <motion.div
                className="absolute top-0 w-[10px] h-full bg-blue-300 opacity-60 blur-md shadow-2xl"
                initial={{ left: "-10%" }}
                animate={{ left: "110%" }}
                transition={{
                  repeat: Infinity,
                  duration: 2,
                  ease: "linear",
                }}
              />
              <Sparkles className="w-4 h-4 relative z-10" />
              <p className="relative z-10">
                UNIVERSAL API CLIENT GENERATOR - 10 LANGUAGES
              </p>
            </span>
          </motion.div>

          <motion.h1
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.4 }}
            className="text-8xl bp3:text-6xl text-center font-light"
          >
            Generate <span className="bg-gradient-to-b from-[#8096D2] to-[#b7b9be] bg-clip-text text-transparent font-semibold">Idiomatic</span> API Clients
          </motion.h1>

          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.6 }}
            className="max-w-2xl mx-auto text-[15px] text-white/80"
          >
            Transform your OpenAPI specifications into production-ready API clients
            in 10 programming languages. Save time, maintain consistency, and focus
            on building great products.
          </motion.p>

          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.8 }}
            className="flex flex-col items-center gap-4"
          >
            <Link href="/generator">
              <HoverBorderGradient className="bg-gradient-to-b from-[rgb(91,105,139)] to-[#828282] px-8 py-3 text-lg font-light">
                <div className="flex items-center gap-2">
                  Try Generator Now
                  <ArrowRight className="w-5 h-5" />
                </div>
              </HoverBorderGradient>
            </Link>
            <p className="text-sm text-white/50">
              Free and open source • Generate clients instantly
            </p>
          </motion.div>
        </motion.div>

        {/* Features Section */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 1 }}
          className="mt-32 grid grid-cols-1 md:grid-cols-3 gap-8"
        >
          {/* Feature 1 */}
          <div className="bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-8 hover:border-[#8096D2]/50 transition-all">
            <div className="w-12 h-12 bg-gradient-to-br from-[#8096D2] to-[#5B698B] rounded-xl flex items-center justify-center mb-4">
              <Code2 className="w-6 h-6 text-white" />
            </div>
            <h3 className="text-xl font-semibold mb-2">10 Languages</h3>
            <p className="text-white/70 text-sm">
              Generate clients for Python, JavaScript, Go, Rust, C#, Java, PHP, and more.
              Each with idiomatic patterns and best practices.
            </p>
          </div>

          {/* Feature 2 */}
          <div className="bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-8 hover:border-[#8096D2]/50 transition-all">
            <div className="w-12 h-12 bg-gradient-to-br from-[#8096D2] to-[#5B698B] rounded-xl flex items-center justify-center mb-4">
              <Zap className="w-6 h-6 text-white" />
            </div>
            <h3 className="text-xl font-semibold mb-2">Instant Generation</h3>
            <p className="text-white/70 text-sm">
              Upload your OpenAPI spec and get production-ready clients in seconds.
              Preview code before downloading.
            </p>
          </div>

          {/* Feature 3 */}
          <div className="bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-8 hover:border-[#8096D2]/50 transition-all">
            <div className="w-12 h-12 bg-gradient-to-br from-[#8096D2] to-[#5B698B] rounded-xl flex items-center justify-center mb-4">
              <Globe className="w-6 h-6 text-white" />
            </div>
            <h3 className="text-xl font-semibold mb-2">CI/CD Ready</h3>
            <p className="text-white/70 text-sm">
              CLI tool for automation, batch generation for multiple languages,
              and seamless integration with your workflow.
            </p>
          </div>
        </motion.div>

        {/* Language Showcase */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 1.2 }}
          className="mt-32"
        >
          <h2 className="text-4xl font-light text-center mb-12">
            Supported <span className="bg-gradient-to-b from-[#8096D2] to-[#b7b9be] bg-clip-text text-transparent font-semibold">Languages</span>
          </h2>

          <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
            {[
              { name: "Python", id: "python", icon: "🐍", status: "active" },
              { name: "JavaScript", id: "javascript", icon: "📜", status: "active" },
              { name: "Go", id: "go", icon: "🔷", status: "active" },
              { name: "Rust", id: "rust", icon: "🦀", status: "active" },
              { name: "C#", id: "csharp", icon: "💎", status: "new" },
              { name: "Java", id: "java", icon: "☕", status: "new" },
              { name: "PHP", id: "php", icon: "🐘", status: "new" },
              { name: "Ruby", id: "ruby", icon: "💎", status: "soon" },
              { name: "Swift", id: "swift", icon: "🦅", status: "soon" },
              { name: "Kotlin", id: "kotlin", icon: "🎯", status: "soon" },
            ].map((lang) => (
              <div
                key={lang.name}
                className="bg-white/5 backdrop-blur-md border border-white/10 rounded-xl p-6 text-center hover:border-[#8096D2]/50 transition-all"
              >
                <div className="text-4xl mb-2">{lang.icon}</div>
                <div className="font-semibold">{lang.name}</div>
                {lang.status === "new" && (
                  <span className="text-xs px-2 py-1 bg-green-500/20 text-green-400 rounded-full mt-2 inline-block">NEW</span>
                )}
                {lang.status === "soon" && (
                  <span className="text-xs px-2 py-1 bg-yellow-500/20 text-yellow-400 rounded-full mt-2 inline-block">SOON</span>
                )}
              </div>
            ))}
          </div>
        </motion.div>

        {/* CTA Section */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 1.4 }}
          className="mt-32 text-center"
        >
          <div className="bg-gradient-to-b from-white/10 to-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-12">
            <h2 className="text-4xl font-light mb-4">
              Ready to <span className="bg-gradient-to-b from-[#8096D2] to-[#b7b9be] bg-clip-text text-transparent font-semibold">Generate</span>?
            </h2>
            <p className="text-white/70 mb-8 max-w-2xl mx-auto">
              Start generating production-ready API clients in seconds.
              No sign-up required, completely free and open source.
            </p>
            <Link href="/generator">
              <HoverBorderGradient className="bg-gradient-to-b from-[rgb(91,105,139)] to-[#828282] px-8 py-3 text-lg font-light">
                <div className="flex items-center gap-2">
                  Get Started
                  <ArrowRight className="w-5 h-5" />
                </div>
              </HoverBorderGradient>
            </Link>
          </div>
        </motion.div>
      </main>
    </div>
  );
}