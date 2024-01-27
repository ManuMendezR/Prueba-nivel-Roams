from flask import Flask, jsonify, request
import controlador
from bbdd import crear_tablas

app = Flask(__name__)

#Esta es la solicitud de la API que va a crear nuevos clientes
@app.route("/crear", methods=["POST"])
def crearCliente():

    nuevoCliente = request.get_json()
    dni = nuevoCliente["dni"]
    letraDni = nuevoCliente["letraDni"]
    nombre = nuevoCliente["nombre"]
    apellido1 = nuevoCliente["apellido1"]
    apellido2 = nuevoCliente["apellido2"]
    email = nuevoCliente["email"]
    capitalSolicitado = nuevoCliente["capitalSolicitado"]
    
    resultado = controlador.crearCliente(dni, letraDni, nombre, apellido1, apellido2, email, capitalSolicitado)
    return jsonify(resultado)

#Esta es la solicitud de la API que va actualizar los datos de los clientes
@app.route("/actualizar", methods=["PUT"])
def actualizarCliente():

    actualizarCliente = request.get_json()
    dni = actualizarCliente["dni"]
    nombre = actualizarCliente["nombre"]
    apellido1 = actualizarCliente["apellido1"]
    apellido2 = actualizarCliente["apellido2"]
    email = actualizarCliente["email"]
    capitalSolicitado = actualizarCliente["capitalSolicitado"]

    resultado = controlador.actualizarCliente(dni, nombre, apellido1, apellido2, email, capitalSolicitado)
    return jsonify(resultado)

#Esta es la solicitud de la API que va consultar los datos de los clientes
@app.route("/consultar", methods=["GET"])
def consultarCliente():

    consultarCliente = request.get_json()
    dni = consultarCliente["dni"]

    resultado = controlador.consultarCliente(dni)
    return jsonify(resultado)

#Esta es la solicitud de la API que va eliminar los datos de los clientes
@app.route("/eliminar", methods=["DELETE"])
def eliminarCliente():

    eliminarCliente = request.get_json()
    dni = eliminarCliente["dni"]

    resultado = controlador.eliminarCliente(dni)
    return jsonify(resultado)

#Esta es la solicitud de la API que va simular hipotecas asociadas a los clientes
@app.route("/simularHipoteca", methods=["POST"])
def simularHipoteca():

    simularHipoteca = request.get_json()
    dni = simularHipoteca["dni"]
    tae = simularHipoteca["tae"]
    plazoAmortizacion = simularHipoteca["plazoAmortizacion"]

    resultado = controlador.simularHipoteca(dni, tae, plazoAmortizacion)
    return jsonify(resultado)

#Este if crea las tablas en caso de que no existan y conecta la API
if __name__ == "__main__":

    crear_tablas()
    app.run(host = "0.0.0.0", port = 8000, debug = False)