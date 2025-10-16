import React from 'react';

// Simple, clean language logos using SVG paths

export const PythonLogo = ({ className = "w-8 h-8" }: { className?: string }) => (
  <svg className={className} viewBox="0 0 24 24" fill="none">
    <path d="M12 2C10.9 2 10 2.9 10 4V8H14V9H8C6.9 9 6 9.9 6 11V17C6 18.1 6.9 19 8 19H10V15H14V19H16C17.1 19 18 18.1 18 17V11C18 9.9 17.1 9 16 9H14V4C14 2.9 13.1 2 12 2Z" fill="#3776AB"/>
    <circle cx="11" cy="6" r="1" fill="#FFD43B"/>
    <circle cx="13" cy="16" r="1" fill="#3776AB"/>
  </svg>
);

export const JavaScriptLogo = ({ className = "w-8 h-8" }: { className?: string }) => (
  <svg className={className} viewBox="0 0 24 24" fill="none">
    <rect width="24" height="24" rx="3" fill="#F7DF1E"/>
    <path d="M7 18L9 18C9 19.1 9.9 20 11 20C12.1 20 13 19.1 13 18V10H11V18C11 18 11 18 11 18H9C9 18 9 18 9 18L7 18Z" fill="#000000"/>
    <path d="M14 16C14 17.1 14.9 18 16 18C17.1 18 18 17.1 18 16H20C20 18.2 18.2 20 16 20C13.8 20 12 18.2 12 16V14H14V16Z" fill="#000000"/>
  </svg>
);

export const GoLogo = ({ className = "w-8 h-8" }: { className?: string }) => (
  <svg className={className} viewBox="0 0 24 24" fill="none">
    <path d="M4 12C4 12 6 10 8 10C10 10 10 12 12 12C14 12 14 10 16 10C18 10 20 12 20 12" stroke="#00ADD8" strokeWidth="2" strokeLinecap="round"/>
    <ellipse cx="12" cy="14" rx="8" ry="4" fill="#00ADD8" opacity="0.3"/>
    <path d="M8 10C8 8.9 8.9 8 10 8H14C15.1 8 16 8.9 16 10" stroke="#00ADD8" strokeWidth="2"/>
  </svg>
);

export const RustLogo = ({ className = "w-8 h-8" }: { className?: string }) => (
  <svg className={className} viewBox="0 0 24 24" fill="none">
    <circle cx="12" cy="12" r="9" stroke="#CE422B" strokeWidth="2"/>
    <path d="M12 6L14 10H10L12 6Z" fill="#CE422B"/>
    <path d="M12 18L10 14H14L12 18Z" fill="#CE422B"/>
    <circle cx="12" cy="12" r="3" fill="#CE422B"/>
  </svg>
);

export const CSharpLogo = ({ className = "w-8 h-8" }: { className?: string }) => (
  <svg className={className} viewBox="0 0 24 24" fill="none">
    <rect width="24" height="24" rx="3" fill="#239120"/>
    <text x="12" y="17" fontSize="14" fontWeight="bold" fill="white" textAnchor="middle">C#</text>
  </svg>
);

export const JavaLogo = ({ className = "w-8 h-8" }: { className?: string }) => (
  <svg className={className} viewBox="0 0 24 24" fill="none">
    <path d="M8 18C8 18 6 17 6 15C6 13 8 12 8 12" stroke="#007396" strokeWidth="2" strokeLinecap="round"/>
    <path d="M10 16C10 16 8 15 8 13C8 11 10 10 10 10" stroke="#007396" strokeWidth="2" strokeLinecap="round"/>
    <path d="M6 20C6 20 18 22 18 18C18 14 6 16 6 20Z" fill="#007396" opacity="0.3"/>
    <ellipse cx="12" cy="7" rx="4" ry="2" fill="#007396"/>
  </svg>
);

export const PHPLogo = ({ className = "w-8 h-8" }: { className?: string }) => (
  <svg className={className} viewBox="0 0 24 24" fill="none">
    <ellipse cx="12" cy="12" rx="10" ry="6" fill="#777BB4"/>
    <text x="12" y="16" fontSize="10" fontWeight="bold" fill="white" textAnchor="middle">PHP</text>
  </svg>
);

export const RubyLogo = ({ className = "w-8 h-8" }: { className?: string }) => (
  <svg className={className} viewBox="0 0 24 24" fill="none">
    <path d="M12 4L18 10L12 20L6 10L12 4Z" fill="#CC342D"/>
    <path d="M12 4L18 10L12 12L6 10L12 4Z" fill="#E74C3C" opacity="0.7"/>
  </svg>
);

export const SwiftLogo = ({ className = "w-8 h-8" }: { className?: string }) => (
  <svg className={className} viewBox="0 0 24 24" fill="none">
    <path d="M6 18C6 18 10 14 14 10C18 6 20 6 20 6C20 6 18 8 14 12C10 16 6 18 6 18Z" fill="#FA7343"/>
    <path d="M4 16C4 16 8 12 12 8C16 4 18 4 18 4" stroke="#FA7343" strokeWidth="2" strokeLinecap="round"/>
  </svg>
);

export const KotlinLogo = ({ className = "w-8 h-8" }: { className?: string }) => (
  <svg className={className} viewBox="0 0 24 24" fill="none">
    <path d="M4 4H20L12 12L20 20H4V4Z" fill="url(#kotlinGradient)"/>
    <defs>
      <linearGradient id="kotlinGradient" x1="4" y1="4" x2="20" y2="20">
        <stop offset="0%" stopColor="#7F52FF"/>
        <stop offset="100%" stopColor="#E44857"/>
      </linearGradient>
    </defs>
  </svg>
);

// Helper component to get logo by language ID
export const LanguageLogo = ({ language, className }: { language: string; className?: string }) => {
  const logos: Record<string, React.ReactNode> = {
    python: <PythonLogo className={className} />,
    javascript: <JavaScriptLogo className={className} />,
    go: <GoLogo className={className} />,
    rust: <RustLogo className={className} />,
    csharp: <CSharpLogo className={className} />,
    java: <JavaLogo className={className} />,
    php: <PHPLogo className={className} />,
    ruby: <RubyLogo className={className} />,
    swift: <SwiftLogo className={className} />,
    kotlin: <KotlinLogo className={className} />,
  };

  return <>{logos[language.toLowerCase()] || null}</>;
};
