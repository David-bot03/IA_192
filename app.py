# -*- coding: utf-8 -*-
#hola
"""app.ipynb"""

from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- Inventario con stock ---
inventario = {
    "camisa":   {"precio": 50000, "descuento": 10, "stock": 15},
    "pantalon": {"precio": 80000, "descuento": 0,  "stock": 8},
    "zapatos":  {"precio": 120000, "descuento": 20, "stock": 5},
}

# --- Función para consultar producto ---
def consultar_producto(nombre_producto):
    nombre_producto = nombre_producto.lower()
    if nombre_producto in inventario:
        producto = inventario[nombre_producto]
        precio = producto["precio"]
        descuento = producto["descuento"]
        stock = producto["stock"]

        if descuento > 0:
            precio_final = precio - (precio * descuento / 100)
            return (f"✅ '{nombre_producto}' cuesta {precio} pesos, "
                    f"con {descuento}% de descuento → Precio final: {precio_final} pesos. "
                    f"📦 Stock disponible: {stock} unidades.")
        else:
            return (f"✅ '{nombre_producto}' cuesta {precio} pesos, "
                    f"sin descuento. "
                    f"📦 Stock disponible: {stock} unidades.")
    else:
        return f"❌ '{nombre_producto}' no está en el inventario."

# --- Plantilla HTML ---
html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>ChatBot Inventario</title>
    <style>
        body { font-family: Arial; background: #f4f6f9; display:flex; justify-content:center; align-items:center; height:100vh;}
        .chatbox { background:white; padding:20px; border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1); width:400px;}
        input, button { padding:10px; width:100%; margin-top:10px; border-radius:8px; border:1px solid #ccc;}
        button { background:#007BFF; color:white; border:none; cursor:pointer;}
        button:hover { background:#0056b3;}
        .respuesta { margin-top:15px; padding:10px; background:#eaf4ff; border-radius:8px;}
    </style>
</head>
<body>
    <div class="chatbox">
        <h2>🤖 ChatBot Inventario</h2>
        <form method="POST">
            <input type="text" name="producto" placeholder="Ej: camisa" required>
            <button type="submit">Consultar</button>
        </form>
        {% if respuesta %}
        <div class="respuesta">{{ respuesta }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    respuesta = ""
    if request.method == "POST":
        producto = request.form["producto"]
        respuesta = consultar_producto(producto)
    return render_template_string(html, respuesta=respuesta)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

