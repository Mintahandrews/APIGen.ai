# Java Generator - Modern Java patterns
from typing import Dict, Any
from .base_generator import BaseGenerator

class JavaGenerator(BaseGenerator):
    def generate(self) -> Dict[str, str]:
        files = {}
        class_name = self.to_pascal_case(self.package_name)
        files[f"src/main/java/com/api/{class_name}Client.java"] = self.generate_client()
        files["pom.xml"] = f"""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.api</groupId>
    <artifactId>{self.package_name}</artifactId>
    <version>{self.info.get('version', '1.0.0')}</version>
    <dependencies>
        <dependency>
            <groupId>com.squareup.okhttp3</groupId>
            <artifactId>okhttp</artifactId>
            <version>4.12.0</version>
        </dependency>
    </dependencies>
</project>"""
        if self.include_docs:
            files["README.md"] = f"# {self.info.get('title')}\n\nJava Client"
        return files
    
    def generate_client(self) -> str:
        class_name = self.to_pascal_case(self.package_name)
        return f"""
package com.api;

import okhttp3.*;
import java.io.IOException;

public class {class_name}Client {{
    private final OkHttpClient client;
    private final String baseUrl;
    private final String apiKey;
    
    public {class_name}Client(String baseUrl, String apiKey) {{
        this.baseUrl = baseUrl.replaceAll("/$", "");
        this.apiKey = apiKey;
        this.client = new OkHttpClient();
    }}
    
    public Response get(String endpoint) throws IOException {{
        Request.Builder builder = new Request.Builder()
            .url(baseUrl + endpoint);
        
        if (apiKey != null) {{
            builder.header("Authorization", "Bearer " + apiKey);
        }}
        
        return client.newCall(builder.build()).execute();
    }}
}}
"""
    
    def generate_models(self) -> str:
        return "package com.api.models;"
