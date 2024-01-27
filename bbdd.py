import sqlite3
nombre_BBDD = "BBDD_Hipotecas"

#Este meétodo crea la base de datos, o se conecta a la misma en caso de que ya esté creada
def get_conexionBBDD():

    try:

        conexion = sqlite3.connect(nombre_BBDD)
        return conexion

    except:

        pass


#Este método crea las tablas de la base de datos en caso de que no existan
def crear_tablas():

    tablas = ["CREATE TABLE IF NOT EXISTS CLIENTES ("
              "DNI INTEGER PRIMARY KEY NOT NULL,"
              "LETRA_DNI VARCHAR(1) NOT NULL,"
              "NOMBRE VARCHAR(50) NOT NULL,"  
              "APELLIDO1 VARCHAR(50) NOT NULL," 
              "APELLIDO2 VARCHAR(50) NOT NULL,"
              "EMAIL VARCHAR(50) NOT NULL," 
              "CAPITAL_SOLICITADO REAL NOT NULL)",
              
              "CREATE TABLE IF NOT EXISTS HIPOTECAS ("
              "ID_HIPOTECA INTEGER PRIMARY KEY AUTOINCREMENT,"
              "CUOTA_MENSUAL REAL NOT NULL,"
              "IMPORTE_TOTAL REAL NOT NULL,"
              "DNI_CLIENTE INTEGER NOT NULL,"
              "FOREIGN KEY(DNI_CLIENTE) REFERENCES CLIENTES(DNI) ON DELETE CASCADE)"]
    
    db = get_conexionBBDD()
    cursor = db.cursor()
    for tabla in tablas:

        cursor.execute(tabla)