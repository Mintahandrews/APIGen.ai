#!/usr/bin/env python3
"""
Universal API Client Generator - CLI Tool
Generate API clients from OpenAPI specifications

Usage:
    python apigen-cli.py generate <spec-file> -l <language> [options]
    python apigen-cli.py languages
    python apigen-cli.py validate <spec-file>
"""

import sys
import os
import argparse
import json
import yaml
import requests
from pathlib import Path
from typing import Optional

# ANSI color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header():
    """Print CLI header"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}╔═══════════════════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.CYAN}{Colors.BOLD}║   Universal API Client Generator - CLI v1.0          ║{Colors.ENDC}")
    print(f"{Colors.CYAN}{Colors.BOLD}╚═══════════════════════════════════════════════════════╝{Colors.ENDC}\n")

def print_success(message: str):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {message}{Colors.ENDC}")

def print_error(message: str):
    """Print error message"""
    print(f"{Colors.RED}✗ {message}{Colors.ENDC}")

def print_info(message: str):
    """Print info message"""
    print(f"{Colors.BLUE}ℹ {message}{Colors.ENDC}")

def print_warning(message: str):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠ {message}{Colors.ENDC}")

def load_spec(spec_file: str) -> dict:
    """Load OpenAPI specification from file"""
    try:
        with open(spec_file, 'r', encoding='utf-8') as f:
            if spec_file.endswith('.json'):
                return json.load(f)
            else:
                return yaml.safe_load(f)
    except FileNotFoundError:
        print_error(f"File not found: {spec_file}")
        sys.exit(1)
    except Exception as e:
        print_error(f"Failed to load spec: {str(e)}")
        sys.exit(1)

def validate_spec(spec_file: str, api_url: str = "http://localhost:8000") -> bool:
    """Validate OpenAPI specification"""
    print_info(f"Validating OpenAPI specification: {spec_file}")
    
    spec = load_spec(spec_file)
    
    try:
        response = requests.post(
            f"{api_url}/api/validate-json",
            json=spec,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get('valid'):
                print_success("OpenAPI specification is valid!")
                info = result.get('info', {})
                print(f"\n{Colors.BOLD}Specification Details:{Colors.ENDC}")
                print(f"  Title: {info.get('title', 'N/A')}")
                print(f"  Version: {info.get('version', 'N/A')}")
                print(f"  Endpoints: {result.get('endpoints_count', 0)}")
                return True
            else:
                print_error("OpenAPI specification is invalid!")
                errors = result.get('errors', [])
                for error in errors:
                    print(f"  - {error}")
                return False
        else:
            print_error(f"Validation failed: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print_error("Cannot connect to API server. Make sure it's running on http://localhost:8000")
        print_info("Start the server with: cd backend && python main.py")
        sys.exit(1)
    except Exception as e:
        print_error(f"Validation error: {str(e)}")
        return False

def generate_client(
    spec_file: str,
    language: str,
    output_dir: Optional[str] = None,
    package_name: Optional[str] = None,
    include_tests: bool = False,
    include_docs: bool = True,
    api_url: str = "http://localhost:8000"
):
    """Generate API client"""
    print_header()
    print_info(f"Generating {language.upper()} client from: {spec_file}")
    
    # Validate first
    if not validate_spec(spec_file, api_url):
        print_error("Generation aborted due to validation errors")
        sys.exit(1)
    
    spec = load_spec(spec_file)
    
    # Prepare request
    data = {
        'language': language.lower(),
        'package_name': package_name or 'api_client',
        'include_tests': include_tests,
        'include_docs': include_docs
    }
    
    print_info(f"Generating client with options:")
    print(f"  Language: {language}")
    print(f"  Package: {data['package_name']}")
    print(f"  Tests: {'Yes' if include_tests else 'No'}")
    print(f"  Docs: {'Yes' if include_docs else 'No'}")
    
    try:
        response = requests.post(
            f"{api_url}/api/generate",
            json={**data, 'spec': spec},
            timeout=60
        )
        
        if response.status_code == 200:
            # Save the ZIP file
            output_path = output_dir or f"./{data['package_name']}_{language}.zip"
            
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            print_success(f"Client generated successfully!")
            print(f"\n{Colors.BOLD}Output:{Colors.ENDC} {output_path}")
            print(f"\n{Colors.GREEN}Next steps:{Colors.ENDC}")
            print(f"  1. Extract the ZIP file")
            print(f"  2. Follow the README.md for installation")
            print(f"  3. Start using your API client!\n")
            
        else:
            print_error(f"Generation failed: {response.text}")
            sys.exit(1)
            
    except requests.exceptions.ConnectionError:
        print_error("Cannot connect to API server. Make sure it's running on http://localhost:8000")
        print_info("Start the server with: cd backend && python main.py")
        sys.exit(1)
    except Exception as e:
        print_error(f"Generation error: {str(e)}")
        sys.exit(1)

def list_languages():
    """List all supported languages"""
    print_header()
    print(f"{Colors.BOLD}Supported Languages:{Colors.ENDC}\n")
    
    languages = [
        ("python", "🐍 Python", "Type hints, async/await, dataclasses", "ACTIVE"),
        ("javascript", "📜 JavaScript/TypeScript", "Promise-based, TypeScript definitions", "ACTIVE"),
        ("go", "🔷 Go", "Context support, idiomatic Go", "ACTIVE"),
        ("rust", "🦀 Rust", "Strong typing, async with Tokio", "ACTIVE"),
        ("csharp", "💎 C#", ".NET 8.0, async patterns", "NEW"),
        ("java", "☕ Java", "Maven, OkHttp, builder pattern", "NEW"),
        ("php", "🐘 PHP", "PHP 8+, Composer, Guzzle", "NEW"),
    ]
    
    for lang_id, name, features, status in languages:
        status_color = Colors.GREEN if status == "ACTIVE" else Colors.YELLOW
        print(f"{name:<30} {Colors.BOLD}[{lang_id}]{Colors.ENDC}")
        print(f"  {Colors.CYAN}{features}{Colors.ENDC}")
        print(f"  Status: {status_color}{status}{Colors.ENDC}\n")
    
    print(f"\n{Colors.BOLD}Usage:{Colors.ENDC}")
    print(f"  python apigen-cli.py generate spec.yaml -l python\n")

def main():
    parser = argparse.ArgumentParser(
        description='Universal API Client Generator CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate Python client
  python apigen-cli.py generate openapi.yaml -l python
  
  # Generate with custom package name
  python apigen-cli.py generate openapi.yaml -l javascript -p my_api
  
  # Generate with tests and custom output
  python apigen-cli.py generate openapi.yaml -l go --tests -o ./output.zip
  
  # List all supported languages
  python apigen-cli.py languages
  
  # Validate OpenAPI spec
  python apigen-cli.py validate openapi.yaml
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Generate command
    generate_parser = subparsers.add_parser('generate', help='Generate API client')
    generate_parser.add_argument('spec_file', help='Path to OpenAPI specification file (.yaml or .json)')
    generate_parser.add_argument('-l', '--language', required=True, 
                                help='Target language (python, javascript, go, rust, csharp, java, php)')
    generate_parser.add_argument('-p', '--package', help='Package name (default: api_client)')
    generate_parser.add_argument('-o', '--output', help='Output file path (default: ./<package>_<lang>.zip)')
    generate_parser.add_argument('--tests', action='store_true', help='Include test files')
    generate_parser.add_argument('--no-docs', action='store_true', help='Exclude documentation')
    generate_parser.add_argument('--api-url', default='http://localhost:8000', 
                                help='API server URL (default: http://localhost:8000)')
    
    # Languages command
    subparsers.add_parser('languages', help='List all supported languages')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate OpenAPI specification')
    validate_parser.add_argument('spec_file', help='Path to OpenAPI specification file')
    validate_parser.add_argument('--api-url', default='http://localhost:8000',
                                help='API server URL (default: http://localhost:8000)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(0)
    
    if args.command == 'generate':
        generate_client(
            spec_file=args.spec_file,
            language=args.language,
            output_dir=args.output,
            package_name=args.package,
            include_tests=args.tests,
            include_docs=not args.no_docs,
            api_url=args.api_url
        )
    elif args.command == 'languages':
        list_languages()
    elif args.command == 'validate':
        print_header()
        if validate_spec(args.spec_file, args.api_url):
            sys.exit(0)
        else:
            sys.exit(1)

if __name__ == '__main__':
    main()
