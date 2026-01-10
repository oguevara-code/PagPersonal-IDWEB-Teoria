from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__, 
            static_folder="static", 
            template_folder="templates"
)

DB_NAME = "comentarios.db"

# =========================
# BASE DE DATOS
# =========================

def conectar_db():
    return sqlite3.connect(DB_NAME)

def inicializar_db():
    if not os.path.exists(DB_NAME):
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            mensaje TEXT NOT NULL,
            fecha TEXT NOT NULL
        )
        """)
        conn.commit()
        conn.close()

# Se ejecuta al iniciar el servidor
inicializar_db()


# Rutas de páginas HTML

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")

@app.route("/estudios")
def estudios():
    return render_template("estudios.html")

@app.route("/metas")
def metas():
    return render_template("metas.html")

@app.route("/comentarios")
def comentarios_page():
    return render_template("comentarios.html")

@app.route("/agregar-comentario-page")
def agregar_comentario_page():
    return render_template("agregar-comentario.html")


# API DE COMENTARIOS

@app.route("/api/comentarios", methods=["GET"])
def obtener_comentarios():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nombre, mensaje, fecha
        FROM comentarios
        ORDER BY id DESC
    """)
    filas = cursor.fetchall()
    conn.close()

    comentarios = []
    for f in filas:
        comentarios.append({
            "nombre": f[0],
            "mensaje": f[1],
            "fecha": f[2]
        })

    return jsonify(comentarios)

@app.route("/comentarios", methods=["POST"])
def agregar_comentario():
    data = request.json

    nombre = data.get("nombre")
    mensaje = data.get("mensaje")

    if not nombre or not mensaje:
        return jsonify({"error": "Datos incompletos"}), 400

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO comentarios (nombre, mensaje, fecha) VALUES (?, ?, datetime('now'))",
        (nombre, mensaje)
    )
    conn.commit()
    conn.close()

    return jsonify({"mensaje": "Comentario guardado correctamente"})


# Iniciar servidor

if __name__ == "__main__":
    app.run(debug=True)