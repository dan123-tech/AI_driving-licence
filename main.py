"""
Vercel Python entrypoint (root main.py).
See https://vercel.com/docs/frameworks/backend/fastapi
"""
from app.main import fastapi_app as app

__all__ = ["app"]
