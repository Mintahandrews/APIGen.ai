"use client";

import { motion } from "framer-motion";
import Header from "@/components/components/header";
import { Mail, Github, MessageSquare } from "lucide-react";

export default function ContactPage() {
  return (
    <div className="relative min-h-screen w-full h-full flex flex-col items-center overflow-hidden">
      <Header />

      <main className="relative pt-32 pb-16 container mx-auto px-4 z-10 max-w-4xl">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-16"
        >
          <h1 className="text-6xl bp3:text-4xl font-light mb-4">
            Get in <span className="bg-gradient-to-b from-[#8096D2] to-[#b7b9be] bg-clip-text text-transparent font-semibold">Touch</span>
          </h1>
          <p className="text-white/70 max-w-2xl mx-auto">
            Have questions? We&apos;re here to help you generate amazing API clients.
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-16">
          <div className="bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-8 text-center">
            <Mail className="w-12 h-12 text-[#8096D2] mx-auto mb-4" />
            <h3 className="text-xl font-semibold mb-2">Email</h3>
            <p className="text-white/70 text-sm mb-4">
              Send us an email
            </p>
            <a href="mailto:support@apigen.ai" className="text-[#8096D2] hover:underline">
              support@apigen.ai
            </a>
          </div>

          <div className="bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-8 text-center">
            <Github className="w-12 h-12 text-[#8096D2] mx-auto mb-4" />
            <h3 className="text-xl font-semibold mb-2">GitHub</h3>
            <p className="text-white/70 text-sm mb-4">
              Open an issue
            </p>
            <a href="#" className="text-[#8096D2] hover:underline">
              View Repository
            </a>
          </div>

          <div className="bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-8 text-center">
            <MessageSquare className="w-12 h-12 text-[#8096D2] mx-auto mb-4" />
            <h3 className="text-xl font-semibold mb-2">Community</h3>
            <p className="text-white/70 text-sm mb-4">
              Join our Discord
            </p>
            <a href="#" className="text-[#8096D2] hover:underline">
              Join Server
            </a>
          </div>
        </div>

        <div className="bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-8">
          <h2 className="text-2xl font-semibold mb-6">Frequently Asked Questions</h2>
          <div className="space-y-6">
            <div>
              <h3 className="text-lg font-semibold mb-2">Is this free to use?</h3>
              <p className="text-white/70">
                Yes! The Universal API Client Generator is completely free and open source.
              </p>
            </div>
            <div>
              <h3 className="text-lg font-semibold mb-2">Which languages are supported?</h3>
              <p className="text-white/70">
                We currently support Python, JavaScript/TypeScript, Go, Rust, C#, Java, and PHP, with more coming soon.
              </p>
            </div>
            <div>
              <h3 className="text-lg font-semibold mb-2">Can I use this in my CI/CD pipeline?</h3>
              <p className="text-white/70">
                Absolutely! We provide a CLI tool specifically designed for automation and CI/CD integration.
              </p>
            </div>
            <div>
              <h3 className="text-lg font-semibold mb-2">How do I report a bug?</h3>
              <p className="text-white/70">
                Please open an issue on our GitHub repository with details about the bug and steps to reproduce it.
              </p>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
