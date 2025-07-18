from flask import Flask, render_template, request, jsonify
from constants import VOTE_ATTEMPTS
from scraper import ejecutar_votaciones
import asyncio
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, "frontend", "templates")
static_dir = os.path.join(base_dir, "frontend", "static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/votar", methods=["POST"])
def votar():
    data = request.get_json()
    intentos = data.get("votes", VOTE_ATTEMPTS)
    logs = asyncio.run(ejecutar_votaciones(intentos))
    return jsonify({
        "mensaje": f"✅ Votaciones completadas ({intentos} intento(s))",
        "logs": logs
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
