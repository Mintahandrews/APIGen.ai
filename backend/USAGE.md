# Usage Guide - Universal API Client Generator

## Table of Contents
1. [Getting Started](#getting-started)
2. [Using the Web Interface](#using-the-web-interface)
3. [Using the API](#using-the-api)
4. [Language-Specific Examples](#language-specific-examples)
5. [Advanced Configuration](#advanced-configuration)

## Getting Started

### Starting the Backend Server

```bash
cd backend
python main.py
```

The server will start on `http://localhost:8000`. You can verify it's running by visiting:
- Health check: `http://localhost:8000/health`
- API docs: `http://localhost:8000/docs`

## Using the Web Interface

### Step 1: Upload OpenAPI Specification

1. Navigate to `http://localhost:3000/generator`
2. Click the upload area or drag and drop your OpenAPI file
3. Supported formats: `.yaml`, `.yml`, `.json`

The interface will automatically validate your specification and show:
- ✅ Valid specification with API details
- ❌ Invalid specification with error messages

### Step 2: Select Target Language

Choose from four supported languages:
- **Python** - For data science, web backends, automation
- **JavaScript/TypeScript** - For Node.js applications, web frontends
- **Go** - For microservices, CLI tools, high-performance apps
- **Rust** - For systems programming, WebAssembly, performance-critical apps

### Step 3: Configure Options

- **Package Name**: Name for your generated client (e.g., `my_api_client`)
- **Include Tests**: Generate basic test files
- **Include Documentation**: Generate README and usage examples

### Step 4: Generate and Download

Click "Generate API Client" to create your client. A ZIP file will be downloaded containing:
- Source code files
- Configuration files (requirements.txt, package.json, etc.)
- Documentation (if enabled)
- Tests (if enabled)

## Using the API

### Generate Client via cURL

```bash
curl -X POST http://localhost:8000/api/generate \
  -F "file=@openapi.yaml" \
  -F "language=python" \
  -F "package_name=my_client" \
  -F "include_tests=true" \
  -F "include_docs=true" \
  --output client.zip
```

### Validate Specification

```bash
curl -X POST http://localhost:8000/api/validate \
  -F "file=@openapi.yaml"
```

Response:
```json
{
  "valid": true,
  "info": {
    "title": "Pet Store API",
    "version": "1.0.0",
    "endpoints": 5
  }
}
```

### Get Supported Languages

```bash
curl http://localhost:8000/api/languages
```

## Language-Specific Examples

### Python Client

**Generated Structure:**
```
my_client/
├── my_client/
│   ├── __init__.py
│   ├── client.py
│   ├── models.py
│   └── exceptions.py
├── tests/
│   └── test_my_client.py
├── requirements.txt
├── setup.py
└── README.md
```

**Usage:**
```python
from my_client import MyClient

# Initialize client
client = MyClient(
    base_url="https://api.example.com",
    api_key="your-api-key"
)

# Make API calls
result = client.list_pets(params={"limit": 10})
pet = client.get_pet_by_id(pet_id=123)
new_pet = client.create_pet(data={"name": "Fluffy", "status": "available"})
```

**Installation:**
```bash
cd my_client
pip install -r requirements.txt
# or
pip install -e .
```

### JavaScript/TypeScript Client

**Generated Structure:**
```
my_client/
├── src/
│   ├── client.js
│   ├── types.d.ts
│   ├── models.js
│   └── index.js
├── tests/
│   └── client.test.js
├── package.json
└── README.md
```

**Usage (JavaScript):**
```javascript
const MyClient = require('my_client');

const client = new MyClient({
    baseURL: 'https://api.example.com',
    apiKey: 'your-api-key'
});

// Using async/await
async function example() {
    const pets = await client.listPets({ limit: 10 });
    const pet = await client.getPetById(123);
    const newPet = await client.createPet({ name: 'Fluffy' });
}
```

**Usage (TypeScript):**
```typescript
import MyClient from 'my_client';

const client = new MyClient({
    baseURL: 'https://api.example.com',
    apiKey: 'your-api-key'
});

const pets = await client.listPets({ limit: 10 });
```

**Installation:**
```bash
cd my_client
npm install
```

### Go Client

**Generated Structure:**
```
my_client/
├── client.go
├── models.go
├── errors.go
├── client_test.go
├── go.mod
└── README.md
```

**Usage:**
```go
package main

import (
    "context"
    "fmt"
    "my_client"
)

func main() {
    client := my_client.NewClient(
        my_client.WithBaseURL("https://api.example.com"),
        my_client.WithAPIKey("your-api-key"),
    )
    
    ctx := context.Background()
    
    // Make API calls
    pets, err := client.ListPets(ctx, nil)
    if err != nil {
        panic(err)
    }
    
    pet, err := client.GetPetById(ctx, 123)
    if err != nil {
        panic(err)
    }
    
    fmt.Println(pets, pet)
}
```

**Installation:**
```bash
go get github.com/yourusername/my_client
```

### Rust Client

**Generated Structure:**
```
my_client/
├── src/
│   ├── lib.rs
│   ├── client.rs
│   ├── models.rs
│   └── error.rs
├── tests/
│   └── integration_test.rs
├── Cargo.toml
└── README.md
```

**Usage:**
```rust
use my_client::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new(
        "https://api.example.com",
        Some("your-api-key".to_string())
    )?;
    
    // Make API calls
    let pets = client.list_pets(None).await?;
    let pet = client.get_pet_by_id(&123).await?;
    
    println!("{:?}", pets);
    Ok(())
}
```

**Installation:**
Add to `Cargo.toml`:
```toml
[dependencies]
my_client = "0.1.0"
```

## Advanced Configuration

### Custom Base URL

All generated clients support custom base URLs:

**Python:**
```python
client = MyClient(base_url="https://staging.api.example.com")
```

**JavaScript:**
```javascript
const client = new MyClient({ baseURL: 'https://staging.api.example.com' });
```

**Go:**
```go
client := my_client.NewClient(
    my_client.WithBaseURL("https://staging.api.example.com"),
)
```

**Rust:**
```rust
let client = Client::new("https://staging.api.example.com", None)?;
```

### Authentication

#### Bearer Token
```python
# Python
client = MyClient(api_key="your-token")

# JavaScript
const client = new MyClient({ apiKey: 'your-token' });

# Go
client := my_client.NewClient(my_client.WithAPIKey("your-token"))

# Rust
let client = Client::new(base_url, Some("your-token".to_string()))?;
```

### Timeout Configuration

**Python:**
```python
client = MyClient(timeout=60)  # 60 seconds
```

**JavaScript:**
```javascript
const client = new MyClient({ timeout: 60000 });  // 60 seconds
```

**Go:**
```go
httpClient := &http.Client{
    Timeout: 60 * time.Second,
}
client := my_client.NewClient(my_client.WithHTTPClient(httpClient))
```

**Rust:**
```rust
let http_client = reqwest::Client::builder()
    .timeout(std::time::Duration::from_secs(60))
    .build()?;
let client = Client::with_http_client(base_url, api_key, http_client);
```

### Error Handling

All generated clients include comprehensive error handling:

**Python:**
```python
from my_client import MyClient, APIException, AuthenticationException

try:
    result = client.some_method()
except AuthenticationException:
    print("Authentication failed")
except APIException as e:
    print(f"API error: {e.status_code}")
```

**JavaScript:**
```javascript
try {
    const result = await client.someMethod();
} catch (error) {
    if (error.name === 'AuthenticationError') {
        console.log('Authentication failed');
    } else {
        console.log(`API error: ${error.statusCode}`);
    }
}
```

**Go:**
```go
result, err := client.SomeMethod(ctx)
if err != nil {
    switch e := err.(type) {
    case *my_client.AuthenticationError:
        fmt.Println("Authentication failed")
    case *my_client.APIError:
        fmt.Printf("API error: %d\n", e.StatusCode)
    }
}
```

**Rust:**
```rust
match client.some_method().await {
    Ok(result) => println!("{:?}", result),
    Err(Error::AuthenticationError) => println!("Authentication failed"),
    Err(Error::ApiError { status_code, message }) => {
        println!("API error {}: {}", status_code, message)
    }
    Err(e) => println!("Error: {}", e),
}
```

## Tips and Best Practices

1. **Version Control**: Always version your OpenAPI spec alongside generated clients
2. **Regeneration**: Regenerate clients when your API changes
3. **Testing**: Use the included tests as a starting point
4. **Customization**: Generated code can be modified, but consider regenerating for major API changes
5. **Documentation**: Keep the generated README updated with your specific usage patterns

## Troubleshooting

### Invalid OpenAPI Specification
- Ensure your spec follows OpenAPI 3.0 format
- Use the validation endpoint to check for errors
- Common issues: missing required fields, invalid references

### Generation Errors
- Check that all required fields are present in your spec
- Verify operation IDs are unique
- Ensure schema definitions are valid

### Runtime Errors
- Verify base URL is correct
- Check authentication credentials
- Ensure API endpoints match the specification

## Next Steps

- Explore the example OpenAPI specs in `backend/examples/`
- Check the API documentation at `http://localhost:8000/docs`
- Customize generated clients for your specific needs
- Contribute new language generators or improvements
