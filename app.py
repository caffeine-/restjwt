from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'restjwt'


@app.route('/<token>')
def token_decode(token):
    return '/<token>'


@app.route('/<token>/eval')
def token_eval(token):
    return '/<token>/eval'


@app.route('/<token>/verify')
def token_verify():
    return '/<token>/verify'


@app.route('/<token>/claims')
def token_claims():
    return '/<token>/claims'


@app.route('/<token>/header')
def token_header():
    return '/<token>/header'

if __name__ == '__main__':
    app.run()
