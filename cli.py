#!/usr/bin/env python
import typer
from rich import print
import json
import requests

app = typer.Typer()


@app.command(help="Load data into the database")
def load():
    with open("output.json") as f:
        data = json.load(f)
    payload = {
        "documents": []
    }
    for d in data[:100]:
        payload["documents"].append(
            {
                "text": d.get("body"),
                "metadata": {"source": d.get("story_url")}
            }
        )

    response = requests.post("http://localhost:8000/documents", json=payload)
    print(response.json())

if __name__ == "__main__":
    app()
