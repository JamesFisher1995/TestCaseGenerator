"""Knowledge base loader and OpenAI call."""
from __future__ import annotations

import os
import pathlib
from dataclasses import dataclass

from openai import AsyncOpenAI


@dataclass
class KnowledgeBase:
    overview: str
    navigation: str
    business_rules: str
    roles: str
    test_data: str
    known_gotchas: str
    features: dict[str, str]
    flows: dict[str, str]
    glossary: str

    @classmethod
    def load(cls, kb_path: pathlib.Path) -> "KnowledgeBase":
        def _read(rel: str) -> str:
            p = kb_path / rel
            return p.read_text() if p.exists() else ""

        def _read_dir(rel: str) -> dict[str, str]:
            d = kb_path / rel
            if not d.exists():
                return {}
            return {
                f.stem: f.read_text()
                for f in d.glob("*.md")
                if not f.name.startswith("_")
            }

        return cls(
            overview=_read("00-application-overview.md"),
            navigation=_read("navigation.md"),
            business_rules=_read("business-rules.md"),
            roles=_read("roles-and-permissions.md"),
            test_data=_read("test-data.md"),
            known_gotchas=_read("known-gotchas.md"),
            features=_read_dir("features"),
            flows=_read_dir("flows"),
            glossary=_read("glossary.md"),
        )

    def as_text(self) -> str:
        parts = [
            "## Application overview\n" + self.overview,
            "## Navigation\n" + self.navigation,
            "## Business rules\n" + self.business_rules,
            "## Roles and permissions\n" + self.roles,
            "## Test data\n" + self.test_data,
            "## Known gotchas and open defects\n" + self.known_gotchas,
            "## Glossary\n" + self.glossary,
        ]
        for name, content in self.features.items():
            parts.append(f"## Feature: {name}\n{content}")
        for name, content in self.flows.items():
            parts.append(f"## Flow: {name}\n{content}")
        return "\n\n---\n\n".join(parts)


async def generate_test_cases(
    *,
    ticket: str,
    key: str,
    kb: KnowledgeBase,
    instructions: str,
    template: str,
) -> str:
    client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

    system_prompt = f"""You are a senior QA analyst for the "Get air pollution data" GOV.UK service.
Your job is to generate manual test cases from a Jira ticket, following the instructions and output template exactly.

INSTRUCTIONS:
{instructions}

OUTPUT TEMPLATE (follow this exactly):
{template}

KNOWLEDGE BASE:
{kb.as_text()}
"""

    user_prompt = f"""Ticket key: {key}

Ticket content:
{ticket}

Generate the test cases now, following the instructions and output template exactly.
Return the full markdown output including analysis, traceability table, test cases, and knowledge base gaps.
"""

    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    response = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content or ""
