from win32com import client
import os
from .a00_catialauncher import launch_catia
from django.conf import settings
import uuid

#--------Aux functions------------------------------------------
def generate_uuid():
    return str(uuid.uuid4())

def set_properties(template: object, part:object) -> None:
    """
    Set properties for a CATPart
    Receive the template, load properties from DB
    and save the new part.
    """

    # Get the parameters collection of the CATPart.
    part_parameters = template.Part.Parameters

    # Set parameters values, works both on tree and part properties.
    pn_catiadoc = part_parameters.Item("Part Number")
    pn_catiadoc.Value = part.partnumber
    
    desig_catiadoc = part_parameters.Item("Definition")
    desig_catiadoc.Value = part.designation

    id_catiadoc = part_parameters.Item("partID")
    id_catiadoc.Value = part.id

#---------------------------------------------------------------

#-----------DOC-CAD functions-----------------------------------
def newpart(part:object) -> None:
    """
    Receive a Part Object as an argument.\n
    Create and save a CATPart file based on a template.
    """
    launch_catia()

    # Template variables
    template_file = "genericPart_v01.CATPart"
    template_path = os.path.join(settings.MEDIA_ROOT, 'templates', template_file)

    # Load the template file.
    catapp = client.Dispatch('CATIA.Application')
    documents = catapp.Documents
    template = documents.Open(template_path)

    # Modify the template based on Part objects properties.
    set_properties(template, part)
    # ...Here the different parameters to be modified

    # Define location and name for the new part.
    file_name = f"{generate_uuid()}.CATPart"
    file_path = os.path.join(settings.MEDIA_ROOT, 'catia_data', file_name)

    # Save the template as new file.
    template.SaveAs(file_path)
    template.Close()

    # Asign file_path to Part obj
    part.file_path = file_path
    part.save()

def doccadDelete(part:object) -> None:
    try:
        os.remove(str(part.file_path))
        part.file_path.delete()
        part.save()
        msg = "DOCCAD deleted!"
    except OSError as err:
        msg = err

    return print(msg)
    
#---------------------------------------------------------------

#--------Load CATPart functions---------------------------------
def asreference(part:object) -> None:
    """
    Receive a Part Object as an argument.\n
    Loads the CATPart file asociated to the Part obj.
    """
    launch_catia()
    # Absolute path (".path" at the end)
    file_path = part.file_path.path

    # Check if exists
    if os.path.exists(file_path):
        # Load CATIA file.
        catapp = client.Dispatch('CATIA.Application')
        documents = catapp.Documents
        partDocument = documents.Open(file_path)
    else:
        print(f"The file does not exist at the specified path: {file_path}")
    
def asnewprod(part:object) -> None:
    """
    Recibe como argumento, un objeto part.\n
    Se encarga de enviar a CATIA V5 el código
    para ABRIR la parte dentro de su estructura
    de producto.
    """
    launch_catia()

    print("Lógica para carga de productos.")
#---------------------------------------------------------------