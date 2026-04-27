"""HTTP request utilities."""
import urllib.request
import urllib.parse
import json as _json


def get(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode()


def post(url, data, headers=None):
    body = _json.dumps(data).encode()
    h = {"Content-Type": "application/json"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, data=body, headers=h, method="POST")
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode()


def build_url(base, **params):
    return base + "?" + urllib.parse.urlencode(params)
