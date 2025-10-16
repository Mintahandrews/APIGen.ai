# Python Generator - Modern with type hints
from typing import Dict, Any
from .base_generator import BaseGenerator

class PythonGenerator(BaseGenerator):
    def generate(self) -> Dict[str, str]:
        files = {}
        files[f"{self.package_name}/client.py"] = self.generate_client()
        files[f"{self.package_name}/models.py"] = self.generate_models()
        files[f"{self.package_name}/__init__.py"] = f"""
__version__ = "{self.info.get('version', '1.0.0')}"
from .client import {self.to_pascal_case(self.package_name)}
"""
        files["requirements.txt"] = "requests>=2.31.0\npython-dateutil>=2.8.2"
        if self.include_docs:
            files["README.md"] = f"# {self.info.get('title')}\n\nPython Client"
        return files
    
    def generate_client(self) -> str:
        return f"""
import requests
from typing import Optional, Dict, Any

class {self.to_pascal_case(self.package_name)}:
    def __init__(self, base_url: str = "{self.get_base_url()}", api_key: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({{'Authorization': f'Bearer {{api_key}}'}})
    
    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{{self.base_url}}{{endpoint}}"
        return self.session.request(method, url, **kwargs)
"""
    
    def generate_models(self) -> str:
        return "# Data models\nfrom dataclasses import dataclass\nfrom typing import Optional"
