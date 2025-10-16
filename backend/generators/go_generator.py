# Go Generator - Idiomatic with context
from typing import Dict, Any
from .base_generator import BaseGenerator

class GoGenerator(BaseGenerator):
    def generate(self) -> Dict[str, str]:
        files = {}
        pkg = self.to_snake_case(self.package_name)
        files["client.go"] = self.generate_client()
        files["go.mod"] = f"module github.com/user/{pkg}\n\ngo 1.21"
        if self.include_docs:
            files["README.md"] = f"# {self.info.get('title')}\n\nGo Client"
        return files
    
    def generate_client(self) -> str:
        pkg = self.to_snake_case(self.package_name)
        return f"""
package {pkg}

import (
    "context"
    "net/http"
    "time"
)

type Client struct {{
    baseURL    string
    apiKey     string
    httpClient *http.Client
}}

func NewClient(baseURL, apiKey string) *Client {{
    return &Client{{
        baseURL: baseURL,
        apiKey: apiKey,
        httpClient: &http.Client{{Timeout: 30 * time.Second}},
    }}
}}
"""
    
    def generate_models(self) -> str:
        return f"package {self.to_snake_case(self.package_name)}"
