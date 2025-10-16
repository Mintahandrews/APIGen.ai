# PHP Generator - Modern PHP 8+ patterns
from typing import Dict, Any
from .base_generator import BaseGenerator

class PHPGenerator(BaseGenerator):
    def generate(self) -> Dict[str, str]:
        files = {}
        files["src/Client.php"] = self.generate_client()
        files["composer.json"] = f"""{{
    "name": "api/{self.package_name}",
    "description": "{self.info.get('description', '')}",
    "require": {{
        "php": ">=8.1",
        "guzzlehttp/guzzle": "^7.8"
    }},
    "autoload": {{
        "psr-4": {{
            "ApiClient\\": "src/"
        }}
    }}
}}"""
        if self.include_docs:
            files["README.md"] = f"# {self.info.get('title')}\n\nPHP Client"
        return files
    
    def generate_client(self) -> str:
        class_name = self.to_pascal_case(self.package_name)
        return f"""<?php

namespace ApiClient;

use GuzzleHttp\Client as HttpClient;

class {class_name}
{{
    private HttpClient $client;
    private string $baseUrl;
    private ?string $apiKey;
    
    public function __construct(string $baseUrl = "{self.get_base_url()}", ?string $apiKey = null)
    {{
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->apiKey = $apiKey;
        
        $headers = [];
        if ($apiKey) {{
            $headers['Authorization'] = "Bearer $apiKey";
        }}
        
        $this->client = new HttpClient([
            'base_uri' => $this->baseUrl,
            'headers' => $headers,
            'timeout' => 30,
        ]);
    }}
    
    public function get(string $endpoint): array
    {{
        $response = $this->client->get($endpoint);
        return json_decode($response->getBody(), true);
    }}
}}
"""
    
    def generate_models(self) -> str:
        return "<?php\n\nnamespace ApiClient\\\\Models;"
