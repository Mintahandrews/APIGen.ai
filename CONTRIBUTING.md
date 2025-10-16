# Contributing to Universal API Client Generator

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## 🎯 Ways to Contribute

### 1. Add Support for New Languages

We're always looking to support more programming languages. Popular requests include:
- C# / .NET
- Java
- PHP
- Ruby
- Swift
- Kotlin
- Dart

**Steps to add a new language:**

1. Create a new generator class in `backend/generators/`:
```python
from .base_generator import BaseGenerator
from typing import Dict, Any

class YourLanguageGenerator(BaseGenerator):
    """Generator for YourLanguage API clients"""
    
    def generate(self) -> Dict[str, str]:
        """Generate all client files"""
        files = {}
        files["main_file.ext"] = self.generate_client()
        # Add more files...
        return files
    
    def generate_client(self) -> str:
        """Generate main client code"""
        # Implementation
        pass
    
    def generate_models(self) -> str:
        """Generate data models"""
        # Implementation
        pass
```

2. Register it in `backend/main.py`:
```python
generators = {
    "python": PythonGenerator,
    "javascript": JavaScriptGenerator,
    "go": GoGenerator,
    "rust": RustGenerator,
    "yourlang": YourLanguageGenerator,  # Add here
}
```

3. Add language info to the frontend in `src/app/generator/page.tsx`:
```typescript
const languages = [
  // ... existing languages
  {
    id: "yourlang",
    name: "Your Language",
    icon: "🔷",
    description: "Description of your language client",
    features: ["Feature 1", "Feature 2", "Feature 3", "Feature 4"]
  }
];
```

4. Create tests and documentation

### 2. Improve Code Generation Quality

- Make generated code more idiomatic
- Add better type inference
- Improve error messages
- Optimize generated code performance
- Add more comprehensive documentation in generated code

### 3. Add New Features

**Backend Features:**
- Custom code templates
- Support for more authentication schemes (OAuth, API Key in header, etc.)
- Retry logic and rate limiting
- Request/response interceptors
- Pagination helpers
- WebSocket support
- GraphQL support

**Frontend Features:**
- Drag-and-drop for multiple files
- Preview generated code before download
- Save/load configurations
- Compare different language outputs
- Dark/light theme toggle
- Code syntax highlighting in preview

### 4. Fix Bugs

Check the [Issues](../../issues) page for:
- Bug reports
- Feature requests
- Enhancement suggestions

## 🛠️ Development Setup

### Prerequisites
- Node.js 18+
- Python 3.7+
- Git

### Setup Steps

1. **Fork and clone the repository**
```bash
git clone https://github.com/yourusername/api-client-generator.git
cd api-client-generator
```

2. **Install dependencies**

Frontend:
```bash
npm install
```

Backend:
```bash
cd backend
pip install -r requirements.txt
```

3. **Run in development mode**

Terminal 1 (Backend):
```bash
cd backend
python main.py
```

Terminal 2 (Frontend):
```bash
npm run dev
```

## 📝 Code Style Guidelines

### Python (Backend)
- Follow PEP 8
- Use type hints
- Write docstrings for all public methods
- Keep functions focused and small
- Use meaningful variable names

Example:
```python
def generate_client(self) -> str:
    """
    Generate the main client class code.
    
    Returns:
        str: The generated client code
    """
    # Implementation
    pass
```

### TypeScript/React (Frontend)
- Use functional components with hooks
- Follow existing component patterns
- Use TypeScript types properly
- Keep components small and focused
- Use meaningful prop names

Example:
```typescript
interface LanguageCardProps {
  language: Language;
  selected: boolean;
  onSelect: (id: string) => void;
}

export function LanguageCard({ language, selected, onSelect }: LanguageCardProps) {
  // Implementation
}
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
npm test
```

### Manual Testing
1. Start both backend and frontend
2. Upload the example OpenAPI spec from `backend/examples/petstore.yaml`
3. Generate clients for all languages
4. Verify the generated code structure
5. Test with your own OpenAPI specifications

## 📋 Pull Request Process

1. **Create a feature branch**
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes**
- Write clean, documented code
- Add tests if applicable
- Update documentation

3. **Test your changes**
- Run all tests
- Test manually in the UI
- Verify generated code works

4. **Commit your changes**
```bash
git add .
git commit -m "Add feature: description of your changes"
```

Use clear commit messages:
- `Add: New feature`
- `Fix: Bug description`
- `Update: What was updated`
- `Refactor: What was refactored`

5. **Push to your fork**
```bash
git push origin feature/your-feature-name
```

6. **Create a Pull Request**
- Go to the original repository
- Click "New Pull Request"
- Select your branch
- Fill out the PR template
- Link any related issues

### PR Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No breaking changes (or documented if necessary)
- [ ] Tested manually
- [ ] Screenshots included (for UI changes)

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Description**: Clear description of the bug
2. **Steps to Reproduce**: Detailed steps
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **OpenAPI Spec**: Sample spec that causes the issue (if applicable)
6. **Environment**: OS, Python version, Node version
7. **Screenshots**: If applicable

## 💡 Suggesting Features

When suggesting features, please include:

1. **Use Case**: Why is this feature needed?
2. **Proposed Solution**: How should it work?
3. **Alternatives**: Other solutions you've considered
4. **Examples**: Examples from other tools (if applicable)

## 📖 Documentation

Good documentation is crucial! When contributing:

- Update README.md if adding features
- Add usage examples
- Document new configuration options
- Update API documentation
- Add inline code comments for complex logic

## 🎨 Design Principles

When contributing, keep these principles in mind:

1. **Idiomatic Code**: Generated code should feel hand-written
2. **Type Safety**: Leverage type systems when available
3. **Production Ready**: Include proper error handling
4. **Maintainable**: Clear structure and documentation
5. **Extensible**: Easy to add new features
6. **User-Friendly**: Simple and intuitive interface

## 🤝 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow
- Celebrate contributions

## 📞 Getting Help

- Open an issue for questions
- Check existing issues and PRs
- Read the documentation
- Ask in discussions

## 🏆 Recognition

Contributors will be:
- Listed in the README
- Mentioned in release notes
- Part of building something awesome!

Thank you for contributing! 🎉
