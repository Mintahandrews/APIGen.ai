"""
Retry configuration utilities for generated API clients
"""
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class RetryConfig:
    """Configuration for automatic retry logic in generated clients"""
    
    max_attempts: int = 3
    initial_interval: int = 500  # milliseconds
    max_interval: int = 60000  # milliseconds
    exponent: float = 1.5
    retry_on_status_codes: List[str] = None
    retry_connection_errors: bool = True
    respect_retry_after: bool = True
    
    def __post_init__(self):
        if self.retry_on_status_codes is None:
            self.retry_on_status_codes = ["5XX", "429", "408"]
    
    def to_dict(self):
        """Convert to dictionary for template rendering"""
        return {
            "max_attempts": self.max_attempts,
            "initial_interval": self.initial_interval,
            "max_interval": self.max_interval,
            "exponent": self.exponent,
            "retry_on_status_codes": self.retry_on_status_codes,
            "retry_connection_errors": self.retry_connection_errors,
            "respect_retry_after": self.respect_retry_after
        }
    
    def generate_python_code(self) -> str:
        """Generate Python retry decorator code"""
        return f"""
import time
import random
from functools import wraps
from typing import Callable, Any

def with_retry(func: Callable) -> Callable:
    '''Automatic retry decorator with exponential backoff'''
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        max_attempts = {self.max_attempts}
        initial_interval = {self.initial_interval} / 1000  # Convert to seconds
        max_interval = {self.max_interval} / 1000
        exponent = {self.exponent}
        
        for attempt in range(max_attempts):
            try:
                response = func(*args, **kwargs)
                
                # Check if we should retry based on status code
                if hasattr(response, 'status_code'):
                    status = response.status_code
                    should_retry = False
                    
                    # Check retry status codes
                    retry_codes = {self.retry_on_status_codes}
                    for code in retry_codes:
                        if 'XX' in code:
                            # Handle wildcard like 5XX
                            base = int(code[0]) * 100
                            if base <= status < base + 100:
                                should_retry = True
                                break
                        elif str(status) == code:
                            should_retry = True
                            break
                    
                    if not should_retry:
                        return response
                    
                    # Respect Retry-After header
                    if {str(self.respect_retry_after).lower()}:
                        retry_after = response.headers.get('Retry-After')
                        if retry_after:
                            try:
                                wait_time = float(retry_after)
                                time.sleep(wait_time)
                                continue
                            except ValueError:
                                pass
                
                return response
                
            except (ConnectionError, TimeoutError) as e:
                if not {str(self.retry_connection_errors).lower()}:
                    raise
                
                if attempt == max_attempts - 1:
                    raise
            
            # Calculate backoff with jitter
            interval = min(initial_interval * (exponent ** attempt), max_interval)
            jitter = random.uniform(0, interval * 0.1)  # 10% jitter
            time.sleep(interval + jitter)
        
        return func(*args, **kwargs)
    
    return wrapper
"""
    
    def generate_javascript_code(self) -> str:
        """Generate JavaScript/TypeScript retry code"""
        return f"""
/**
 * Automatic retry with exponential backoff
 */
async function withRetry<T>(
  fn: () => Promise<T>,
  options = {{}}
): Promise<T> {{
  const maxAttempts = {self.max_attempts};
  const initialInterval = {self.initial_interval};
  const maxInterval = {self.max_interval};
  const exponent = {self.exponent};
  const retryCodes = {self.retry_on_status_codes};
  
  for (let attempt = 0; attempt < maxAttempts; attempt++) {{
    try {{
      const response = await fn();
      
      // Check if response has status code
      if (response && typeof response === 'object' && 'status' in response) {{
        const status = (response as any).status;
        let shouldRetry = false;
        
        // Check retry status codes
        for (const code of retryCodes) {{
          if (code.includes('XX')) {{
            const base = parseInt(code[0]) * 100;
            if (status >= base && status < base + 100) {{
              shouldRetry = true;
              break;
            }}
          }} else if (status === parseInt(code)) {{
            shouldRetry = true;
            break;
          }}
        }}
        
        if (!shouldRetry) {{
          return response;
        }}
        
        // Respect Retry-After header
        if ({str(self.respect_retry_after).lower()}) {{
          const retryAfter = (response as any).headers?.get?.('Retry-After');
          if (retryAfter) {{
            const waitTime = parseFloat(retryAfter) * 1000;
            await new Promise(resolve => setTimeout(resolve, waitTime));
            continue;
          }}
        }}
      }}
      
      return response;
      
    }} catch (error) {{
      if (attempt === maxAttempts - 1) {{
        throw error;
      }}
      
      // Calculate backoff with jitter
      const interval = Math.min(
        initialInterval * Math.pow(exponent, attempt),
        maxInterval
      );
      const jitter = Math.random() * interval * 0.1;
      await new Promise(resolve => setTimeout(resolve, interval + jitter));
    }}
  }}
  
  throw new Error('Max retry attempts reached');
}}

export {{ withRetry }};
"""
    
    def generate_go_code(self) -> str:
        """Generate Go retry code"""
        return f"""
package client

import (
    "math"
    "math/rand"
    "net/http"
    "strconv"
    "strings"
    "time"
)

type RetryConfig struct {{
    MaxAttempts         int
    InitialInterval     time.Duration
    MaxInterval         time.Duration
    Exponent            float64
    RetryStatusCodes    []string
    RespectRetryAfter   bool
}}

func DefaultRetryConfig() *RetryConfig {{
    return &RetryConfig{{
        MaxAttempts:       {self.max_attempts},
        InitialInterval:   {self.initial_interval} * time.Millisecond,
        MaxInterval:       {self.max_interval} * time.Millisecond,
        Exponent:          {self.exponent},
        RetryStatusCodes:  []string{{{', '.join(f'"{code}"' for code in self.retry_on_status_codes)}}},
        RespectRetryAfter: {str(self.respect_retry_after).lower()},
    }}
}}

func (c *RetryConfig) ShouldRetry(statusCode int) bool {{
    for _, code := range c.RetryStatusCodes {{
        if strings.Contains(code, "XX") {{
            base, _ := strconv.Atoi(string(code[0]))
            base *= 100
            if statusCode >= base && statusCode < base+100 {{
                return true
            }}
        }} else {{
            codeInt, _ := strconv.Atoi(code)
            if statusCode == codeInt {{
                return true
            }}
        }}
    }}
    return false
}}

func (c *RetryConfig) WithRetry(fn func() (*http.Response, error)) (*http.Response, error) {{
    var resp *http.Response
    var err error
    
    for attempt := 0; attempt < c.MaxAttempts; attempt++ {{
        resp, err = fn()
        
        if err == nil && resp != nil {{
            if !c.ShouldRetry(resp.StatusCode) {{
                return resp, nil
            }}
            
            // Respect Retry-After header
            if c.RespectRetryAfter {{
                if retryAfter := resp.Header.Get("Retry-After"); retryAfter != "" {{
                    if seconds, err := strconv.Atoi(retryAfter); err == nil {{
                        time.Sleep(time.Duration(seconds) * time.Second)
                        continue
                    }}
                }}
            }}
        }}
        
        if attempt < c.MaxAttempts-1 {{
            // Calculate backoff with jitter
            interval := time.Duration(
                math.Min(
                    float64(c.InitialInterval)*math.Pow(c.Exponent, float64(attempt)),
                    float64(c.MaxInterval),
                ),
            )
            jitter := time.Duration(rand.Float64() * float64(interval) * 0.1)
            time.Sleep(interval + jitter)
        }}
    }}
    
    return resp, err
}}
"""


