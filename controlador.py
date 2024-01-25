from bbdd import get_conexionBBDD

#Este método va a validar que el DNI introducido sea válido
def validarDNI(dni, letraDni):

            listaLetras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        
            resultado = dni%23
        
            if(letraDni.upper() == listaLetras[resultado]):

                
                return True
            
            else:

                return False
            
#Este método comprueba que el cliente introducido exista
def comprobarExistenciaCliente(dni):
      
      valorValidarDNI = [dni]
      bbdd = get_conexionBBDD()
      cursor = bbdd.cursor()
      cursor.execute("SELECT * FROM CLIENTES WHERE DNI = ?", valorValidarDNI)
      validarCliente = cursor.fetchall()
      bbdd.commit()
      bbdd.close()

      #Valido que el cliente asociado al dni exista
      if(len(validarCliente)>0):
            
            return True
            
      else:
            
            return False
      


#Este método crea nuevos clientes, validando que el dni introducido sea correcto
def crearCliente(dni, letraDni, nombre, apellido1, apellido2, email, capitalSolicitado):

    if(validarDNI(dni,letraDni) == True):
          
          bbdd = get_conexionBBDD()
          cursor = bbdd.cursor()
          sentencia = "INSERT INTO CLIENTES(DNI, LETRA_DNI, NOMBRE, APELLIDO1, APELLIDO2, EMAIL, CAPITAL_SOLICITADO) VALUES(?,?,?,?,?,?,?)"
          cursor.execute(sentencia,[dni, letraDni, nombre, apellido1, apellido2, email, capitalSolicitado])
          bbdd.commit()
          bbdd.close()

          return True

    else:
          return False

#Este método actualiza los datos de un cliente, validando que este exista   
def actualizarCliente(dni, nombre, apellido1, apellido2, email, capitalSolicitado):
      
      if(comprobarExistenciaCliente(dni)==True):
            
            bbdd = get_conexionBBDD()
            cursor = bbdd.cursor()
            sentencia = "UPDATE CLIENTES SET NOMBRE = ?, APELLIDO1 = ?, APELLIDO2 = ?, EMAIL = ?, CAPITAL_SOLICITADO = ? WHERE DNI = ?"
            cursor.execute(sentencia,[nombre, apellido1, apellido2, email, capitalSolicitado, dni])
            bbdd.commit()
            bbdd.close()

            return True

      else:
            
            return False

#Este método devuelve los datos de un cliente, validando que este exista    
def consultarCliente(dni):
      
      if(comprobarExistenciaCliente(dni)==True):
            
            bbdd = get_conexionBBDD()
            cursor = bbdd.cursor()
            sentencia = "SELECT LETRA_DNI, NOMBRE, APELLIDO1, APELLIDO2, EMAIL, CAPITAL_SOLICITADO FROM CLIENTES WHERE DNI = ?"
            cursor.execute(sentencia,[dni])
            resultado = cursor.fetchone
            bbdd.commit()
            bbdd.close()

            return resultado

      else:
            
            return False

#Este método eliminar los datos de un cliente, validando que exista, y eliminando también las hipotecas asociadas al mismo.    
def eliminarCliente(dni):
      
      if(comprobarExistenciaCliente(dni)==True):
            
            bbdd = get_conexionBBDD()
            bbdd.execute("PRAGMA foreign_keys = 1")
            cursor = bbdd.cursor()
            sentencia = "DELETE FROM CLIENTES WHERE DNI = ?"
            cursor.execute(sentencia,[dni])
            bbdd.commit()
            bbdd.close()

            return True
      
      else:
            
            return False