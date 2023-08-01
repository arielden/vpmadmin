from win32com import client
import os
from .a00_catialauncher import launch_catia
from django.conf import settings

def asreference(part:object) -> None:
    """
    Recibe como argumento un objeto Part.
    Abre el archivo CATPart asociado al objeto Part.
    """
    launch_catia()
    # Obtiene la ruta absoluta del archivo asociado (".path" al final)
    file_path = part.file_path.path

    # Verifica si existe
    if os.path.exists(file_path):
        # Abre el archivo en CATIA
        catapp = client.Dispatch('CATIA.Application')
        documents = catapp.Documents
        partDocument = documents.Open(file_path)
    else:
        print(f"El archivo no existe en la ruta especificada: {file_path}")
    
def asnewprod(part:object) -> None:
    """
    Recibe como argumento, un objeto part.\n
    Se encarga de enviar a CATIA V5 el código
    para ABRIR la parte dentro de su estructura
    de producto.
    """
    launch_catia()

    print("Lógica para carga de productos.")

def newpart(part:object) -> None:
    """
    Recibe como argumento, un objeto part.\n
    Se encarga de enviar a CATIA V5 el código
    para CREAR el archivo CATPART.
    """
    launch_catia()

    # Define la ubicación, nombre y extensión (CATPart) del archivo.
    file_path = os.path.join(settings.MEDIA_ROOT, 'catia_data', f"{part.partnumber}.CATPart")

    # Crea el CATPart (vacío)
    catapp = client.Dispatch('CATIA.Application')
    documents = catapp.Documents
    partDocument = documents.Add("Part")

    # Guarda
    partDocument.SaveAs(file_path)
    #partDocument.Close()

    # Asigna el file_path a la instancia de Part.
    part.file_path = file_path
    part.save()