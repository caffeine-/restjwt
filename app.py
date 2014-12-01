import jwt
from flask import Flask, jsonify, request, send_from_directory
from flask.ext.cors import CORS

app = Flask(__name__)
cors = CORS(app)

def json_error(msg):
    return jsonify({'result': 'error', 'message': str(msg)})


@app.route('/')
def index():
    return send_from_directory(app.root_path, 'README.md', mimetype='text/plain')


@app.route('/<token>')
def token_decode(token):
    secret = request.args.get('secret', '')
    try:
        payload = jwt.decode(token, secret, verify_expiration=False)
        return jsonify(payload)
    except Exception as e:
        return json_error(e)


@app.route('/<token>/eval')
def token_eval(token):
    secret = request.args.get('secret', '')
    try:
        payload = jwt.decode(token, secret, verify_expiration=False)
        return jsonify({'signature': True, 'claims': payload})
    except:
        payload = jwt.decode(token, secret, verify=False)
        return jsonify({'signature': False, 'claims': payload})


@app.route('/<token>/verify')
def token_verify(token):
    secret = request.args.get('secret', '')
    try:
        _ = jwt.decode(token, secret, verify_expiration=False)
        return jsonify({'result': 'success'})
    except Exception as e:
        response = json_error(e)
        response.status_code = 409
        return response


@app.route('/<token>/claims')
def token_claims(token):
    try:
        return jsonify(jwt.decode(token, verify=False))
    except Exception as e:
        return jsonify({'result': 'error', 'message': str(e)})


@app.route('/<token>/header')
def token_header(token):
    try:
        return jsonify(jwt.header(token.encode('utf-8')))
    except Exception as e:
        return json_error(e)

if __name__ == '__main__':
    app.run(debug=True, port=8881)
