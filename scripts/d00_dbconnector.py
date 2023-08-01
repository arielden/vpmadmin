import win32com.client

def show_query():
    # Establecer la conexión con la base de datos MySQL
    conn = win32com.client.Dispatch("ADODB.Connection")

    # Configurar los detalles de conexión
    dsn = "dbsource"
    username = "root"
    password = "root"

    # Establecer la cadena de conexión utilizando el DSN
    conn.ConnectionString = "DSN={};UID={};PWD={};".format(dsn, username, password)

    print(conn.ConnectionString)

    # Conectar a la base de datos
    conn.Open()

    # Verificar si la conexión se ha establecido correctamente
    if conn.State == 1:
        print("Conexión exitosa")
    else:
        print("Error al conectar a la base de datos")
        return

 # Ejecutar la consulta en la base de datos
    query = "SELECT partnumber FROM partstr_part"
    rs = win32com.client.Dispatch("ADODB.Recordset")
    rs.Open(query, conn)

    # Obtener los valores de la columna "partnumber"
    partnumbers = []
    if not rs.EOF:
        rs.MoveFirst()
        while not rs.EOF:
            partnumber = rs.Fields("partnumber").Value
            partnumbers.append(partnumber)
            rs.MoveNext()

    # Cerrar el recordset y la conexión con la base de datos
    rs.Close()
    conn.Close()

    # Mostrar el resultado en un MsgBox en CATIA V5
    catia = win32com.client.Dispatch("CATIA.Application")
    # catia.SystemService.Processes.Execute("MsgBox \"Part Numbers:\\n{}\"".format('\n'.join(partnumbers)))

    # Cerrar la conexión con la base de datos
    # conn.Close()
    print(partnumbers)
# Llamar a la función para crear la estructura
show_query()
