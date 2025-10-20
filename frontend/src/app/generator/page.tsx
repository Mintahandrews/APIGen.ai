"use client";

import { motion } from "framer-motion";
import Header from "@/components/components/header";
import { useState, useRef } from "react";
import { 
  Code2, 
  Upload, 
  Download, 
  CheckCircle2, 
  AlertCircle,
  FileCode,
  Sparkles,
  Zap,
  Eye,
  Layers
} from "lucide-react";
import { HoverBorderGradient } from "@/components/components/FramerButton";

const languages = [
  {
    id: "python",
    name: "Python",
    icon: "🐍",
    description: "Modern Python with type hints and async support",
    features: ["Type Hints", "Async/Await", "Dataclasses", "Error Handling"],
    status: "available"
  },
  {
    id: "javascript",
    name: "JavaScript/TypeScript",
    icon: "📜",
    description: "Modern JS/TS with Promise support",
    features: ["TypeScript", "Promises", "ES6+", "Axios"],
    status: "available"
  },
  {
    id: "go",
    name: "Go",
    icon: "🔷",
    description: "Idiomatic Go with proper error handling",
    features: ["Structs", "Context", "Interfaces", "Error Handling"],
    status: "available"
  },
  {
    id: "rust",
    name: "Rust",
    icon: "🦀",
    description: "Safe Rust with strong typing",
    features: ["Strong Types", "Result Types", "Async/Await", "Serde"],
    status: "available"
  },
  {
    id: "csharp",
    name: "C#",
    icon: "💎",
    description: "Modern .NET 8.0 with async patterns",
    features: ["Async/Await", "LINQ", "Nullable", "Records"],
    status: "new"
  },
  {
    id: "java",
    name: "Java",
    icon: "☕",
    description: "Modern Java with Maven and OkHttp",
    features: ["Maven", "OkHttp", "Streams", "Optional"],
    status: "new"
  },
  {
    id: "php",
    name: "PHP",
    icon: "🐘",
    description: "PHP 8+ with Composer and Guzzle",
    features: ["PHP 8+", "Composer", "Guzzle", "PSR-4"],
    status: "new"
  },
  {
    id: "ruby",
    name: "Ruby",
    icon: "💎",
    description: "Ruby with Faraday HTTP client",
    features: ["Gems", "Faraday", "RSpec", "Bundler"],
    status: "coming_soon"
  },
  {
    id: "swift",
    name: "Swift",
    icon: "🦅",
    description: "Swift with Alamofire",
    features: ["SwiftPM", "Alamofire", "Codable", "Async"],
    status: "coming_soon"
  },
  {
    id: "kotlin",
    name: "Kotlin",
    icon: "🎯",
    description: "Kotlin with Ktor client",
    features: ["Coroutines", "Ktor", "Gradle", "Data Classes"],
    status: "coming_soon"
  }
];

