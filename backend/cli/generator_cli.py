#!/usr/bin/env python3
"""
CLI Tool for Universal API Client Generator
Enables CI/CD integration and batch processing
"""

import click
import yaml
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
import sys
import os

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from parsers.openapi_parser import OpenAPIParser
    from generators.python_generator import PythonGenerator
    from generators.javascript_generator import JavaScriptGenerator
    from generators.go_generator import GoGenerator
    from generators.rust_generator import RustGenerator
    from generators.csharp_generator import CSharpGenerator
    from generators.java_generator import JavaGenerator
    from generators.php_generator import PHPGenerator
except ImportError as e:
    print(f"Error importing generators: {e}")
    sys.exit(1)

console = Console()

GENERATORS = {
    "python": PythonGenerator,
    "javascript": JavaScriptGenerator,
    "go": GoGenerator,
    "rust": RustGenerator,
    "csharp": CSharpGenerator,
    "java": JavaGenerator,
    "php": PHPGenerator,
}

@click.group()
@click.version_option(version="1.0.0")
def cli():
    """🚀 Universal API Client Generator CLI - v1.0"""
    pass

@cli.command()
@click.argument('spec_file', type=click.Path(exists=True))
@click.option('--language', '-l', required=True, type=click.Choice(list(GENERATORS.keys())))
@click.option('--output', '-o', default='./output', help='Output directory')
@click.option('--package-name', '-p', default='api_client', help='Package name')
@click.option('--include-tests/--no-tests', default=False, help='Include test files')
@click.option('--include-docs/--no-docs', default=True, help='Include documentation')
def generate(spec_file, language, output, package_name, include_tests, include_docs):
    """Generate API client from OpenAPI specification"""
    
    console.print(f"[bold blue]🚀 Generating {language} client...[/bold blue]")
    
    try:
        # Load spec
        with open(spec_file, 'r') as f:
            if spec_file.endswith(('.yaml', '.yml')):
                spec = yaml.safe_load(f)
            else:
                spec = json.load(f)
        
        # Parse
        parser = OpenAPIParser(spec)
        parsed_data = parser.parse()
        
        # Generate
        generator_class = GENERATORS[language]
        generator = generator_class(
            parsed_data=parsed_data,
            package_name=package_name,
            include_tests=include_tests,
            include_docs=include_docs
        )
        
        generated_files = generator.generate()
        
        # Write files
        output_path = Path(output) / package_name
        output_path.mkdir(parents=True, exist_ok=True)
        
        with Progress() as progress:
            task = progress.add_task("[green]Writing files...", total=len(generated_files))
            
            for file_path, content in generated_files.items():
                full_path = output_path / file_path
                full_path.parent.mkdir(parents=True, exist_ok=True)
                full_path.write_text(content)
                progress.update(task, advance=1)
        
        console.print(f"[bold green]✅ Generated {len(generated_files)} files in {output_path}[/bold green]")
        
    except Exception as e:
        console.print(f"[bold red]❌ Error: {str(e)}[/bold red]")
        sys.exit(1)

@cli.command()
@click.argument('spec_file', type=click.Path(exists=True))
@click.option('--languages', '-l', required=True, help='Comma-separated list of languages')
@click.option('--output', '-o', default='./output', help='Output directory')
@click.option('--package-name', '-p', default='api_client', help='Package name')
def batch(spec_file, languages, output, package_name):
    """Generate clients for multiple languages at once"""
    
    lang_list = [l.strip() for l in languages.split(',')]
    
    console.print(f"[bold blue]🚀 Batch generating for {len(lang_list)} languages...[/bold blue]")
    
    for lang in lang_list:
        if lang not in GENERATORS:
            console.print(f"[yellow]⚠️  Skipping unsupported language: {lang}[/yellow]")
            continue
        
        console.print(f"[cyan]Generating {lang}...[/cyan]")
        
        try:
            # Load spec
            with open(spec_file, 'r') as f:
                if spec_file.endswith(('.yaml', '.yml')):
                    spec = yaml.safe_load(f)
                else:
                    spec = json.load(f)
            
            parser = OpenAPIParser(spec)
            parsed_data = parser.parse()
            
            generator_class = GENERATORS[lang]
            generator = generator_class(parsed_data=parsed_data, package_name=package_name)
            
            generated_files = generator.generate()
            
            output_path = Path(output) / lang / package_name
            output_path.mkdir(parents=True, exist_ok=True)
            
            for file_path, content in generated_files.items():
                full_path = output_path / file_path
                full_path.parent.mkdir(parents=True, exist_ok=True)
                full_path.write_text(content)
            
            console.print(f"[green]✅ {lang} completed ({len(generated_files)} files)[/green]")
            
        except Exception as e:
            console.print(f"[red]❌ {lang} failed: {str(e)}[/red]")
    
    console.print(f"[bold green]🎉 Batch generation complete![/bold green]")

@cli.command()
def languages():
    """List all supported programming languages"""
    
    table = Table(title="Supported Languages")
    table.add_column("Language", style="cyan")
    table.add_column("ID", style="green")
    table.add_column("Status", style="yellow")
    
    for lang_id, generator_class in GENERATORS.items():
        table.add_row(generator_class.__name__.replace("Generator", ""), lang_id, "✅ Available")
    
    console.print(table)

@cli.command()
@click.argument('spec_file', type=click.Path(exists=True))
def validate(spec_file):
    """Validate an OpenAPI specification"""
    
    console.print("[bold blue]🔍 Validating OpenAPI specification...[/bold blue]")
    
    try:
        with open(spec_file, 'r') as f:
            if spec_file.endswith(('.yaml', '.yml')):
                spec = yaml.safe_load(f)
            else:
                spec = json.load(f)
        
        parser = OpenAPIParser(spec)
        errors = parser.validate()
        
        if errors:
            console.print("[bold red]❌ Validation failed:[/bold red]")
            for error in errors:
                console.print(f"  • {error}")
            sys.exit(1)
        else:
            parsed_data = parser.parse()
            info = parsed_data['info']
            
            console.print("[bold green]✅ Valid OpenAPI specification![/bold green]")
            console.print(f"  Title: {info['title']}")
            console.print(f"  Version: {info['version']}")
            console.print(f"  Endpoints: {len(parsed_data['paths'])}")
            
    except Exception as e:
        console.print(f"[bold red]❌ Error: {str(e)}[/bold red]")
        sys.exit(1)

if __name__ == '__main__':
    cli()
