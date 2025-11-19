"""
sql_generator.py

This module contains helper functions to build SQL queries
from parsed metric, dimension, and filter information.

The implementation here is intentionally simple and acts
as a placeholder to show how a real system could be structured.
"""


from typing import Optional


def build_revenue_by_month_sql(table: str = "analytics.orders") -> str:
    """
    Example SQL builder: total_revenue by month for last 6 months.
    """
    return f"""
    SELECT
        date_trunc('month', order_date) AS month,
        SUM(order_amount) AS total_revenue
    FROM {table}
    WHERE order_date >= date_add('month', -6, current_date)
    GROUP BY 1
    ORDER BY 1;
    """.strip()


def build_generic_sql(
    metric: str,
    dimension: Optional[str] = None,
    filter_expression: Optional[str] = None,
    table: str = "analytics.orders",
) -> str:
    """
    Very simplified example of SQL generation.

    In a real implementation, this would:
    - Look up metric definitions
    - Handle different warehouses (Athena, Redshift, Postgres)
    - Apply filters and groupings dynamically
    """
    select_clause = "SUM(order_amount) AS total_revenue"

    if metric == "total_orders":
        select_clause = "COUNT(*) AS total_orders"

    group_by_clause = ""
    if dimension == "month":
        group_by_clause = "date_trunc('month', order_date) AS month"
    elif dimension == "day":
        group_by_clause = "date_trunc('day', order_date) AS day"

    where_clause = "1=1"
    if filter_expression:
        where_clause = filter_expression

    if group_by_clause:
        sql = f"""
        SELECT
            {group_by_clause},
            {select_clause}
        FROM {table}
        WHERE {where_clause}
        GROUP BY 1
        ORDER BY 1;
        """
    else:
        sql = f"""
        SELECT
            {select_clause}
        FROM {table}
        WHERE {where_clause};
        """

    return sql.strip()
