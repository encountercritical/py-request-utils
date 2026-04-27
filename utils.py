"""HTTP request utilities."""
import urllib.request
import urllib.parse
import json as _json
from typing import Optional, Any


def get(url: str, headers: Optional[dict] = None) -> str:
    """Perform an HTTP GET request.

    Args:
        url: The URL to request.
        headers: Optional dictionary of HTTP headers.

    Returns:
        The response body as a string.
    """
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode()


def post(url: str, data: dict, headers: Optional[dict] = None) -> str:
    """Perform an HTTP POST request with a JSON body.

    Args:
        url: The URL to request.
        data: Dictionary of data to send as JSON.
        headers: Optional dictionary of HTTP headers.

    Returns:
        The response body as a string.
    """
    body = _json.dumps(data).encode()
    h = {"Content-Type": "application/json"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, data=body, headers=h, method="POST")
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode()


def build_url(base: str, **params: Any) -> str:
    """Build a URL with query parameters.

    Args:
        base: The base URL.
        **params: Query parameters as keyword arguments.

    Returns:
        The full URL with encoded parameters.
    """
    if not params:
        return base

    url_parts = list(urllib.parse.urlparse(base))
    query = urllib.parse.parse_qsl(url_parts[4])

    # Rebuild query list to preserve order as much as possible
    new_query = []
    seen_keys = set()
    for key, value in query:
        if key in params:
            if key not in seen_keys:
                new_query.append((key, str(params[key])))
                seen_keys.add(key)
        else:
            new_query.append((key, value))

    for key, value in params.items():
        if key not in seen_keys:
            new_query.append((key, str(value)))

    url_parts[4] = urllib.parse.urlencode(new_query)

    return urllib.parse.urlunparse(url_parts)
