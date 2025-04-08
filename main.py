from fastapi import FastAPI
from pydantic import BaseModel
from Calculadora_noches import calcular_estadia

app = FastAPI()

class HospedajeRequest(BaseModel):
    fecha_inicio: str
    fecha_salida: str
    numero_perros: int

@app.post("/calcular_precio")
def calcular_precio(data: HospedajeRequest):
    resultado = calcular_estadia(
        fecha_inicio=data.fecha_inicio,
        fecha_salida=data.fecha_salida,
        numero_perros=data.numero_perros
    )
    return {"precio_total": resultado}