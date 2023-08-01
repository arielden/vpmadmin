import win32com.client

"""
Ejecuta macros de CATIA en formato .catvbs
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
    library_name = "F:\\Projects\\SOFTWARE\\vpmadmin\\files\\catia\\macrolib"
    library_type = 1  # Según la documentación, el valor de catScriptLibraryTypeDocument es 3
    program_name = "Macro1.catvbs"
    function_name = "CATMain"
    parameters = ["Ariel"]

    # Llamar a la función para ejecutar la macro
    success = execute_catia_macro(library_name, library_type, program_name, function_name, parameters)

    if success:
        print("La macro se ejecutó exitosamente.")
    else:
        print("Error al ejecutar la macro.")