export default function GeneratorPage() {
  const [selectedLanguages, setSelectedLanguages] = useState<string[]>(["python"]);
  const [file, setFile] = useState<File | null>(null);
  const [packageName, setPackageName] = useState("api_client");
  const [includeTests, setIncludeTests] = useState(false);
  const [includeDocs, setIncludeDocs] = useState(true);
  const [isGenerating, setIsGenerating] = useState(false);
  const [isPreviewing, setIsPreviewing] = useState(false);
  type ValidationInfo = {
    title?: string;
    version?: string;
    endpoints?: number;
  };

  type ValidationResult = {
    valid: boolean;
    info?: ValidationInfo;
  } | null;

  const [validationResult, setValidationResult] = useState<ValidationResult>(null);
  const [error, setError] = useState<string | null>(null);
  const [batchMode, setBatchMode] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const isPreviewDisabled = !file || isPreviewing || selectedLanguages.length === 0;
  const isGenerateDisabled = !file || isGenerating || selectedLanguages.length === 0;

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (selectedFile) {
      setFile(selectedFile);
      setError(null);
      
      const formData = new FormData();
      formData.append('file', selectedFile);
      
      try {
        const response = await fetch('http://localhost:8000/api/validate', {
          method: 'POST',
          body: formData,
        });
        
        const result = (await response.json()) as ValidationResult;
        setValidationResult(result);
      } catch (err) {
        console.error(err);
        setError('Failed to validate OpenAPI specification');
      }
    }
  };

  const toggleLanguage = (langId: string) => {
    if (batchMode) {
      setSelectedLanguages(prev => 
        prev.includes(langId) 
          ? prev.filter(id => id !== langId)
          : [...prev, langId]
      );
    } else {
      setSelectedLanguages([langId]);
    }
  };

  const handlePreview = async () => {
    if (!file) {
      setError('Please upload an OpenAPI specification file');
      return;
    }

    setIsPreviewing(true);
    setError(null);

    try {
      const formData = new FormData();
      formData.append('file', file);
      formData.append('language', selectedLanguages[0]);
      formData.append('package_name', packageName);

      const response = await fetch('http://localhost:8000/api/preview', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to preview code');
      }

      const result = await response.json();
      alert(`Preview:\n${JSON.stringify(result, null, 2)}`);
    } catch (err) {
      console.error(err);
      setError('Failed to preview code');
    } finally {
      setIsPreviewing(false);
    }
  };

  const handleGenerate = async () => {
    if (!file) {
      setError('Please upload an OpenAPI specification file');
      return;
    }

    if (selectedLanguages.length === 0) {
      setError('Please select at least one language');
      return;
    }

    setIsGenerating(true);
    setError(null);

    try {
      if (batchMode && selectedLanguages.length > 1) {
        // Batch generation
        const formData = new FormData();
        formData.append('file', file);
        formData.append('languages', selectedLanguages.join(','));
        formData.append('package_name', packageName);

        const response = await fetch('http://localhost:8000/api/batch-generate', {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          throw new Error('Failed to queue batch generation');
        }

        await response.json();
        alert(`Batch generation queued for: ${selectedLanguages.join(', ')}`);
      } else {
        // Single generation
        const formData = new FormData();
        formData.append('file', file);
        formData.append('language', selectedLanguages[0]);
        formData.append('package_name', packageName);
        formData.append('include_tests', includeTests.toString());
        formData.append('include_docs', includeDocs.toString());

        const response = await fetch('http://localhost:8000/api/generate', {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          const errorText = await response.text();
          throw new Error(errorText || 'Failed to generate client');
        }

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${packageName}_${selectedLanguages[0]}.zip`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
      }
    } catch (err) {
      console.error(err);
      setError('Failed to generate API client. Please try again.');
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="relative min-h-screen w-full h-full flex flex-col items-center overflow-hidden">
      <Header />

      <main className="relative pt-32 pb-16 container mx-auto px-4 z-10 max-w-7xl">
        {/* Hero Section */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="text-center space-y-6 flex flex-col gap-8 items-center justify-center mb-16"
        >
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2 }}
            className="inline-block"
          >
            <span className="relative px-4 py-2 rounded-xl flex flex-row gap-2 items-center bg-gray-100 dark:bg-white/10 text-sm text-gray-900 dark:text-white/90 backdrop-blur-sm border border-gray-200 dark:border-white/10 overflow-hidden transition-colors">
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
                10 LANGUAGES • PREVIEW • BATCH GENERATION
              </p>
            </span>
          </motion.div>

          <motion.h1
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.4 }}
            className="text-6xl bp3:text-4xl text-center font-light text-gray-900 dark:text-white transition-colors"
          >
            Generate <span className="bg-gradient-to-b from-[#8096D2] to-[#b7b9be] bg-clip-text text-transparent font-semibold">Idiomatic</span> API Clients
          </motion.h1>

          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.6 }}
            className="max-w-2xl mx-auto text-[15px] text-gray-700 dark:text-white/80 transition-colors"
          >
            Transform your OpenAPI specifications into production-ready API clients
            in 10 programming languages. Preview code, batch generate, and integrate with CI/CD.
          </motion.p>

          {/* Batch Mode Toggle */}
          <div className="flex items-center gap-3">
            <input
              type="checkbox"
              id="batchMode"
              checked={batchMode}
              onChange={(e) => setBatchMode(e.target.checked)}
              className="w-4 h-4 rounded border-white/20"
            />
            <label htmlFor="batchMode" className="text-sm flex items-center gap-2 text-gray-900 dark:text-white transition-colors">
              <Layers className="w-4 h-4" />
              Batch Mode (select multiple languages)
            </label>
          </div>
        </motion.div>

        {/* Main Generator Interface */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-16">
          {/* Left Column - Configuration */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.8 }}
            className="space-y-6"
          >
            {/* File Upload */}
            <div className="bg-gray-50 dark:bg-white/5 backdrop-blur-md border border-gray-200 dark:border-white/10 rounded-2xl p-6 transition-all">
              <h3 className="text-xl font-semibold mb-4 flex items-center gap-2 text-gray-900 dark:text-white transition-colors">
                <Upload className="w-5 h-5 text-[#8096D2]" />
                Upload OpenAPI Specification
              </h3>
              
              <div
                onClick={() => fileInputRef.current?.click()}
                className="border-2 border-dashed border-gray-300 dark:border-white/20 rounded-xl p-8 text-center cursor-pointer hover:border-[#8096D2] transition-colors"
              >
                <FileCode className="w-12 h-12 mx-auto mb-4 text-gray-400 dark:text-white/50 transition-colors" />
                <p className="text-gray-700 dark:text-white/70 mb-2 transition-colors">
                  {file ? file.name : 'Click to upload or drag and drop'}
                </p>
                <p className="text-sm text-gray-500 dark:text-white/50 transition-colors">
                  YAML or JSON format
                </p>
                <input
                  ref={fileInputRef}
                  type="file"
                  accept=".yaml,.yml,.json"
                  onChange={handleFileChange}
                  className="hidden"
                />
              </div>

              {validationResult && (
                <div className={`mt-4 p-4 rounded-lg ${validationResult.valid ? 'bg-green-500/10 border border-green-500/20' : 'bg-red-500/10 border border-red-500/20'}`}>
                  <div className="flex items-center gap-2 mb-2">
                    {validationResult.valid ? (
                      <CheckCircle2 className="w-5 h-5 text-green-500" />
                    ) : (
                      <AlertCircle className="w-5 h-5 text-red-500" />
                    )}
                    <span className={validationResult.valid ? 'text-green-500' : 'text-red-500'}>
                      {validationResult.valid ? 'Valid OpenAPI Specification' : 'Invalid Specification'}
                    </span>
                  </div>
                  {validationResult.valid && validationResult.info && (
                    <div className="text-sm text-gray-700 dark:text-white/70 space-y-1 transition-colors">
                      <p>Title: {validationResult.info.title}</p>
                      <p>Version: {validationResult.info.version}</p>
                      <p>Endpoints: {validationResult.info.endpoints}</p>
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* Configuration Options */}
            <div className="bg-gray-50 dark:bg-white/5 backdrop-blur-md border border-gray-200 dark:border-white/10 rounded-2xl p-6 transition-all">
              <h3 className="text-xl font-semibold mb-4 flex items-center gap-2 text-gray-900 dark:text-white transition-colors">
                <Code2 className="w-5 h-5 text-[#8096D2]" />
                Configuration
              </h3>

              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium mb-2 text-gray-900 dark:text-white transition-colors">Package Name</label>
                  <input
                    type="text"
                    value={packageName}
                    onChange={(e) => setPackageName(e.target.value)}
                    className="w-full bg-gray-100 dark:bg-white/5 border border-gray-300 dark:border-white/10 rounded-lg px-4 py-2 text-gray-900 dark:text-white focus:outline-none focus:border-[#8096D2] transition-colors"
                    placeholder="api_client"
                  />
                </div>

                <div className="flex items-center gap-3">
                  <input
                    type="checkbox"
                    id="includeTests"
                    checked={includeTests}
                    onChange={(e) => setIncludeTests(e.target.checked)}
                    className="w-4 h-4 rounded border-white/20"
                  />
                  <label htmlFor="includeTests" className="text-sm text-gray-900 dark:text-white transition-colors">Include Unit Tests</label>
                </div>

                <div className="flex items-center gap-3">
                  <input
                    type="checkbox"
                    id="includeDocs"
                    checked={includeDocs}
                    onChange={(e) => setIncludeDocs(e.target.checked)}
                    className="w-4 h-4 rounded border-white/20"
                  />
                  <label htmlFor="includeDocs" className="text-sm text-gray-900 dark:text-white transition-colors">Include Documentation</label>
                </div>
              </div>
            </div>
          </motion.div>

          {/* Right Column - Language Selection */}
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.8 }}
            className="space-y-6"
          >
            <div className="bg-gray-50 dark:bg-white/5 backdrop-blur-md border border-gray-200 dark:border-white/10 rounded-2xl p-6 transition-all">
              <h3 className="text-xl font-semibold mb-4 flex items-center gap-2 text-gray-900 dark:text-white transition-colors">
                <Zap className="w-5 h-5 text-[#8096D2]" />
                Select Target Language{batchMode ? 's' : ''}
              </h3>

              <div className="grid grid-cols-1 gap-3 max-h-[600px] overflow-y-auto">
                {languages.map((lang) => (
                  <div
                    key={lang.id}
                    onClick={() => lang.status !== 'coming_soon' && toggleLanguage(lang.id)}
                    className={`p-3 rounded-xl cursor-pointer transition-all ${
                      selectedLanguages.includes(lang.id)
                        ? 'bg-[#8096D2]/20 border-2 border-[#8096D2]'
                        : lang.status === 'coming_soon'
                        ? 'bg-white/5 border border-white/10 opacity-50 cursor-not-allowed'
                        : 'bg-white/5 border border-white/10 hover:border-white/20'
                    }`}
                  >
                    <div className="flex items-start gap-3">
                      <span className="text-2xl">{lang.icon}</span>
                      <div className="flex-1">
                        <div className="flex items-center gap-2">
                          <h4 className="font-semibold text-base">{lang.name}</h4>
                          {lang.status === 'new' && (
                            <span className="text-xs px-2 py-0.5 bg-green-500/20 text-green-400 rounded-full">NEW</span>
                          )}
                          {lang.status === 'coming_soon' && (
                            <span className="text-xs px-2 py-0.5 bg-yellow-500/20 text-yellow-400 rounded-full">SOON</span>
                          )}
                        </div>
                        <p className="text-xs text-gray-700 dark:text-white/70 mb-2 transition-colors">{lang.description}</p>
                        <div className="flex flex-wrap gap-1">
                          {lang.features.map((feature) => (
                            <span
                              key={feature}
                              className="text-xs px-2 py-0.5 bg-gray-200 dark:bg-white/10 rounded-full text-gray-900 dark:text-white transition-colors"
                            >
                              {feature}
                            </span>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </motion.div>
        </div>

        {/* Action Buttons */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 1 }}
          className="flex flex-col items-center gap-4"
        >
          {error && (
            <div className="bg-red-500/10 border border-red-500/20 rounded-lg p-4 text-red-400">
              {error}
            </div>
          )}

          <div className="flex gap-4">
            <HoverBorderGradient
              onClick={() => {
                if (isPreviewDisabled) return;
                void handlePreview();
              }}
              className={`bg-gradient-to-b from-[rgb(91,105,139)] to-[#828282] px-6 py-3 ${
                isPreviewDisabled ? 'opacity-50 cursor-not-allowed pointer-events-none' : ''
              }`}
            >
              <div className="flex items-center gap-2">
                <Eye className="w-5 h-5" />
                {isPreviewing ? 'Previewing...' : 'Preview Code'}
              </div>
            </HoverBorderGradient>

            <HoverBorderGradient
              onClick={() => {
                if (isGenerateDisabled) return;
                void handleGenerate();
              }}
              className={`bg-gradient-to-b from-[rgb(91,105,139)] to-[#828282] px-8 py-3 text-lg ${
                isGenerateDisabled ? 'opacity-50 cursor-not-allowed pointer-events-none' : ''
              }`}
            >
              <div className="flex items-center gap-2">
                {isGenerating ? (
                  <>
                    <div className="w-5 h-5 border-2 border-white/20 border-t-white rounded-full animate-spin" />
                    Generating...
                  </>
                ) : (
                  <>
                    <Download className="w-5 h-5" />
                    Generate {batchMode && selectedLanguages.length > 1 ? `(${selectedLanguages.length})` : 'Client'}
                  </>
                )}
              </div>
            </HoverBorderGradient>
          </div>

          {selectedLanguages.length > 0 && (
            <p className="text-sm text-gray-500 dark:text-white/50 transition-colors">
              Selected: {selectedLanguages.map(id => languages.find(l => l.id === id)?.name).join(', ')}
            </p>
          )}
        </motion.div>
      </main>
    </div>
  );
}