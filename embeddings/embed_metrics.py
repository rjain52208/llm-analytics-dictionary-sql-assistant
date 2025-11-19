"""
embed_metrics.py

This script is a placeholder that represents how metric embeddings
would be generated in a real system.

In production, this could:
- Load metric definitions from metric_dictionary.json
- Use an embedding model (e.g. OpenAI, SentenceTransformers)
- Store the vectors for similarity search
"""

import json
from pathlib import Path


def load_metric_definitions(path: str = "backend/metric_dictionary.json"):
    file_path = Path(path)
    if not file_path.exists():
        print(f"[embed_metrics] Metric dictionary not found at: {file_path}")
        return []

    data = json.loads(file_path.read_text())
    return data.get("metrics", [])


def fake_generate_embedding(text: str):
    """
    This is just a dummy function to stand in for a real embedding model.
    It returns a small list of numbers as a placeholder.
    """
    return [len(text), len(text) % 7, len(text) % 11]


def main():
    metrics = load_metric_definitions()
    if not metrics:
        print("[embed_metrics] No metrics found to embed.")
        return

    print("[embed_metrics] Generating fake embeddings for metrics...\n")
    for metric in metrics:
        name = metric.get("name", "unknown_metric")
        desc = metric.get("description", "")
        embedding = fake_generate_embedding(desc)
        print(f"Metric: {name} | Embedding: {embedding}")

    print("\n[embed_metrics] Done (placeholder).")


if __name__ == "__main__":
    main()
