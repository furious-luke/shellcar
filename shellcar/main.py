from flask import Flask, request, jsonify

from .command import run_command

app = Flask('shellcar')


@app.route('/exec', methods=['POST'])
def hello_world():
    data = request.json
    command = data['command']
    return jsonify(run_command(command))
