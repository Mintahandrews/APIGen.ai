"""
Configuration file support for apigen CLI
"""
import os
import yaml
from typing import Optional, Dict, Any
from pathlib import Path


class Config:
    """Configuration manager for apigen CLI"""
    
    CONFIG_FILENAMES = ['.apigenrc.yaml', '.apigenrc.yml', 'apigen.yaml', 'apigen.yml']
    
    def __init__(self):
        self.config_data: Dict[str, Any] = {}
        self.config_path: Optional[Path] = None
    
    def load(self, config_path: Optional[str] = None) -> bool:
        """
        Load configuration from file
        
        Args:
            config_path: Optional path to config file. If None, searches for config in current directory
        
        Returns:
            True if config was loaded, False otherwise
        """
        if config_path:
            path = Path(config_path)
            if path.exists():
                self._load_from_file(path)
                return True
            return False
        
        # Search for config file in current directory
        for filename in self.CONFIG_FILENAMES:
            path = Path.cwd() / filename
            if path.exists():
                self._load_from_file(path)
                return True
        
        return False
    
    def _load_from_file(self, path: Path):
        """Load configuration from YAML file"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                self.config_data = yaml.safe_load(f) or {}
                self.config_path = path
        except Exception as e:
            print(f"Warning: Failed to load config from {path}: {e}")
            self.config_data = {}
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.config_data.get(key, default)
    
    def get_default_language(self) -> Optional[str]:
        """Get default language from config"""
        return self.get('default_language')
    
    def get_output_dir(self) -> Optional[str]:
        """Get default output directory"""
        return self.get('output_dir')
    
    def get_package_name(self) -> Optional[str]:
        """Get default package name"""
        return self.get('package_name')
    
    def get_include_tests(self) -> bool:
        """Get whether to include tests by default"""
        return self.get('include_tests', False)
    
    def get_include_docs(self) -> bool:
        """Get whether to include docs by default"""
        return self.get('include_docs', True)
    
    def get_api_url(self) -> str:
        """Get API server URL"""
        return self.get('api_url', 'http://localhost:8000')
    
    def get_custom_templates(self) -> Optional[str]:
        """Get custom templates directory"""
        return self.get('custom_templates')
    
    def get_retry_config(self) -> Dict[str, Any]:
        """Get retry configuration"""
        return self.get('retry', {
            'max_attempts': 3,
            'initial_interval': 500,
            'retry_on': ['5XX', '429', '408']
        })
    
    def get_timeout_config(self) -> Dict[str, int]:
        """Get timeout configuration"""
        return self.get('timeout', {
            'connect': 10,
            'read': 30
        })
    
    @staticmethod
    def create_example_config(path: str = '.apigenrc.yaml'):
        """Create an example configuration file"""
        example_config = """# APIGen CLI Configuration File
# Place this file in your project root as .apigenrc.yaml

# Default language for generation
default_language: python

# Default output directory
output_dir: ./generated

# Default package name
package_name: api_client

# Include test files by default
include_tests: true

# Include documentation by default
include_docs: true

# API server URL
api_url: http://localhost:8000

# Custom templates directory (optional)
# custom_templates: ./templates

# Retry configuration
retry:
  max_attempts: 3
  initial_interval: 500  # milliseconds
  max_interval: 60000
  exponent: 1.5
  retry_on:
    - "5XX"
    - "429"
    - "408"

# Timeout configuration
timeout:
  connect: 10  # seconds
  read: 30     # seconds

# Watch mode configuration
watch:
  enabled: false
  debounce: 1000  # milliseconds
  patterns:
    - "**/*.yaml"
    - "**/*.yml"
    - "**/*.json"

# Languages to generate (for batch mode)
languages:
  - python
  - javascript
  - go

# Language-specific options
language_options:
  python:
    version: "3.8+"
    async_support: true
  javascript:
    typescript: true
    target: "ES2020"
  go:
    module_path: "github.com/user/repo"
"""
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(example_config)
        
        print(f"Created example configuration file: {path}")
        print("Edit this file to customize your settings.")


def load_config(config_path: Optional[str] = None) -> Config:
    """
    Load configuration from file
    
    Args:
        config_path: Optional path to config file
    
    Returns:
        Config object
    """
    config = Config()
    config.load(config_path)
    return config
