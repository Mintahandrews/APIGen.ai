"""
Timeout configuration utilities for generated API clients
"""
from typing import Optional, Dict
from dataclasses import dataclass


@dataclass
class TimeoutConfig:
    """Configuration for request timeouts"""
    
    connect_timeout: int = 10  # seconds
    read_timeout: int = 30  # seconds
    total_timeout: Optional[int] = None  # seconds, None = no limit
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for template rendering"""
        return {
            "connect_timeout": self.connect_timeout,
            "read_timeout": self.read_timeout,
            "total_timeout": self.total_timeout
        }
    
    def generate_python_code(self) -> str:
        """Generate Python timeout configuration"""
        return f"""
# Timeout configuration
CONNECT_TIMEOUT = {self.connect_timeout}  # seconds
READ_TIMEOUT = {self.read_timeout}  # seconds
{'TOTAL_TIMEOUT = ' + str(self.total_timeout) if self.total_timeout else '# No total timeout limit'}

# Usage with requests
timeout = (CONNECT_TIMEOUT, READ_TIMEOUT)
"""
    
    def generate_javascript_code(self) -> str:
        """Generate JavaScript/TypeScript timeout configuration"""
        total_line = f"  totalTimeout: {self.total_timeout}," if self.total_timeout else "  // No total timeout limit"
        return f"""
// Timeout configuration
export const TIMEOUT_CONFIG = {{
  connectTimeout: {self.connect_timeout} * 1000,  // milliseconds
  readTimeout: {self.read_timeout} * 1000,  // milliseconds
{total_line}
}};

// Usage with fetch + AbortController
const controller = new AbortController();
const timeoutId = setTimeout(() => controller.abort(), TIMEOUT_CONFIG.readTimeout);

try {{
  const response = await fetch(url, {{
    signal: controller.signal,
    // ... other options
  }});
  clearTimeout(timeoutId);
  return response;
}} catch (error) {{
  clearTimeout(timeoutId);
  throw error;
}}
"""
    
    def generate_go_code(self) -> str:
        """Generate Go timeout configuration"""
        return f"""
package client

import (
    "context"
    "net"
    "net/http"
    "time"
)

// TimeoutConfig holds timeout settings
type TimeoutConfig struct {{
    ConnectTimeout time.Duration
    ReadTimeout    time.Duration
    TotalTimeout   time.Duration
}}

// DefaultTimeoutConfig returns default timeout configuration
func DefaultTimeoutConfig() *TimeoutConfig {{
    return &TimeoutConfig{{
        ConnectTimeout: {self.connect_timeout} * time.Second,
        ReadTimeout:    {self.read_timeout} * time.Second,
        {'TotalTimeout:   ' + str(self.total_timeout) + ' * time.Second,' if self.total_timeout else '// No total timeout'}
    }}
}}

// NewHTTPClient creates an HTTP client with timeout configuration
func (c *TimeoutConfig) NewHTTPClient() *http.Client {{
    return &http.Client{{
        Timeout: c.TotalTimeout,
        Transport: &http.Transport{{
            DialContext: (&net.Dialer{{
                Timeout: c.ConnectTimeout,
            }}).DialContext,
            ResponseHeaderTimeout: c.ReadTimeout,
        }},
    }}
}}
"""


def parse_timeout_from_spec(spec: dict, operation: Optional[dict] = None) -> TimeoutConfig:
    """
    Parse timeout configuration from OpenAPI spec
    Checks operation-level first, then global
    """
    # Check operation-level timeout
    if operation and 'x-timeout' in operation:
        timeout_data = operation['x-timeout']
        return TimeoutConfig(
            connect_timeout=timeout_data.get('connect', 10),
            read_timeout=timeout_data.get('read', 30),
            total_timeout=timeout_data.get('total')
        )
    
    # Check global timeout
    if 'x-timeout' in spec:
        timeout_data = spec['x-timeout']
        return TimeoutConfig(
            connect_timeout=timeout_data.get('connect', 10),
            read_timeout=timeout_data.get('read', 30),
            total_timeout=timeout_data.get('total')
        )
    
    # Return default
    return TimeoutConfig()
