from flask import Flask
from flask import request
import operations

app = Flask(__name__)

# @app.route('/add')
# def add():
#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     return str(a+b)

# @app.route('/sub')
# def sub():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     return str(a-b)

# @app.route('/mult')
# def mult():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     return str(a*b)

# @app.route('/div')
# def div():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     return str(a/b)


@app.route('/add')
def add():
    """add a and b"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.add(a,b))

@app.route('/sub')
def sub():
    """ subtracts b from a"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.sub(a,b))

@app.route('/mult')
def mult():
    """ multiplies a and b"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.mult(a,b))

@app.route('/div')
def div():
    """ divides a by b"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations.div(a,b))

@app.route('/math/<op>')
def operation(op):
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations_dict[op](a,b))