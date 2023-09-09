from win32com import client
import pythoncom
import psutil

class CatiaSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        print("...getting CATIA instance")
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.catia = None

    def start_or_get_catia(self):
        if not self.catia or not self.is_catia_running():
            pythoncom.CoInitialize()
            self.catia = client.Dispatch("CATIA.Application")
            self.catia.Visible = True
            print("Catia V5 successfully loaded!")

    def is_catia_running(self):
        for process in psutil.process_iter(['name']):
            if "CATIA.EXE" in process.info['name']:
                return True
        return False

    def close_catia(self):
        if self.catia:
            try:
                self.catia.Quit()
                self.catia = None
                print("Catia V5 has been closed.")
            except Exception as e:
                print("Catia V5 error on close", e)

def launch_catia():
    catia_instance = CatiaSingleton.get_instance()
    catia_instance.start_or_get_catia()

if __name__ == "__main__":
    launch_catia()