from flask import Flask, render_template_string, request

app = Flask(__name__)

# Datos de ejemplo
productos = [
    {"nombre": "Camiseta Minimal", "tallas": ["S", "M", "L", "XL"], "precio": 29.99, "imagen": "https://via.placeholder.com/300"},
    {"nombre": "Chaqueta Urbana", "tallas": ["XS", "S", "M", "L"], "precio": 89.99, "imagen": "https://via.placeholder.com/300"},
    {"nombre": "Pantalón Clásico", "tallas": ["M", "L", "XL", "2XL"], "precio": 49.99, "imagen": "https://via.placeholder.com/300"},
    {"nombre": "Sudadera Transparente", "tallas": ["XXS","XS","S","M","L","XL","2XL","3XL","4XL"], "precio": 59.99, "imagen": "https://via.placeholder.com/300"}
]

# Plantilla HTML con CSS y JS embebido
html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Tienda de Ropa</title>
    <style>
        body {
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: #f2f2f2;
            color: #111;
        }
        header {
            position: sticky;
            top: 0;
            background: rgba(255,255,255,0.8);
            backdrop-filter: blur(10px);
            padding: 20px;
            text-align: center;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 { margin: 0 0 10px 0; font-weight: 600; }
        main.productos-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            padding: 30px;
        }
        .producto {
            background: rgba(255,255,255,0.6);
            backdrop-filter: blur(8px);
            border-radius: 20px;
            overflow: hidden;
            text-align: center;
            padding: 20px;
            transform: translateY(50px);
            opacity: 0;
            transition: all 0.8s ease;
        }
        .producto img { width: 100%; border-radius: 15px; }
        .producto h2 { margin: 10px 0 5px 0; }
        .producto p { margin: 0; font-weight: 500; }
        select { padding: 5px; border-radius: 5px; border: 1px solid #ccc; }
        label { margin-right: 10px; }
    </style>
</head>
<body>
    <header>
        <h1>Tienda de Ropa</h1>
        <form method="get" id="filtroTalla">
            <label for="talla">Filtrar por talla:</label>
            <select name="talla" id="talla" onchange="this.form.submit()">
                <option value="">Todas</option>
                <option value="XXS">XXS</option>
                <option value="XS">XS</option>
                <option value="S">S</option>
                <option value="M">M</option>
                <option value="L">L</option>
                <option value="XL">XL</option>
                <option value="2XL">2XL</option>
                <option value="3XL">3XL</option>
                <option value="4XL">4XL</option>
            </select>
        </form>
    </header>

    <main class="productos-container">
        {% for producto in productos %}
        <div class="producto">
            <img src="{{ producto.imagen }}" alt="{{ producto.nombre }}">
            <h2>{{ producto.nombre }}</h2>
            <p>{{ producto.precio }}€</p>
        </div>
        {% endfor %}
    </main>

    <script>
        // Animación al hacer scroll
        const productos = document.querySelectorAll('.producto');
        function mostrarProductos() {
            const triggerBottom = window.innerHeight / 5 * 4;
            productos.forEach(producto => {
                const productoTop = producto.getBoundingClientRect().top;
                if(productoTop < triggerBottom) {
                    producto.style.transform = 'translateY(0)';
                    producto.style.opacity = '1';
                }
            });
        }
        window.addEventListener('scroll', mostrarProductos);
        window.addEventListener('load', mostrarProductos);
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    talla_filtrada = request.args.get("talla")
    if talla_filtrada:
        filtrados = [p for p in productos if talla_filtrada in p["tallas"]]
    else:
        filtrados = productos
    return render_template_string(html, productos=filtrados)

if __name__ == "__main__":
    app.run(debug=True)
