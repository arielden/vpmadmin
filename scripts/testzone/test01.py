import win32com.client

"""
Ejecuta macros de CATIA en formato .catvba
"""

def execute_catia_macro(library_name, library_type, program_name, function_name, parameters):
    try:
        catia = win32com.client.Dispatch("CATIA.Application")  # Iniciar la aplicación CATIA
        catia.SystemService.ExecuteScript(library_name, library_type, program_name, function_name, parameters)
        #catia.Quit()
        return True
    except Exception as e:
        print("Error al ejecutar la macro:", str(e))
        return False

if __name__ == "__main__":
    # Definir los argumentos necesarios para la función ExecuteScript

    #(catScriptLibraryTypeDocument = 0, catScriptLibraryTypeDirectory = 1, catScriptLibraryTypeVBAProject = 2)

    library_name = "F:\\Projects\\SOFTWARE\\vpmadmin\\files\\catia\\vba\\macros-set.catvba" #Ruta completa al proyecto
    library_type = 2  # Según la documentación, para catScriptLibraryTypeVBAProject = 2
    program_name = "hola"
    function_name = "CATMain"
    parameters = ["mongo"]

    # Llamar a la función para ejecutar la macro
    success = execute_catia_macro(library_name, library_type, program_name, function_name, parameters)

    if success:
        print("La macro se ejecutó exitosamente.")
    else:
        print("Error al ejecutar la macro.")
