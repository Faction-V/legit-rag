#!/usr/bin/env python
import typer
from rich import print
import json
import requests
from src.config import Settings
settings = Settings()
app = typer.Typer()

@app.command(help="List the current settings the app is using.")
def print_settings():
    print(settings)


if __name__ == "__main__":
    app()
