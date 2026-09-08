from fastapi import FastAPI
# Crear la instancia de la aplicación
app = FastAPI()

alumnos = [
    {
        "id": 1,
        "nombre": "Sergio V",
        "edad": 20,
        "carrera": "Ingeniería en IA",
        "semestre": 3
    },
    {
        "id": 2,
        "nombre": "Carlos López",
        "edad": 21,
        "carrera": "Ingeniería Informática",
        "semestre": 5
    }
]

# Definir una ruta de tipo GET
@app.get("/")
def read_root():
    return {"Hola": "Mundo"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/alumnos")
def obtener_alumnos():
    return alumnos

@app.get("/alumnos/{alumno_id}")
def obtener_alumno(alumno_id: int):

    for alumno in alumnos:
        if alumno["id"] == alumno_id:
            return alumno

    return {
        "mensaje": "Alumno no encontrado"
    }
