from typing import Dict, Any, List, Optional
import re

class OpenAPIParser:
    """Parser for OpenAPI 3.0 specifications - 2025 Best Practices"""
    
    def __init__(self, spec: Dict[str, Any]):
        self.spec = spec
        self.openapi_version = spec.get("openapi", "3.0.0")
        
    def validate(self) -> List[str]:
        """Validate the OpenAPI specification"""
        errors = []
        
        if "openapi" not in self.spec:
            errors.append("Missing 'openapi' field")
        if "info" not in self.spec:
            errors.append("Missing 'info' field")
        elif "title" not in self.spec["info"]:
            errors.append("Missing 'info.title' field")
        if "paths" not in self.spec or not self.spec["paths"]:
            errors.append("Missing or empty 'paths' field")
            
        return errors
    
    def parse(self) -> Dict[str, Any]:
        """Parse the OpenAPI specification into a structured format"""
        return {
            "info": self._parse_info(),
            "servers": self._parse_servers(),
            "paths": self._parse_paths(),
            "components": self._parse_components(),
            "security": self._parse_security()
        }
    
    def _parse_info(self) -> Dict[str, Any]:
        """Parse API information"""
        info = self.spec.get("info", {})
        return {
            "title": info.get("title", "API Client"),
            "version": info.get("version", "1.0.0"),
            "description": info.get("description", ""),
            "contact": info.get("contact", {}),
            "license": info.get("license", {})
        }
    
    def _parse_servers(self) -> List[Dict[str, Any]]:
        """Parse server information"""
        servers = self.spec.get("servers", [])
        if not servers:
            return [{"url": "http://localhost", "description": "Default server"}]
        return servers
    
    def _parse_paths(self) -> List[Dict[str, Any]]:
        """Parse API paths/endpoints"""
        paths = []
        
        for path, path_item in self.spec.get("paths", {}).items():
            for method, operation in path_item.items():
                if method in ["get", "post", "put", "patch", "delete", "options", "head"]:
                    paths.append({
                        "path": path,
                        "method": method.upper(),
                        "operation_id": operation.get("operationId", self._generate_operation_id(method, path)),
                        "summary": operation.get("summary", ""),
                        "description": operation.get("description", ""),
                        "parameters": self._parse_parameters(operation.get("parameters", [])),
                        "request_body": self._parse_request_body(operation.get("requestBody")),
                        "responses": self._parse_responses(operation.get("responses", {})),
                        "security": operation.get("security", []),
                        "tags": operation.get("tags", [])
                    })
        
        return paths
    
    def _parse_parameters(self, parameters: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Parse operation parameters"""
        parsed_params = []
        
        for param in parameters:
            parsed_params.append({
                "name": param.get("name"),
                "in": param.get("in"),
                "description": param.get("description", ""),
                "required": param.get("required", False),
                "schema": param.get("schema", {}),
                "example": param.get("example")
            })
        
        return parsed_params
    
    def _parse_request_body(self, request_body: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Parse request body"""
        if not request_body:
            return None
        
        content = request_body.get("content", {})
        
        return {
            "description": request_body.get("description", ""),
            "required": request_body.get("required", False),
            "content": content
        }
    
    def _parse_responses(self, responses: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Parse operation responses"""
        parsed_responses = []
        
        for status_code, response in responses.items():
            parsed_responses.append({
                "status_code": status_code,
                "description": response.get("description", ""),
                "content": response.get("content", {}),
                "headers": response.get("headers", {})
            })
        
        return parsed_responses
    
    def _parse_components(self) -> Dict[str, Any]:
        """Parse reusable components"""
        components = self.spec.get("components", {})
        
        return {
            "schemas": components.get("schemas", {}),
            "security_schemes": components.get("securitySchemes", {}),
            "parameters": components.get("parameters", {}),
            "responses": components.get("responses", {}),
            "request_bodies": components.get("requestBodies", {})
        }
    
    def _parse_security(self) -> List[Dict[str, Any]]:
        """Parse global security requirements"""
        return self.spec.get("security", [])
    
    def _generate_operation_id(self, method: str, path: str) -> str:
        """Generate operation ID from method and path"""
        clean_path = re.sub(r'\{[^}]+\}', '', path)
        parts = [p for p in clean_path.split('/') if p]
        
        if not parts:
            return f"{method}_root"
        
        operation_id = method + '_' + '_'.join(parts)
        return re.sub(r'[^a-zA-Z0-9_]', '_', operation_id)
