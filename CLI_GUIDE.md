# 🚀 CLI Tool User Guide

## Overview

The **Universal API Client Generator CLI** allows you to generate API clients directly from your terminal. Perfect for automation, CI/CD pipelines, and quick local generation.

---

## 📦 Installation

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# Required packages
pip install requests pyyaml
```

### Quick Setup

```bash
# 1. Make sure the backend server is running
cd backend
python main.py

# 2. In a new terminal, use the CLI
python apigen-cli.py --help
```

---

## 🎯 Commands

### 1. Generate Client

Generate an API client from an OpenAPI specification.

```bash
python apigen-cli.py generate <spec-file> -l <language> [options]
```

**Arguments:**
- `spec-file` - Path to your OpenAPI specification (.yaml or .json)
- `-l, --language` - Target language (required)

**Options:**
- `-p, --package` - Custom package name (default: api_client)
- `-o, --output` - Output file path (default: ./<package>_<lang>.zip)
- `--tests` - Include test files
- `--no-docs` - Exclude documentation
- `--api-url` - Custom API server URL (default: http://localhost:8000)

**Examples:**

```bash
# Basic generation
python apigen-cli.py generate openapi.yaml -l python

# With custom package name
python apigen-cli.py generate openapi.yaml -l javascript -p my_awesome_api

# With tests and custom output
python apigen-cli.py generate openapi.yaml -l go --tests -o ./clients/go-client.zip

# Generate C# client
python apigen-cli.py generate openapi.yaml -l csharp -p MyAPI.Client

# Generate Java client with tests
python apigen-cli.py generate openapi.yaml -l java --tests -p com.mycompany.api
```

---

### 2. List Languages

View all supported languages and their features.

```bash
python apigen-cli.py languages
```

**Output:**
```
╔═══════════════════════════════════════════════════════╗
║   Universal API Client Generator - CLI v2.0          ║
╚═══════════════════════════════════════════════════════╝

Supported Languages:

🐍 Python                      [python]
  Type hints, async/await, dataclasses
  Status: ACTIVE

📜 JavaScript/TypeScript       [javascript]
  Promise-based, TypeScript definitions
  Status: ACTIVE

🔷 Go                          [go]
  Context support, idiomatic Go
  Status: ACTIVE

🦀 Rust                        [rust]
  Strong typing, async with Tokio
  Status: ACTIVE

💎 C#                          [csharp]
  .NET 8.0, async patterns
  Status: NEW

☕ Java                        [java]
  Maven, OkHttp, builder pattern
  Status: NEW

🐘 PHP                         [php]
  PHP 8+, Composer, Guzzle
  Status: NEW
```

---

### 3. Validate Specification

Validate your OpenAPI specification before generating.

```bash
python apigen-cli.py validate <spec-file>
```

**Example:**

```bash
python apigen-cli.py validate openapi.yaml
```

**Output:**
```
ℹ Validating OpenAPI specification: openapi.yaml
✓ OpenAPI specification is valid!

Specification Details:
  Title: Pet Store API
  Version: 1.0.0
  Endpoints: 5
```

---

## 📋 Complete Examples

### Example 1: Generate Python Client

```bash
# Validate first
python apigen-cli.py validate backend/examples/petstore.yaml

# Generate Python client
python apigen-cli.py generate backend/examples/petstore.yaml -l python -p petstore_client

# Output: ./petstore_client_python.zip
```

### Example 2: Generate Multiple Languages

```bash
# Generate for all languages
python apigen-cli.py generate openapi.yaml -l python -o ./clients/python.zip
python apigen-cli.py generate openapi.yaml -l javascript -o ./clients/js.zip
python apigen-cli.py generate openapi.yaml -l go -o ./clients/go.zip
python apigen-cli.py generate openapi.yaml -l rust -o ./clients/rust.zip
python apigen-cli.py generate openapi.yaml -l csharp -o ./clients/csharp.zip
python apigen-cli.py generate openapi.yaml -l java -o ./clients/java.zip
python apigen-cli.py generate openapi.yaml -l php -o ./clients/php.zip
```

### Example 3: CI/CD Integration

```bash
#!/bin/bash
# generate-clients.sh

# Generate clients for CI/CD
python apigen-cli.py generate api-spec.yaml -l python --tests -o dist/python-client.zip
python apigen-cli.py generate api-spec.yaml -l javascript --tests -o dist/js-client.zip

