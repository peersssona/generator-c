import argparse
from quotes.cli import run_cli
from quotes.api import app


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Random Quote Generator")
    parser.add_argument("--mode", choices=["cli", "api"], default="cli")
    args = parser.parse_args()

    if args.mode == "cli":
        run_cli()
    else:
        app.run(host="0.0.0.0", port=5000, debug=True)