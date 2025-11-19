# 📘 LLM Analytics Dictionary & SQL Assistant

A production-style **LLM-powered analytics dictionary and SQL generation assistant** built to help analytics and BI teams translate plain-English questions into standardized business metrics and optimized SQL queries. This project simulates a real internal enterprise AI tool used by data teams to maintain metric consistency and accelerate SQL creation.

---

## 📁 Project Structure

llm-analytics-dictionary-sql-assistant/
│
├── backend/  
│   ├── main.py                # FastAPI endpoints  
│   ├── sql_generator.py       # Builds SQL from metrics + filters  
│   ├── parser.py              # Parses user queries using LLM/rules  
│   ├── metric_dictionary.json # Metric definitions  
│   ├── requirements.txt       # Placeholder dependencies  
│
├── embeddings/  
│   ├── embed_metrics.py       # Generates embeddings for metric search  
│   ├── vectors.npy            # Stored embeddings (placeholder)  
│   └── model.txt              # Placeholder embedding model  
│
├── frontend/  
│   ├── README.md              # Notes for optional React UI  
│   └── placeholder.txt        # Placeholder file  
│
└── README.md

---

## 🚀 Overview

This system acts like an “AI data analyst.” A user enters a question like:

**“Show me revenue by month for 2024”**

The system then:

1. Parses the question using an LLM-style logic  
2. Identifies relevant metrics and dimensions  
3. Looks them up using an analytics dictionary  
4. Uses embeddings to match ambiguous terms  
5. Generates SQL in the correct warehouse format  
6. Returns the final SQL query to the user or UI

This reduces dependency on analysts, prevents inconsistent metrics, and accelerates BI workflows.

---

## 🧠 Architecture (High-Level Flow)

User Query → Query Parser → Metric Resolver (Dictionary + Embeddings) → SQL Generator → Warehouse (Athena/Redshift/Postgres)

- **Query Parser**: Extracts metric, dimension, and filters from natural language  
- **Metric Resolver**: Matches user words to dictionary definitions  
- **SQL Generator**: Creates clean, optimized SQL  
- **Embeddings**: Improve accuracy when user uses vague terms  
- **API Layer**: Exposes the system to UIs or other apps  

---

## 🧩 Example End-to-End Flow

### 🔹 User Query:
“Show me total revenue by month for the last six months.”

### 🔹 Interpreted As:
- Metric → total_revenue  
- Dimension → month  
- Filter → last 6 months  
- Table → analytics.orders  

### 🔹 Example SQL Result:
SELECT
    date_trunc('month', order_date) AS month,
    SUM(order_amount) AS total_revenue
FROM analytics.orders
WHERE order_date >= date_add('month', -6, current_date)
GROUP BY 1
ORDER BY 1;

---

## ⚙️ Setup Instructions (Conceptual Only)

These steps represent how a real system would be run. You do **not** need to run them — they are here to make the repo look authentic.

### 🔹 Backend Setup (FastAPI)
pip install -r backend/requirements.txt  
uvicorn backend.main:app --reload

### 🔹 Embeddings Generation
python embeddings/embed_metrics.py

### 🔹 Optional React UI
npm install  
npm start

---

## 🔗 API Endpoints (Conceptual)

- **POST /parse_query** – Extracts metrics and filters  
- **POST /generate_sql** – Produces final SQL  
- **GET /metrics** – Lists available metrics  

---

## 🔮 Future Enhancements

- Add RAG pipeline (LangChain)  
- Add support for Snowflake / BigQuery  
- Enhance metric lineage tracking  
- Add user authentication  
- Add UI-based SQL editor  
- Add metadata connectors (dbt semantic layer)  

---

## 📄 License

MIT License.

