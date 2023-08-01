import win32com.client

def execute_macro(mod_name:str, function_name:str, parameters:list)->None:
    """
    Ejecuta una subrutina en CATIA de nombre 'function_name' perteneciente al
    módulo 'mod_name'. Los parámetros necesarios se pasan en una lista
    'parameters'.
    """
    
    library_name = "F:\\Projects\\SOFTWARE\\vpmadmin\\files\\catia\\macros\\macros-set.catvba" #Ruta completa al proyecto
    library_type = 2  # Según la documentación, para catScriptLibraryTypeVBAProject = 2

    try:
        catia = win32com.client.Dispatch("CATIA.Application")  # Iniciar la aplicación CATIA
        catia.SystemService.ExecuteScript(library_name, library_type, mod_name, function_name, parameters)
        return True
    except Exception as e:
        print("Error al ejecutar la macro:", str(e))
        return False
