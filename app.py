from pathlib import Path

from flask import Flask, render_template, send_from_directory

PUBLIC_DIRECTORY = Path(__file__).resolve().parent / "public"
app = Flask(__name__, static_folder=None)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/<path:asset_path>")
def public_asset(asset_path):
    return send_from_directory(PUBLIC_DIRECTORY, asset_path)


if __name__ == "__main__":
    app.run(debug=True)
