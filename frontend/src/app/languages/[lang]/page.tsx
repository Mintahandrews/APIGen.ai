"use client";

import { motion } from "framer-motion";
import Header from "@/components/components/header";
import { use } from "react";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { HoverBorderGradient } from "@/components/components/FramerButton";

type LanguageDetails = {
  name: string;
  icon: string;
  description: string;
  features: string[];
  example: string;
};

const languageData: Record<string, LanguageDetails> = {
  python: {
    name: "Python",
    icon: "🐍",
    description: "Generate idiomatic Python clients with type hints and async support",
    features: [
      "Type hints for better IDE support",
      "Async/await support",
      "Dataclasses for models",
      "Comprehensive error handling",
      "Requests library integration",
      "Auto-generated documentation"
    ],
    example: `from api_client import APIClient

client = APIClient(
    base_url="https://api.example.com",
    api_key="your-key"
)

# Make API calls
result = client.list_pets(params={"limit": 10})
print(result)`
  },
  javascript: {
    name: "JavaScript/TypeScript",
    icon: "📜",
    description: "Modern JavaScript/TypeScript clients with Promise support",
    features: [
      "TypeScript definitions included",
      "Promise-based API",
      "ES6+ syntax",
      "Axios integration",
      "Automatic type inference",
      "JSDoc comments"
    ],
    example: `const APIClient = require('api-client');

const client = new APIClient({
    baseURL: 'https://api.example.com',
    apiKey: 'your-key'
});

// Make API calls
const result = await client.listPets({ limit: 10 });
console.log(result);`
  },
  go: {
    name: "Go",
    icon: "🔷",
    description: "Idiomatic Go clients with context support",
    features: [
      "Context support",
      "Struct-based models",
      "Interface-based design",
      "Proper error handling",
      "Standard library HTTP",
      "Go modules support"
    ],
    example: `package main

import "api-client"

func main() {
    client := apiclient.NewClient(
        apiclient.WithBaseURL("https://api.example.com"),
        apiclient.WithAPIKey("your-key"),
    )
    
    result, err := client.ListPets(ctx, nil)
}`
  },
  rust: {
    name: "Rust",
    icon: "🦀",
    description: "Safe Rust clients with strong typing",
    features: [
      "Strong typing",
      "Result types",
      "Async/await with Tokio",
      "Serde integration",
      "Reqwest HTTP client",
      "Comprehensive error types"
    ],
    example: `use api_client::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(
        "https://api.example.com",
        Some("your-key".to_string())
    )?;
    
    let result = client.list_pets(None).await?;
    Ok(())
}`
  },
  csharp: {
    name: "C#",
    icon: "💎",
    description: "Modern .NET clients with async patterns",
    features: [
      ".NET 8.0 support",
      "Async/await patterns",
      "LINQ support",
      "Nullable reference types",
      "HttpClient integration",
      "XML documentation"
    ],
    example: `using APIClient;

var client = new Client(
    "https://api.example.com",
    "your-key"
);

var result = await client.GetAsync("/pets");`
  },
  java: {
    name: "Java",
    icon: "☕",
    description: "Modern Java clients with Maven support",
    features: [
      "Maven integration",
      "OkHttp client",
      "Stream API support",
      "Optional types",
      "Javadoc comments",
      "Builder pattern"
    ],
    example: `import com.api.APIClient;

APIClient client = new APIClient(
    "https://api.example.com",
    "your-key"
);

Response response = client.get("/pets");`
  },
  php: {
    name: "PHP",
    icon: "🐘",
    description: "PHP 8+ clients with Composer support",
    features: [
      "PHP 8+ features",
      "Composer integration",
      "Guzzle HTTP client",
      "PSR-4 autoloading",
      "Type declarations",
      "PHPDoc comments"
    ],
    example: `<?php

use ApiClient\\Client;

$client = new Client(
    'https://api.example.com',
    'your-key'
);

$result = $client->get('/pets');`
  }
};

export default function LanguagePage({ params }: { params: Promise<{ lang: string }> }) {
  const { lang } = use(params);
  const data = languageData[lang] || languageData.python;

  return (
    <div className="relative min-h-screen w-full h-full flex flex-col items-center overflow-hidden">
      <Header />

      <main className="relative pt-32 pb-16 container mx-auto px-4 z-10 max-w-6xl">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center mb-16"
        >
          <div className="text-8xl mb-4">{data.icon}</div>
          <h1 className="text-6xl bp3:text-4xl font-light mb-4">
            {data.name} <span className="bg-gradient-to-b from-[#8096D2] to-[#b7b9be] bg-clip-text text-transparent font-semibold">Client</span>
          </h1>
          <p className="text-white/70 max-w-2xl mx-auto mb-8">
            {data.description}
          </p>
          <Link href="/generator">
            <HoverBorderGradient className="bg-gradient-to-b from-[rgb(91,105,139)] to-[#828282] px-8 py-3">
              <div className="flex items-center gap-2">
                Generate {data.name} Client
                <ArrowRight className="w-5 h-5" />
              </div>
            </HoverBorderGradient>
          </Link>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
          <div className="bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-8">
            <h2 className="text-2xl font-semibold mb-6">Features</h2>
            <ul className="space-y-3">
              {data.features.map((feature: string, idx: number) => (
                <li key={idx} className="flex items-start gap-3">
                  <span className="text-[#8096D2] mt-1">✓</span>
                  <span className="text-white/80">{feature}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-8">
            <h2 className="text-2xl font-semibold mb-6">Example Usage</h2>
            <pre className="bg-black/50 p-4 rounded-lg overflow-x-auto">
              <code className="text-sm text-white/90">{data.example}</code>
            </pre>
          </div>
        </div>

        <div className="bg-gradient-to-b from-white/10 to-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-12 text-center">
          <h2 className="text-3xl font-light mb-4">
            Ready to generate your {data.name} client?
          </h2>
          <p className="text-white/70 mb-8">
            Upload your OpenAPI specification and get production-ready code in seconds.
          </p>
          <Link href="/generator">
            <HoverBorderGradient className="bg-gradient-to-b from-[rgb(91,105,139)] to-[#828282] px-8 py-3">
              <div className="flex items-center gap-2">
                Start Generating
                <ArrowRight className="w-5 h-5" />
              </div>
            </HoverBorderGradient>
          </Link>
        </div>
      </main>
    </div>
  );
}
