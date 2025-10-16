# Rust Generator - Safe with strong typing
from typing import Dict, Any
from .base_generator import BaseGenerator

class RustGenerator(BaseGenerator):
    def generate(self) -> Dict[str, str]:
        files = {}
        files["src/lib.rs"] = self.generate_lib()
        files["src/client.rs"] = self.generate_client()
        files["Cargo.toml"] = f"""[package]
name = "{self.to_snake_case(self.package_name)}"
version = "{self.info.get('version', '1.0.0')}"
edition = "2021"

[dependencies]
reqwest = {{ version = "0.11", features = ["json"] }}
serde = {{ version = "1.0", features = ["derive"] }}
tokio = {{ version = "1.0", features = ["full"] }}
"""
        if self.include_docs:
            files["README.md"] = f"# {self.info.get('title')}\n\nRust Client"
        return files
    
    def generate_lib(self) -> str:
        return "pub mod client;\npub use client::Client;"
    
    def generate_client(self) -> str:
        return """
use reqwest::Client as HttpClient;

pub struct Client {
    base_url: String,
    api_key: Option<String>,
    http_client: HttpClient,
}

impl Client {
    pub fn new(base_url: impl Into<String>, api_key: Option<String>) -> Self {
        Self {
            base_url: base_url.into(),
            api_key,
            http_client: HttpClient::new(),
        }
    }
}
"""
    
    def generate_models(self) -> str:
        return "use serde::{Deserialize, Serialize};"
