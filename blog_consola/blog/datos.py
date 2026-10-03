# blog/datos.py

# 1. Perfil base
perfil_autor = {
    "nombre": "Ana Gómez",
    "rol": "Data Scientist",
    "email": "ana@ejemplo.com"
}

# 2. Tuplas y Sets (Variables estáticas de validación)
estados_post = ("publicado", "borrador", "archivado")
etiquetas_blog = {"python", "datos", "ia", "sql"}

# 3. Base de datos simulada (Lista de diccionarios)
posts = [
    {
        "id": 1,
        "titulo": "Introducción a Data Science",
        "contenido": "El análisis de datos nos permite extraer valor...",
        "autor": perfil_autor,
        "tags": ["datos", "python"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Mejores prácticas en SQL",
        "contenido": "Las Window Functions son vitales para...",
        "autor": perfil_autor,
        "tags": ["sql", "datos"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "", 
        "contenido": "Contenido de prueba",
        "autor": "Juan Pérez", 
        "estado": "en_revision" 
    }
]