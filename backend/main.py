from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="LLM Analytics Dictionary & SQL Assistant",
    description="API layer for parsing analytics questions and generating SQL.",
    version="0.1.0",
)


class QueryRequest(BaseModel):
    question: str
    warehouse: Optional[str] = "athena"


class ParsedQuery(BaseModel):
    metric: str
    dimension: Optional[str] = None
    filter: Optional[str] = None


class SQLResponse(BaseModel):
    sql: str
    parsed: ParsedQuery


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/generate_sql", response_model=SQLResponse)
def generate_sql(request: QueryRequest):
    """
    This is a simple placeholder implementation.

    In a real system, this would:
    1. Parse the question using an LLM / rules.
    2. Resolve the metric from a metric dictionary.
    3. Build a warehouse-specific SQL query.
    """
    # Fake parsed output just for demonstration
    parsed = ParsedQuery(
        metric="total_revenue",
        dimension="month",
        filter="last_6_months",
    )

    # Example SQL string (placeholder)
    sql = """
    SELECT
        date_trunc('month', order_date) AS month,
        SUM(order_amount) AS total_revenue
    FROM analytics.orders
    WHERE order_date >= date_add('month', -6, current_date)
    GROUP BY 1
    ORDER BY 1;
    """.strip()

    return SQLResponse(sql=sql, parsed=parsed)
