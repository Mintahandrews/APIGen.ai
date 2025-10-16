# JavaScript/TypeScript Generator
from typing import Dict, Any
from .base_generator import BaseGenerator

class JavaScriptGenerator(BaseGenerator):
    def generate(self) -> Dict[str, str]:
        files = {}
        files["src/client.js"] = self.generate_client()
        files["src/types.d.ts"] = self.generate_types()
        files["package.json"] = f"""{{
  "name": "{self.package_name}",
  "version": "{self.info.get('version', '1.0.0')}",
  "main": "src/client.js",
  "dependencies": {{ "axios": "^1.6.0" }}
}}"""
        if self.include_docs:
            files["README.md"] = f"# {self.info.get('title')}\n\nJavaScript/TypeScript Client"
        return files
    
    def generate_client(self) -> str:
        return f"""
const axios = require('axios');

class {self.to_pascal_case(self.package_name)} {{
    constructor(options = {{}}) {{
        this.baseURL = options.baseURL || '{self.get_base_url()}';
        this.apiKey = options.apiKey;
        this.client = axios.create({{
            baseURL: this.baseURL,
            headers: this.apiKey ? {{ 'Authorization': `Bearer ${{this.apiKey}}` }} : {{}}
        }});
    }}
}}

module.exports = {self.to_pascal_case(self.package_name)};
"""
    
    def generate_types(self) -> str:
        return f"export interface ClientOptions {{ baseURL?: string; apiKey?: string; }}"
    
    def generate_models(self) -> str:
        return "// Data models\nexport interface Model {}"
