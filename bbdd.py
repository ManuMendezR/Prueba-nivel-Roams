import sqlite3
nombre_BBDD = "BBDD_Hipotecas"

def get_conexionBBDD():

    conexion = sqlite3.connect(nombre_BBDD)
    return conexion

def crear_tablas():

    tablas = ["CREATE TABLE CLIENTES ("
              "DNI INTEGER PRIMARY KEY NOT NULL,"
              "LETRA_DNI VARCHAR2(1) NOT NULL,"
              "NOMBRE VARCHAR(50) NOT NULL,"  
              "APELLIDO1 VARCHAR(50) NOT NULL," 
              "APELLIDO2 VARCHAR(50) NOT NULL,"
              "EMAIL VARCHAR(50) NOT NULL," 
              "CAPITAL_SOLICITADO REAL NOT NULL)",
              
              "CREATE TABLE HIPOTECAS ("
              "ID_HIPOTECA INTEGER PRIMARY KEY AUTOINCREMENT,"
              "CUOTA_MENSUAL REAL NOT NULL,"
              "IMPORTE_TOTAL REAL NOT NULL,"
              "DNI_CLIENTE INTEGER NOT NULL,"
              "FOREIGN KEY(DNI_CLIENTE) REFERENCES CLIENTES(DNI) ON DELETE CASCADE)"]
    
    db = get_conexionBBDD()
    cursor = db.cursor()
    for tabla in tablas:

        cursor.execute(tabla)