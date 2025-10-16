#!/usr/bin/env python3
"""
Comprehensive test script for Universal API Client Generator
Tests all modules, generators, and functionality
"""

import sys
from pathlib import Path

print("=" * 70)
print("🧪 Testing Universal API Client Generator Backend")
print("=" * 70)
print()

# Test 1: Import all modules
print("[1/7] Testing module imports...")
try:
    from parsers import OpenAPIParser
    from generators import (
        BaseGenerator,
        PythonGenerator,
        JavaScriptGenerator,
        GoGenerator,
        RustGenerator,
        CSharpGenerator,
        JavaGenerator,
        PHPGenerator
    )
    print("✅ All modules imported successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

# Test 2: Load example OpenAPI spec
print("\n[2/7] Testing OpenAPI parser...")
try:
    import yaml
    with open('examples/petstore.yaml', 'r') as f:
        spec = yaml.safe_load(f)
    
    parser = OpenAPIParser(spec)
    errors = parser.validate()
    
    if errors:
        print(f"❌ Validation errors: {errors}")
        sys.exit(1)
    
    parsed_data = parser.parse()
    print(f"✅ Parser working - Found {len(parsed_data['paths'])} endpoints")
except Exception as e:
    print(f"❌ Parser error: {e}")
    sys.exit(1)

# Test 3: Test Python generator
print("\n[3/7] Testing Python generator...")
try:
    gen = PythonGenerator(parsed_data, "test_client")
    files = gen.generate()
    print(f"✅ Python generator - Generated {len(files)} files")
except Exception as e:
    print(f"❌ Python generator error: {e}")
    sys.exit(1)

# Test 4: Test JavaScript generator
print("\n[4/7] Testing JavaScript generator...")
try:
    gen = JavaScriptGenerator(parsed_data, "test_client")
    files = gen.generate()
    print(f"✅ JavaScript generator - Generated {len(files)} files")
except Exception as e:
    print(f"❌ JavaScript generator error: {e}")
    sys.exit(1)

# Test 5: Test Go generator
print("\n[5/7] Testing Go generator...")
try:
    gen = GoGenerator(parsed_data, "test_client")
    files = gen.generate()
    print(f"✅ Go generator - Generated {len(files)} files")
except Exception as e:
    print(f"❌ Go generator error: {e}")
    sys.exit(1)

# Test 6: Test new generators (C#, Java, PHP)
print("\n[6/7] Testing new generators...")
try:
    # C#
    gen = CSharpGenerator(parsed_data, "test_client")
    files = gen.generate()
    print(f"✅ C# generator - Generated {len(files)} files")
    
    # Java
    gen = JavaGenerator(parsed_data, "test_client")
    files = gen.generate()
    print(f"✅ Java generator - Generated {len(files)} files")
    
    # PHP
    gen = PHPGenerator(parsed_data, "test_client")
    files = gen.generate()
    print(f"✅ PHP generator - Generated {len(files)} files")
except Exception as e:
    print(f"❌ New generator error: {e}")
    sys.exit(1)

# Test 7: Test Rust generator
print("\n[7/7] Testing Rust generator...")
try:
    gen = RustGenerator(parsed_data, "test_client")
    files = gen.generate()
    print(f"✅ Rust generator - Generated {len(files)} files")
except Exception as e:
    print(f"❌ Rust generator error: {e}")
    sys.exit(1)

print()
print("=" * 70)
print("🎉 ALL TESTS PASSED!")
print("=" * 70)
print()
print("✅ All 7 language generators working")
print("✅ OpenAPI parser functioning correctly")
print("✅ All modules properly imported")
print()
print("Backend is ready for use!")
print("Run: python main.py")
