"use client";

import React, { useState } from 'react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { Copy, Check, Download } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface CodePreviewProps {
  code: string;
  language: string;
  filename?: string;
  showLineNumbers?: boolean;
}

export const CodePreview: React.FC<CodePreviewProps> = ({
  code,
  language,
  filename,
  showLineNumbers = true
}) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    await navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleDownload = () => {
    const blob = new Blob([code], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename || `code.${getFileExtension(language)}`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const getFileExtension = (lang: string): string => {
    const extensions: Record<string, string> = {
      python: 'py',
      javascript: 'js',
      typescript: 'ts',
      go: 'go',
      rust: 'rs',
      java: 'java',
      csharp: 'cs',
      php: 'php',
      ruby: 'rb',
      swift: 'swift',
      kotlin: 'kt'
    };
    return extensions[lang.toLowerCase()] || 'txt';
  };

  return (
    <div className="relative rounded-xl overflow-hidden border border-white/10 bg-[#1e1e1e]">
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-2 bg-white/5 border-b border-white/10">
        <div className="flex items-center gap-2">
          {filename && (
            <span className="text-sm text-white/70 font-mono">{filename}</span>
          )}
          <span className="text-xs px-2 py-1 bg-[#8096D2]/20 text-[#8096D2] rounded">
            {language}
          </span>
        </div>
        
        <div className="flex items-center gap-2">
          <button
            onClick={handleCopy}
            className="p-2 hover:bg-white/10 rounded transition-colors"
            title="Copy to clipboard"
          >
            <AnimatePresence mode="wait">
              {copied ? (
                <motion.div
                  key="check"
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  exit={{ scale: 0 }}
                >
                  <Check className="w-4 h-4 text-green-400" />
                </motion.div>
              ) : (
                <motion.div
                  key="copy"
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  exit={{ scale: 0 }}
                >
                  <Copy className="w-4 h-4 text-white/70" />
                </motion.div>
              )}
            </AnimatePresence>
          </button>
          
          <button
            onClick={handleDownload}
            className="p-2 hover:bg-white/10 rounded transition-colors"
            title="Download file"
          >
            <Download className="w-4 h-4 text-white/70" />
          </button>
        </div>
      </div>

      {/* Code */}
      <div className="overflow-x-auto">
        <SyntaxHighlighter
          language={language}
          style={vscDarkPlus}
          showLineNumbers={showLineNumbers}
          customStyle={{
            margin: 0,
            padding: '1rem',
            background: 'transparent',
            fontSize: '0.875rem'
          }}
          lineNumberStyle={{
            minWidth: '3em',
            paddingRight: '1em',
            color: '#858585',
            userSelect: 'none'
          }}
        >
          {code}
        </SyntaxHighlighter>
      </div>
    </div>
  );
};

interface MultiFileCodePreviewProps {
  files: Array<{
    filename: string;
    code: string;
    language: string;
  }>;
}

export const MultiFileCodePreview: React.FC<MultiFileCodePreviewProps> = ({ files }) => {
  const [activeTab, setActiveTab] = useState(0);

  return (
    <div className="rounded-xl overflow-hidden border border-white/10 bg-[#1e1e1e]">
      {/* Tabs */}
      <div className="flex items-center gap-1 px-2 py-2 bg-white/5 border-b border-white/10 overflow-x-auto">
        {files.map((file, index) => (
          <button
            key={index}
            onClick={() => setActiveTab(index)}
            className={`px-4 py-2 rounded text-sm font-mono whitespace-nowrap transition-colors ${
              activeTab === index
                ? 'bg-[#8096D2]/20 text-[#8096D2]'
                : 'text-white/70 hover:bg-white/5'
            }`}
          >
            {file.filename}
          </button>
        ))}
      </div>

      {/* Active File */}
      <AnimatePresence mode="wait">
        <motion.div
          key={activeTab}
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -10 }}
          transition={{ duration: 0.2 }}
        >
          <CodePreview
            code={files[activeTab].code}
            language={files[activeTab].language}
            filename={files[activeTab].filename}
          />
        </motion.div>
      </AnimatePresence>
    </div>
  );
};