echo "✓ All clients generated successfully!"
```

### Example 4: With Custom API Server

```bash
# If your backend is running on a different port or host
python apigen-cli.py generate openapi.yaml -l python --api-url http://localhost:9000
```

---

## 🎨 CLI Output

The CLI provides colorful, informative output:

- ✓ **Green** - Success messages
- ✗ **Red** - Error messages
- ℹ **Blue** - Information
- ⚠ **Yellow** - Warnings

---

## 🔧 Troubleshooting

### Error: "Cannot connect to API server"

**Solution:**
```bash
# Make sure the backend is running
cd backend
python main.py

# In another terminal, try again
python apigen-cli.py generate openapi.yaml -l python
```

### Error: "File not found"

**Solution:**
```bash
# Check the file path
ls -la openapi.yaml

# Use absolute path if needed
python apigen-cli.py generate /full/path/to/openapi.yaml -l python
```

### Error: "Invalid OpenAPI specification"

**Solution:**
```bash
# Validate first to see specific errors
python apigen-cli.py validate openapi.yaml

# Fix the errors shown in the output
```

---

## 🚀 Advanced Usage

### Batch Generation Script

Create a script to generate multiple clients:

```python
# batch_generate.py
import subprocess
import sys

languages = ['python', 'javascript', 'go', 'rust', 'csharp', 'java', 'php']
spec_file = 'openapi.yaml'

for lang in languages:
    print(f"\n{'='*60}")
    print(f"Generating {lang.upper()} client...")
    print('='*60)
    
    result = subprocess.run([
        'python', 'apigen-cli.py', 'generate',
        spec_file, '-l', lang,
        '-o', f'./dist/{lang}-client.zip'
    ])
    
    if result.returncode != 0:
        print(f"Failed to generate {lang} client")
        sys.exit(1)

print("\n✓ All clients generated successfully!")
```

Run it:
```bash
python batch_generate.py
```

---

## 📚 Integration Examples

### GitHub Actions

```yaml
name: Generate API Clients

on:
  push:
    paths:
      - 'openapi.yaml'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          pip install requests pyyaml
      
      - name: Start API server
        run: |
          cd backend
          python main.py &
          sleep 5
      
      - name: Generate clients
        run: |
          python apigen-cli.py generate openapi.yaml -l python -o python-client.zip
          python apigen-cli.py generate openapi.yaml -l javascript -o js-client.zip
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v2
        with:
          name: api-clients
          path: |
            python-client.zip
            js-client.zip
```

### Makefile

```makefile
.PHONY: generate-all validate clean

validate:
	python apigen-cli.py validate openapi.yaml

generate-python:
	python apigen-cli.py generate openapi.yaml -l python --tests

generate-javascript:
	python apigen-cli.py generate openapi.yaml -l javascript --tests

generate-all: validate
	@echo "Generating all clients..."
	python apigen-cli.py generate openapi.yaml -l python -o dist/python.zip
	python apigen-cli.py generate openapi.yaml -l javascript -o dist/js.zip
	python apigen-cli.py generate openapi.yaml -l go -o dist/go.zip
	python apigen-cli.py generate openapi.yaml -l rust -o dist/rust.zip
	@echo "✓ Done!"

clean:
	rm -rf dist/*.zip
```

---

## 🎯 Quick Reference

```bash
# Help
python apigen-cli.py --help
python apigen-cli.py generate --help

# List languages
python apigen-cli.py languages

# Validate
python apigen-cli.py validate spec.yaml

# Generate
python apigen-cli.py generate spec.yaml -l <language>

# With options
python apigen-cli.py generate spec.yaml -l python -p my_api --tests -o output.zip
```

---

## 💡 Tips

1. **Always validate first** - Use `validate` command before generating
2. **Use meaningful package names** - Makes your code more professional
3. **Include tests** - Use `--tests` flag for production clients
4. **Automate with scripts** - Create bash/python scripts for batch generation
5. **Version control** - Keep your OpenAPI spec in git

---

## 📞 Support

- **Issues**: Check the main README.md
- **Examples**: See `backend/examples/` folder
- **Web UI**: Visit http://localhost:3000/generator for visual interface

---

**Happy Generating! 🚀**
