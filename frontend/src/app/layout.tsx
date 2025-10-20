import type React from "react";
import type { Metadata } from "next";
import { Poppins } from "next/font/google";
import "./globals.css";

const poppins = Poppins({
  subsets: ["latin"],
  weight: ["300", "400", "600", "700"],
});

export const metadata: Metadata = {
  title: {
    default: "APIGen.ai - Universal API Client Generator",
    template: "%s | APIGen.ai"
  },
  description:
    "Generate production-ready API clients in 10+ languages from OpenAPI specifications. Support for Python, JavaScript, Go, Rust, C#, Java, PHP, and more.",
  keywords: ["API", "OpenAPI", "Swagger", "Client Generator", "SDK", "Code Generation", "REST API", "GraphQL"],
  authors: [{ name: "APIGen Team" }],
  creator: "APIGen.ai",
  publisher: "APIGen.ai",
  metadataBase: new URL(process.env.NEXT_PUBLIC_BASE_URL || 'http://localhost:3000'),
  openGraph: {
    title: "APIGen.ai - Universal API Client Generator",
    description: "Generate production-ready API clients in 10+ languages from OpenAPI specifications",
    url: 'https://apigen.ai',
    siteName: 'APIGen.ai',
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: "APIGen.ai - Universal API Client Generator",
    description: "Generate production-ready API clients in 10+ languages",
    creator: '@apigenai',
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
    },
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark" suppressHydrationWarning>
      <head>
        <meta name="theme-color" content="#0C0F16" media="(prefers-color-scheme: dark)" />
        <meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)" />
      </head>
      <body className={`${poppins.className} min-h-screen transition-colors duration-300`}>
        {/* Scrollable Container */}
        <div className="relative min-h-screen overflow-hidden bg-white dark:bg-gradient-to-b dark:from-black dark:to-[#0C0F16]">
          {/* Background Grid */}
          <div className="absolute inset-0 pointer-events-none">
            <div
              className="absolute left-1/2 top-[20px] -translate-x-1/2 w-[700px] h-[700px] bg-grid-black/[0.15] dark:bg-grid-white/[0.2] bg-[length:50px_50px]"
              style={{
                maskImage:
                  "radial-gradient(circle, rgba(0,0,0,1) 20%, rgba(0,0,0,0) 60%)",
                WebkitMaskImage:
                  "radial-gradient(circle, rgba(0,0,0,1) 20%, rgba(0,0,0,0) 60%)",
              }}
            />
          </div>

          {/* Taller Triangle Glow Effect (Moved Upwards by 40px) */}
          <div className="absolute inset-x-0 top-[-80px] z-0 flex justify-center">
            {/* Larger Soft Ambient Glow */}
            <div
              className="w-0 h-0
                border-l-[450px] border-l-transparent
                border-r-[450px] border-r-transparent
                border-b-[900px] border-b-[#5B698B]/40
                blur-[100px]
                opacity-50"
            />

            {/* Inner Glow for More Softness */}
            <div
              className="absolute top-[80px]
                w-0 h-0
                border-l-[300px] border-l-transparent
                border-r-[300px] border-r-transparent
                border-b-[650px] border-b-[#5B698B]/50
                blur-[120px]
                opacity-60"
            />
          </div>

          {/* Main Content */}
          <div className="relative z-10">{children}</div>
        </div>
      </body>
    </html>
  );
}
