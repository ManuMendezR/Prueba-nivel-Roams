from flask import Flask, jsonify, request
import controlador
from bbdd import crear_tablas

app = Flask(__name__)

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

@app.route("/consultar", methods=["GET"])
def consultarCliente():

    consultarCliente = request.get_json()
    dni = consultarCliente["dni"]

    resultado = controlador.consultarCliente(dni)
    return jsonify(resultado)

@app.route("/eliminar", methods=["DELETE"])
def eliminarCliente():

    eliminarCliente = request.get_json()
    dni = eliminarCliente(dni)

    resultado = controlador.eliminarCliente(dni)
    return jsonify(resultado)

if __name__ == "__main__":

    crear_tablas()
    app.run(host = "0.0.0.0", port = 8000, debug = False)