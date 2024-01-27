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

      bbdd = get_conexionBBDD()
      cursor = bbdd.cursor()
      sentencia = "SELECT * FROM CLIENTES WHERE DNI = ?"
      cursor.execute(sentencia, [dni])
      validarCliente = cursor.fetchall()
      bbdd.commit()
      bbdd.close()

      
      if(len(validarCliente)>0):
            
            return True
            
      else:
            
            return False
      


#Este método crea nuevos clientes, validando que el dni introducido sea correcto y que no exista en la base de datos
def crearCliente(dni, letraDni, nombre, apellido1, apellido2, email, capitalSolicitado):

    if(validarDNI(dni,letraDni) == True):
          
          if(comprobarExistenciaCliente(dni)==False):
          
            bbdd = get_conexionBBDD()
            cursor = bbdd.cursor()
            sentencia = "INSERT INTO CLIENTES(DNI, LETRA_DNI, NOMBRE, APELLIDO1, APELLIDO2, EMAIL, CAPITAL_SOLICITADO) VALUES(?,?,?,?,?,?,?)"
            cursor.execute(sentencia,[dni, letraDni, nombre, apellido1, apellido2, email, capitalSolicitado])
            bbdd.commit()
            bbdd.close()

            return True
          
          else:
                
                return False


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
            resultado = cursor.fetchone()
            bbdd.commit()
            bbdd.close()

            return resultado

      else:
            
            return False

#Este método elimina los datos de un cliente, validando que exista, y eliminando también las hipotecas asociadas al mismo.    
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
      
#Este método simula una hipoteca asociada a un cliente, vlidando que este exista
def simularHipoteca(dni, tae, plazoAmortizacion):

      if(comprobarExistenciaCliente(dni)==True):

            #En este bloque de código, tomo el capital solicitado por el cliente
            bbdd = get_conexionBBDD()
            cursor = bbdd.cursor()
            sentenciaCapital = "SELECT CAPITAL_SOLICITADO FROM CLIENTES WHERE DNI = ?"
            cursor.execute(sentenciaCapital,[dni])
            resultadoAux = cursor.fetchall()
            capitalSolicitado = resultadoAux[0][0]
            bbdd.commit()
            bbdd.close()

            #En este bloque de código calculo el interés mensual y el número de meses de plazo de amortización, con los que después calculo la cuota mensual y el importe total
            i = tae/100/12
            n = plazoAmortizacion*12
            cuota = round(capitalSolicitado * i /(1 - pow((1 + i),-n)),2)
            importeTotal = round(cuota * n,2)

            #En este bloque de código se crea el nuevo registro en la base de datos de las hipotécas
            bbdd = get_conexionBBDD()
            cursor = bbdd.cursor()
            sentenciaInsercion = "INSERT INTO HIPOTECAS(CUOTA_MENSUAL, IMPORTE_TOTAL, DNI_CLIENTE) VALUES(?,?,?)"
            cursor.execute(sentenciaInsercion, [cuota, importeTotal, dni])
            bbdd.commit()
            bbdd.close()

            return "Cuota mensual: "+str(cuota)+"€"+" Importe total: "+str(importeTotal)+"€"
      else:

            return False