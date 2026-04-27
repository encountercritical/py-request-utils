"""HTTP request utilities."""
import urllib.request
import urllib.parse
import json as _json
from typing import Optional


def get(url: str, headers: Optional[dict] = None) -> str:
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode()


def post(url: str, data: dict, headers: Optional[dict] = None) -> str:
    body = _json.dumps(data).encode()
    h: dict = {"Content-Type": "application/json"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, data=body, headers=h, method="POST")
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode()


def build_url(base: str, **params: str) -> str:
    return base + "?" + urllib.parse.urlencode(params)
