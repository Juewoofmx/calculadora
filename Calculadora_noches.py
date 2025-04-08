from datetime import datetime, timedelta

def calcular_estadia(fecha_inicio: str, fecha_salida: str, numero_perros: int) -> float:
    # Lista de fechas de temporada alta
    temporada_alta = ["24/12", "25/12", "26/12", "31/12", "01/01", "02/01", "14/02", "01/07", "15/09", "16/09"]

    # Convertir fechas a objetos datetime
    formato = "%d/%m/%Y"
    inicio = datetime.strptime(fecha_inicio, formato)
    salida = datetime.strptime(fecha_salida, formato)

    # Calcular número de noches
    noches = (salida - inicio).days
    if noches <= 0:
        return 0

    # Calcular cuántas noches son de temporada alta
    noches_alta = sum(
        1 for i in range(noches)
        if (inicio + timedelta(days=i)).strftime("%d/%m") in temporada_alta
    )

    # Precios
    precio_base = 300
    precio_alta = 350

    total = ((noches - noches_alta) * precio_base + noches_alta * precio_alta) * numero_perros
    return total
