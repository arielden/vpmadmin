import win32com.client
import pythoncom

class CatiaSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.catia = None
        try:
            pythoncom.CoInitialize()
            self.start_or_get_catia()
            print("Catia V5 se ha iniciado correctamente.")
        except Exception as e:
            print("Error al lanzar Catia V5:", e)

    def start_or_get_catia(self):
        try:
            self.catia = win32com.client.GetActiveObject("CATIA.Application")
        except Exception:
            self.catia = win32com.client.Dispatch("CATIA.Application")
            self.catia.Visible = True

    def close_catia(self):
        if self.catia:
            try:
                self.catia.Quit()
                self.catia = None
                print("Catia V5 se ha cerrado correctamente.")
            except Exception as e:
                print("Error al cerrar Catia V5:", e)

    def create_new_part(self, part_object):
        # Código para crear una nueva parte, como se mostró anteriormente
        pass

def launch_catia():
    catia_instance = CatiaSingleton.get_instance()
    # Suponiendo que ya tienes el objeto parte disponible en la variable "part"
    part = ...  # Tu objeto parte aquí
    catia_instance.create_new_part(part)

if __name__ == "__main__":
    launch_catia()



# class CatiaSingleton:
#     _instance = None

#     @classmethod
#     def get_instance(cls):
#         if not cls._instance:
#             cls._instance = cls()
#         return cls._instance

#     def __init__(self):
#         try:
#             pythoncom.CoInitialize()
#             self.catia = win32com.client.Dispatch("CATIA.Application")
#             self.catia.Visible = True
#             print("Catia V5 se ha iniciado correctamente.")
#         except Exception as e:
#             print("Error al lanzar Catia V5:", e)

# def launch_catia():
#     catia_instance = CatiaSingleton.get_instance()

# if __name__ == "__main__":
#     launch_catia()


def asreference(part:object) -> None:
    """
    Recibe como parámetro, un objeto part.\n
    Se encarga de enviar a CATIA V5 el código
    para crear/abrir la parte como referencia.
    """
    
    print(part)
    print(part.designation)
    print("se lanza CATIA...")

    launch_catia()

    

def newprod(part:object) -> None:
    """
    Recibe como parámetro, un objeto part.\n
    Se encarga de enviar a CATIA V5 el código
    para crear/abrir la parte dentro de su estructura
    de producto.
    """

    print(part)
    print("Lógica para carga de productos.")


