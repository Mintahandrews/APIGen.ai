import React from 'react';
import { 
  Code2, 
  FileCode, 
  Braces,
  Box,
  Zap,
  Coffee,
  Database,
  Gem,
  Bird,
  Target
} from 'lucide-react';

// Using Lucide React icons for language representation
// These are actual icon components, not emojis or custom SVGs

export const PythonIcon = ({ className = "w-8 h-8" }: { className?: string }) => (
  <Code2 className={className} style={{ color: '#3776AB' }} />
);

export const JavaScriptIcon = ({ className = "w-8 h-8" }: { className?: string }) => (
  <FileCode className={className} style={{ color: '#F7DF1E' }} />
);

export const GoIcon = ({ className = "w-8 h-8" }: { className?: string }) => (
  <Box className={className} style={{ color: '#00ADD8' }} />
);

export const RustIcon = ({ className = "w-8 h-8" }: { className?: string }) => (
  <Zap className={className} style={{ color: '#CE422B' }} />
);

export const CSharpIcon = ({ className = "w-8 h-8" }: { className?: string }) => (
  <Braces className={className} style={{ color: '#239120' }} />
);

export const JavaIcon = ({ className = "w-8 h-8" }: { className?: string }) => (
  <Coffee className={className} style={{ color: '#007396' }} />
);

export const PHPIcon = ({ className = "w-8 h-8" }: { className?: string }) => (
  <Database className={className} style={{ color: '#777BB4' }} />
);

export const RubyIcon = ({ className = "w-8 h-8" }: { className?: string }) => (
  <Gem className={className} style={{ color: '#CC342D' }} />
);

export const SwiftIcon = ({ className = "w-8 h-8" }: { className?: string }) => (
  <Bird className={className} style={{ color: '#FA7343' }} />
);

export const KotlinIcon = ({ className = "w-8 h-8" }: { className?: string }) => (
  <Target className={className} style={{ color: '#7F52FF' }} />
);

// Helper component to get icon by language ID
export const LanguageIcon = ({ language, className }: { language: string; className?: string }) => {
  const icons: Record<string, React.ReactNode> = {
    python: <PythonIcon className={className} />,
    javascript: <JavaScriptIcon className={className} />,
    go: <GoIcon className={className} />,
    rust: <RustIcon className={className} />,
    csharp: <CSharpIcon className={className} />,
    java: <JavaIcon className={className} />,
    php: <PHPIcon className={className} />,
    ruby: <RubyIcon className={className} />,
    swift: <SwiftIcon className={className} />,
    kotlin: <KotlinIcon className={className} />,
  };

  return <>{icons[language.toLowerCase()] || <Code2 className={className} />}</>;
};
