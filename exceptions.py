"""
Custom exceptions for JIRA automation toolkit.

This module defines specific exception types for better error handling
and debugging throughout the JIRA automation workflow.
"""

from typing import Optional, Dict, Any


class JiraApiError(Exception):
    """
    Base exception for all JIRA API related errors.
    
    This is the parent class for all JIRA-specific exceptions,
    allowing for broad exception handling when needed.
    
    Attributes:
        message (str): Human-readable error message
        status_code (Optional[int]): HTTP status code if applicable
        response_data (Optional[Dict]): API response data if available
    """
    
    def __init__(
        self, 
        message: str, 
        status_code: Optional[int] = None,
        response_data: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.status_code = status_code
        self.response_data = response_data
        super().__init__(self.message)
    
    def __str__(self) -> str:
        """String representation with status code if available"""
        if self.status_code:
            return f"JIRA API Error {self.status_code}: {self.message}"
        return f"JIRA API Error: {self.message}"


class JiraAuthenticationError(JiraApiError):
    """
    Raised when JIRA authentication fails.
    
    This exception is raised for various authentication-related issues:
    - Invalid credentials
    - Expired session cookies
    - Account locked or disabled
    - Two-factor authentication required
    - CAPTCHA challenges
    
    Example:
        >>> try:
        ...     await client.authenticate()
        ... except JiraAuthenticationError as e:
        ...     print(f"Login failed: {e}")
        ...     # Handle re-authentication
    """
    
    def __init__(
        self, 
        message: str, 
        auth_type: Optional[str] = None,
        status_code: Optional[int] = None,
        response_data: Optional[Dict[str, Any]] = None
    ):
        self.auth_type = auth_type  # 'login', 'cookie', 'token', etc.
        super().__init__(message, status_code, response_data)
    
    def __str__(self) -> str:
        """Enhanced string representation for authentication errors"""
        base_msg = f"JIRA Authentication Error: {self.message}"
        if self.auth_type:
            base_msg = f"JIRA Authentication Error ({self.auth_type}): {self.message}"
        if self.status_code:
            base_msg += f" (HTTP {self.status_code})"
        return base_msg


class JiraNetworkError(JiraApiError):
    """
    Raised when network-related issues occur.
    
    This exception covers:
    - Connection timeouts
    - DNS resolution failures
    - Proxy connection issues
    - SSL/TLS errors
    - Network unreachable errors
    
    Example:
        >>> try:
        ...     response = client.search_issues(jql)
        ... except JiraNetworkError as e:
        ...     print(f"Network issue: {e}")
        ...     # Implement retry logic or fallback
    """
    
    def __init__(
        self, 
        message: str, 
        original_exception: Optional[Exception] = None,
        retry_count: Optional[int] = None
    ):
        self.original_exception = original_exception
        self.retry_count = retry_count
        super().__init__(message)
    
    def __str__(self) -> str:
        """Enhanced string representation for network errors"""
        base_msg = f"JIRA Network Error: {self.message}"
        if self.retry_count is not None:
            base_msg += f" (after {self.retry_count} retries)"
        if self.original_exception:
            base_msg += f" - Original: {type(self.original_exception).__name__}: {self.original_exception}"
        return base_msg


class JiraConfigurationError(JiraApiError):
    """
    Raised when there are configuration-related issues.
    
    This exception covers:
    - Missing required environment variables
    - Invalid configuration values
    - Malformed URLs
    - Missing files or directories
    
    Example:
        >>> try:
        ...     client = JiraApiClient()
        ... except JiraConfigurationError as e:
        ...     print(f"Configuration issue: {e}")
        ...     # Guide user to fix configuration
    """
    
    def __init__(self, message: str, config_key: Optional[str] = None):
        self.config_key = config_key
        super().__init__(message)
    
    def __str__(self) -> str:
        """Enhanced string representation for configuration errors"""
        if self.config_key:
            return f"JIRA Configuration Error ({self.config_key}): {self.message}"
        return f"JIRA Configuration Error: {self.message}"


class JiraValidationError(JiraApiError):
    """
    Raised when input validation fails.
    
    This exception covers:
    - Invalid JQL syntax
    - Malformed project keys
    - Invalid field names
    - Out-of-range values
    
    Example:
        >>> try:
        ...     client.search_issues("invalid jql; DROP TABLE users;")
        ... except JiraValidationError as e:
        ...     print(f"Invalid input: {e}")
        ...     # Prompt user for correct input
    """
    
    def __init__(
        self, 
        message: str, 
        field_name: Optional[str] = None,
        invalid_value: Optional[str] = None
    ):
        self.field_name = field_name
        self.invalid_value = invalid_value
        super().__init__(message)
    
    def __str__(self) -> str:
        """Enhanced string representation for validation errors"""
        base_msg = f"JIRA Validation Error: {self.message}"
        if self.field_name:
            base_msg = f"JIRA Validation Error ({self.field_name}): {self.message}"
        if self.invalid_value:
            base_msg += f" - Invalid value: '{self.invalid_value}'"
        return base_msg


class JiraRateLimitError(JiraApiError):
    """
    Raised when JIRA API rate limits are exceeded.
    
    This exception is raised when the JIRA server returns a 429 status
    code, indicating that the client has made too many requests.
    
    Attributes:
        retry_after (Optional[int]): Seconds to wait before retrying
        limit_type (str): Type of rate limit ('requests', 'concurrent', etc.)
    
    Example:
        >>> try:
        ...     response = client.search_issues(jql)
        ... except JiraRateLimitError as e:
        ...     print(f"Rate limited: {e}")
        ...     time.sleep(e.retry_after or 60)
        ...     # Retry the request
    """
    
    def __init__(
        self, 
        message: str, 
        retry_after: Optional[int] = None,
        limit_type: str = "requests"
    ):
        self.retry_after = retry_after
        self.limit_type = limit_type
        super().__init__(message, status_code=429)
    
    def __str__(self) -> str:
        """Enhanced string representation for rate limit errors"""
        base_msg = f"JIRA Rate Limit Error ({self.limit_type}): {self.message}"
        if self.retry_after:
            base_msg += f" - Retry after {self.retry_after} seconds"
        return base_msg


class JiraPermissionError(JiraApiError):
    """
    Raised when the user lacks permissions for the requested operation.
    
    This exception covers:
    - Insufficient project permissions
    - Read-only access when write is required
    - Admin-only operations
    - Field-level security restrictions
    
    Example:
        >>> try:
        ...     client.get_project_info("RESTRICTED")
        ... except JiraPermissionError as e:
        ...     print(f"Access denied: {e}")
        ...     # Request appropriate permissions
    """
    
    def __init__(
        self, 
        message: str, 
        resource: Optional[str] = None,
        required_permission: Optional[str] = None
    ):
        self.resource = resource
        self.required_permission = required_permission
        super().__init__(message, status_code=403)
    
    def __str__(self) -> str:
        """Enhanced string representation for permission errors"""
        base_msg = f"JIRA Permission Error: {self.message}"
        if self.resource:
            base_msg = f"JIRA Permission Error ({self.resource}): {self.message}"
        if self.required_permission:
            base_msg += f" - Required permission: {self.required_permission}"
        return base_msg


def classify_http_error(status_code: int, response_text: str = "") -> type[JiraApiError]:
    """
    Classify HTTP status codes into appropriate exception types.
    
    Args:
        status_code (int): HTTP status code from response
        response_text (str): Response body text for additional context
        
    Returns:
        type[JiraApiError]: Appropriate exception class for the status code
        
    Example:
        >>> exception_class = classify_http_error(401, "Invalid session")
        >>> raise exception_class("Authentication failed")
    """
    if status_code == 401:
        return JiraAuthenticationError
    elif status_code == 403:
        return JiraPermissionError
    elif status_code == 429:
        return JiraRateLimitError
    elif status_code in (500, 502, 503, 504):
        return JiraNetworkError
    else:
        return JiraApiError


def handle_requests_exception(exception: Exception) -> JiraApiError:
    """
    Convert requests library exceptions to JIRA-specific exceptions.
    
    Args:
        exception (Exception): Original requests exception
        
    Returns:
        JiraApiError: Appropriate JIRA exception with context
        
    Example:
        >>> try:
        ...     response = requests.get(url)
        ... except requests.RequestException as e:
        ...     raise handle_requests_exception(e)
    """
    import requests.exceptions as req_exc
    
    if isinstance(exception, req_exc.ConnectionError):
        return JiraNetworkError(
            "Failed to connect to JIRA server. Check network connectivity and proxy settings.",
            original_exception=exception
        )
    elif isinstance(exception, req_exc.Timeout):
        return JiraNetworkError(
            "Request timed out. JIRA server may be overloaded or network is slow.",
            original_exception=exception
        )
    elif isinstance(exception, req_exc.SSLError):
        return JiraNetworkError(
            "SSL/TLS error occurred. Check certificate configuration.",
            original_exception=exception
        )
    elif isinstance(exception, req_exc.ProxyError):
        return JiraNetworkError(
            "Proxy connection failed. Check proxy configuration in .env file.",
            original_exception=exception
        )
    elif isinstance(exception, req_exc.HTTPError):
        return JiraApiError(
            f"HTTP error occurred: {exception}",
            status_code=getattr(exception.response, 'status_code', None)
        )
    else:
        return JiraApiError(
            f"Unexpected network error: {exception}"
        )