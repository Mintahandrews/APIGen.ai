#!/usr/bin/env python3
"""
Universal API Client Generator - CLI Tool v1.0
Generate API clients from OpenAPI specifications

Usage:
    apigen generate <spec-file> -l <language> [options]
    apigen languages
    apigen validate <spec-file>
"""

import sys
import os
import argparse
import json
import yaml
import requests
from pathlib import Path
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def print_header():
    """Print CLI header with rich formatting"""
    console.print(Panel.fit(
        "[bold cyan]Universal API Client Generator[/bold cyan]\n"
        "[dim]CLI Tool v1.0[/dim]",
        border_style="cyan",
        padding=(1, 2)
    ))

def load_spec(spec_file: str) -> dict:
    """Load OpenAPI specification from file"""
    try:
        with open(spec_file, 'r', encoding='utf-8') as f:
            if spec_file.endswith('.json'):
                return json.load(f)
            else:
                return yaml.safe_load(f)
    except FileNotFoundError:
        console.print(f"[red]✗[/red] File not found: {spec_file}")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]✗[/red] Failed to load spec: {str(e)}")
        sys.exit(1)

def validate_spec(spec_file: str, api_url: str = "http://localhost:8000") -> bool:
    """Validate OpenAPI specification"""
    console.print(f"\n[blue]ℹ[/blue] Validating: [cyan]{spec_file}[/cyan]")
    
    spec = load_spec(spec_file)
    
    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Validating specification...", total=None)
            
            response = requests.post(
                f"{api_url}/api/validate-json",
                json=spec,
                timeout=30
            )
            
            progress.update(task, completed=True)
        
        if response.status_code == 200:
            result = response.json()
            if result.get('valid'):
                console.print("\n[green]✓[/green] OpenAPI specification is valid!\n")
                
                # Create info table
                table = Table(show_header=False, box=box.ROUNDED, border_style="green")
                table.add_column("Property", style="cyan")
                table.add_column("Value", style="white")
                
                info = result.get('info', {})
                table.add_row("Title", info.get('title', 'N/A'))
                table.add_row("Version", info.get('version', 'N/A'))
                table.add_row("Endpoints", str(result.get('endpoints_count', 0)))
                
                console.print(table)
                return True
            else:
                console.print("\n[red]✗[/red] OpenAPI specification is invalid!\n")
                errors = result.get('errors', [])
                for error in errors:
                    console.print(f"  [red]•[/red] {error}")
                return False
        else:
            console.print(f"[red]✗[/red] Validation failed: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        console.print("\n[red]✗[/red] Cannot connect to API server")
        console.print("[yellow]ℹ[/yellow] Make sure the server is running:")
        console.print("  [dim]cd backend && python main.py[/dim]\n")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]✗[/red] Validation error: {str(e)}")
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
    console.print(f"\n[blue]ℹ[/blue] Generating [cyan]{language.upper()}[/cyan] client from: [cyan]{spec_file}[/cyan]\n")
    
    # Validate first
    if not validate_spec(spec_file, api_url):
        console.print("\n[red]✗[/red] Generation aborted due to validation errors\n")
        sys.exit(1)
    
    spec = load_spec(spec_file)
    
    # Prepare request
    data = {
        'language': language.lower(),
        'package_name': package_name or 'api_client',
        'include_tests': include_tests,
        'include_docs': include_docs
    }
    
    # Create options table
    table = Table(title="Generation Options", box=box.ROUNDED, border_style="blue")
    table.add_column("Option", style="cyan")
    table.add_column("Value", style="white")
    
    table.add_row("Language", language)
    table.add_row("Package", data['package_name'])
    table.add_row("Tests", "Yes" if include_tests else "No")
    table.add_row("Docs", "Yes" if include_docs else "No")
    
    console.print(table)
    console.print()
    
    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Generating client...", total=None)
            
            response = requests.post(
                f"{api_url}/api/generate",
                json={**data, 'spec': spec},
                timeout=60
            )
            
            progress.update(task, completed=True)
        
        if response.status_code == 200:
            # Save the ZIP file
            output_path = output_dir or f"./{data['package_name']}_{language}.zip"
            
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            console.print(f"\n[green]✓[/green] Client generated successfully!\n")
            console.print(f"[cyan]Output:[/cyan] {output_path}\n")
            
            # Next steps panel
            console.print(Panel(
                "[bold]Next Steps:[/bold]\n\n"
                "1. Extract the ZIP file\n"
                "2. Follow the README.md for installation\n"
                "3. Start using your API client!",
                border_style="green",
                title="[bold green]Success[/bold green]"
            ))
            console.print()
            
        else:
            console.print(f"\n[red]✗[/red] Generation failed: {response.text}\n")
            sys.exit(1)
            
    except requests.exceptions.ConnectionError:
        console.print("\n[red]✗[/red] Cannot connect to API server")
        console.print("[yellow]ℹ[/yellow] Make sure the server is running:")
        console.print("  [dim]cd backend && python main.py[/dim]\n")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]✗[/red] Generation error: {str(e)}\n")
        sys.exit(1)

def list_languages():
    """List all supported languages"""
    print_header()
    
    table = Table(title="\nSupported Languages", box=box.ROUNDED, border_style="cyan")
    table.add_column("Language", style="cyan bold", width=20)
    table.add_column("ID", style="dim", width=12)
    table.add_column("Features", style="white", width=40)
    table.add_column("Status", justify="center", width=10)
    
    languages = [
        ("Python", "python", "Type hints, async/await, dataclasses", "✓ Active", "green"),
        ("JavaScript/TS", "javascript", "Promises, TypeScript definitions", "✓ Active", "green"),
        ("Go", "go", "Context support, idiomatic Go", "✓ Active", "green"),
        ("Rust", "rust", "Strong typing, async with Tokio", "✓ Active", "green"),
        ("C#", "csharp", ".NET 8.0, async patterns", "⭐ New", "yellow"),
        ("Java", "java", "Maven, OkHttp, builder pattern", "⭐ New", "yellow"),
        ("PHP", "php", "PHP 8+, Composer, Guzzle", "⭐ New", "yellow"),
        ("Ruby", "ruby", "Gems, Faraday, RSpec", "⏳ Soon", "blue"),
        ("Swift", "swift", "SwiftPM, Alamofire, Codable", "⏳ Soon", "blue"),
        ("Kotlin", "kotlin", "Coroutines, Ktor, Gradle", "⏳ Soon", "blue"),
    ]
    
    for name, lang_id, features, status, color in languages:
        table.add_row(name, lang_id, features, f"[{color}]{status}[/{color}]")
    
    console.print(table)
    
    console.print("\n[bold]Usage:[/bold]")
    console.print("  [dim]apigen generate spec.yaml -l python[/dim]\n")

def main():
    parser = argparse.ArgumentParser(
        description='Universal API Client Generator CLI v1.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate Python client
  apigen generate openapi.yaml -l python
  
  # Generate with custom package name
  apigen generate openapi.yaml -l javascript -p my_api
  
  # Generate with tests and custom output
  apigen generate openapi.yaml -l go --tests -o ./output.zip
  
  # List all supported languages
  apigen languages
  
  # Validate OpenAPI spec
  apigen validate openapi.yaml
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
            console.print()
            sys.exit(0)
        else:
            console.print()
            sys.exit(1)

if __name__ == '__main__':
    main()
