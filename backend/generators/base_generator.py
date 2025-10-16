from typing import Dict, Any, List
from abc import ABC, abstractmethod
import re

class BaseGenerator(ABC):
    """Base class for all language-specific generators - 2025 Modern Patterns"""
    
    def __init__(self, parsed_data: Dict[str, Any], package_name: str = "api_client",
                 include_tests: bool = False, include_docs: bool = True):
        self.parsed_data = parsed_data
        self.package_name = package_name
        self.include_tests = include_tests
        self.include_docs = include_docs
        self.info = parsed_data.get("info", {})
        self.servers = parsed_data.get("servers", [])
        self.paths = parsed_data.get("paths", [])
        self.components = parsed_data.get("components", {})
        self.security = parsed_data.get("security", [])
    
    @abstractmethod
    def generate(self) -> Dict[str, str]:
        """Generate all client files. Returns dict of {filepath: content}"""
        pass
    
    @abstractmethod
    def generate_client(self) -> str:
        """Generate main client class"""
        pass
    
    @abstractmethod
    def generate_models(self) -> str:
        """Generate data models/types"""
        pass
    
    def sanitize_name(self, name: str) -> str:
        """Sanitize names for use in code"""
        sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', name)
        sanitized = re.sub(r'^[0-9]+', '', sanitized)
        return sanitized
    
    def to_snake_case(self, name: str) -> str:
        """Convert name to snake_case"""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
        return s2.lower()
    
    def to_camel_case(self, name: str) -> str:
        """Convert name to camelCase"""
        components = name.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
    
    def to_pascal_case(self, name: str) -> str:
        """Convert name to PascalCase"""
        return ''.join(x.title() for x in name.split('_'))
    
    def get_base_url(self) -> str:
        """Get the base URL from servers"""
        if self.servers:
            return self.servers[0].get("url", "")
        return ""
    
    def group_paths_by_tag(self) -> Dict[str, List[Dict[str, Any]]]:
        """Group API paths by their tags"""
        grouped = {}
        
        for path in self.paths:
            tags = path.get("tags", ["default"])
            for tag in tags:
                if tag not in grouped:
                    grouped[tag] = []
                grouped[tag].append(path)
        
        return grouped
    
    def get_type_from_schema(self, schema: Dict[str, Any], language: str) -> str:
        """Get type string from OpenAPI schema"""
        if not schema:
            return self._get_default_type(language)
        
        schema_type = schema.get("type", "object")
        
        type_mappings = {
            "python": {
                "string": "str",
                "integer": "int",
                "number": "float",
                "boolean": "bool",
                "array": "List",
                "object": "Dict[str, Any]"
            },
            "javascript": {
                "string": "string",
                "integer": "number",
                "number": "number",
                "boolean": "boolean",
                "array": "Array",
                "object": "object"
            },
            "go": {
                "string": "string",
                "integer": "int",
                "number": "float64",
                "boolean": "bool",
                "array": "[]interface{}",
                "object": "map[string]interface{}"
            },
            "rust": {
                "string": "String",
                "integer": "i64",
                "number": "f64",
                "boolean": "bool",
                "array": "Vec<serde_json::Value>",
                "object": "serde_json::Value"
            },
            "csharp": {
                "string": "string",
                "integer": "int",
                "number": "double",
                "boolean": "bool",
                "array": "List<object>",
                "object": "Dictionary<string, object>"
            },
            "java": {
                "string": "String",
                "integer": "Integer",
                "number": "Double",
                "boolean": "Boolean",
                "array": "List<Object>",
                "object": "Map<String, Object>"
            },
            "php": {
                "string": "string",
                "integer": "int",
                "number": "float",
                "boolean": "bool",
                "array": "array",
                "object": "array"
            }
        }
        
        return type_mappings.get(language, {}).get(schema_type, self._get_default_type(language))
    
    def _get_default_type(self, language: str) -> str:
        """Get default/any type for language"""
        defaults = {
            "python": "Any",
            "javascript": "any",
            "go": "interface{}",
            "rust": "serde_json::Value",
            "csharp": "object",
            "java": "Object",
            "php": "mixed"
        }
        return defaults.get(language, "any")
