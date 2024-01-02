from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

METHODS = ['GET', 'POST', 'PUT', 'DELETE']

@app.route('/', methods=METHODS)
def root_is_ok():
    http_code = set_response_code(request.method)
    data = {'message': 'This is a dummy module, it only responds with success codes.', 'code': http_code}
    return make_response(jsonify(data), http_code)

@app.route('/<interface>', methods=METHODS)
def anypath_is_ok(interface):
    http_code = set_response_code(request.method)
    data = {'message': 'This is a dummy response for {}'.format(interface), 'code': http_code}
    return make_response(jsonify(data), http_code)

@app.route('/<interface>/<second>', methods=METHODS)
def any_double_path_is_ok(interface, second):
    http_code = set_response_code(request.method)
    data = {'message': 'This is a dummy response for {}'.format('/'.join([interface, second])), 'code': http_code}
    return make_response(jsonify(data), http_code)

@app.route('/<interface>/<second>/<third>', methods=METHODS)
def any_triple_path_is_ok(interface, second, third):
    http_code = set_response_code(request.method)
    data = {'message': 'This is a dummy response for {}'.format('/'.join([interface, second, third])), 'code': http_code}
    return make_response(jsonify(data), http_code)

def set_response_code(request_method):
    if request.method == 'POST' or request.method == 'PUT':
        http_code = 201
    elif request.method == 'DELETE':
        http_code = 204
    else:
        http_code = 200

    return http_code

# run this app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
