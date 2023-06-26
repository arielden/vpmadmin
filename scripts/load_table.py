from partstr.models import Part, Level, PnType
from django.contrib.auth.models import User
import csv

def run():
    with open ('files/tabla_test.csv') as f:
        reader = csv.reader(f)
        next(reader) #Salta el encabezado

        Part.objects.all().delete() # Borra todas las entradas de la tabla partstr_part
        n = 0
        for row in reader:
            #print(row)
            user = User.objects.get(username='arield')
            pnlevel, _ = Level.objects.get_or_create(name=row[0])
            ptype, _ = PnType.objects.get_or_create(name=row[3])

            part = Part(partnumber = row[1],
                        designation = row[2],
                        pntype = ptype,
                        resp = user,
                        level = pnlevel,
                        mass = row[4],
                        xcg = row[5],
                        ycg = row[6],
                        zcg = row[7],
                        #status = ,
                        #parent = ,

            )
            part.save()
            n += 1

        print(f"Se cargaron {n} filas.")

# Para ejecutar este script:
# Crear la carpeta script en el directorio raiz, dentro crear __init__.py
# instalar django-extensions con pip y agregar 'django_extensions' a INSTALLED_APPS
# --> python manage.py runscript load_table <-- # load_table sin .py!