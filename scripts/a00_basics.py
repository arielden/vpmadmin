def asreference(part:object) -> None:
    """
    Recibe como parámetro, un objeto part.\n
    Se encarga de enviar a CATIA V5 el código
    para crear/abrir la parte como referencia.
    """
    
    print(part)
    print(part.designation)
    print(f"Lógica para carga de partes.")

def newprod(part:object) -> None:
    """
    Recibe como parámetro, un objeto part.\n
    Se encarga de enviar a CATIA V5 el código
    para crear/abrir la parte dentro de su estructura
    de producto.
    """

    print(part)
    print("Lógica para carga de productos.")
