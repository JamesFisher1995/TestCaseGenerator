"""Test Case Generator — HTTP service wrapper.

POST /generate   { "ticket": "<raw ticket text>", "key": "<JIRA-KEY>" }
                 → { "key": "...", "test_cases_md": "...", "raw_output": "..." }
GET  /health     → { "status": "ok" }
"""
from __future__ import annotations

import os
import pathlib
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .generator import generate_test_cases, KnowledgeBase


KB_PATH = pathlib.Path(__file__).parent.parent / "knowledge-base"
INSTRUCTIONS_PATH = pathlib.Path(__file__).parent.parent / "instructions" / "generate-test-cases.md"
TEMPLATE_PATH = pathlib.Path(__file__).parent.parent / "templates" / "test-case-format.md"

_kb: KnowledgeBase | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _kb
    _kb = KnowledgeBase.load(KB_PATH)
    yield


app = FastAPI(title="Test Case Generator", lifespan=lifespan)


class GenerateRequest(BaseModel):
    ticket: str
    key: str = "NOKEY"


class GenerateResponse(BaseModel):
    key: str
    test_cases_md: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    if not req.ticket.strip():
        raise HTTPException(status_code=400, detail="ticket must not be empty")
    if _kb is None:
        raise HTTPException(status_code=503, detail="knowledge base not loaded")

    instructions = INSTRUCTIONS_PATH.read_text()
    template = TEMPLATE_PATH.read_text()

    result = await generate_test_cases(
        ticket=req.ticket,
        key=req.key,
        kb=_kb,
        instructions=instructions,
        template=template,
    )
    return GenerateResponse(key=req.key, test_cases_md=result)
