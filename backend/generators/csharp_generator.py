# C# Generator - Modern .NET patterns
from typing import Dict, Any
from .base_generator import BaseGenerator

class CSharpGenerator(BaseGenerator):
    def generate(self) -> Dict[str, str]:
        files = {}
        files["Client.cs"] = self.generate_client()
        files[f"{self.to_pascal_case(self.package_name)}.csproj"] = f"""<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="System.Net.Http.Json" Version="8.0.0" />
  </ItemGroup>
</Project>"""
        if self.include_docs:
            files["README.md"] = f"# {self.info.get('title')}\n\nC# .NET Client"
        return files
    
    def generate_client(self) -> str:
        class_name = self.to_pascal_case(self.package_name)
        return f"""
using System;
using System.Net.Http;
using System.Threading.Tasks;

namespace {class_name}
{{
    public class Client
    {{
        private readonly HttpClient _httpClient;
        private readonly string _baseUrl;
        
        public Client(string baseUrl = "{self.get_base_url()}", string apiKey = null)
        {{
            _baseUrl = baseUrl.TrimEnd('/');
            _httpClient = new HttpClient();
            if (!string.IsNullOrEmpty(apiKey))
            {{
                _httpClient.DefaultRequestHeaders.Add("Authorization", $"Bearer {{apiKey}}");
            }}
        }}
        
        public async Task<HttpResponseMessage> GetAsync(string endpoint)
        {{
            return await _httpClient.GetAsync($"{{_baseUrl}}{{endpoint}}");
        }}
    }}
}}
"""
    
    def generate_models(self) -> str:
        return f"namespace {self.to_pascal_case(self.package_name)}.Models {{ }}"
