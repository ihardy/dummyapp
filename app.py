from flask import Flask, jsonify, make_response, request
import logging
import json

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

METHODS = ['GET', 'POST', 'PUT', 'DELETE']

def log_request():
    logging.info("Received %s request for %s", request.method, request.path)
    logging.info("Query Params: %s", request.args.to_dict())
    logging.info("Headers: %s", dict(request.headers))

    try:
        if request.is_json:
            logging.info("JSON Body: %s", request.get_json())
        else:
            logging.info("Form Data: %s", request.form.to_dict())
    except Exception as e:
        logging.warning("Could not parse request body: %s", e)

@app.route('/', methods=METHODS)
def root_is_ok():
    log_request()
    http_code = set_response_code(request.method)
    data = {'message': 'This is a dummy module, it only responds with success codes.', 'code': http_code}
    return make_response(jsonify(data), http_code)

@app.route('/<interface>', methods=METHODS)
def anypath_is_ok(interface):
    log_request()
    http_code = set_response_code(request.method)
    data = {'message': f'This is a dummy response for {interface}', 'code': http_code}
    return make_response(jsonify(data), http_code)

@app.route('/<interface>/<second>', methods=METHODS)
def any_double_path_is_ok(interface, second):
    log_request()
    http_code = set_response_code(request.method)
    data = {'message': f'This is a dummy response for {interface}/{second}', 'code': http_code}
    return make_response(jsonify(data), http_code)

@app.route('/<interface>/<second>/<third>', methods=METHODS)
def any_triple_path_is_ok(interface, second, third):
    log_request()
    http_code = set_response_code(request.method)
    data = {'message': f'This is a dummy response for {interface}/{second}/{third}', 'code': http_code}
    return make_response(jsonify(data), http_code)

def set_response_code(request_method):
    if request_method in ['POST', 'PUT']:
        return 201
    elif request_method == 'DELETE':
        return 204
    return 200

# run this app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
