from flask import Flask, jsonify, make_response

app = Flask(__name__)

METHODS = ['GET', 'POST', 'PUT', 'DELETE']

@app.route('/', methods=METHODS)
def root_is_ok():
    data = {'message': 'This is a dummy module, it only responds with 200.', 'code': '200'}
    return make_response(jsonify(data), 200)

@app.route('/<interface>', methods=METHODS)
def anypath_is_ok(interface):
    data = {'message': 'This is a dummy response for {}'.format(interface), 'code': '200'}
    return make_response(jsonify(data), 200)

@app.route('/<interface>/<second>', methods=METHODS)
def any_double_path_is_ok(interface, second):
    data = {'message': 'This is a dummy response for {}'.format('/'.join([interface, second])), 'code': '200'}
    return make_response(jsonify(data), 200)

@app.route('/<interface>/<second>/<third>', methods=METHODS)
def any_triple_path_is_ok(interface, second, third):
    data = {'message': 'This is a dummy response for {}'.format('/'.join([interface, second, third])), 'code': '200'}
    return make_response(jsonify(data), 200)

# run this app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
