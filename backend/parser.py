"""
parser.py

This module simulates parsing of natural-language analytics questions.

In a production system, this layer could:
- Call an LLM (OpenAI, etc.)
- Use regex / rules for simple patterns
- Map phrases to known business metrics and dimensions
"""


from dataclasses import dataclass
from typing import Optional


@dataclass
class ParsedQuery:
    metric: str
    dimension: Optional[str] = None
    filter: Optional[str] = None


def parse_question(question: str) -> ParsedQuery:
    """
    Very naive placeholder parser.

    For demonstration only:
    - If question contains 'revenue' → metric = total_revenue
    - If question contains 'orders' → metric = total_orders
    - If question mentions 'month' → dimension = month
    """
    q = question.lower()

    metric = "total_revenue"
    if "order" in q:
        metric = "total_orders"

    dimension = None
    if "month" in q:
        dimension = "month"
    elif "day" in q:
        dimension = "day"

    # Example filter placeholder
    filter_expression = None
    if "last 6 months" in q or "last six months" in q:
        filter_expression = "order_date >= date_add('month', -6, current_date)"

    return ParsedQuery(metric=metric, dimension=dimension, filter=filter_expression)