def parse_retry_config_from_spec(spec: dict) -> Optional[RetryConfig]:
    """
    Parse retry configuration from OpenAPI spec extensions
    Looks for x-retry-config or x-speakeasy-retries
    """
    # Check for custom retry config
    if 'x-retry-config' in spec:
        config_data = spec['x-retry-config']
        return RetryConfig(
            max_attempts=config_data.get('maxAttempts', 3),
            initial_interval=config_data.get('initialInterval', 500),
            max_interval=config_data.get('maxInterval', 60000),
            exponent=config_data.get('exponent', 1.5),
            retry_on_status_codes=config_data.get('statusCodes', ["5XX", "429", "408"]),
            retry_connection_errors=config_data.get('retryConnectionErrors', True),
            respect_retry_after=config_data.get('respectRetryAfter', True)
        )
    
    # Check for Speakeasy-style config
    if 'x-speakeasy-retries' in spec:
        config_data = spec['x-speakeasy-retries']
        strategy = config_data.get('strategy', 'backoff')
        backoff = config_data.get('backoff', {})
        
        return RetryConfig(
            max_attempts=config_data.get('maxAttempts', 3),
            initial_interval=backoff.get('initialInterval', 500),
            max_interval=backoff.get('maxInterval', 60000),
            exponent=backoff.get('exponent', 1.5),
            retry_on_status_codes=config_data.get('statusCodes', ["5XX", "429", "408"]),
            retry_connection_errors=config_data.get('retryConnectionErrors', True),
            respect_retry_after=True
        )
    
    # Return default config
    return RetryConfig()
