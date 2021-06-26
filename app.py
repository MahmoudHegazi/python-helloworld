from flask import Flask, jsonify, json
import json
import logging, logging.config, yaml

app = Flask(__name__)

logging.config.dictConfig(yaml.load(open('logging.conf')))
logfile    = logging.getLogger('app.log')
logconsole = logging.getLogger('console')
logfile.debug("Debug File")
logconsole.debug("Debug CONSOLE")

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"

@app.route('/status')
def status():
    response = app.response_class(
            response = json.dumps({"result":"Ok - healthy"}),
            status=200,
            mimetype="application/json"
            )
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
            response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
            status= 200,
            mimetype="application/json"
            )
    return response
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
